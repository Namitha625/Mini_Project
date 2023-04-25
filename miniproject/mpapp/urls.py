from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),

    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('loginasuser/',views.loginasuser,name='loginasuser'),
    path('loginastutor/',views.loginastutor,name='loginastutor'),
    path('signupasuser/',views.signupasuser,name='signupasuser'),
    path('signupastutor/',views.signupastutor,name='signupastutor'),
    path('userpage/',views.userpage,name='userpage'),
    path('afterlogin/',views.afterlogin,name='afterlogin'),
    path('languages/',views.languages,name='languages'),
    path('teachers/',views.teachers,name='teachers'),
    path('choiceofteacher/',views.choiceofteacher,name='choiceofteacher')
]


