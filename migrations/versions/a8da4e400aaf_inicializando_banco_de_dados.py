"""Inicializando banco de dados

Revision ID: a8da4e400aaf
Revises: 
Create Date: 2023-12-13 14:55:12.889175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8da4e400aaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Nome', sa.String(length=100), nullable=True),
    sa.Column('Sexo', sa.String(length=100), nullable=True),
    sa.Column('Cpf', sa.String(length=100), nullable=True),
    sa.Column('Data_de_Nascimento', sa.String(length=100), nullable=True),
    sa.Column('Matricula', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alunos')
    # ### end Alembic commands ###