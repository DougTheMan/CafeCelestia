"""empty message

Revision ID: 3fbfbb3559f2
Revises: 851ca95bb977
Create Date: 2024-10-25 13:41:51.141466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fbfbb3559f2'
down_revision = '851ca95bb977'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuario', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('id_usuario')

    # ### end Alembic commands ###
