import os
from flask import Flask, render_template, request, redirect, \
	url_for, session, logging, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, TextField, StringField, TextAreaField, PasswordField, \
	BooleanField, SelectField, SelectMultipleField, validators
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, \
	login_required, logout_user, current_user

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# CLASSES
# Database Classes
# adminusers

class adminusers(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return adminusers.query.get(int(user_id))


class jobs(db.Model):
    jobsid = db.Column(db.Integer, primary_key=True)
    jobtitle = db.Column(db.String(255))
    reference = db.Column(db.String(255), unique=True)
    postcategoryid = db.Column(db.String(255))
    salary = db.Column(db.String(255))
    currency = db.Column(db.String(255))
    locationcity = db.Column(db.String(255))
    companytype = db.Column(db.String(255))
    companyculture = db.Column(db.String(255))
    experiencelevelid = db.Column(db.String(255))
    jobtype = db.Column(db.String(255))
    jobbenefits = db.Column(db.String())
    educationalrequirements = db.Column(db.String(255))
    postcode = db.Column(db.String(255))
    responsibilities = db.Column(db.String(255))
    workhours = db.Column(db.String(255))
    validthrough = db.Column(db.String(255))
    jobdescription = db.Column(db.String(255))

###################################################
#                     FORMS                       #
###################################################

# SargonForm
class SargonForm(FlaskForm):
    jobtitle       = StringField('',
                              validators=[InputRequired(),
                                          Length(min=3, max=50)])

    jobtype        = SelectField(label='',
                              choices=[('pr', 'Permanent'), 
                                       ('cn', 'Contract'), 
                                       ('fl', 'Freeance')])

    companytype    = SelectField(label='',
                              choices=[('st', 'Startup'), 
                                       ('sme', 'SME'), 
                                       ('ep', 'Enterprise')])

    companyculture = SelectField(label='',
                              choices=[('cl', 'Cool'), 
                                       ('mx', 'Mixed'), 
                                       ('su', 'Suits')])

    locationcity   = StringField('',
                              validators=[InputRequired(),
                                          Length(min=3, max=50)])

    salary         = SelectField('',
                              choices=[('1', 'first_range'), 
                                       ('2', 'second_range')])

    skills         = StringField('',
                              validators=[InputRequired(),
                                          Length(min=3, max=50)])

    experience     = SelectField(label='',
                              choices=[('tr', 'Trainee'), 
                                       ('gr', 'Graduate'), 
                                       ('ju', 'Junior'),
                                       ('mi', 'Mid'),
                                       ('se', 'Senior')])

    reference      = StringField('',
                               validators=[InputRequired(),
                                           Length(min=3, max=50)])



# Registration
class RegisterForm(FlaskForm):
    companyname = StringField('Company Name',
                              validators=[InputRequired(),
                                          Length(min=3, max=50)])
    firstname = StringField('First Name',
                            validators=[InputRequired(),
                                        Length(min=2, max=50)])
    surname = StringField('Surname',
                          validators=[InputRequired(),
                                      Length(min=2, max=50)])
    username = StringField('Username',
                           validators=[InputRequired(),
                                       Length(min=4, max=25)])
    email = StringField('Email',
                        validators=[InputRequired(),
                                    Email(message='Invalid Email'),
                                    Length(min=6, max=50)])
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6)])


# Login
class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(),
                                       Length(min=4, max=25)])
    password = PasswordField('Password',
                             validators=[InputRequired(),
                                         Length(min=6)])
    remember = BooleanField('remember me')


# AddJob
class Jobs(FlaskForm):
    jobtitle =  SelectField('Title', choices=[('RR', 'Ruby Developer'),
                                              ('FE', 'Front End'),
                                              ('BE', 'Back End'),
                                              ('FS', 'Full Stack'),
                                              ('ASP.Net',
                                               'ASP.Net Developer')])
    reference = StringField('Reference',
                            validators=[InputRequired(),
                                        Length(min=4, max=25)])
    postcategoryid = SelectField('Category',
                                 choices=[('Jobboard', 'Jobboard'),
                                          ('Split', 'Split Fee')])
    salary = StringField('Salary',
                         validators=[InputRequired(),
                                     Length(min=4, max=25)])
    currency = SelectField('Currency', choices=[('British Pound', 'GBP'),
                                                ('Euro', 'EUR')])
    locationcity = SelectField('Location', choices=[('London', 'London'),
                                                    ('Berlin', 'Berlin'),
                                                    ('Guildford',
                                                     'Guildford')])
    companytype = StringField('Company Type', validators=[InputRequired(),
                                                          Length(min=4,
                                                                 max=25)])
    companyculture = StringField('Company Culture',
                                 validators=[InputRequired(),
                                             Length(min=4, max=25)])
    experiencelevelid = StringField('Experience Level',
                                    validators=[InputRequired(),
                                                Length(min=4, max=25)])
    jobtype = SelectField('Job Type', choices=[('Permanent', 'Permanent'),
                                               ('Contract', 'Contract'),
                                               ('Remote', 'Remote')])
    jobbenefits = SelectMultipleField('Benfits',
                                      choices=[('Pension', 'Pension'),
                                              ('Gym', 'Gym Membership')])
    educationalrequirements = StringField('Education Requirements',
                                          validators=[InputRequired(),
                                                      Length(min=4, max=25)])
    postcode = StringField('Post Code', validators=[InputRequired(),
                                                    Length(min=4, max=25)])
    responsibilities = StringField('Responsibilities',
                                   validators=[InputRequired(),
                                                 Length(min=4, max=25)])
    workhours = StringField('Work Hours', validators=[InputRequired(),
                                                      Length(min=4, max=25)])
    validthrough = StringField('Valid Till Date',
                               validators=[InputRequired(),
                                           Length(min=4, max=25)])
    jobdescription = TextAreaField('Description',
                                   validators=[InputRequired(),
                                               Length(min=4, max=25)])

###################################################
#                     ROUTES                      #
###################################################

# sargonboard
@app.route('/sargonboard')
def sargonboard():
    return render_template('sargon.html')


# Home Page
@app.route('/')
def index():
    return render_template('home.html')


# Role Page
@app.route('/role', methods=['GET', 'POST'])
def role():
    form = SargonForm()
    return render_template('role.html', form=form)


# Candidate Page
@app.route('/candidate', methods=['GET', 'POST'])
def candidate():
    # form = SargonForm()
    templateData ={'title':'Registration'}
    return render_template('candidate.html', **templateData)


# Registration Page
@app.route('/registration')
def registration():
    templateData ={'title':'Registration'}
    return render_template('registration.html', **templateData)


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Jobboard
@app.route('/jobboard')
def jobboard():
    jobdata = jobs.query.all()
    return render_template('jobboard.html', jobdata=jobdata)


# SingleJoB
# Single Job Info
@app.route('/job/<jobsid>')
def job(jobsid):

    job = jobs.query.filter_by(jobsid=jobsid).first_or_404()
    return render_template('job.html', job=job)


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                  method='sha256')
        new_user = adminusers(companyname=form.companyname.data,
                              firstname=form.firstname.data,
                              surname=form.surname.data,
                              username=form.username.data,
                              email=form.email.data,
                              password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# Sargon - Home Page
@app.route('/sargon', methods=['GET', 'POST'])
def sargonhome():
  form = SargonForm()

  return render_template('sargon.html', form=form)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = adminusers.query.filter_by(username=form.username.data).first()
        if user:
           if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('adminboard'))

        return'Invalid username or password'

    return render_template('login.html', form=form)


# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('logout'))


# AdminBoard
@app.route('/adminboard')
@login_required
def adminboard():
    return render_template('adminboard.html', name=current_user.username)


# sargonBoard
@app.route('/sargon', methods=['GET', 'POST'])
def sargon():
  return render_template('sargon.html')

# AddJob
@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = Jobs()

    if form.validate_on_submit():
        new_job = jobs(jobtitle=form.jobtitle.data,
                       reference=form.reference.data,
                       postcategoryid=form.postcategoryid.data,
                       salary=form.salary.data,
            currency=form.currency.data, locationcity=form.locationcity.data,
                       companytype=form.companytype.data,
                       experiencelevelid=form.experiencelevelid.data,
            jobtype=form.jobtype.data, jobbenefits=form.jobbenefits.data,
                       educationalrequirements=form.
                       educationalrequirements.data,
                       postcode=form.postcode.data,
            workhours=form.workhours.data,
                       validthrough=form.validthrough.data,
                       jobdescription=form.jobdescription.data)
        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for('adminboard'))
    return render_template('add_job.html', form=form)


# EditJob
@app.route('/edit_job')
def edit_job():
    return render_template('edit_job.html')


if __name__ == '__main__':
    #app.secret_key = 'secret123'
    app.config['DEBUG'] = True
    app.run(debug=True)
