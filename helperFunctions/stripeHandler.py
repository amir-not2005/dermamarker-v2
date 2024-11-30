from flask import jsonify, url_for
import stripe

def stripe_create_checkout_session(filename):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1QPyXYGADQ2qx7ZNbtMyxcHc',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for("causes", q=filename, _external=True),
            cancel_url=url_for("causes", q=filename, _external=True),
            automatic_tax={'enabled': True},
            metadata={'filename':filename}
        )
    except Exception as e:
        return str(e)
    
    print("CHECKOUT BEFORE PURCHASE SESSION:",checkout_session)
    return checkout_session

def stripe_payment_status_webhook(payload, sig_header, STRIPE_ENDPOINT_KEY):

    filename = ''

    # Verify the signature first
    try:
        # Construct the event using the payload and signature
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_ENDPOINT_KEY)
    except ValueError as e:
        # Invalid payload
        return jsonify(success=False, error=e), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify(success=False, error=e), 400

    # Successful payment
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object'] # contains a stripe.checkout.Session
        print("checkout.session.completed", session)
        filename = session['metadata']['filename']
        print('Webhook filename', filename)
        user_id = session['id']
        customer_details = session['customer_details']
    # Return a success response
    return jsonify(success=True, filename=filename, user_id=user_id, customer_details=customer_details), 200