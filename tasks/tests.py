from django.http import HttpResponse
from django.test import RequestFactory, TestCase
from unittest.mock import patch

from .views import task_list


class TaskListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_task_list_uses_queryset_and_renders_template(self):
        request = self.factory.get("/tasks/")

        with patch("tasks.views.Task.objects.all", return_value=[]) as mock_all, \
             patch("tasks.views.render", return_value=HttpResponse("ok")) as mock_render:
            response = task_list(request)

        self.assertEqual(response.status_code, 200)
        mock_all.assert_called_once_with()
        mock_render.assert_called_once_with(
            request,
            "tasks/task_list.html",
            {"tasks": []},
        )
