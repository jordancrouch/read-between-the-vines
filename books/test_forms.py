from django.test import TestCase

from .forms import CommentForm, ContactForm, ReadingProgressForm


class TestCommentForm(TestCase):
    """
    Test that the comment form is valid
    """

    def test_form_is_valid(self):
        comment_form = CommentForm({"body": "This is a great book!"})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        comment_form = CommentForm({"body": ""})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestReadingProgressForm(TestCase):
    """
    Test that the reading progress form is valid
    """

    def test_form_is_valid(self):
        reading_progress_form = ReadingProgressForm({"percentage": 100})
        self.assertTrue(reading_progress_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        reading_progress_form = ReadingProgressForm({"percentage": ""})
        self.assertFalse(reading_progress_form.is_valid(), msg="Form is valid")


class TestContactForm(TestCase):
    """
    Test that the contact form is valid
    """

    def test_form_is_valid(self):
        """
        Test all form fields
        """
        contact_form = ContactForm(
            {
                "name": "John Doe",
                "email": "test@test.com",
                "message": "Test contact form message",
            }
        )
        self.assertTrue(contact_form.is_valid(), msg="Form is invalid")

    def test_name_is_required(self):
        """
        Test that the name field is required
        """
        contact_form = ContactForm(
            {
                "name": "",
                "email": "test@test.com",
                "message": "Test contact form message",
            }
        )
        self.assertFalse(
            contact_form.is_valid(), msg="Form is valid, but a name was not provided"
        )

    def test_email_is_required(self):
        """
        Test that the email field is required
        """
        contact_form = ContactForm(
            {
                "name": "John Doe",
                "email": "",
                "message": "Test contact form message",
            }
        )
        self.assertFalse(
            contact_form.is_valid(), msg="Form is valid, but an email was not provided"
        )

    def test_message_is_required(self):
        """
        Test that the message field is required
        """
        contact_form = ContactForm(
            {
                "name": "",
                "email": "",
                "message": "Test contact form message",
            }
        )
        self.assertFalse(
            contact_form.is_valid(), msg="Form is valid, but a message was not provided"
        )

    def test_form_is_invalid(self):
        contact_form = ContactForm({"name": "", "email": "", "message": ""})
        self.assertFalse(contact_form.is_valid(), msg="Form is valid")
