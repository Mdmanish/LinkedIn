from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User, auth
from .models import Profile, Experience, Education, Certificates, Followers, Skills, Languages, Message
from django.db.models import Q
from .form import ExperienceForm, EducationForm, CertificatesForm, SkillsForm, LanguagesForm
from django.http import HttpResponse, JsonResponse
# Create your views here.


def profile_page(request):
    if request.method == 'POST':
        # user = Profile.objects.get(user=request.user)
        # user.image = request.FILES.get('profile_pic')
        # # user.cover_image = request.FILES.get('cover_pic')
        # user.save()
        return redirect('/profile')

    else:
        login_user = Profile.objects.get(user=request.user)
        user = Profile.objects.get(user=request.user)
        user_for_name = request.user
        follower_count = len(Followers.objects.filter(user=user))

        user_experience = Experience.objects.filter(user=request.user).values()
        user_education = Education.objects.filter(user=request.user).values()
        user_skills = Skills.objects.filter(user=request.user).values()
        user_language = Languages.objects.filter(user=request.user).values()
        user_certificates = Certificates.objects.filter(user=request.user)
        print('user_experience:', user_experience)
        context = {
            'login_user': login_user,
            'user_for_name': user_for_name,
            'user': user,
            'follower_count': follower_count,
            'user_experience': user_experience,
            'user_education': user_education,
            'user_skills': user_skills,
            'user_language': user_language,
            'user_certificates': user_certificates
        }
        return render(request, template_name='user_profile/profile.html', context=context)


def upload_pic(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        user.image = request.FILES.get('profile_pic')
        user.save()
        return redirect('/profile')
    else:
        user = Profile.objects.get(user=request.user)
        return render(request, template_name='user_profile/upload_pic.html', context={'user': user})


def upload_cover_pic(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        user.cover_image = request.FILES.get('cover_pic')
        user.save()
        return redirect('/profile')
    else:
        user = Profile.objects.get(user=request.user)
        return render(request, template_name='user_profile/upload_cover_pic.html', context={'user': user})


def edit_profile(request, id):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        company = request.POST.get('company')
        about = request.POST.get('about')
        user = Profile.objects.get(id=id)
        user.bio = bio
        user.company = company
        user.about = about

        # experience = request.POST.get('experience')
        # if not Experience.objects.filter(user_id=id).exists():
        #     user_experience = Experience()
        #     user_experience.user = request.user
        #     user_experience.title = experience
        #     user_experience.save()
        # else:
        #     user_experience = Experience.objects.get(id=id)
        #     user_experience.title = experience
        #     user_experience.save()

        user.save()
        return redirect(reverse('user_profile:profile_page'))

    else:
        user = Profile.objects.get(user=request.user)
        # user_experience = Experience.objects.filter(user=request.user)
        context = {
            'user': user,
            # 'user_experience': user_experience,
        }
        return render(request, template_name='user_profile/edit_profile.html', context=context)


def search(request):
    if request.method == 'POST':
        login_user = Profile.objects.get(user=request.user)
        print('login_user: ', login_user)
        username = request.POST.get('search')
        all_users = User.objects.filter(username__contains=username).exclude(
            username=login_user).values()
        context = {
            'login_user': login_user,
            'all_users': all_users
        }

        return render(request, template_name='user_profile/search.html', context=context)


def search_profile(request, username):
    print('username is : ', username)
    login_user = Profile.objects.get(user=request.user)
    user = Profile.objects.get(user__username=username)
    user_for_name = User.objects.get(username=username)
    follower_count = len(Followers.objects.filter(user=user))
    # print('login_user:', login_user, 'user_for_name:', user_for_name)
    # if login_user != user:
    #     print(True)
    follow_button = 'follow'
    login_user_followers, search_user_followers = [], []
    for entity in Followers.objects.filter(user=login_user):
        login_user_followers.append(entity.follower)

    for entity in Followers.objects.filter(user=user):
        search_user_followers.append(entity.follower)

        if str(login_user) == str(entity.follower):
            follow_button = 'unfollow'
        else:
            follow_button = 'follow'

    mutual_followers = (set(login_user_followers) & set(search_user_followers))
    count_mutual_followers = len(mutual_followers)

    user_experience = Experience.objects.filter(user__username=username)
    user_education = Education.objects.filter(user__username=username)
    user_certificates = Certificates.objects.filter(user__username=username)
    user_skills = Skills.objects.filter(user__username=username).values()
    user_language = Languages.objects.filter(user__username=username).values()
    context = {
        'login_user': login_user,
        'user_for_name': user_for_name,
        'follower_count': follower_count,
        'follow_button': follow_button,
        'count_mutual_followers': count_mutual_followers,
        'mutual_followers': mutual_followers,
        'user': user,
        'user_experience': user_experience,
        'user_education': user_education,
        'user_certificates': user_certificates,
        'user_skills': user_skills,
        'user_language': user_language
    }
    return render(request, template_name='user_profile/profile.html', context=context)


def followers(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']

        if value == 'follow':
            follower_created = Followers.objects.create(
                follower=follower, user=user)
            follower_created.save()
        else:
            follower_created = Followers.objects.get(
                follower=follower, user=user)
            follower_created.delete()

    return redirect('/search_profile/'+user)


def experience_form(request, id=-1):
    if request.method == 'POST':
        if int(id)== -1:
            form = ExperienceForm(request.POST)
            # print("r9999999999999999999  :",request.POST, request.FILES, form)
        else:
            experience = Experience.objects.get(pk=id, user=request.user)
            form = ExperienceForm(request.POST, instance=experience)

        if form.is_valid():
            print("VALID")
            form.save()
        else:
            print("NOT VALID")
        # print(Experience.objects.filter(user=request.user).values())
        return redirect('/profile')
    else:
        if int(id)==-1:
            form = ExperienceForm(initial={'user':request.user})
            field = form.fields['user']
            field.widget = field.hidden_widget()
        else:
            experience = Experience.objects.get(pk=id, user=request.user)
            form = ExperienceForm(instance=experience)
            field = form.fields['user']
            field.widget = field.hidden_widget()
        return render(request, 'user_profile/form.html', {"form": form})


def education_form(request, id=-1):
    if request.method == 'POST':
        if int(id)== -1:
            form = EducationForm(request.POST)
        else:
            education = Education.objects.get(pk=id, user=request.user)
            form = EducationForm(request.POST, instance=education)
            
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        if int(id)==-1:
            form = EducationForm(initial={'user':request.user})
            field = form.fields['user']
            field.widget = field.hidden_widget()
        else:
            education = Education.objects.get(pk=id, user=request.user)
            form = EducationForm(instance=education)
            field = form.fields['user']
            field.widget = field.hidden_widget()
        return render(request, 'user_profile/form.html', {"form": form})

    print('id=',id)


def certificate_form(request, id=-1):
    if request.method == 'POST':
        if int(id)== -1:
            form = CertificatesForm(request.POST)
        else:
            certificates = Certificates.objects.get(pk=id, user=request.user)
            form = CertificatesForm(request.POST, instance=certificates)
        
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        if int(id)==-1:
            form = CertificatesForm(initial={'user':request.user})
            field = form.fields['user']
            field.widget = field.hidden_widget()
        else:
            certificates = Certificates.objects.get(pk=id, user=request.user)
            form = CertificatesForm(instance=certificates)
            field = form.fields['user']
            field.widget = field.hidden_widget()
        return render(request, 'user_profile/form.html', {"form": form})


def skills_form(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        form = SkillsForm(initial={'user':request.user})
        field = form.fields['user']
        field.widget = field.hidden_widget()
        return render(request, 'user_profile/form.html', {"form": form})


def language_form(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/profile')
    else:
        form = LanguagesForm(initial={'user':request.user})
        field = form.fields['user']
        field.widget = field.hidden_widget()
        return render(request, 'user_profile/form.html', {"form": form})



def message(request, username):
    message_obj = Message.objects.filter(sender=request.user, reciver=User.objects.get(username=username))
    return render(request, 'user_profile/message.html', {'reciver':username,'message_obj':message_obj})


def checkview(request, username):
    # reciver = request.POST['reciver']
    # print('reciver is: ',reciver)
    if Message.objects.filter(sender=request.user, reciver=User.objects.get(username=username)).exists():
        return redirect('/message/'+username)
    else:
        new_message1 = Message.objects.create(sender=request.user, reciver=User.objects.get(username=username))
        new_message1.save()
        new_message2 = Message.objects.create(reciver=request.user, sender=User.objects.get(username=username))
        new_message2.save()
        return redirect('/message/'+username)
    
def send(request):
    message = request.POST['message']
    reciver = request.POST['reciver']
    message_id = request.POST['message_obj_id']
    new_message = Message.objects.create(sender= request.user, reciver=User.objects.get(username=reciver), value=message)
    new_message.save()
    return HttpResponse("message sent succesfully")

def sort_messages(element):
    return element['date']

def get_all_messages(request, username):
    all_login_user_message = list(Message.objects.filter(sender=request.user, reciver=User.objects.get(username=username)).values())
    all_reciver_user_message = list(Message.objects.filter(reciver=request.user, sender=User.objects.get(username=username)).values())
   
    all_message = all_login_user_message + all_reciver_user_message
    all_message.sort(key=sort_messages)
    if len(all_message) > 0:
        sender_id = all_message[0]['sender_id']
        reciver_id = all_message[0]['reciver_id']
        sender_user = User.objects.get(id=sender_id).username
        reciver_user = User.objects.get(id=reciver_id).username

    print('all_message::: ',all_message)
    json_result = {
        "all_message":all_message,
        "sender_user":sender_user,
        "reciver_user":reciver_user,
        'sender_id':sender_id,
        'reciver_id':reciver_id,
    }
    return JsonResponse(json_result)
    