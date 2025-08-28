from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect("login")
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        user_form = UserCreationForm()

    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("device_list")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        login_form = AuthenticationForm()

    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect("login")
