"""empty message

Revision ID: 19f3cb36c6b9
Revises: d0bcef1f2c28
Create Date: 2024-09-05 12:10:27.165743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19f3cb36c6b9'
down_revision = 'd0bcef1f2c28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagamento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuario', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'usuario', ['id_usuario'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagamento', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_usuario')

    # ### end Alembic commands ###
