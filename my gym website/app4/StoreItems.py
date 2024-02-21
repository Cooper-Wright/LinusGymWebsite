from app4 import app, db, Equipment

# Your existing equipment list
equipment_list = [
    { "name": "20 Kg Barbell", "price": "£80", "description": "Extremely sturdy barbell, used in many power lifting competitions, with a beautiful colouring.", "image_path": "barbell.jpg"  },
    { "name": "1.25 - 20 Kg plate set", "price": "£300", "description": "Extremely sturdy plates, used in many power lifting competitions, with beautiful colouring.", "image_path": "plates.jpg" },
    { "name": "1-10 Kg Dumbbells", "price": "£200", "description": "Extremely sturdy dumbells, loved by many bodybuilders, with beautiful colouring.", "image_path": "dumbells.jpg" },
]


def populate_database():
    if not Equipment.query.first():  # Check if the table is empty
        print("populating")
        for item in equipment_list:
            new_item = Equipment(name=item['name'], price=item['price'], description=item['description'], image_path=item['image_path'])
            db.session.add(new_item)
        db.session.commit()
        print("been populated")
    else:
        print("already populated")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        populate_database()
    
