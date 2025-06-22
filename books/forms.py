from django import forms

from .models import Comment, ReadingProgress


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class ReadingProgressForm(forms.ModelForm):
    class Meta:
        model = ReadingProgress
        fields = ["percentage"]
        widgets = {
            "percentage": forms.NumberInput(attrs={"min": 0, "max": 100}),
        }
