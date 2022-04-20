from django.db import models


class Author(models.Model):
    email = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.email}"


class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return f"{self.owner.email}-{self.title}"
