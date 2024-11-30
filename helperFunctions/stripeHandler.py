from flask import jsonify, url_for
import stripe

def stripe_create_checkout_session(metadata):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1QPyXYGADQ2qx7ZNbtMyxcHc',
                    'quantity': 1,
                },
            ],
            metadata={"file_path": metadata},
            mode='payment',
            success_url=url_for("causes", file_path = metadata, _external=True),
            cancel_url=url_for("causes", file_path = metadata, _external=True),
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)
    
    print("CHECKOUT SESSION:",checkout_session)
    return checkout_session

def stripe_payment_status_webhook(payload, sig_header, STRIPE_ENDPOINT_KEY):
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

    # Return a success response
    print("WEBHOOK EVENT:", event)
    return jsonify(success=True, event=event['type']), 200