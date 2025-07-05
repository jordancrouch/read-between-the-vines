from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404


class Books(models.Model):
    """
    Books model.

    This model contains the information for each book entry.

    Attributes:
        title (CharField): the title of the book (unique).
        slug (SlugField): the path used for the book page in URL-friendly format (unique).
        excerpt (TextField): the book excerpt displayed beneath the title on the book listings and single pages (can be left blank).
        content (TextField): the full content for the book displayed for each single book page.
        featured_image (CloudinaryField): the image used as the book featured image, generally the book cover (default: placeholder).
        created_on (DateTimeField): auto-generated timestamp of when the book was created.
        updated_on (DateTimeField): auto-generated timestamp of when the book was last updated/edited.
        status (IntegerField): the published status of the book (draft/published, default: draft).
        category (CharField): the reading status category of the book.
    """

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


class Comment(models.Model):
    """
    Comment model.

    This model contains the information for each comment entry.

    Attributes:
        book (ForeignKey): the book entry that this comment is assigned to.
        author (ForeignKey): the author (user) who submitted the comment.
        body (TextField): the actual comment text submitted.
        approved (BolleanField): the approval status of the comment (false/true, default: false).
        created_on (DateTimeField): auto-generated timestamp of when the comment was created.
    """

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        status = "Approved" if self.approved else "Awaiting approval"
        return f"Comment: {self.body} by {self.author} | Status: {status}"

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body: models.TextField = models.TextField()
    approved: models.BooleanField = models.BooleanField(default=False)
    created_on: models.DateTimeField = models.DateTimeField(auto_now_add=True)


class ReadingProgress(models.Model):
    """
    Reading Progress model.

    This model contains the information relating to the reading progress for each book.

    Attributes:
        user (ForeignKey): the user who submitted the reading progress.
        book (ForeignKey): the book entry that the reading progress is assigned to.
        percentage (PositiveIntegerField): the reading progress value (default: 0).
        created_on (DateTimeField): auto-generated timestamp of when the reading progress was created.
        updated_on (DateTimeField): auto-generated timestamp of when the reading progress was last edited/updated.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Books", on_delete=models.CASCADE, related_name="progress")
    percentage = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.percentage}%)"
