from users.schemas import CreateUser


def create_user(user: CreateUser):
    return {"success": True, "user": user}
