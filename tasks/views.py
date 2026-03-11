from django.http import JsonResponse
from django.shortcuts import render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def healthz(request):
    return JsonResponse({"status": "ok"})