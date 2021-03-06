"""add admin

Revision ID: 0e2ff406ce03
Revises: 26598d758e58
Create Date: 2022-01-12 00:14:58.843035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e2ff406ce03'
down_revision = '26598d758e58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('main_login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=False),
    sa.Column('pwd', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_main_login')),
    sa.UniqueConstraint('name', name=op.f('uq_main_login_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('main_login')
    # ### end Alembic commands ###
