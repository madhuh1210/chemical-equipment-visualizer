from django.db import models


class UploadHistory(models.Model):
    file_name = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)
    total_count = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()

    def __str__(self):
        return self.file_name

