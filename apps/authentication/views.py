# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm , LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


# def login_view(request):
#     msg = None
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 if 'next' in request.POST:
#                     return redirect(request.POST.get('next'))
#                 else:
#                     return HttpResponseRedirect(request.path_info)
#         # return redirect("/home")
#             else:
#                 messages.error(request, "Invalid username or password.")
#                 msg = 'Invalid credentials'
#         else:
#             messages.error(request, "Invalid username or password.")
#             msg = 'Error validating the form'
#     form = AuthenticationForm()
#     # return render(request=request, template_name="newUser/login.html", context={"login_form": form})
#     return render(request, "accounts/login.html", {"form": form, "msg": msg})



def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


# def register_user(request):
#     msg = None
#     success = False
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             group = Group.objects.get(name='Authors')
#             user.groups.add(group)
#             login(request, user)
#             # messages.success(
#             #     request, f"{user.username} Registration Successful.")
#             msg = f"{user.username} Created & Logged In Successfully."
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return HttpResponseRedirect(request.path_info)
#             success = True
#             # return redirect("homepage")
#             # return redirect('success')
#         else:
#             msg = 'Form is not valid'
#             # messages.error(
#             #     request, "Unsuccessful registration. Invalid information.")
#     else:
#         form = NewUserForm()
#     # return render(request=request, template_name="newUser/register.html", context={"register_form": form})
#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})




def logout_request(request):
    redirect_to = request.GET.get('next', '')
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect(redirect_to)
    # return redirect("main:homepage")
