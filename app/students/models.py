from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    start_datetime = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    min_participants = models.IntegerField
    max_participants = models.IntegerField

    def __str__(self):
        return f"{str(self.id)} {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100, default="unnamed subject")
    video_link = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="subjects",
    )

    def __str__(self):
        return f"{str(self.id)} {self.name}"


class Group(models.Model):
    name = models.CharField(max_length=100)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="groups",
    )

    def __str__(self):
        return f"{str(self.id)} {self.name}"


class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    course = models.CharField(max_length=100)

    group = models.ManyToManyField(
        Group,
        related_name="users",
    )

    def __str__(self):
        return f"{str(self.id)} {self.f_name} {self.l_name} {self.email}"
