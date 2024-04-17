from models import Database

if __name__ == "__main__":
    database_url = "sqlite:///test.db"
    db = Database(database_url)
    db.make_migrations()
    engine = db.get_engine()
    print("Migrations created successfully!")