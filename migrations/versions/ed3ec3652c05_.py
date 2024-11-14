"""empty message

Revision ID: ed3ec3652c05
Revises: 7fe60f013b58
Create Date: 2024-09-05 12:07:15.493960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed3ec3652c05'
down_revision = '7fe60f013b58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagamento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuariop', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'usuario', ['id_usuariop'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pagamento', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_usuariop')

    # ### end Alembic commands ###
