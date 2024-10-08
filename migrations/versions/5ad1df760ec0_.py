"""empty message

Revision ID: 5ad1df760ec0
Revises: 5e9fc066d843
Create Date: 2024-08-15 14:55:40.675409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ad1df760ec0'
down_revision = '5e9fc066d843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.alter_column('team1_score',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('team2_score',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.alter_column('team2_score',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('team1_score',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
