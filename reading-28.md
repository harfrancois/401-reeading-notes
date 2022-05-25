# Django Forms

source - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#overview

An HTML Form is a group of one or more fields/widgets on a web page, which can be used to collect information from 
users for submission to a server. Forms are a flexible mechanism for collecting user input because there are suitable 
widgets for entering many different types of data, including text boxes, checkboxes, radio buttons, date pickers and 
so on. Forms are also a relatively secure way of sharing data with the server, as they allow us to send data in POST 
requests with cross-site request forgery protection.

The form is defined in HTML as a collection of elements inside <form>...</form> tags, containing at least one input element of type="submit".

    <form action="/team_name_url/" method="post">
        <label for="team_name">Enter name: </label>
        <input id="team_name" type="text" name="name_field" value="Default name for team.">
        <input type="submit" value="OK">
    </form>

action: The resource/URL where data is to be sent for processing when the form is submitted. If this is not set 
(or set to an empty string), then the form will be submitted back to the current page URL.

method: The HTTP method used to send the data: post or get.

The POST method should always be used if the data is going to result in a change to the server's database, because it 
can be made more resistant to cross-site forgery request attacks.

The GET method should only be used for forms that don't change user data (for example, a search form). It is 
recommended for when you want to be able to bookmark or share the URL.

orm data is stored in an application's forms.py file, inside the application directory. Create and open the file 
locallibrary/catalog/forms.py. To create a Form, we import the forms library, derive from the Form class, and declare 
the form's fields. A very basic form class for our library book renewal form is shown below — add this to your new file:

    from django import forms

    class RenewBookForm(forms.Form):
        renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

There are many other types of form fields, which you will largely recognize from their similarity to the equivalent 
model field classes: BooleanField, CharField, ChoiceField, TypedChoiceField, DateField, DateTimeField, DecimalField, 
DurationField, EmailField, FileField, FilePathField, FloatField, ImageField, IntegerField, GenericIPAddressField, 
MultipleChoiceField, TypedMultipleChoiceField, NullBooleanField, RegexField, SlugField, TimeField, URLField, UUIDField, 
ComboField, MultiValueField, SplitDateTimeField, ModelMultipleChoiceField, ModelChoiceField.

The arguments that are common to most fields are listed below (these have sensible default values):

required: If True, the field may not be left blank or given a None value. Fields are required by default, so you would 
set required=False to allow blank values in the form.
label: The label to use when rendering the field in HTML. If a label is not specified, Django will create one from the 
field name by capitalizing the first letter and replacing underscores with spaces (e.g. Renewal date).
label_suffix: By default, a colon is displayed after the label (e.g. Renewal date​:). This argument allows you to 
specify a different suffix containing other character(s).
initial: The initial value for the field when the form is displayed.
widget: The display widget to use.
help_text (as seen in the example above): Additional text that can be displayed in forms to explain how to use the 
field.
error_messages: A list of error messages for the field. You can override these with your own messages if needed.
validators: A list of functions that will be called on the field when it is validated.
localize: Enables the localization of form data input (see link for more information).
disabled: The field is displayed but its value cannot be edited if this is True. The default is False.

Validation
Django provides numerous places where you can validate your data. The easiest way to validate a single field is to 
override the method clean_<fieldname>() for the field you want to check. So for example, we can validate that entered 
renewal_date values are between now and 4 weeks by implementing clean_renewal_date() as shown below.

Update your forms.py file so it looks like this:

    import datetime

    from django import forms

    from django.core.exceptions import ValidationError
    from django.utils.translation import gettext_lazy as _
    
    class RenewBookForm(forms.Form):
        renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    
        def clean_renewal_date(self):
            data = self.cleaned_data['renewal_date']
    
            # Check if a date is not in the past.
            if data < datetime.date.today():
                raise ValidationError(_('Invalid date - renewal in past'))
    
            # Check if a date is in the allowed range (+4 weeks from today).
            if data > datetime.date.today() + datetime.timedelta(weeks=4):
                raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
    
            # Remember to always return the cleaned data.
            return data
    Copy to Clipboard

URL configuration

    urlpatterns += [
        path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    ]


View

    import datetime
    
    from django.shortcuts import render, get_object_or_404
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    
    from catalog.forms import RenewBookForm
    
    def renew_book_librarian(request, pk):
        book_instance = get_object_or_404(BookInstance, pk=pk)
    
        # If this is a POST request then process the Form data
        if request.method == 'POST':
    
            # Create a form instance and populate it with data from the request (binding):
            form = RenewBookForm(request.POST)
    
            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                book_instance.due_back = form.cleaned_data['renewal_date']
                book_instance.save()
    
                # redirect to a new URL:
                return HttpResponseRedirect(reverse('all-borrowed') )
    
        # If this is a GET (or any other method) create the default form.
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
        context = {
            'form': form,
            'book_instance': book_instance,
        }
    
        return render(request, 'catalog/book_renew_librarian.html', context)

get_object_or_404(): Returns a specified object from a model based on its primary key value, and raises an Http404 
exception (not found) if the record does not exist.

HttpResponseRedirect: This creates a redirect to a specified URL (HTTP status code 302).

reverse(): This generates a URL from a URL configuration name and a set of arguments. It is the Python equivalent of 
the url tag that we've been using in our templates.

datetime: A Python library for manipulating dates and times.

In the view, we first use the pk argument in get_object_or_404() to get the current BookInstance 
(if this does not exist, the view will immediately exit and the page will display a "not found" error). 
If this is not a POST request (handled by the else clause) then we create the default form passing in an initial value 
for the renewal_date field, 3 weeks from the current date.

    book_instance = get_object_or_404(BookInstance, pk=pk)
    
    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
    context = {
        'form': form,
        'book_instance': book_instance,
    }
    
    return render(request, 'catalog/book_renew_librarian.html', context)

if this is a POST request, then we create our form object and populate it with data from the request. This process is 
called "binding" and allows us to validate the form.

    book_instance = get_object_or_404(BookInstance, pk=pk)
    
    # If this is a POST request then process the Form data
    if request.method == 'POST':
    
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)
    
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
    
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )
    
    context = {
        'form': form,
        'book_instance': book_instance,
    }
    
    return render(request, 'catalog/book_renew_librarian.html', context)

The final view is therefore as shown below. Please copy this into the bottom of locallibrary/catalog/views.py.

    import datetime
    
    from django.contrib.auth.decorators import login_required, permission_required
    from django.shortcuts import get_object_or_404
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    
    from catalog.forms import RenewBookForm
    
    @login_required
    @permission_required('catalog.can_mark_returned', raise_exception=True)
    def renew_book_librarian(request, pk):
        """View function for renewing a specific BookInstance by librarian."""
        book_instance = get_object_or_404(BookInstance, pk=pk)
    
        # If this is a POST request then process the Form data
        if request.method == 'POST':
    
            # Create a form instance and populate it with data from the request (binding):
            form = RenewBookForm(request.POST)
    
            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                book_instance.due_back = form.cleaned_data['renewal_date']
                book_instance.save()
    
                # redirect to a new URL:
                return HttpResponseRedirect(reverse('all-borrowed') )
    
        # If this is a GET (or any other method) create the default form.
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
        context = {
            'form': form,
            'book_instance': book_instance,
        }
    
        return render(request, 'catalog/book_renew_librarian.html', context)
