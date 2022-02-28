import imp
import logging
import time
from flask import render_template, session, redirect, url_for, current_app, flash

from . import main
from .forms import MessageForm

from concurrent.futures import ThreadPoolExecutor
# 创建线程池执行器
executor = ThreadPoolExecutor(2)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name=session.get('name'))


@main.route('/message', methods=['GET', 'POST'])
def message():
    form = MessageForm()
    
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data

        session['name'] = name
        session['message'] = message
        session['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        
        flash('Send successfully')
        return redirect(url_for('main.message'))
    return render_template('message.html', form=form)

@main.route('/config', methods=['GET', 'POST'])
def config():
    return render_template('config.html')
