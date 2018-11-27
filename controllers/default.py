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

def register():
    return dict()

def store():
	submitted_email = request.vars.email
	submitted_password = request.vars.password
	submitted_accountname = request.vars.accountname
	submitted_accountnumber = request.vars.accountnumber
	submitted_bankname = request.vars.bankname
	submitted_bankbranch = request.vars.bankbranch

	results = db.users.insert(
		db_email = submitted_email,
		db_password = submitted_password,
		db_accountname = submitted_accountname,
    	db_accountnumber = submitted_accountnumber,
        db_bankname = submitted_bankname,
        db_bankbranch = submitted_bankbranch
    )

	if results: 
		return "Information Entered Successfully"
	else:
  		return "An Error Occurred"

def seeUsers():
  	users= db().select(db.users.ALL)
  	return dict(users=users)

def login():
	return dict()

def authenticate():
	submitted_email = request.vars.email
	submitted_password = request.vars.password

	if db(db.users.db_email==submitted_email
			and db.users.db_password==submitted_password).count()>0:
			return "User Logged in Successfully"
	else:
			return "User Not Found.  Please sign up"

	