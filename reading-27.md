# Django Models
source - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

giDjango web applications access and manage data through Python objects referred to as models. Models define the 
structure of stored data, including the field types and possibly also their maximum size, default values, selection 
list options, help text for documentation, label text for forms, etc.

Model definition
Models are usually defined in an application's models.py file. They are implemented as subclasses of 
django.db.models.Model, and can include fields, methods and metadata. The code fragment below shows a "typical" model, 
named MyModelName:

        from django.db import models
        from django.urls import reverse
        
        class MyModelName(models.Model):
            """A typical class defining a model, derived from the Model class."""
        
            # Fields
            my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
            ...
        
            # Metadata
            class Meta:
                ordering = ['-my_field_name']
        
            # Methods
            def get_absolute_url(self):
                """Returns the URL to access a particular instance of MyModelName."""
                return reverse('model-detail-view', args=[str(self.id)])
        
            def __str__(self):
                """String for representing the MyModelName object (in Admin site etc.)."""
                return self.my_field_name

Fields
A model can have an arbitrary number of fields, of any type — each one represents a column of data that we want to 
store in one of our database tables. Each database record (row) will consist of one of each field value.

CharField is used to define short-to-mid sized fixed-length strings. You must specify the max_length of the data to 
be stored.

TextField is used for large arbitrary-length strings. You may specify a max_length for the field, but this is used 
only when the field is displayed in forms (it is not enforced at the database level).

IntegerField is a field for storing integer (whole number) values, and for validating entered values as integers 
in forms.

DateField and DateTimeField are used for storing/representing dates and date/time information (as Python datetime.date 
in and datetime.datetime objects, respectively). These fields can additionally declare the (mutually exclusive) 
parameters auto_now=True (to set the field to the current date every time the model is saved), auto_now_add (to only 
set the date when the model is first created) , and default (to set a default date that can be overridden by the user).

EmailField is used to store and validate email addresses.

FileField and ImageField are used to upload files and images respectively (the ImageField adds additional validation 
that the uploaded file is an image). These have parameters to define how and where the uploaded files are stored.

AutoField is a special type of IntegerField that automatically increments. A primary key of this type is automatically 
added to your model if you don't explicitly specify one.

ForeignKey is used to specify a one-to-many relationship to another database model (e.g. a car has one manufacturer, 
but a manufacturer can make many cars). The "one" side of the relationship is the model that contains the "key" (models 
containing a "foreign key" referring to that "key", are on the "many" side of such a relationship).

ManyToManyField is used to specify a many-to-many relationship (e.g. a book can have several genres, and each genre can 
contain several books). In our library app we will use these very similarly to ForeignKeys, but they can be used in 
more complicated ways to describe the relationships between groups. These have the parameter on_delete to define what 
happens when the associated record is deleted (e.g. a value of models.SET_NULL would set the value to NULL).

The Django admin application can use your models to automatically build a site area that you can use to create, view, 
update, and delete records. This can save you a lot of time during development, making it very easy to test your models 
and get a feel for whether you have the right data. The admin application can also be useful for managing data in 
production, depending on the type of website. The Django project recommends it only for internal data management 
(i.e. just for use by admins, or people internal to your organization), as the model-centric approach is not 
necessarily the best possible interface for all users, and exposes a lot of unnecessary detail about the models.