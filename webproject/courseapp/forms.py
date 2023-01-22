from django import forms
from . import models



class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
#for better look:
        widgets = {
            "crs_id":forms.TextInput(attrs={'class':'form-control'}),
            "crs_name":forms.TextInput(attrs={'class':'form-control'}),
            "crs_credit":forms.TextInput(attrs={'class':'form-control'}),
            "crs_at_marks":forms.TextInput(attrs={'class':'form-control'}),
            "crs_ct_marks":forms.TextInput(attrs={'class':'form-control'}),
            "crs_mid_marks":forms.TextInput(attrs={'class':'form-control'}),
            "crs_final_marks":forms.TextInput(attrs={'class':'form-control'}),
        }
