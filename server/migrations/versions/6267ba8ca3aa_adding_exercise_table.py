"""adding exercise table

Revision ID: 6267ba8ca3aa
Revises: e0653e164ace
Create Date: 2023-10-04 10:10:20.796282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6267ba8ca3aa'
down_revision = 'e0653e164ace'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_name', sa.String(), nullable=True),
    sa.Column('target_muscle', sa.String(), nullable=True),
    sa.Column('sets', sa.Integer(), nullable=True),
    sa.Column('reps', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises')
    # ### end Alembic commands ###
