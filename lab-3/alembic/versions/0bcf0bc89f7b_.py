"""empty message

Revision ID: 0bcf0bc89f7b
Revises: a8f9a401c4d4
Create Date: 2020-12-02 01:46:33.080418

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bcf0bc89f7b'
down_revision = 'a8f9a401c4d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('datetimeofrequest', sa.DATETIME(), nullable=True))
    op.add_column('request', sa.Column('status', sa.String(length=16), nullable=True))
    op.create_index(op.f('ix_request_new_text'), 'request', ['new_text'], unique=False)
    op.create_index(op.f('ix_request_request_id'), 'request', ['request_id'], unique=False)
    op.create_index(op.f('ix_request_status'), 'request', ['status'], unique=False)
    op.drop_index('ix_Request_Status', table_name='request')
    op.drop_index('ix_Request_new_text', table_name='request')
    op.drop_index('ix_Request_request_id', table_name='request')
    op.drop_column('request', 'user_id')
    op.drop_column('request', 'DateTimeOfRequest')
    op.drop_column('request', 'Status')
    op.add_column('user', sa.Column('firstname', sa.String(length=16), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=16), nullable=True))
    op.add_column('user', sa.Column('untipassword', sa.String(length=16), nullable=True))
    op.add_column('user', sa.Column('userrole', sa.String(length=16), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=False)
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    op.create_index(op.f('ix_user_phone'), 'user', ['phone'], unique=False)
    op.create_index(op.f('ix_user_untipassword'), 'user', ['untipassword'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_index(op.f('ix_user_userrole'), 'user', ['userrole'], unique=False)
    op.drop_index('ix_User_email', table_name='user')
    op.drop_index('ix_User_firstName', table_name='user')
    op.drop_index('ix_User_lastName', table_name='user')
    op.drop_index('ix_User_password', table_name='user')
    op.drop_index('ix_User_phone', table_name='user')
    op.drop_index('ix_User_userRole', table_name='user')
    op.drop_index('ix_User_username', table_name='user')
    op.drop_column('user', 'lastName')
    op.drop_column('user', 'userRole')
    op.drop_column('user', 'firstName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstName', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('user', sa.Column('userRole', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('user', sa.Column('lastName', mysql.VARCHAR(length=16), nullable=True))
    op.create_index('ix_User_username', 'user', ['username'], unique=False)
    op.create_index('ix_User_userRole', 'user', ['userRole'], unique=False)
    op.create_index('ix_User_phone', 'user', ['phone'], unique=False)
    op.create_index('ix_User_password', 'user', ['password'], unique=False)
    op.create_index('ix_User_lastName', 'user', ['lastName'], unique=False)
    op.create_index('ix_User_firstName', 'user', ['firstName'], unique=False)
    op.create_index('ix_User_email', 'user', ['email'], unique=False)
    op.drop_index(op.f('ix_user_userrole'), table_name='user')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_untipassword'), table_name='user')
    op.drop_index(op.f('ix_user_phone'), table_name='user')
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'userrole')
    op.drop_column('user', 'untipassword')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.add_column('request', sa.Column('Status', mysql.VARCHAR(length=16), nullable=True))
    op.add_column('request', sa.Column('DateTimeOfRequest', mysql.DATETIME(), nullable=True))
    op.add_column('request', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_Request_request_id', 'request', ['request_id'], unique=False)
    op.create_index('ix_Request_new_text', 'request', ['new_text'], unique=False)
    op.create_index('ix_Request_Status', 'request', ['Status'], unique=False)
    op.drop_index(op.f('ix_request_status'), table_name='request')
    op.drop_index(op.f('ix_request_request_id'), table_name='request')
    op.drop_index(op.f('ix_request_new_text'), table_name='request')
    op.drop_column('request', 'status')
    op.drop_column('request', 'datetimeofrequest')
    # ### end Alembic commands ###
