from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

slug = models.SlugField()

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="recipes")
    created_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    meal_type = models.CharField(max_length=50)
    meal_tags = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="recipe_likes",
                                blank=True)

    class Meta:
        ordering = ["-created_on"]

    prepopulated_fields = {'slug': ('title',)}

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                                related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="user_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
