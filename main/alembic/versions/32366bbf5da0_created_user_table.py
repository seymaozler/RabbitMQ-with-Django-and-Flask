"""created user table

Revision ID: 32366bbf5da0
Revises: 774bf94b7480
Create Date: 2023-11-26 19:12:37.621405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32366bbf5da0'
down_revision: Union[str, None] = '774bf94b7480'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product_user",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("product_id", sa.Integer, nullable=False),
    )
    pass


def downgrade() -> None:
    pass
