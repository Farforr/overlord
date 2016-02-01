from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object.
        return self.get_object_owner(obj) == request.user

    @staticmethod
    def get_object_owner(obj):
        if hasattr(obj, 'owner'):
            return obj.owner
        elif hasattr(obj, 'network'):
            return obj.network.owner
        elif hasattr(obj, 'node'):
            return obj.node.network.owner
        elif hasattr(obj, 'sensor'):
            return obj.sensor.node.network.owner
        elif hasattr(obj, 'actuator'):
            return obj.actuator.node.network.owner
        else:
            return False
