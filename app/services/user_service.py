from app.storage import db 
def create_user(user):
    user_id = db.next_user_id
    new_user = {
        "id": user_id,
        "username": user.username,
        "email": user.email,
        "phone": user.phone,
        "role": user.role
    }
    db.user_db[user_id] = new_user
    db.next_user_id += 1
    return new_user
def get_all_users():
    return list(db.user_db.values())

def get_user(user_id):
    return db.user_db.get(user_id)
def update_user(user_id, user_update):
    existing_user = db.user_db.get(user_id)

    if not existing_user:
        return None

    update_data = user_update.model_dump(exclude_unset=True)

    existing_user.update(update_data)

    return existing_user


def delete_user(user_id):
    return db.users_db.pop(user_id, None)