from django.db import models
from uuid import uuid4
from django.conf import settings
from django.utils.translation import gettext as _


class Task(models.Model):
    """Model definition for Task."""

    TASK_STATUS = {
        "TODO": "TODO",
        "IN_PROGRESS": "in_progress",
        "DEFERRED": "defer",
        "COMPLETED": "completed",
    }
    TASK_PRIORITY = {
        "LOW": "low",
        "MEDIUM": "medium",
        "HIGH": "high",
    }
    id = models.UUIDField(
        _("id"), primary_key=True, default=uuid4, editable=False, db_index=True
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=100, blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    status = models.CharField(
        _("completed"), choices=TASK_STATUS, max_length=11, default=TASK_STATUS["TODO"]
    )
    priority = models.CharField(
        _("priority"),
        choices=TASK_PRIORITY,
        default=TASK_PRIORITY["LOW"],
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
        self.title
