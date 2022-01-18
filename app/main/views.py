import imp
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from . import main
from .forms import MessageForm

from ..screen.script import print_message


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name=session.get('name'))


@main.route('/message', methods=['GET', 'POST'])
def message():
    form = MessageForm()
    
    if form.validate_on_submit():
        name = form.name.data
        message = form.name.data

        session['name'] = name
        session['message'] = message

        print_message(session.get('message'))

        return redirect(url_for('.message'))
    return render_template('message.html', form=form, name=session.get('name'), message=session.get('message'))
