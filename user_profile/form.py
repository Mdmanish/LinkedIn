from django import forms
from .models import Experience, Education, Certificates, Skills, Languages


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('user','title','company','job_type','joining_date','leaving_date','duration','description')


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('user','college','course','starting_date','end_date')


class CertificatesForm(forms.ModelForm):

    class Meta:
        model = Certificates
        fields = ('user','title','organisation','issue_date','expiry_date')


class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = '__all__'


class LanguagesForm(forms.ModelForm):

    class Meta:
        model = Languages
        fields = '__all__'
