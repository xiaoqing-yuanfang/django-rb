# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class students(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()

    def __unicode__(self):
        return self.stu_name


class teacher(models.Model):
    tea_id = models.IntegerField(primary_key=True)
    tea_name = models.CharField(max_length=100)
    tea_age = models.IntegerField()


class courese(models.Model):
    cou_id = models.IntegerField(primary_key=True)
    cou_name = models.CharField(max_length=100)

class RbData(models.Model):
    qishu = models.IntegerField(primary_key=True)
    riqi = models.DateField()
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()
    r6 = models.IntegerField()
    b1 = models.IntegerField()

    def __str__(self):
        '''
        :return qishu temporaly:
        '''
        return str(self.qishu)

class RData(models.Model):
    qishu = models.IntegerField(primary_key=True)
    riqi = models.DateField()
    r1 = models.IntegerField(default=0)
    r2 = models.IntegerField(default=0)
    r3 = models.IntegerField(default=0)
    r4 = models.IntegerField(default=0)
    r5 = models.IntegerField(default=0)
    r6 = models.IntegerField(default=0)
    r7 = models.IntegerField(default=0)
    r8 = models.IntegerField(default=0)
    r9 = models.IntegerField(default=0)
    r10 = models.IntegerField(default=0)
    r11 = models.IntegerField(default=0)
    r12 = models.IntegerField(default=0)
    r13 = models.IntegerField(default=0)
    r14 = models.IntegerField(default=0)
    r15 = models.IntegerField(default=0)
    r16 = models.IntegerField(default=0)
    r17 = models.IntegerField(default=0)
    r18 = models.IntegerField(default=0)
    r19 = models.IntegerField(default=0)
    r20 = models.IntegerField(default=0)
    r21 = models.IntegerField(default=0)
    r22 = models.IntegerField(default=0)
    r23 = models.IntegerField(default=0)
    r24 = models.IntegerField(default=0)
    r25 = models.IntegerField(default=0)
    r26 = models.IntegerField(default=0)
    r27 = models.IntegerField(default=0)
    r28 = models.IntegerField(default=0)
    r29 = models.IntegerField(default=0)
    r30 = models.IntegerField(default=0)
    r31 = models.IntegerField(default=0)
    r32 = models.IntegerField(default=0)
    r33 = models.IntegerField(default=0)

    def __str__(self):
        '''
        :return qishu temporaly:
        '''
        return str(self.qishu+" R")

class BData(models.Model):
    qishu = models.IntegerField(primary_key=True)
    riqi = models.DateField()
    b1 = models.IntegerField(default=0)
    b2 = models.IntegerField(default=0)
    b3 = models.IntegerField(default=0)
    b4 = models.IntegerField(default=0)
    b5 = models.IntegerField(default=0)
    b6 = models.IntegerField(default=0)
    b7 = models.IntegerField(default=0)
    b8 = models.IntegerField(default=0)
    b9 = models.IntegerField(default=0)
    b10 = models.IntegerField(default=0)
    b11 = models.IntegerField(default=0)
    b12 = models.IntegerField(default=0)
    b13 = models.IntegerField(default=0)
    b14 = models.IntegerField(default=0)
    b15 = models.IntegerField(default=0)
    b16 = models.IntegerField(default=0)


    def __str__(self):
        '''
        :return qishu temporaly:
        '''
        return str(self.qishu+" B")