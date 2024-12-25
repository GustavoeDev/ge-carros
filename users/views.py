from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()

    context = {
        'user_form': user_form,
    }

    return render(request, 'register.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
        
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form': login_form,
    }

    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('cars_list')