from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='home'),
    path('register',views.Register,name='register'),
    path('login',views.LogIn,name='login'),
    path('logout/',views.LogOut,name="logout"),
    path('update_photo',views.UpdatePhoto,name="photo"),
    path('rank/',views.Rank,name="rank"),
    path('progress/',views.Progress,name="progress"),
    path('save_score',views.SaveScore,name="savescore"),
]
