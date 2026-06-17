from app.storage import db





def create_order(order):

    if order.user_id not in db.user_db:
        return None

    order_id = db.next_order_id

    new_order = {
        "order_id": order_id,
        "user_id": order.user_id,
        "product_name": order.product_name,
        "quantity": order.quantity,
        "price": order.price,
        "status": "pending"
    }

    db.order_db[order_id] = new_order

    db.next_order_id += 1

    return new_order
def get_order(order_id):
    return db.order_db.get(order_id)
def get_all_orders():
    return list(db.order_db.values())
def update_order(order_id, order_update):
    existing_order = db.order_db.get(order_id)

    if not existing_order:
        return None 
    update_data =order_update.model_dump(exclude_unset=True)

    existing_order.update(update_data)
    return existing_order
def delete_order(order_id):
    return db.order_db.pop(order_id, None)

def get_user_orders(user_id):
    orders=[]
    for order in db.order_db.values():
        if order["user_id"]==user_id:
            orders.append(order)