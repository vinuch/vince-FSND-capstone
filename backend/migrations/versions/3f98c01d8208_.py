"""empty message

Revision ID: 3f98c01d8208
Revises: 98b1ccced4a0
Create Date: 2020-08-24 17:25:18.933987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f98c01d8208'
down_revision = '98b1ccced4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'extra')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('extra', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
