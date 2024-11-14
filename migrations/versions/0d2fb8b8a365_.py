"""empty message

Revision ID: 0d2fb8b8a365
Revises: afbe77a8579d
Create Date: 2024-09-12 16:30:29.160603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d2fb8b8a365'
down_revision = 'afbe77a8579d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('itens', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preco_novo', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('itens', schema=None) as batch_op:
        batch_op.drop_column('preco_novo')

    # ### end Alembic commands ###
