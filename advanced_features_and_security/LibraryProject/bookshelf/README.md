Permissions & Groups Setup

1. Custom Permissions (models.py)
Defined within the Book model’s Meta class to provide granular control:
can_view, can_create, can_edit, can_delete.

2. Group Configuration (Admin)
Roles are managed via Django Groups:
Viewers: Assigned can_view.
Editors: Assigned can_view, can_create, can_edit.
Admins: Assigned all permissions.

3. Enforcement (views.py)
Views use the @permission_required decorator to restrict access.
Format: @permission_required('bookshelf.can_edit', raise_exception=True)
Behavior: Unauthorized users receive a 403 Forbidden response.

4. Testing
Assign a user to the Editors group.
Attempt to access the delete_book/ URL.
Verification: Access is denied because only Admins have can_delete.



