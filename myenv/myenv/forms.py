from django import forms

class student(forms.Form):
    name = forms.CharField(max_length=100, label = 'Student name', widget=forms.TextInput(attrs=({'class': 'forms-control'})))
    stu_id=forms.CharField(max_length=100, label = 'Student Id')
    stu_addr=forms.CharField(max_length=100, label = 'Student Address')
    stu_dep=forms.CharField(max_length=100, label = 'Student Department')
    stu_result=forms.CharField(max_length=100, label = 'Student Result')
    stu_mail=forms.CharField(max_length=100, label = 'Student Mail')
    stu_phone=forms.CharField(max_length=100, label = 'Student Phone')
