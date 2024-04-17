import os as _os
from alembic.config import Config as _Config
from alembic import command as _command
from sqlmodel import create_engine as _create_sqlmodel_engine

# Import the Models
from .example import Example


class Database:
    def __init__(self, url="sqlite:///db.db") -> None:
        self.url = url
        self.engine = None

    def make_migrations(self):
        """Create migrations folder and run alembic commands to create migrations and upgrade the database to the latest version."""

        assert _os.path.exists("migrations"), "Migration folder does not exist. Please create it first."

        if not _os.path.exists(_os.path.join("migrations", "versions")):
            _os.makedirs(_os.path.join("migrations", "versions"))

        alembic_cfg = _Config("alembic.ini")
        alembic_cfg.set_main_option("script_location", "migrations")
        alembic_cfg.set_main_option("sqlalchemy.url", self.url)
        
        # First check, if the database if empty, then upgrade to head
        try:
            _command.check(alembic_cfg)
        except Exception as e:
            _command.upgrade(alembic_cfg, "head")

        # Create a new revision, if the databse is still not up to date
        try:
            _command.check(alembic_cfg)
        except Exception as e:
            _command.revision(alembic_cfg, autogenerate=True)
            _command.upgrade(alembic_cfg, "head")

    def get_engine(self):
        """Create a database engine."""
        if not self.engine:
            self.engine = _create_sqlmodel_engine(self.url)
        return self.engine

