from flask import render_template, redirect, url_for, request, jsonify, session
from app import app, db
from app.models import User
import stripe
from datetime import datetime

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            if user.subscribed or user.is_free_trial_active():
                return render_template('home.html')
            else:
                return redirect(url_for('subscribe'))
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
    return redirect(url_for('home'))

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'EZStudy Premium Plan',
                    },
                    'unit_amount': 300,
                },
                'quantity': 1,
            }],
            mode='subscription',
            success_url=url_for('success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('cancel', _external=True),
        )
        return jsonify({
            'id': checkout_session.id
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/success')
def success():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user.subscribed = True
            db.session.commit()
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')
