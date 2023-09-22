from app import db, app
from models import Users  # Adjust the import path based on your project structure

# Create the database tables
with app.app_context():
    db.create_all()

print("Database tables created successfully.")