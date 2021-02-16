from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets


from .models import Task
from .serializers import TaskSerializer, UserSerializer, UserSerializerRegister

from .permissions import IsOwner

class RegisterUser(generics.CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializerRegister


class TasksList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "tasks/tasks_panel.html"
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request):
        tasks = Task.objects.filter(owner=self.request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            {
                "serializer": TaskSerializer,
                "data": serializer.data,
            }
        )

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(
                {
                    "serializer": TaskSerializer,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class TasksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        filter = Task.objects.filter(owner=self.request.user)
        queryset = self.filter_queryset(filter)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
