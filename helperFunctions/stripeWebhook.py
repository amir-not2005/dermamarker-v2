from flask import jsonify
import stripe

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
    return jsonify(success=True, event=event['type']), 200