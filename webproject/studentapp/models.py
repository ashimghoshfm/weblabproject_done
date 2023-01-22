from django.db import models

# Create your models here.

class Program(models.Model):
    program_name = models.CharField(verbose_name="Program Name", max_length=30)

    def __str__(self):
        return str(self.program_name)


class Student(models.Model):
    st_id = models.SmallIntegerField(verbose_name="Student ID")
    st_name = models.CharField(verbose_name="Student Name", max_length=20)
    st_dist = models.CharField(verbose_name="District", max_length=20)
    st_dob = models.DateField(verbose_name="Birth Date", max_length=20)
    st_edate = models.DateField(verbose_name="Enroll Date")
    st_program = models.ForeignKey(Program, on_delete= models.CASCADE,verbose_name="Program Name")
    st_gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.st_id)