"""add all.

Revision ID: edda3357467e
Revises: 
Create Date: 2022-01-08 20:19:18.713737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edda3357467e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('desc', sa.String(length=180), nullable=False),
    sa.Column('date_crated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tests')),
    sa.UniqueConstraint('desc', name=op.f('uq_tests_desc'))
    )
    op.create_table('pictures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('pic', sa.String(length=180), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tests.id'], name=op.f('fk_pictures_user_id_tests')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pictures')),
    sa.UniqueConstraint('pic', name=op.f('uq_pictures_pic'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pictures')
    op.drop_table('tests')
    # ### end Alembic commands ###
