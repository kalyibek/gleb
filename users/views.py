from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def register_user(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['login']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        re_password = request.POST['re-password']
        if password != re_password:
            return render(request, "registration.html", {'error': True})

        new_user = models.CustomUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        new_user.save()
        return redirect(reverse('medshow'))
    return render(request, "registration.html", {'error': False})


def log_in_user(request):

    error = False
    context = {'error': error}

    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        users = models.CustomUser.objects.all()
        user = None
        for i in users:
            if i.username == username and i.password == password:
                user = i
        if user:
            login(request, user)
            return redirect(reverse('medshow'))
        error = True
        context = {'error': error}

    return render(request, "login.html", context)


def log_out_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('medshow'))
