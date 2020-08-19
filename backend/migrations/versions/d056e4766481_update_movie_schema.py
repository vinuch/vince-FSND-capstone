"""update Movie schema

Revision ID: d056e4766481
Revises: 
Create Date: 2020-08-17 20:43:38.117975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd056e4766481'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('cover_image', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('description', sa.String(), nullable=True))
    op.add_column('movies', sa.Column('genres', sa.String(), nullable=True))
    op.drop_column('movies', 'attributes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('attributes', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('movies', 'genres')
    op.drop_column('movies', 'description')
    op.drop_column('movies', 'cover_image')
    # ### end Alembic commands ###
