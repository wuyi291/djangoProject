from django.urls import path

from worktable import views

urlpatterns = [
    path('',views.show)
]