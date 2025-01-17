"""Update ExerciseEntry model.

Revision ID: 77469be3d1a2
Revises: cef85d960895
Create Date: 2024-08-02 01:31:20.947535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77469be3d1a2'
down_revision = 'cef85d960895'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise_entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('calories_burned', sa.Float(), nullable=False))
        batch_op.drop_column('calories_nurned')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise_entry', schema=None) as batch_op:
        batch_op.add_column(sa.Column('calories_nurned', sa.FLOAT(), nullable=False))
        batch_op.drop_column('calories_burned')

    # ### end Alembic commands ###
