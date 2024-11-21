### **Django Models**

In Django, models are Python classes that define the structure of your database tables. Each model corresponds to a single table in the database, and the attributes of the model correspond to the columns of the table. Django's Object-Relational Mapping (ORM) handles interactions between the models and the database.

---

### **1. Key Features of Django Models**

1. **Data Representation**: Each model represents a table in the database.
2. **Automatic Table Creation**: Django automatically creates database tables based on model definitions.
3. **Relationships**: Models can define relationships such as one-to-one, one-to-many, and many-to-many.
4. **Validation**: Field-level validation ensures data integrity.
5. **Query Interface**: Django ORM provides an intuitive API for querying data.

---

### **2. Creating a Model**

A Django model is a Python class that inherits from `django.db.models.Model`.

#### **Example**
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # A string field with a max length of 100
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field for monetary values
    description = models.TextField()  # A field for large text
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to the current date and time
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp whenever the record is saved

    def __str__(self):
        return self.name  # Defines how objects of this model are represented as strings
```

---

### **3. Common Field Types**

| **Field Type**          | **Description**                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------|
| `CharField`             | Stores short text, requires a `max_length` parameter.                                             |
| `TextField`             | Stores long text.                                                                                 |
| `IntegerField`          | Stores integers.                                                                                  |
| `FloatField`            | Stores floating-point numbers.                                                                    |
| `DecimalField`          | Stores decimal numbers, requires `max_digits` and `decimal_places`.                               |
| `DateField`             | Stores dates.                                                                                     |
| `DateTimeField`         | Stores date and time.                                                                              |
| `BooleanField`          | Stores `True` or `False` values.                                                                  |
| `ForeignKey`            | Defines a many-to-one relationship.                                                               |
| `ManyToManyField`       | Defines a many-to-many relationship.                                                              |
| `OneToOneField`         | Defines a one-to-one relationship.                                                                |
| `ImageField`            | Stores image files.                                                                               |
| `FileField`             | Stores files.                                                                                     |

---

### **4. Relationships in Django Models**

1. **One-to-Many Relationship (`ForeignKey`)**
   ```python
   class Author(models.Model):
       name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
   ```

2. **Many-to-Many Relationship (`ManyToManyField`)**
   ```python
   class Tag(models.Model):
       name = models.CharField(max_length=50)

   class Post(models.Model):
       title = models.CharField(max_length=100)
       tags = models.ManyToManyField(Tag)
   ```

3. **One-to-One Relationship (`OneToOneField`)**
   ```python
   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField()
   ```

---

### **5. Meta Options**

Django models have an inner class `Meta` to define additional behavior for the model.

#### **Example**
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']  # Default ordering by name
        verbose_name = 'Product'  # Singular name for admin
        verbose_name_plural = 'Products'  # Plural name for admin
```

---

### **6. Model Methods**

You can define custom methods in your models to add business logic.

#### **Example**
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField()

    def discounted_price(self):
        return self.price - (self.price * (self.discount_percentage / 100))
```

---

### **7. Querying Models**

Django provides a QuerySet API to interact with models.

#### **Basic Queries**
```python
# Retrieve all products
products = Product.objects.all()

# Filter products by price
cheap_products = Product.objects.filter(price__lt=50)

# Get a single product
product = Product.objects.get(id=1)

# Count products
count = Product.objects.count()
```

#### **Chaining Queries**
```python
# Filter and order products
products = Product.objects.filter(price__lt=50).order_by('name')
```

---

### **8. Migration Workflow**

1. **Create or Update a Model**:
   - Modify your models in `models.py`.

2. **Generate Migrations**:
   ```bash
   python manage.py makemigrations
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

---

### **9. Advanced Features**

#### **Model Managers**
Model Managers allow customization of queries.
```python
class ProductManager(models.Manager):
    def expensive_products(self):
        return self.filter(price__gt=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()
```

#### **Signals**
Django signals allow you to hook into model events.
```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Product)
def product_saved(sender, instance, **kwargs):
    print(f"Product {instance.name} has been saved.")
```

---

### **10. Summary**

| **Feature**            | **Description**                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| **Models**              | Represent database tables as Python classes.                                                              |
| **Fields**              | Define the structure of data stored in the database.                                                      |
| **Relationships**       | Represent links between models (e.g., ForeignKey, ManyToManyField).                                       |
| **ORM Queries**         | Retrieve, filter, and manipulate data using the QuerySet API.                                             |
| **Meta Options**        | Customize model behavior like ordering, verbose names, etc.                                               |
| **Migrations**          | Automatically create and apply database schema changes.                                                   |
| **Custom Methods**      | Add business logic to models.                                                                             |
| **Signals**             | Perform actions when specific events occur (e.g., saving or deleting an instance).                        |

Django models are a central part of any Django application, enabling seamless interaction between Python code and the database. Let me know if you need more details or examples!
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
