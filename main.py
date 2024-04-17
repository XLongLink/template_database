
from alembic.config import Config
from alembic import command


def upgrade_database_to_latest():
    # Specify the path to your Alembic configuration file
    alembic_cfg = Config("alembic.ini")
    
    try:
        command.check(alembic_cfg)
    except Exception as e:
        command.revision(alembic_cfg, autogenerate=True)
        command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    upgrade_database_to_latest()
