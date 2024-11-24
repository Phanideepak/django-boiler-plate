Uploading and managing images in Django can be easily handled using the `ImageField` in a Django model. Here’s a step-by-step guide to implement an image upload feature:

---

### **1. Prerequisites**

Ensure the following dependencies are installed:

- **Pillow**: A Python Imaging Library required to handle image files.

Install Pillow:
```bash
pip install pillow
```

---

### **2. Define the Model**

Use the `ImageField` in your model to handle image uploads.

```python
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')  # Directory where images will be stored

    def __str__(self):
        return self.name
```

- `upload_to='profile_pictures/'`: Specifies the directory inside the `MEDIA_ROOT` where the uploaded files will be saved.

---

### **3. Configure Settings**

Add configurations for media files in `settings.py`:

```python
import os

MEDIA_URL = '/media/'  # URL for serving media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Path where media files are stored
```

---

### **4. Update URLs**

Serve media files during development by adding the following to your `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
]

# Add media file serving
if settings.DEBUG:  # Only serve during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### **5. Create a Form**

Create a form to handle file uploads using `forms.ModelForm`:

```python
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'profile_picture']
```

---

### **6. Create a View**

Handle the form submission and save the uploaded image in your view:

```python
from django.shortcuts import render, redirect
from .forms import ProfileForm

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)  # Handle both data and file uploads
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the same page or another after saving
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})
```

---

### **7. Create a Template**

Create a template (`profile.html`) with an HTML form to upload files:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Profile Upload</title>
</head>
<body>
    <h1>Upload Profile</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

- `enctype="multipart/form-data"`: Required to handle file uploads.
- `{% csrf_token %}`: Adds protection against CSRF attacks.

---

### **8. Access Uploaded Files**

After a successful upload, the images will be stored in the `media/profile_pictures/` directory (as per the `upload_to` configuration).

You can access the uploaded images in your templates like this:
```html
<img src="{{ profile.profile_picture.url }}" alt="Profile Picture">
```

---

### **9. Serving Media in Production**

In production, configure your web server (e.g., Nginx or Apache) to serve media files from the `MEDIA_ROOT` directory. Django does not handle this automatically in production.

---

With this setup, you can handle image uploads using the `ImageField` in Django! Let me know if you need help with any part of this process.