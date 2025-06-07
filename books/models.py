from django.db import models


# Create your models here.
class Books(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Draft"
        PUBLISHED = 1, "Published"

    class ReadingStatus(models.TextChoices):
        TO_BE_READ = "TBR", "To Be Read"
        CURRENTLY_READING = "CR", "Currently Reading"
        FINISHED_READING = "FR", "Finished Reading"

    title: models.CharField = models.CharField(max_length=100, unique=True)
    slug: models.SlugField = models.SlugField(max_length=100, unique=True)
    content: models.TextField = models.TextField()
    created_on: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    status: models.IntegerField = models.IntegerField(
        choices=Status.choices, default=Status.DRAFT
    )
    category: models.CharField = models.CharField(
        max_length=3,
        choices=ReadingStatus.choices,
        default=ReadingStatus.TO_BE_READ,
    )
