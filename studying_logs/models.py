from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is studying about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Add specifics syudied about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns string representation of the model."""
        return f"{self.text[:50]}..."
