"""empty message

Revision ID: 7ada716db359
Revises: edeb65617aa0
Create Date: 2024-03-31 12:11:56.899438

"""
import sqlmodel
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ada716db359'
down_revision: Union[str, None] = 'edeb65617aa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('date', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'date')
    # ### end Alembic commands ###