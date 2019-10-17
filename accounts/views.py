from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegistrationForm
from django.urls import reverse
from django.contrib import messages
from .models import EmailConfirmed
import re
def logout_view(request):
    messages.info(request,"You have been logged out successfully. Feel free to login again. ")
    logout(request)
    return HttpResponseRedirect("/")


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Yoh have been logged in successfully.")
        return HttpResponseRedirect(reverse('home'))

    context = {
        "form": form,
        "btn":"Login"
    }
    return render(request, "accounts_templates/login_form.html", context)



# Registration view is for registering the new user to the website, when user make new account
# by signing up it triggers the @post_save in signals.py and an is sent to the user
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
        messages.success(request, "You have been registered successfully. Enjoy shopping.")
        messages.info(request,"An email has been sent to you for confirmation please click on the link provided to confirm your email address.")
        return HttpResponseRedirect(reverse('home'))
    context = {"form": form,"btn":"Join"}
    return render(request, "accounts_templates/signup_form.html", context)
# regular expression for checking whether or not activation key fits with this search
SHA1_RE = re.compile('^[a-f0-9]{40}$')
def activation_view(request, activation_key):
    if SHA1_RE.search(activation_key):
        print("activation key is real")
        try:
            instance = EmailConfirmed.objects.get(activation_key=activation_key)
        except EmailConfirmed.DoesNotExist:
            instance = None
            messages.error(request,'There was an error with your requrest.')
            return HttpResponseRedirect('/')
        if instance is not None and not instance.confirmed:
            page_message = "Confirmation Successful Welcome"
            instance.confirmed = True
            instance.activation_key = "Confirmed."
            instance.save()
        elif instance is not None and instance.confirmed:
            page_message = "Already Confirmed."
        else:
            page_message = ""
    else:
        raise Http404
    context = {'page_message':page_message}
    return render(request,'accounts_templates/activation_view.html',context)

def forgot_password(request):
    return render(request, 'coming_soon.html',{})