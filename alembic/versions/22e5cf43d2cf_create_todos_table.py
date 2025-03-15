"""create todos table

Revision ID: 22e5cf43d2cf
Revises: ad1c380734f8
Create Date: 2025-03-14 20:16:49.719450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
# revision: str = '22e5cf43d2cf'
revision: str = 'ad1c380734f8'
# down_revision: Union[str, None] = 'ad1c380734f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)

def downgrade():
    op.execute("drop table todos;")