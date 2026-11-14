from django import forms

from .models import ProfileContact, Skill


class ContactForm(forms.ModelForm):

    class Meta:
        model = ProfileContact
        fields = ['name', 'email', 'subject', 'message']


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['skill_name', 'category', 'description']