"""auto-comments3

Revision ID: 5f3882058a35
Revises: 679a214c48e5
Create Date: 2021-12-25 04:10:04.090823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f3882058a35'
down_revision = '679a214c48e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('comments', 'comment_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('comments', 'id')
    # ### end Alembic commands ###
