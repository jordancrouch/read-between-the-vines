from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import CommentForm, ContactForm, ReadingProgressForm
from .models import Books, ReadingProgress


class TestBooksViews(TestCase):
    """
    Testing book detail views, forms, and functionality
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="testSuperUser",
            password="testSuperUserPassword",
            email="test1@test.com",
        )
        self.user = User.objects.create_user(
            username="testUser", password="testUserPassword", email="test2@test.com"
        )
        self.book = Books(
            title="Book title",
            slug="book-title",
            excerpt="Book excerpt",
            content="Book content",
            status=1,
            category="CR",
        )
        self.book.save()

        ReadingProgress.objects.create(user=self.user, book=self.book, percentage=60)

    def test_render_book_detail_page_with_forms(self):
        """
        Test for rendering book detail view with reading progress and comment forms
        """
        response = self.client.get(reverse("books:book_detail", args=["book-title"]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book title", response.content)
        self.assertIn(b"Book content", response.content)
        self.assertIsInstance(response.context["progress_form"], ReadingProgressForm)
        self.assertIsInstance(response.context["comment_form"], CommentForm)

    def test_successful_reading_progress_submission(self):
        """
        Test for submitting reading progress on a book
        """
        self.client.login(username="testSuperUser", password="testSuperUserPassword")
        progress_data = {"percentage": 100, "progress_submit": "Update Progress"}
        response = self.client.post(
            reverse("books:book_detail", args=["book-title"]),
            progress_data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Reading progress updated!")

    def test_book_category_auto_update(self):
        """
        Test that the book category changes to 'Finished Reading' when average progress is equal to, or greater than, 80%
        """

        self.client.login(username="testSuperUser", password="testSuperUserPassword")

        progress_data = {"percentage": 100, "progress_submit": "Update Progress"}
        self.client.post(
            reverse("books:book_detail", args=["book-title"]),
            progress_data,
            follow=True,
        )

        self.book.refresh_from_db()
        self.assertEqual(self.book.category, "FR")

    def test_successful_comment_submission(self):
        """
        Test for posting a comment on a book
        """
        self.client.login(username="testSuperUser", password="testSuperUserPassword")
        comment_data = {"body": "This is a test comment.", "comment_submit": "Submit"}
        response = self.client.post(
            reverse("books:book_detail", args=["book-title"]), comment_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Comment submitted and awaiting approval.")


def TestContactView(TestCase):
    """
    Tests for the contact page view
    """

    def test_render_contact_page_with_form(self):
        """
        Test for rendering contact page with contact form
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIsInstance(response.context["form"], ContactForm)

    def test_successful_contact_form_submission(self):
        """
        Test for submitting the contact form on the contact page
        """
        contact_data = {
            "name": "John Smith",
            "email": "johnsmith@test.com",
            "message": "Test contact message.",
        }
        response = self.client.post(reverse("contact"), contact_data, follow=True)
        self.assertEqual(response.status_code, 200)
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your message has been sent!")
