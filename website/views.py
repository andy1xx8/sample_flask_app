from flask import (Blueprint, render_template, request, flash, jsonify, 
                    session, redirect, url_for, g)
from flask_login import login_required, current_user
from .models import Order, Sample
from . import db
import json
from io import StringIO
import pandas as pd

views = Blueprint('views', __name__)

fromwhere = 'None'
dummy = 0

def text_to_samples(text):
    samples = [x.strip() for x in text.split('\n') if x.strip()]
    return samples


def create_order(user, text, note):
    samples = text_to_samples(text)
    num_samples = len(samples)

    print('pretend to submit order!!!')

    # new_order = Order(user_id=current_user.id, num_samples=num_samples,
    #     status='submitted', note=note)

    # db.session.add(new_order)
    # db.session.commit()


@views.route('/confirm-order', methods=['GET', 'POST'])
#@login_required
def confirm_order():
    global fromwhere
    global dummy

    if request.method == 'POST':
        print(dummy)
        print('-'*20 + 'this is a test')
        dummy += 1
        return 'Done1234'

    return 'GET'

    if request.method == 'POST':
        print('<'*80)
        print(f"I'm in confirm_order(POST) I came from {fromwhere}")
        fromwhere = 'confirm_order(POST)'

        # text = session['order_sample_text']
        # note = session['order_note']

        # session.pop('order_sample_text', None)
        # session.pop('order_note', None)

        text, note = 'test', 'testing'

        create_order(current_user, text, note)

        flash('Order Submitted!', category='success')

    #return redirect(url_for('views.home'))
    return render_template("home.html", user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    global fromwhere

    if request.method == 'POST':
        text = request.form.get('samples')
        note = request.form.get('note')

        # session['order_sample_text'] = text
        # session['order_note'] = note

        if not text.strip():
            flash('No sample names provided!', category='error')
            # session.pop('order_sample_text', None)
            # session.pop('order_note', None)
        else:
            print('*'*80)
            print('*'*80)
            fromwhere = 'home(POST)'
            print('Before redirect to review_order template, i am %s' % fromwhere)

            # print(text)
            # sample_list = text_to_samples(text)

            sample_list = ['not actual samples','fake testing']

            return render_template("review_order.html", user=current_user, 
                sample_list=sample_list)

    fromwhere = 'home(GET)'
    return render_template("home.html", user=current_user)

@views.route('/cancel-order', methods=['POST'])
@login_required
def cancel_order():
    data = json.loads(request.data)
    order_id = data['orderId']
    order = Order.query.get(order_id)
    if order and order.status == 'submitted':
        if order.user_id == current_user.id:
            order.status = 'canceled'
            db.session.commit()

    return jsonify({})

