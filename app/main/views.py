from flask import render_template
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import Reviews, User
from .forms import ReviewForm,UpdateProfile
from flask_login import login_required


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'welcom'
    return render_template('index.html',message = message) 

    
@main.route('/pickup')
def pickUpLine():
    
    posts = [
        {
            'author': 'Trevor M',
            'pickupLine': 'Id a boxer',
            'date_posted': 'May 14th, 1885',
            'pickup_id' : 1
        },
        {
            'author': 'Jose But',
            'pickupLine': 'you  else !',
            'date_posted': 'January 14th, 2080',
            'pickup_id': 2
        }
    ]
    
    return render_template('pickup.html', posts = posts)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    

@main.route('/user/<uname>'update',methods = ['GET','POST'])
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/cryptography')
def crypto_line():
    
    posts = [
        {
            'author': 'WERE',
            'crypto_line': ' will?',
            'date_posted': 'May 14th, 9095',
            'crypto_id' : 1
        },
        {
            'author': 'Jakes Jakes',
            'crypto_line': 'accept Me.',
            'date_posted': 'January 14th, 8020',
            'crypto_id': 2
        },
        {
            'author': 'Susan Jakes',
            'crypto_line': 'Everything is possible. The impossible just takes longer.',
            'date_posted': 'January 14th, 2020',
            'crypto_id': 2
        }
    ]
    
    return render_template('cryptography.html', posts = posts)