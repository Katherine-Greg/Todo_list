from django import forms

from todo_list_service.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
