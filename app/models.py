from django.db import models

# Create your models here.
class URL(models.Model):
    final_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=50)
    checks = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.short_url} => {self.final_url} [Checked {self.checks}]"