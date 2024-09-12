from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', views.displayTweet, name='displayTweet'),    
    path('create/', views.createTweet, name='createTweet'),    
    path('<int:tweetId>/edit/', views.editTweet, name='editTweet'),    
    path('<int:tweetId>/delete/', views.deleteTweet, name='deleteTweet'),    
    path('register/', views.register, name='register'),    
      
]