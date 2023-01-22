from django.db import models

# Create your models here.


class Course(models.Model):
    crs_id = models.PositiveSmallIntegerField(verbose_name="Course ID")

#we can create optional input field by using (blank=True, null=True):
    crs_name = models.CharField(verbose_name="Course Name", max_length=20, blank=True, null=True)

    crs_credit = models.PositiveSmallIntegerField(verbose_name="Course Credit", default=4)
    crs_at_marks = models.DecimalField(verbose_name="Attendence Full Marks", max_digits=5, decimal_places=2, default=10)
    crs_ct_marks = models.DecimalField(verbose_name="CT Full Marks", max_digits=5, decimal_places=2, default=40)
    crs_mid_marks = models.DecimalField(verbose_name="MID Full Marks", max_digits=5, decimal_places=2, default=100)
    crs_final_marks = models.DecimalField(verbose_name="Final Full Marks", max_digits=5, decimal_places=2, default=150)

# To return the object in CUSTOM_NAME:
    def __str__(self):
        if self.crs_name:       #
            return str(self.crs_name)     #return data type must be "String"
        else:
            return "Course Name is not Defined"    #default is "None"