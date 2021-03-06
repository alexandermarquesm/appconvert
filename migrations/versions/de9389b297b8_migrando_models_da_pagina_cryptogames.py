"""Migrando models da pagina cryptogames

Revision ID: de9389b297b8
Revises:
Create Date: 2022-01-31 00:30:15.872335
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "de9389b297b8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("categories")
    op.drop_table("token")
    op.drop_table("category")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "token",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=20), nullable=False),
        sa.Column("ticker", sa.VARCHAR(length=6), nullable=False),
        sa.Column("price", sa.VARCHAR(length=20), nullable=False),
        sa.Column("marketcap", sa.VARCHAR(length=15), nullable=False),
        sa.Column("blockchain", sa.VARCHAR(length=60), nullable=False),
        sa.Column("site", sa.VARCHAR(length=60), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("site"),
        sa.UniqueConstraint("ticker"),
    )
    op.create_table(
        "categories",
        sa.Column("token_id", sa.INTEGER(), nullable=False),
        sa.Column("category_id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["token_id"],
            ["token.id"],
        ),
        sa.PrimaryKeyConstraint("token_id", "category_id"),
    )
    # ### end Alembic commands ###
