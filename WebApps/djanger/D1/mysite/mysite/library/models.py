from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        "Name", max_length=200, help_text="Enter the name of the book genre."
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        "Book",
        max_length=200,
    )
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        "Description", max_length=1000, help_text="Enter the description of the book."
    )
    isbn = models.CharField("ISBN", max_length=13)
    genre = models.ManyToManyField(Genre, help_text="Pick a genre for this book.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])


class Author(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique identifier for the book copy.",
    )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField("Available on", null=True, blank=True)

    LOAN_STATUS = (
        ("a", "Administered"),
        ("p", "Picked"),
        ("g", "Good for picking"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, default="a", help_text="Status"
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id} {self.book.title}"
