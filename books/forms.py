from django import forms

from .models import Comment, ReadingProgress


class CommentForm(forms.ModelForm):
    """
    A simple form for submitting comments on a book.

    Attributes:
        model (Model): the Comment model.
        fields (tuple): the field(s) to allow user input for.

    """

    class Meta:
        model = Comment
        fields = ("body",)


class ReadingProgressForm(forms.ModelForm):
    """
    A form for submitting reading progress changes for books.

    Attributes:
        model (Model): the ReadingProgress model.
        fields (list): the field(s) to allow user input for.
        widgets (dict): custom widget(s) used to render form fields.

    """

    class Meta:
        model = ReadingProgress
        fields = ["percentage"]
        widgets = {
            "percentage": forms.NumberInput(attrs={"min": 0, "max": 100}),
        }


class ContactForm(forms.Form):
    """
    A basic contact form for users to send messages from.

    Attributes:
        name (CharField): a field users to input their name (limited to 100 characters).
        email (EmailField): a field for users to input their email address.
        message (CharField): a field for users to inpute their message, rendered as a text area to allow for multiple lines.

    """

    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
