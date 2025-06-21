from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Books model.
class Books(models.Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-created_on"]

    class Status(models.IntegerChoices):
        DRAFT = 0, "Draft"
        PUBLISHED = 1, "Published"

    class ReadingStatus(models.TextChoices):
        TO_BE_READ = "TBR", "To Be Read"
        CURRENTLY_READING = "CR", "Currently Reading"
        FINISHED_READING = "FR", "Finished Reading"

    @property
    def category_label(self):
        return self.get_category_display()

    def __str__(self):
        return f"{self.title} | Category: {self.category_label} | Status: {self.get_status_display()}"

    title: models.CharField = models.CharField(max_length=100, unique=True)
    slug: models.SlugField = models.SlugField(max_length=100, unique=True)
    excerpt: models.TextField = models.TextField(null=True, blank=True)
    content: models.TextField = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    created_on: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_on: models.DateTimeField = models.DateTimeField(auto_now=True)
    status: models.IntegerField = models.IntegerField(
        choices=Status.choices, default=Status.DRAFT
    )
    category: models.CharField = models.CharField(
        max_length=3,
        choices=ReadingStatus.choices,
        default=ReadingStatus.TO_BE_READ,
    )


# Comment model
class Comment(models.Model):
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        status = "Approved" if self.approved else "Awaiting approval"
        return f"Comment: {self.body} by {self.author} | Status: {status}"

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body: models.TextField = models.TextField()
    approved: models.BooleanField = models.BooleanField(default=False)
    created_on: models.DateTimeField = models.DateTimeField(auto_now_add=True)
