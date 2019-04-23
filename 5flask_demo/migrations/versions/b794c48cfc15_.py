"""empty message

Revision ID: b794c48cfc15
Revises: 
Create Date: 2019-04-23 18:41:57.868098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b794c48cfc15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=12), nullable=True),
    sa.Column('telnumber', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('vip', sa.BOOLEAN(), nullable=True),
    sa.Column('isdelate', sa.BOOLEAN(), nullable=True),
    sa.Column('logintime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('telnumber')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('need_vip', sa.BOOLEAN(), nullable=True),
    sa.Column('introduce', sa.Text(), nullable=True),
    sa.Column('book_image', sa.String(length=50), nullable=True),
    sa.Column('isdelate', sa.BOOLEAN(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_book',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'book_id')
    )
    op.create_table('chapter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('need_vip', sa.BOOLEAN(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_chapter',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('chapter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapter.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'chapter_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_chapter')
    op.drop_table('chapter')
    op.drop_table('category_book')
    op.drop_table('book')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###