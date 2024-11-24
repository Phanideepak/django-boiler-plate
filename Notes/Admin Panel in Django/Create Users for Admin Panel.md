To create a **User** and a **Superuser** in the Django admin panel or via the command line, follow these steps:

---

### **1. Using the Admin Panel**

1. **Log in to the Admin Panel:**
   - Start your Django development server:
     ```bash
     python manage.py runserver
     ```
   - Navigate to the admin panel in your web browser:
     ```
     http://127.0.0.1:8000/admin/
     ```
   - Log in with the superuser account you created earlier during the initial setup.

2. **Create a New User:**
   - In the admin panel, go to the **Users** section (usually under **Authentication and Authorization**).
   - Click **Add User**.
   - Fill out the fields:
     - Enter the username, password, and other details.
     - Optionally set permissions or assign groups.
   - Save the user.

3. **Create a Superuser:**
   - Follow the same steps as creating a regular user.
   - Ensure you check the **"Staff status"**, **"Superuser status"**, and **"Active"** boxes under **Permissions**.

---

### **2. Using the Command Line**

#### **Create a Superuser**
1. Open your terminal and run:
   ```bash
   python manage.py createsuperuser
   ```
2. Enter the required details when prompted:
   - Username
   - Email (optional)
   - Password (twice to confirm)

3. Your superuser is now created and can log in to the admin panel.

#### **Create a Regular User**
If you want to create a non-superuser via the command line:

1. Open the Django shell:
   ```bash
   python manage.py shell
   ```
2. Enter the following commands:
   ```python
   from django.contrib.auth.models import User

   # Create a regular user
   user = User.objects.create_user(
       username='newuser',
       email='newuser@example.com',
       password='password123'
   )
   user.save()

   print("Regular user created:", user)
   ```

3. Optionally, you can add groups or permissions for the user:
   ```python
   from django.contrib.auth.models import Permission

   # Add a permission
   permission = Permission.objects.get(codename='can_add_model')
   user.user_permissions.add(permission)
   ```

---

### **Additional Notes**
- To access the Django admin panel, ensure that `django.contrib.admin` is added to the `INSTALLED_APPS` list in your `settings.py`.
- If you want to customize user creation (e.g., adding custom fields), consider extending the `AbstractUser` model in your project. Let me know if you'd like guidance on this!


# Users for this Project.

Sample Super user: user = `admin`,email = `admin123@gmail.com`, pwd = `Alekya@736`