from django import forms

class ResumeForm(forms.Form):
    career_objective = forms.CharField(widget=forms.Textarea, required=True)
    academic_details = forms.CharField(widget=forms.Textarea, required=True)
    current_status = forms.CharField(required=True)
    areas_of_interest = forms.CharField(widget=forms.Textarea, required=True)
    professional_skills = forms.CharField(widget=forms.Textarea, required=True)
    personal_skills = forms.CharField(widget=forms.Textarea, required=True)
    work_experience = forms.CharField(widget=forms.Textarea, required=True)
    academic_activities = forms.CharField(widget=forms.Textarea, required=True)
    extracurricular_activities = forms.CharField(widget=forms.Textarea, required=True)
    personal_profile = forms.CharField(widget=forms.Textarea, required=True)
    declaration = forms.CharField(widget=forms.Textarea, required=True)
    date = forms.DateField()
    place = forms.CharField(required=True)
