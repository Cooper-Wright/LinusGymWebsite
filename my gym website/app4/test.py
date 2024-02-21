from app4 import app, db, Equipment  # Replace 'app4' with the name of your main Flask script

with app.app_context():
    items = Equipment.query.all()
    for item in items:
        print(item.name, item.price) 