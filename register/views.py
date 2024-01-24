from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print("pass1: ", password1, password2)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username is already registered.")
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('/register')

    else:
        return render(request, template_name='register/register.html', context={})
