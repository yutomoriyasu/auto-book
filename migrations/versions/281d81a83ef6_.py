"""empty message

Revision ID: 281d81a83ef6
Revises: 39e0a0939aaf
Create Date: 2022-01-15 01:13:25.722568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281d81a83ef6'
down_revision = '39e0a0939aaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'user_id')
    )
    op.create_table('group_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_post')
    op.drop_table('group')
    # ### end Alembic commands ###