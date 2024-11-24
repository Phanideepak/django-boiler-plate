### **Deleting in Django Models**

Django provides several ways to delete records from the database using the ORM. You can delete individual objects, multiple objects, or even entire model instances.

---

### **1. Deleting Individual Records**

To delete a single record, first retrieve the object using a query, then call the `.delete()` method on it.

#### **Example**
```python
# Assuming a Product model
from myapp.models import Product

# Retrieve a single product by its ID
product = Product.objects.get(id=1)

# Delete the product
product.delete()
```

- The `delete()` method will remove the object from the database.
- If the object does not exist, Django will raise a `DoesNotExist` exception.

---

### **2. Deleting Multiple Records**

To delete multiple records, use the `filter()` or `all()` method and call `.delete()` on the resulting QuerySet.

#### **Example**
```python
# Delete all products with a price less than 50
Product.objects.filter(price__lt=50).delete()

# Delete all records in the Product table
Product.objects.all().delete()
```

---

### **3. Cascading Deletes**

When deleting objects with relationships (e.g., `ForeignKey`), the behavior depends on the `on_delete` option specified in the related field.

#### **Example**
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- If an `Author` instance is deleted, all related `Book` instances will also be deleted because of `on_delete=models.CASCADE`.

---

### **4. Deleting with Signals**

You can perform additional actions when an object is deleted by using the `post_delete` or `pre_delete` signals.

#### **Example**
```python
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from myapp.models import Product

@receiver(pre_delete, sender=Product)
def before_product_delete(sender, instance, **kwargs):
    print(f"Product '{instance.name}' is about to be deleted.")
```

---

### **5. Restrictions on Deletion**

- **Protected Relationships**:
  Use `on_delete=models.PROTECT` to prevent the deletion of related objects.
  ```python
  class Book(models.Model):
      title = models.CharField(max_length=100)
      author = models.ForeignKey(Author, on_delete=models.PROTECT)
  ```

  In this case, attempting to delete an `Author` instance will raise a `ProtectedError` if it is referenced by any `Book` instance.

- **Soft Deletes**:
  Instead of permanently deleting records, you can implement a "soft delete" by adding a `is_deleted` field to the model and filtering out deleted records in queries.
  ```python
  class Product(models.Model):
      name = models.CharField(max_length=100)
      is_deleted = models.BooleanField(default=False)

      def delete(self, using=None, keep_parents=False):
          self.is_deleted = True
          self.save()
  ```

---

### **6. Example Usage**

#### **Model Definition**
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

#### **Deleting Objects**
```python
# Delete a specific product
product = Product.objects.get(id=1)
product.delete()

# Delete all products under $50
Product.objects.filter(price__lt=50).delete()

# Delete all products
Product.objects.all().delete()
```

---

### **7. Summary**

| **Method**                        | **Description**                                                                                                                                             |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `.delete()` (on an object)        | Deletes a single instance from the database.                                                                                                                |
| `.delete()` (on a QuerySet)       | Deletes all objects in the QuerySet.                                                                                                                        |
| `on_delete=models.CASCADE`        | Deletes related objects automatically when the referenced object is deleted.                                                                                 |
| `on_delete=models.PROTECT`        | Prevents deletion of the referenced object if it is related to others.                                                                                       |
| **Soft Deletes**                  | Mark records as deleted without removing them from the database (requires custom implementation).                                                            |
| **Signals** (`pre_delete`, `post_delete`) | Allows executing additional logic before or after deletion.                                                                                              |

Let me know if you'd like more help implementing any of these approaches! 🚀