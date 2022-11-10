from django.urls import path
from apps.BlogApp import views

urlpatterns = [
    # path('',views.homePage, name = 'home'),
    path('home/', views.homePage, name = 'home'),
    path('about/', views.aboutPage, name = 'about'),
    path('blog/', views.blogPage, name = 'blog'),
    path('contact/', views.contactPage, name = 'contact'),
    path('detail/', views.detailPage, name = 'detail'),
    path('feature/', views.featurePage, name = 'feature'),
    path('price/', views.pricePage, name = 'price'),
    path('quote/', views.quotePage, name = 'quote'),
    path('service/', views.servicePage, name = 'service'),
    path('team/', views.teamPage, name = 'team'),
    path('testimonial/', views.testimonialPage, name = 'testimonial'),
    # path("register", views.register_request, name="register"),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name= "logout"),
    
    
    
    path('image_upload', views.image_request, name = 'image_upload'),
    path('success', views.success, name = 'success'),
]
