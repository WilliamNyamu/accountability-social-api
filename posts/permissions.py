from rest_framework import permissions

class IsAuthororReadOnly(permissions.BasePermission):
    """
    Custom permission to check whether the author is the same as the currently
    authenticated user. Allows only the authors to edit or delete a post
    """
#  This is an object-level permission method. DRF calls this when a view is acting on a particular object 
# (e.g., RetrieveUpdateDestroyAPIView for a specific Post instance). Parameters:
# request: the current HTTP request (so you can inspect request.method, request.user, etc.)
# view: the view instance handling the request (rarely needed here)
# obj: the model instance being accessed (e.g., a Post object)
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS  = "GET, HEAD, OPTIONS"
        # UNSAFE_METHODS = "POST", "PUT", "PATCH", "DELETE"
        if request.method in permissions.SAFE_METHODS:
            return True
        # If unsafe method, then:
        return obj.author == request.user