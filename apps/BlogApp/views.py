from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group

# from apps.BlogApp.forms import NewUserForm, UserImageForm
from apps.BlogApp.models import UploadImage , Blog

from . import templates


def homePage(request):
    return render(request, "website/index.html")


def aboutPage(request):
    return render(request, "website/about.html")



def image_request(request):

    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Image Uploaded Successfully.")
            return HttpResponseRedirect(request.path_info)
            # return redirect('success')
    else:
        form = UserImageForm()
    return render(request, 'image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def blogPage(request):
    featured_obj = Blog.objects.all().filter(status='active', visible=True,
                                             featured=True).order_by('catagories', '-created_at')[:5]
    post_obj = Blog.objects.all().order_by('catagories', '-created_at')
    # As per Templates Views
    # first_post = featured_obj.first()
    # s_post = featured_obj[1]
    # last_post = featured_obj[2:]
    context = {
        'post': post_obj,
        'f_post': featured_obj,
        'list': [1]
        # 'first': first_post,
        # 's_post': s_post,
        # 'last_post': last_post
    }
    return render(request, "website/blog.html", context)


def contactPage(request):
    return render(request, "website/contact.html")


def detailPage(request):
    return render(request, "website/detail.html")


def featurePage(request):
    return render(request, "website/feature.html")


def pricePage(request):
    return render(request, "website/price.html")


def quotePage(request):
    return render(request, "website/quote.html")


def servicePage(request):
    return render(request, "website/service.html")


def teamPage(request):
    return render(request, "website/team.html")


def testimonialPage(request):
    return render(request, "website/testimonial.html")

"""
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Authors')
            user.groups.add(group)
            login(request, user)
            messages.success(
                request, f"{user.username} Registration Successful.")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(request.path_info)
            # return redirect("homepage")
            # return redirect('success')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="newUser/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect(request.path_info)
        # return redirect("/home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="newUser/login.html", context={"login_form": form})


def logout_request(request):
    redirect_to = request.GET.get('next', '')
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect(redirect_to)
    # return redirect("main:homepage")

"""