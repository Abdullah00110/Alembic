"""Student

Revision ID: d956286d21e3
Revises: 
Create Date: 2024-01-18 11:31:47.138556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd956286d21e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "student",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(20), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('student')
