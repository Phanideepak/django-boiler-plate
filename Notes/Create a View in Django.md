# Create a view in Django

- Create a function in the views.py file of the module.
- In the module, create urls.py to define the urls and methods in views.
- In the project urls.py, Import the urls of the module by using path and include functions.


## Path variables in Django

- url : '<path_variable>'
- path_variable can be accessed in handler method in views file.
- Path Convertors can be used to assign data type to the path_variable
  - url : '<str:path_variable>'
  - url : '<int:path_variable>'


### Reverse Function in URLS:
- reverse function (django.urls) is used to create path of the url.