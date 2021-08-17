from django.urls import path
from .views import *

app_name= 'firstapp'
urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('career/', career, name="career"),
    path('os/', os, name="os"),
    path('dc/', dc, name="dc"),
    path('curriculum/', curriculum, name="curriculum"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name= "create"),
    path('post/', post, name= "post"),
    path('edit/<str:id>', edit, name= "edit"),
    path('update/<str:id>', update, name= "update"),
    path('delete/<str:id>', delete, name= "delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path("edit_comment/<str:id>", edit_comment, name="edit_comment"),
    path("update_comment/<str:id>", update_comment, name="update_comment"),
    path("delete_comment/<str:id>", delete_comment, name="delete_comment"),
    path("like_toggle/<str:post_id>", like_toggle, name="like_toggle"),
    path("dislike_toggle/<str:post_id>", dislike_toggle, name="dislike_toggle"),

]
