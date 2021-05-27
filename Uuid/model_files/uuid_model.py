from django.db import models


class Uuid(models.Model):
    value = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "uuid"

    def __str__(self):
        return str(self.value)
