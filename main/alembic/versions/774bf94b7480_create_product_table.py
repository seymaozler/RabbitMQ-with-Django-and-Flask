"""create product table

Revision ID: 774bf94b7480
Revises: 
Create Date: 2023-11-26 18:14:50.118624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '774bf94b7480'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("price", sa.Integer, nullable=False),
        sa.Column("image", sa.String(255), nullable=False),
    )
    pass


def downgrade() -> None:
    pass
