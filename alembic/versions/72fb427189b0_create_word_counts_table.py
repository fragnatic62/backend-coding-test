"""Create word_counts table

Revision ID: 72fb427189b0
Revises: 
Create Date: 2023-06-28 13:36:23.934531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72fb427189b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word_counts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('word_counts')
    # ### end Alembic commands ###
