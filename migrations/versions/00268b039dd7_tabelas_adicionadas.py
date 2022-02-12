"""Tabelas Adicionadas

Revision ID: 00268b039dd7
Revises: 
Create Date: 2022-02-12 18:12:44.143924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "00268b039dd7"
down_revision = None
branch_labels = None
depends_on = None


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("token")
    op.drop_table("categories")
    op.drop_table("category")
    # ### end Alembic commands ###


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
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
    op.create_table(
        "token",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("name", sa.VARCHAR(length=20), nullable=False),
        sa.Column("ticker", sa.VARCHAR(length=6), nullable=False),
        sa.Column("price", sa.VARCHAR(length=20), nullable=False),
        sa.Column("marketcap", sa.VARCHAR(length=15), nullable=False),
        sa.Column("blockchain", sa.VARCHAR(length=60), nullable=False),
        sa.Column("address", sa.VARCHAR(length=60), nullable=False),
        sa.Column("site", sa.VARCHAR(length=60), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("site"),
        sa.UniqueConstraint("ticker"),
    )
    # ### end Alembic commands ###
