db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)

db.define_table('ads',
                Field('title'),
                Field('description','text'),
                Field('location'),
                Field('price'),
                Field('phone'),
                Field('file', 'upload'),
                auth.signature              
                )

db.define_table('users',
               Field('db_email'),
               Field('db_password'))
               

