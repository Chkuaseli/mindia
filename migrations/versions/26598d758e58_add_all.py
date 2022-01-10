"""add all.

Revision ID: 26598d758e58
Revises: 
Create Date: 2022-01-10 23:04:19.703851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26598d758e58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_tests_desc', 'tests', type_='unique')
    op.create_unique_constraint(op.f('uq_tests_code'), 'tests', ['code'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_tests_code'), 'tests', type_='unique')
    op.create_unique_constraint('uq_tests_desc', 'tests', ['desc'])
    # ### end Alembic commands ###