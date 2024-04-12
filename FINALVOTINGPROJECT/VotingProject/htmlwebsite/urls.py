from django.contrib import admin
from django.urls import path,include
from htmlwebsite import views

urlpatterns = [
     path('', views.home, name='home'),
     path('loginPage', views.Login, name='login'),
     path('signupPage', views.signup, name='signup'),
     path('contact', views.contact, name='contact'),
     path('createPollPage', views.createPoll, name='createPoll'),
     path('polls',views.viewpoll, name='polls'),
     path('send_vote<str:choiceoption>', views.send_vote, name='send_vote'),
     path('result.html', views.result, name='result'),
     path('logout/', views.logout_view, name='logout'),
     
]


