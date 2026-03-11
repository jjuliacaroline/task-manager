from django.urls import path

from .views import healthz, task_list

urlpatterns = [
    path("", task_list, name="task_list"),
    path("healthz/", healthz, name="healthz"),
]
