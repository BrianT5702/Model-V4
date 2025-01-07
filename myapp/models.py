from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wall(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='walls')
    start_x = models.FloatField()
    start_y = models.FloatField()
    end_x = models.FloatField()
    end_y = models.FloatField()
    thickness = models.FloatField(default=0.2)

    def __str__(self):
        return f"Wall for {self.project.name} from ({self.start_x}, {self.start_y}) to ({self.end_x}, {self.end_y})"
