from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo_list_service.models import Task, Tag


class ViewsTests(TestCase):
    def test_ordering_tasks(self):
        Task.objects.create(
            content="task1",
            created_at=timezone.now(),
            is_done=False
        )
        Task.objects.create(
            content="task2",
            created_at=timezone.now() - timezone.timedelta(days=25),
            is_done=False
        )
        Task.objects.create(
            content="task3",
            created_at=timezone.now() - timezone.timedelta(days=56),
            is_done=True
        )

        response = self.client.get(reverse("todo_list:task-list"))
        tasks = Task.objects.all().order_by("is_done", "-created_at")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]),
                         list(tasks))
        self.assertTemplateUsed(response,
                                "todo_list_service/task_list.html")

    def test_tags(self):
        Tag.objects.create(name="test tag1")
        Tag.objects.create(name="test tag2")

        response = self.client.get(reverse("todo_list:tag-list"))
        tags = Tag.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]),
                         list(tags))
        self.assertTemplateUsed(response,
                                "todo_list_service/tag_list.html")
