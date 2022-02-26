"""Alteração nas colunas de metadados static

Revision ID: b0f70af2a55c
Revises: 43c43986c66e
Create Date: 2022-02-23 22:43:59.459989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0f70af2a55c'
down_revision = '43c43986c66e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    op.drop_table('categories')
    op.drop_table('token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('ticker', sa.VARCHAR(length=6), nullable=False),
    sa.Column('marketcap', sa.VARCHAR(length=15), nullable=False),
    sa.Column('logo_url', sa.VARCHAR(length=85), nullable=False),
    sa.Column('price', sa.VARCHAR(length=20), nullable=True),
    sa.Column('blockchain', sa.VARCHAR(length=60), nullable=True),
    sa.Column('address', sa.VARCHAR(length=60), nullable=True),
    sa.Column('site', sa.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('ticker')
    )
    op.create_table('categories',
    sa.Column('token_id', sa.INTEGER(), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['token_id'], ['token.id'], ),
    sa.PrimaryKeyConstraint('token_id', 'category_id')
    )
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
