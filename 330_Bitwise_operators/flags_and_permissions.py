class Permissions:
    READ_PERMISSION = 1      # 0b001
    WRITE_PERMISSION = 2     # 0b010
    EXECUTE_PERMISSION = 4   # 0b100

    def __init__(self):
        self.user_permissions = 0

    def add_permission(self, permission):
        if permission not in [self.READ_PERMISSION, self.WRITE_PERMISSION, self.EXECUTE_PERMISSION]:
            raise ValueError("Invalid permission value")
        self.user_permissions |= permission

    def remove_permission(self, permission):
        if permission not in [self.READ_PERMISSION, self.WRITE_PERMISSION, self.EXECUTE_PERMISSION]:
            raise ValueError("Invalid permission value")
        self.user_permissions &= ~permission

    def has_permission(self, permission):
        if permission not in [self.READ_PERMISSION, self.WRITE_PERMISSION, self.EXECUTE_PERMISSION]:
            raise ValueError("Invalid permission value")
        return bool(self.user_permissions & permission)


try:
    user_permissions = Permissions()

    user_permissions.add_permission(Permissions.READ_PERMISSION)
    user_permissions.add_permission(Permissions.WRITE_PERMISSION)

    if user_permissions.has_permission(Permissions.READ_PERMISSION):
        print("User has read permission")

    if user_permissions.has_permission(Permissions.WRITE_PERMISSION):
        print("User has write permission")

    if user_permissions.has_permission(Permissions.EXECUTE_PERMISSION):
        print("User has execute permission")
    else:
        print("User does not have execute permission")

    user_permissions.remove_permission(Permissions.WRITE_PERMISSION)

    if user_permissions.has_permission(Permissions.WRITE_PERMISSION):
        print("User still has write permission")
    else:
        print("User no longer has write permission")

except ValueError as e:
    print(f"Error: {e}")
