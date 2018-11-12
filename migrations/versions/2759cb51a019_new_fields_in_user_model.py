"""new fields in user model

Revision ID: 2759cb51a019
Revises: 8b02c102f364
Create Date: 2018-11-11 20:57:32.451287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2759cb51a019'
down_revision = '8b02c102f364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
