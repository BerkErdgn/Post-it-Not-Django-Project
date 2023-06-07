
from django.urls import path, include
from . import views

app_name="postitnotapp"

urlpatterns = [
    path("",views.index, name="index"),
    path("singup/", views.SignUpView.as_view(), name="singup"),
    path("addNot/", views.addNot, name="addNot"),
    path("postit/", views.postit, name="postit"),
    path("subjectview/<str:sybject>", views.subjectview, name="subjectview"),
    path("delete/<int:pk>", views.delete, name="delete")

    
     
]
