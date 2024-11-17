# Templates and Static Files
- Register the templates  with Django.
- Create templates folder insider module folder
- Use render_to_string in django.template.loader.
- ADD templates folder to `DIRS` - TEMPLATES in settings.py

# Use of render (django.shortcut) method
- render method is used to load templates in views folder.


# Django Template Language (DTL) and Variable Interpolation

- It helps Enable html files to create dynamic pages
- Standard Html Syntax + Special DTL Syntax
- We send parameters to `render` method in form of the dictionary. This parameters can be accessed in the template html file.


# Filters in DTL

- Django Template Engine provides filters which are used to transform the values of variables and tag arguments
- Syntax : {{ variable_name | filter_name }}
- Eg 1: {{ value | length }}
- Eg 2: {{text | title }}
- Eg 3 : {{value | add : "2"}}, If value is 4, It will display 6.


# Tags and For tag

- For Tag syntax :  {% for element in arr %} {% endfor %}



# URL Tag for dynamic urls in template

- URL Tag Syntax: {% url 'name of urls in urls.py' %}
  Eg:  {% url 'month-challenge' %}  
- URL Tag syntax with path parameter : {% url 'url_name' path_variable %}
  Eg:   {% url 'month-challenge' month %}


# If Tag for conditional in template

- If Tag syntax: {% if %} {% endif %}
- If elif Tag Syntax: {% if %} {% elif %} {% else %} {% endif %} 



# Template Inheritance

- Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.
- Eg: home template will inherit from sidebar, navbar, footer parent templates.
- Create a templates folder for main project. Create a base html file and add the below syntax:
  - {% block %} {% endblock %}


# Include one page in another

- We can include one page in another by using {% include 'html_file.html' %}

# Static Files

- Create a `static` folder inside module folder. We can add css files inside module folder.
- Load `static` folder in the template file.
- Import fonts from `font.google.com` . 
- Enable `STATICFILES_DIRS` in settings.py of main project. 



# Building Static URLs Dynamically
- Imagine, that you want to build a static URL where some part of the URL (e.g. the filename) is actually stored in a variable that's exposed to the template.
 - {% static "my_path/to/" + the_file %}
- Here, "the_file" would be a variable holding the actual filename.

The above code would fail.

- Instead, you can use the "add" filter provided by Django to construct this path dynamically:

- {% static "my_path/to/"|add:the_file %}




# References 

- https://docs.djangoproject.com/en/5.1/topics/templates/