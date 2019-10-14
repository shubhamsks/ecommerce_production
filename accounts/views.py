from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegistrationForm
from django.urls import reverse
from django.contrib import messages
def logout_view(request):
    messages.info(request,"You have been logged out successfully.")
    logout(request)
    return HttpResponseRedirect("/")


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request,"Yoh have been logged in successfully.")
        return HttpResponseRedirect(reverse('home'))

    context = {
        "form": form,
        "btn":"Login"
    }
    return render(request, "accounts/login_form.html", context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        print('is valid ')
        new_user = form.save(commit=False)
        new_user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password2')
        user = authenticate(request,username = username, password = password)
        login(request, new_user)
        messages.success(request,"You have been registered successfully.")
        return HttpResponseRedirect(reverse('home'))
    #     # username = form.cleaned_data["username"]
    #     # password = form.cleaned_data["password"]
    #     # user = authenticate(username=username, password=password)
    #     # login(request, user)
    context = {"form": form,"btn":"Join"}
    return render(request, "accounts/signup_form.html", context)
