from collections import OrderedDict

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient, force_authenticate, APIRequestFactory
from rest_framework import status

from .views import TasksViewSet
from .models import Task

class TasksTestCases(TestCase):
    def setUp(self):
        user = User(email="lucas@polymath.com", username="lucas", password="Lucaspass")
        user.save()
        task = Task(description="test_task_1", owner=user)
        task.save()

        strange_user = User(
            email="strange@polymath.com", username="strange", password="strangepass"
        )
        strange_user.save()

    def test_get_all_tasks(self):
        client = APIRequestFactory()
        request = client.get("api/tasks/")
        view = TasksViewSet.as_view({"get": "list"})
        user = User.objects.get(username="lucas")
        force_authenticate(request, user)
        response = view(request)
        task_description = response.data["results"][0]
        self.assertEqual(
            task_description,
            OrderedDict(
                [("id", 1), ("description", "test_task_1"), ("owner", "lucas")]
            ),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_new_task(self):
        client = APIClient()
        user = User.objects.get(username="lucas")
        client.force_authenticate(user)
        response = client.post("/tasks/", {"description": "test_task_2"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_task(self):
        client = APIClient()
        user = User.objects.get(username="lucas")
        client.force_authenticate(user)
        response = client.delete("/api/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_task(self):
        client = APIClient()
        user = User.objects.get(username="lucas")
        client.force_authenticate(user)
        test_task_1 = Task.objects.get(description="test_task_1")
        response = client.put(
            "/api/tasks/{}/".format(test_task_1.id),
            {"description": "test_task_1_modified"},
        )
        task_modified = Task.objects.get(description="test_task_1_modified")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(test_task_1.id, task_modified.id)

    def test_put_no_owner_task(self):
        client = APIClient()
        strange = User.objects.get(username="strange")
        client.force_authenticate(user=strange)

        test_task_1 = Task.objects.get(description="test_task_1")
        response = client.put(
            "/api/tasks/{}/".format(test_task_1.id),
            {"description": "test_task_1_modified"},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
