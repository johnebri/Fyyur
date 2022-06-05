"""empty message

Revision ID: 09dc88a9e7e8
Revises: 16a7ab16842d
Create Date: 2022-06-05 15:57:43.428396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09dc88a9e7e8'
down_revision = '16a7ab16842d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('genres', sa.String(length=500), nullable=True))
    op.add_column('venues', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('venues', sa.Column('seeking_talent', sa.String(length=20), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'seeking_talent')
    op.drop_column('venues', 'website_link')
    op.drop_column('venues', 'genres')
    # ### end Alembic commands ###
