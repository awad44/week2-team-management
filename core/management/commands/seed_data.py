from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.models import Comment, Membership, Organization, Project, Task

User = get_user_model()


class Command(BaseCommand):
    help = "Create sample data for the Team Work Management platform"

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(
            username="demo_user",
            defaults={
                "email": "demo@example.com",
            },
        )

        organization, _ = Organization.objects.get_or_create(
            name="NERUOS Demo Organization",
            defaults={
                "description": "Sample organization for development",
            },
        )

        Membership.objects.get_or_create(
            organization=organization,
            user=user,
            defaults={
                "role": Membership.Role.ADMIN,
            },
        )

        project, _ = Project.objects.get_or_create(
            organization=organization,
            name="Internship Platform",
            defaults={
                "description": "Sample project for Week 2",
                "created_by": user,
            },
        )

        task, _ = Task.objects.get_or_create(
            project=project,
            title="Finish Week 2",
            defaults={
                "description": "Complete Django domain modeling",
                "priority": Task.Priority.HIGH,
                "completed": False,
                "assigned_to": user,
            },
        )

        Comment.objects.get_or_create(
            task=task,
            author=user,
            body="Week 2 is progressing well.",
        )

        self.stdout.write(
            self.style.SUCCESS("Sample data created successfully.")
        )