from django.db import models


class PublishedModel(models.Model):
    """Abstract model that adds the `is_published` flag."""
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
