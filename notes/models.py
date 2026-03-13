from django.db import models


class Note(models.Model):
    """
    Model representing a single sticky note.
    """

    # Title of the note
    title = models.CharField(max_length=255)

    # Main content of the note
    content = models.TextField()

    # Auto timestamp when created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation.
        """
        return self.title
