"""Fix UUID and username unique in User model

Revision ID: 1faea1cd71c7
Revises: b8574df7f903
Create Date: 2023-08-12 22:19:25.021285

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1faea1cd71c7"
down_revision = "b8574df7f903"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "users", ["username"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    # ### end Alembic commands ###