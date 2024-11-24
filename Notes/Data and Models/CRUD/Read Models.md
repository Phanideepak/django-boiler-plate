# Read Models

- SELECT * FROM books ----> Book.objects.all()

- Filtering By Column nane ---> Book.objects.get(column_name = given_name)

- Filtering By multiple columns (AND) ---> Book.objects.get(col1 = val1, col2 = val2)

- Filtering by column less than val ---> Book.objects.get(col1__lt = val)

- Filtering by column less than or equal to val ---> Book.objects.get(col1__lte = val)

- Filtering by column greater than val ---> Book.objects.get(col2__gt = val)

- Filtering by column greater than or equal to val ---> Book.objects.get(col1__gte = val)

- Like Operator (string case sensitive) ---> Book.objects.get(col__contains = val)

- Like Operator (string case insensitive) ---> Book.objects.get(col__icontains = val)



# Or Condition:

- from django.db.models import Q
- OR Condition :  Book.objects.filter(Q(rating__lt = 5) | Q(is_bestselling = True)) 
- OR Condition AND Condition:  Book.objects.filter(Q(rating__lt = 5) | Q(is_bestselling = True), Q(author = 'JK Rowling'))




### **Reading Data in Django Models**

Reading data in Django involves retrieving records from the database using Django's **Object-Relational Mapping (ORM)**. Django provides a powerful and flexible QuerySet API to perform queries on your models.

---

### **1. QuerySet API Overview**

A **QuerySet** is a collection of database queries to retrieve objects from the database. QuerySets are lazy, meaning the database query is not executed until the data is accessed.

---

### **2. Retrieving All Records**

You can use the `.all()` method to retrieve all records of a model.

#### **Example**
```python
from myapp.models import Product

# Retrieve all products
products = Product.objects.all()
```

---

### **3. Filtering Data**

Use `.filter()` to retrieve records matching specific conditions. The method returns a QuerySet.

#### **Example**
```python
# Retrieve all products with a price less than 50
cheap_products = Product.objects.filter(price__lt=50)

# Retrieve products containing a specific keyword in the name
matching_products = Product.objects.filter(name__icontains="phone")
```

#### **Filter Lookup Examples**
| **Lookup**       | **Description**                                    | **Example**                                   |
|-------------------|----------------------------------------------------|-----------------------------------------------|
| `field__exact`    | Matches the exact value.                          | `price__exact=100`                           |
| `field__lt`       | Less than.                                        | `price__lt=50`                               |
| `field__lte`      | Less than or equal to.                            | `price__lte=50`                              |
| `field__gt`       | Greater than.                                     | `price__gt=50`                               |
| `field__gte`      | Greater than or equal to.                         | `price__gte=50`                              |
| `field__icontains`| Case-insensitive match.                           | `name__icontains='phone'`                    |
| `field__startswith`| Starts with.                                     | `name__startswith='Smart'`                   |
| `field__in`       | Matches any value in the given list.              | `id__in=[1, 2, 3]`                           |

---

### **4. Retrieving a Single Object**

Use `.get()` to retrieve a single object that matches a condition. If no object is found, it raises a `DoesNotExist` exception. If more than one object is found, it raises a `MultipleObjectsReturned` exception.

#### **Example**
```python
# Retrieve a product by its ID
product = Product.objects.get(id=1)
```

---

### **5. Ordering Results**

Use `.order_by()` to sort the results. By default, it sorts in ascending order. Prefix a field with a `-` for descending order.

#### **Example**
```python
# Order products by price (ascending)
products = Product.objects.order_by('price')

# Order products by price (descending)
products = Product.objects.order_by('-price')
```

---

### **6. Limiting Results**

Use slicing to limit the number of results returned by a QuerySet.

#### **Example**
```python
# Retrieve the first 5 products
products = Product.objects.all()[:5]

# Retrieve products from 5th to 10th
products = Product.objects.all()[5:10]
```

---

### **7. Aggregating Data**

Use aggregation functions like `Sum`, `Avg`, `Count`, `Max`, and `Min` for calculations.

#### **Example**
```python
from django.db.models import Sum, Avg, Count

# Total price of all products
total_price = Product.objects.aggregate(Sum('price'))

# Average price of products
average_price = Product.objects.aggregate(Avg('price'))

# Count of all products
product_count = Product.objects.aggregate(Count('id'))
```

---

### **8. Using QuerySet Methods**

| **Method**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| `.all()`            | Retrieves all objects.                                                         |
| `.filter()`         | Filters objects based on conditions.                                           |
| `.exclude()`        | Excludes objects that match a condition.                                       |
| `.get()`            | Retrieves a single object based on conditions.                                |
| `.order_by()`       | Orders the results based on fields.                                            |
| `.values()`         | Returns a QuerySet of dictionaries instead of model instances.                |
| `.values_list()`    | Returns a QuerySet of tuples with specific fields.                             |
| `.distinct()`       | Removes duplicate rows from the QuerySet.                                      |
| `.exists()`         | Returns `True` if the QuerySet contains any records, otherwise `False`.        |

---

### **9. Retrieving Related Data**

Django handles relationships between models efficiently.

#### **Example: ForeignKey**
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Retrieve books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books = author.book_set.all()
```

#### **Example: ManyToManyField**
```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

# Retrieve posts with a specific tag
tag = Tag.objects.get(name="Django")
posts = tag.post_set.all()
```

---

### **10. Query Optimization Tips**

1. **Select Specific Fields**: Use `.only()` or `.defer()` to optimize queries by loading only the fields you need.
   ```python
   # Load only the name and price fields
   products = Product.objects.only('name', 'price')
   ```

2. **Avoid N+1 Queries**: Use `.select_related()` for `ForeignKey` relationships and `.prefetch_related()` for `ManyToManyField`.
   ```python
   # Efficiently fetch related data
   books = Book.objects.select_related('author')
   ```

3. **Use `exists()`**: To check if any records exist, use `.exists()` instead of `.count()` for better performance.
   ```python
   # Check if there are any cheap products
   Product.objects.filter(price__lt=50).exists()
   ```

---

### **11. Complete Example**

#### **Model**
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### **Reading Data**
```python
from myapp.models import Product

# Retrieve all products
all_products = Product.objects.all()

# Filter products
cheap_products = Product.objects.filter(price__lt=50)

# Retrieve a single product
product = Product.objects.get(id=1)

# Order products by price
ordered_products = Product.objects.order_by('price')

# Aggregate data
total_price = Product.objects.aggregate(Sum('price'))

# Limit results
first_five_products = Product.objects.all()[:5]

# Related queries (with relationships)
related_products = Product.objects.select_related()
```

---

### **12. Summary**

| **Operation**          | **Method**                   | **Description**                                                             |
|-------------------------|------------------------------|-----------------------------------------------------------------------------|
| Retrieve all records    | `.all()`                    | Returns all records in the table.                                           |
| Filter records          | `.filter()`                 | Filters records based on conditions.                                        |
| Exclude records         | `.exclude()`                | Excludes records that match the condition.                                  |
| Single record retrieval | `.get()`                    | Retrieves a single record matching the condition.                           |
| Ordering records        | `.order_by()`               | Orders the records by a specific field.                                     |
| Aggregations            | `.aggregate()`              | Performs calculations like sum, average, count, etc.                        |
| Related data            | `.select_related()`         | Optimizes queries for ForeignKey relationships.                             |
| Existence check         | `.exists()`                 | Checks if the QuerySet contains any records.                                |

Let me know if you'd like detailed examples or further help with specific use cases! 🚀