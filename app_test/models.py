from django.db import models

# Create your models here.
class students(models.Model):
    stu_id  = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    def __unicode__(self):
        return self.stu_name
class teacher(models.Model):
    tea_id  = models.IntegerField(primary_key=True)
    tea_name = models.CharField(max_length=100)
    tea_age = models.IntegerField()
class courese(models.Model):
    cou_id = models.IntegerField(primary_key=True)
    cou_name = models.CharField(max_length = 100)