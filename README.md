# Database

> [!WARNING]  
> This is still in prototype mode, many things could not work as intended

This is a template for a project with a database. The project uses `sqlmodel` to automatically handle the orm and the database connection.
The database migrtion is handled by `alembic`, and all the commit messages are.

The models are stored into the `models` folder, and the migrations are stored into the `migrations` folder.

## Automatic database migration

The function `make_migrations` will make sure that the database is up to date with the models. If the database is not up to date, the function will create a new migration file and apply it to the database.

```python
from models import Database

db = Database("sqlite:///test.db")
db.make_migrations()
engine = db.get_engine()
```
