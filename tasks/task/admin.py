from django.contrib import admin

from task.models import TaskItem

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["name", "pin", "transaction", "sum", "date", "owner"]
    list_filter = ["date", "owner"]
    search_fields = ["name", "pin", "date", "owner__email"]

admin.site.register(TaskItem, TaskModelAdmin)