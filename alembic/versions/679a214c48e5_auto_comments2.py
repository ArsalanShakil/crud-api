"""auto-comments2

Revision ID: 679a214c48e5
Revises: da0eafb6855d
Create Date: 2021-12-25 03:50:28.968360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '679a214c48e5'
down_revision = 'da0eafb6855d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'comment_id')
    # ### end Alembic commands ###
