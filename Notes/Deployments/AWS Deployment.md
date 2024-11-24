Deploying a Django app to AWS involves several steps, including setting up your AWS infrastructure, preparing your Django application, and configuring deployment. Below is a step-by-step guide:

---

### **1. Prepare Your Django Application**
1. **Install Required Packages:**
   - Ensure `django`, `gunicorn`, and database drivers (e.g., `psycopg2` for PostgreSQL) are installed in your project.
   ```bash
   pip install gunicorn psycopg2
   ```
2. **Configure Settings for Production:**
   - Set `DEBUG = False` in `settings.py`.
   - Add your AWS instance's public IP or domain name to `ALLOWED_HOSTS`:
     ```python
     ALLOWED_HOSTS = ['your-instance-ip', 'your-domain.com']
     ```
   - Configure static and media files:
     ```python
     STATIC_URL = '/static/'
     STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
     MEDIA_URL = '/media/'
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
     ```

3. **Collect Static Files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Set Up a Production Database:**
   - Use a cloud database service like AWS RDS or install a database server on your EC2 instance.

---

### **2. Launch an AWS EC2 Instance**
1. **Log in to AWS Management Console** and navigate to the EC2 dashboard.
2. **Create an EC2 Instance:**
   - Choose an Amazon Machine Image (AMI), such as Ubuntu or Amazon Linux.
   - Select an instance type (e.g., `t2.micro` for small projects).
   - Configure security groups to allow SSH (port 22), HTTP (port 80), and HTTPS (port 443) traffic.

3. **Connect to Your Instance:**
   - Use SSH to connect to the instance:
     ```bash
     ssh -i your-key.pem ubuntu@your-ec2-public-ip
     ```

---

### **3. Set Up the Server Environment**
1. **Update and Install Required Software:**
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install python3-pip python3-venv nginx
   ```

2. **Create a Virtual Environment and Install Dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install django gunicorn psycopg2
   ```

3. **Upload Your Django Project:**
   - Use `scp` or tools like `FileZilla` to upload your project files to the server.

4. **Migrate the Database:**
   ```bash
   python manage.py migrate
   ```

---

### **4. Configure Gunicorn**
1. **Test Gunicorn Locally:**
   ```bash
   gunicorn --bind 0.0.0.0:8000 your_project_name.wsgi:application
   ```

2. **Create a Gunicorn Systemd Service:**
   - Create a service file: `/etc/systemd/system/gunicorn.service`
     ```ini
     [Unit]
     Description=gunicorn daemon
     After=network.target

     [Service]
     User=ubuntu
     Group=www-data
     WorkingDirectory=/path/to/your/project
     ExecStart=/path/to/your/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/project/gunicorn.sock your_project_name.wsgi:application

     [Install]
     WantedBy=multi-user.target
     ```
   - Enable and start the service:
     ```bash
     sudo systemctl start gunicorn
     sudo systemctl enable gunicorn
     ```

---

### **5. Configure Nginx**
1. **Set Up Nginx as a Reverse Proxy:**
   - Create a configuration file for your site: `/etc/nginx/sites-available/your_project`
     ```nginx
     server {
         listen 80;
         server_name your-domain.com;

         location = /favicon.ico { access_log off; log_not_found off; }
         location /static/ {
             root /path/to/your/project;
         }

         location / {
             include proxy_params;
             proxy_pass http://unix:/path/to/your/project/gunicorn.sock;
         }
     }
     ```
   - Enable the site and restart Nginx:
     ```bash
     sudo ln -s /etc/nginx/sites-available/your_project /etc/nginx/sites-enabled
     sudo nginx -t
     sudo systemctl restart nginx
     ```

2. **Update Security Group:**
   - Ensure port 80 (HTTP) and 443 (HTTPS) are open in your EC2 instance's security group.

---

### **6. Optional: Set Up a Domain and SSL**
1. **Point Your Domain to the EC2 Instance:**
   - Update your domain's DNS settings to point to the instance's public IP.

2. **Install SSL with Certbot:**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

---

### **7. Test and Monitor**
1. Visit your domain or public IP to ensure the site is working.
2. Monitor server logs for issues:
   ```bash
   sudo journalctl -u gunicorn
   sudo tail -f /var/log/nginx/error.log
   ```

---