from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_profile.models import Profile
from .models import Post, Like, Comment
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def home_page(request):
    if request.method == 'POST':
        text_post = request.POST.get('text_post')
        image_post = request.POST.get('photo')
        user = Post.objects.create(user=request.user, text=text_post, image=image_post)
        user.save()
        return redirect('/home')
    else:
        # to show login user details
        user = Profile.objects.get(user=request.user)
        all_posts = Post.objects.all()  # to show all posts of every user in LinkedIn

        profile_dict = {}  # to show profile pic of posted user
        for post in all_posts:
            if post.user not in profile_dict:
                profile_dict[post.user] = Profile.objects.get(user=post.user)

        # Storing all liked post of the login user in a set.
        all_likes = Like.objects.filter(user=request.user).values()
        all_likes_set = set()
        for like in all_likes:
            all_likes_set.add(like['post_id_id'])
        print('all_likes', all_likes_set)

        # Storing total likes of a post
        total__like_of_a_post = {}
        for post in all_posts:
            total__like_of_a_post[post.post_id] = len(
                Like.objects.filter(post_id=post.post_id))

        # Storing all comments for every post
        all_comments = {}
        for post in all_posts:
            all_comments[post.post_id] = Comment.objects.filter(
                post_id=Post.objects.get(post_id=post.post_id))

        context = {
            'user': user,
            'all_posts': all_posts,
            'all_comments': all_comments,
            'profile_dict': profile_dict,
            'all_likes_set': all_likes_set,
            'total__like_of_a_post': total__like_of_a_post
        }

        return render(request, template_name='home/home.html', context=context)


def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        value = request.POST.get('value')
        if value == 'Like':
            like = Like.objects.create(post_id=Post.objects.get(
                post_id=post_id), user=request.user)
            like.save()
        else:
            like = Like.objects.get(post_id=Post.objects.get(
                post_id=post_id), user=request.user)
            like.delete()

    return redirect('/')


def comment_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        commnet = request.POST.get('comment')
        create_comment = Comment.objects.create(post_id=Post.objects.get(
            post_id=post_id), user=request.user.username, text=commnet)
        create_comment.save()

    return redirect('/')
