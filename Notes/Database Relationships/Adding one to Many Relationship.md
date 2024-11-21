# One to Many RelationShips

A **one-to-many relationship** in Django is implemented using a `ForeignKey` field. Here's a step-by-step guide to defining and working with one-to-many relationships in Django:

---

### **1. Define the Models**

In your `models.py` file, create two models where one model contains a `ForeignKey` to the other.

#### Example: Blog and Comments Relationship
```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog.title}"
```

---

### **2. Explanation of Fields**

- **`ForeignKey`**: This creates a one-to-many relationship. Each `Comment` is linked to one `Blog`, but a `Blog` can have many `Comments`.
  - `on_delete=models.CASCADE`: Ensures that when a `Blog` is deleted, all its related `Comments` are also deleted.
  - `related_name="comments"`: Allows you to access related comments from a `Blog` object using `blog_instance.comments.all()`.
  
---

### **3. Register Models in Admin**

In `admin.py`, register both models so they appear in the admin panel.

```python
from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'created_at')
```

---

### **4. Apply Migrations**

Run the following commands to create the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **5. Query the One-to-Many Relationship**

You can query the relationship in both directions:

- **Get all comments for a blog:**
  ```python
  blog = Blog.objects.get(id=1)
  comments = blog.comments.all()  # Uses the `related_name`
  ```

- **Get the blog for a specific comment:**
  ```python
  comment = Comment.objects.get(id=1)
  blog = comment.blog
  ```

---

### **6. Additional Features**

- **Inline Admin for Comments:**
  You can display `Comment` entries directly within the `Blog` admin page.
  ```python
  class CommentInline(admin.TabularInline):
      model = Comment
      extra = 1

  @admin.register(Blog)
  class BlogAdmin(admin.ModelAdmin):
      inlines = [CommentInline]
  ```

- **Validation:**
  Add custom validation to the models by overriding the `clean` method or using Django Forms.

---

With these steps, you now have a working one-to-many relationship in Django!