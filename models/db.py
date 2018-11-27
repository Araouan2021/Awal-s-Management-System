from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",
               Field('db_email'),
               Field('db_password'),
               Field('db_accountname'),
               Field('db_accountnumber'),
               Field('db_bankname'),
               Field('db_bankbranch'))
