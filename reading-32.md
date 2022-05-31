# DRF Permissions
source - https://www.django-rest-framework.org/api-guide/permissions/
Permissions
Permission checks are always run at the very start of the view, before any other code is allowed to proceed. Permission 
checks will typically use the authentication information in the request.user and request.auth properties to determine 
if the incoming request should be permitted.

How permissions are determined
Permissions in REST framework are always defined as a list of permission classes.

Before running the main body of the view each permission in the list is checked. If any permission check fails, an 
exceptions.PermissionDenied or exceptions.NotAuthenticated exception will be raised, and the main body of the view 
will not run.
The request was successfully authenticated, but permission was denied. — An HTTP 403 Forbidden response will be 
returned.

The request was not successfully authenticated, and the highest priority authentication class does not use 
WWW-Authenticate headers. — An HTTP 403 Forbidden response will be returned.

The request was not successfully authenticated, and the highest priority authentication class does use 
WWW-Authenticate headers. — An HTTP 401 Unauthorized response, with an appropriate WWW-Authenticate header will be 
returned.

Object level permissions
REST framework permissions also support object-level permissioning. Object level permissions are used to determine if 
a user should be allowed to act on a particular object, which will typically be a model instance.

Object level permissions are run by REST framework's generic views when .get_object() is called. As with view level 
permissions, an exceptions.PermissionDenied exception will be raised if the user is not allowed to act on the given object.

If you're writing your own views and want to enforce object level permissions, or if you override the get_object method 
on a generic view, then you'll need to explicitly call the .check_object_permissions(request, obj) method on the view 
at the point at which you've retrieved the object.

This will either raise a PermissionDenied or NotAuthenticated exception, or simply return if the view has the 
appropriate permissions.

Setting the permission policy
The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting. For example.
You can also set the authentication policy on a per-view, or per-viewset basis, using the APIView class-based views.
Or, if you're using the @api_view decorator with function based views.