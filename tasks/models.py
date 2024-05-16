from django.db import models
from uuid import uuid4
from django.conf import settings
from django.utils.translation import gettext as _
from enum import Enum


class TaskStatus(Enum):
    TODO = "TODO"
    IN_PROGRESS = "in_progress"
    DEFERRED = "defer"
    COMPLETED = "completed"


class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task(models.Model):
    """Model definition for Task."""

    id = models.UUIDField(
        _("id"), primary_key=True, default=uuid4, editable=False, db_index=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=100, blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    status = models.CharField(
        _("completed"),
        choices=[(tag.value, tag.name) for tag in TaskStatus],
        max_length=11,
        default=TaskStatus.TODO.value,
    )
    priority = models.CharField(
        _("priority"),
        choices=[(tag.value, tag.name) for tag in TaskPriority],
        default=TaskPriority.MEDIUM.value,
        max_length=6,
    )
    deadline = models.DateTimeField(_("deadline"))
    updated_timestamp = models.DateTimeField(_("updated timestamp"), auto_now_add=True)
    created_timestamp = models.DateTimeField(_("created timestamp"), auto_now=True)

    class Meta:
        """Meta definition for Task."""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        """Unicode representation of Task."""
        return self.title


class SubTask(Task):
    """Model definition for SubTask."""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")

    class Meta:
        """Meta definition for SubTask."""

        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"

    def __str__(self):
        """Unicode representation of SubTask."""
        return self.title
