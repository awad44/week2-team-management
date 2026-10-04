from django.db import transaction

from core.models import Comment, Organization, Project, Task


@transaction.atomic
def create_project_with_initial_task(
    *,
    organization: Organization,
    user,
    project_name: str,
) -> Project:
    project = Project.objects.create(
        organization=organization,
        name=project_name,
        created_by=user,
    )

    task = Task.objects.create(
        project=project,
        title="Initial project setup",
        priority=Task.Priority.HIGH,
        assigned_to=user,
    )

    Comment.objects.create(
        task=task,
        author=user,
        body="Initial task created automatically.",
    )

    return project


def get_tasks_with_details():
    return Task.objects.select_related(
        "project",
        "assigned_to",
    )


def get_projects_with_tasks():
    return Project.objects.prefetch_related("tasks")