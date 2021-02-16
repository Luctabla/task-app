from rest_framework.urls import path

from .views import TasksList, TasksViewSet, RegisterUser

urlpatterns = [
    path("tasks/", TasksList.as_view(), name="tasks"),
    path(
        "api/tasks/<int:pk>/",
        TasksViewSet.as_view({"put": "update", "delete": "destroy"}),
        name="tasks-detail",
    ),
    path("api/tasks/", TasksViewSet.as_view({"get": "list"})),
    path('register/', RegisterUser.as_view())
]
