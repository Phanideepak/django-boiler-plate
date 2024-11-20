# File Uploads

File uploads in Django allow users to upload files to your application and store them on the server or a cloud service. Django provides built-in tools to handle file uploads efficiently, including handling the upload process, validation, and storage.

---

### Key Steps for File Uploads in Django

1. **Set Up a Model**
2. **Create a Form**
3. **Write a View**
4. **Configure Media Settings**
5. **Update URLs**
6. **Create a Template**

---

### Step-by-Step Example

#### 1. Configure **Media Settings** in `settings.py`
Define where uploaded files will be stored and how they will be served.

```python
import os

MEDIA_URL = '/media/'  # URL to access uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directory to store uploaded files
```

---

#### 2. Define a **Model**
Create a model to store file information.

```python
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')  # Uploads to media/documents/
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

---

#### 3. Create a **Form**
Use Django's `forms.ModelForm` to create a file upload form.

```python
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']
```

---

#### 4. Write a **View**
Handle file uploads using Django's `request.FILES`.

```python
from django.shortcuts import render, redirect
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)  # Handle POST data and files
        if form.is_valid():
            form.save()  # Save the file
            return redirect('file_list')  # Redirect after successful upload
    else:
        form = DocumentForm()
    
    return render(request, 'upload.html', {'form': form})
```

---

#### 5. Create a **Template**
Create an HTML template for file upload.

```html
<!DOCTYPE html>
<html>
<head>
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

---

#### 6. Serve Uploaded Files
Update your `urls.py` to serve media files during development.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your other URL patterns...
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### Display Uploaded Files
Create a view to display a list of uploaded files.

**View:**
```python
from django.shortcuts import render
from .models import Document

def file_list(request):
    files = Document.objects.all()
    return render(request, 'file_list.html', {'files': files})
```

**Template (`file_list.html`):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Uploaded Files</title>
</head>
<body>
    <h1>Uploaded Files</h1>
    <ul>
        {% for file in files %}
            <li>
                <a href="{{ file.file.url }}">{{ file.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

### Handling Validation and File Types
You can validate file uploads by:
- **Restricting file size**: 
  ```python
  def clean_file(self):
      file = self.cleaned_data['file']
      if file.size > 5 * 1024 * 1024:  # 5 MB limit
          raise forms.ValidationError("File size exceeds 5 MB")
      return file
  ```

- **Restricting file types**:
  ```python
  import mimetypes

  def clean_file(self):
      file = self.cleaned_data['file']
      allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
      if file.content_type not in allowed_types:
          raise forms.ValidationError("Unsupported file type")
      return file
  ```

---

### Storing Files in Cloud Services
For production, you can use **cloud storage services** like Amazon S3, Google Cloud Storage, or Azure Blob Storage. Install and configure Django storage backends like **`django-storages`** for seamless integration.

Example using Amazon S3:
1. Install `boto3` and `django-storages`.
   ```bash
   pip install boto3 django-storages
   ```
2. Update your `settings.py`:
   ```python
   DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
   AWS_ACCESS_KEY_ID = 'your-access-key'
   AWS_SECRET_ACCESS_KEY = 'your-secret-key'
   AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
   ```

This setup ensures scalability and reliability for file storage in production environments.