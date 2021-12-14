## App (photopedia)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('search/<slug:action>', views.search, name='search'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),

    path('profile/<int:pk>', views.profile, name='profile'),
    path('setting/', views.setting, name='setting'),
    

    path('pin/new/', views.pin_new, name='pin_new'),
    path('pin/<int:pk>/', views.pin_view, name='pin_view'),
    path('pin/<int:pk>/edit/', views.pin_edit, name='pin_edit'),
    path('pin/<int:pk>/remove/', views.pin_remove, name='pin_remove'),
]
