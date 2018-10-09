from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, User
from forms import UsersForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/homework_users'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', title='Home', users=users)

@app.route('/read')
def read():
    #users_shorts = User.query.filter(User.prog_lang == 'py')
    users = User.query.all()
    return render_template('read.html', title='All Users', users=users)

@app.route('/update_user/<int:uid>', methods=['GET', 'POST'])
def update_user(uid):
    form = UsersForm()
    #uid = "Test ID"
    users = User.query.all()
    user_up = User.query.filter(User.uid == uid).first()
    if request.method == 'GET':
        return render_template('update_user.html', title='Update', uid=uid, users=users, form=form)
    else:
        if form.validate_on_submit():
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            prog_lang = request.form['prog_lang']
            experience_yr = request.form['experience_yr']
            age = request.form['age']
            hw1_hrs  = request.form['hw1_hrs']
            user_up.username = username
            user_up.first_name= first_name
            user_up.last_name= last_name
            user_up.prog_lang= prog_lang
            user_up.experience_yr= experience_yr
            user_up.age= age
            user_up.hw1_hrs= hw1_hrs
            db.session.commit()
            return redirect(url_for('index'))


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = UsersForm()
    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            prog_lang = request.form['prog_lang']
            experience_yr = request.form['experience_yr']
            age = request.form['age']
            hw1_hrs  = request.form['hw1_hrs']
            new_user = User(username =username, first_name=first_name, last_name=last_name, prog_lang=prog_lang, experience_yr=experience_yr, age=age, hw1_hrs=hw1_hrs)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

@app.route('/dlt_user/<int:uid>')
def dlt_user(uid):
    user_up = User.query.filter(User.uid == uid).first()
    db.session.delete(user_up)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/load_data', methods=['GET'])
def load_data():
    users_json = {'users': []}
    users = User.query.all()
    for user in users:
        user_info = user.__dict__
        del user_info['_sa_instance_state']
        users_json['users'].append(user_info)
    return jsonify(users_json)

if __name__ == "__main__":
    app.run(debug=True)
