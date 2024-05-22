from django.db import models

TODO_CATEGORIES = [
    ("home", "Home"),
    ("work", "Work"),
    ("hobby", "Hobby"),
    ("other", "Other"),
]


class Project(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Todo(models.Model):
    label = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField()
    category = models.CharField(choices=TODO_CATEGORIES, default=TODO_CATEGORIES[0][0], max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
