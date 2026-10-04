from django.contrib import admin

from core.models import Comment, Membership, Organization, Project, Task

admin.site.register(Organization)
admin.site.register(Membership)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)


# We can make it more useful.
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = (
#         "title",
#         "project",
#         "priority",
#         "completed",
#         "assigned_to",
#     )
#     list_filter = (
#         "priority",
#         "completed",
#     )
#     search_fields = (
#         "title",
#         "description",
#     )