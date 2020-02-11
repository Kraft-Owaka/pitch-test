from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to The best Website Online'
    
    return render_template('index.html', title = title)


@main.route('/pickup')
def pickUpLine():
    
    posts = [
        {
            'author': 'Wendy Munyasi',
            'pickupLine': 'Is your dad a boxer? Because you sure as hell are a knock out!',
            'date_posted': 'May 14th, 1995',
            'pickup_id' : 1
        },
        {
            'author': 'Jakes Jakes',
            'pickupLine': 'Are you a magician? Because whenever I look at you, everyone else disappears!',
            'date_posted': 'January 14th, 2020',
            'pickup_id': 2
        }
    ]
    
    return render_template('pickup.html', posts = posts)

@main.route('/cryptography')
def crypto_line():
    
    posts = [
        {
            'author': 'Wendy Munyasi',
            'crypto_line': 'Quis custodiet ipsos custodes? Who will guard the guards?',
            'date_posted': 'May 14th, 1995',
            'crypto_id' : 1
        },
        {
            'author': 'Jakes Jakes',
            'crypto_line': 'Please accept this humble fax. My love for you is without wax.',
            'date_posted': 'January 14th, 2020',
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