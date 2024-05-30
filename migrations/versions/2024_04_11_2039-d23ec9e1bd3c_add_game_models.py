"""Add Game models

Revision ID: d23ec9e1bd3c
Revises: fe46c3e40a7f
Create Date: 2024-04-11 20:39:12.928788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d23ec9e1bd3c"
down_revision = "fe46c3e40a7f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "games",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "type",
            sa.Enum("multiplayer", "single", "analysis", name="gametype"),
            nullable=False,
        ),
        sa.Column("players_number", sa.Integer(), nullable=False),
        sa.Column("is_finished", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.Column("finished_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_games_id"), "games", ["id"], unique=False)
    op.create_table(
        "players",
        sa.Column("game_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("game_id", "user_id"),
    )
    op.create_table(
        "winners",
        sa.Column("game_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("game_id", "user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("winners")
    op.drop_table("players")
    op.drop_index(op.f("ix_games_id"), table_name="games")
    op.drop_table("games")
    # ### end Alembic commands ###