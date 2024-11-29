import stripe
from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField
import os
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, DataRequired, Regexp
from wtforms import StringField, SubmitField, SelectField, IntegerField
from findPhotos import execute
from helperFunctions.renderTextScanner import render_text_scanner_page
from helperFunctions.stripeWebhook import stripe_payment_status_webhook
from helperFunctions.dbHandler import save_contact_db, save_analytics_db
from config import DOMAIN, STRIPE_PUBLISHABLE, STRIPE_SECRET, STRIPE_ENDPOINT_KEY
import base64

app = Flask(__name__)

# Flask file upload size 10 MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 

# Stripe secret key
stripe.api_key = STRIPE_SECRET

# User data input
class UserDataForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    email = StringField('Your Email', validators=[DataRequired()], render_kw={"placeholder": "Your Email"})
    phone = StringField('Phone Number', 
                        validators=[Regexp(r'^\+?\d{1,4}?[\s.-]?\(?\d{1,3}?\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}$', 
                                          message="Phone number must include a country code (e.g., +1, +44) and follow a valid format.")])
    age = IntegerField('Age', validators=[DataRequired()], render_kw={"placeholder": "Enter your age"})
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 
                         validators=[DataRequired()])
    howKnow = SelectField('How did you hear about us?', 
                          choices=[('friends', 'Friends'), 
                                   ('socialNetworks', 'Social Networks'), 
                                   ('webSearch', 'Web Search'), ("other", "Other")],
                          validators=[DataRequired()])
    message = TextAreaField('Message', render_kw={"placeholder": "Leave a message here"})

    submit = SubmitField('Submit Data')

# File input
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField('Submit File')

# File and User input combined form
class CombinedForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_form = UserDataForm()
        self.file_form = UploadFileForm()
    
    submit = SubmitField('Submit Both')

app.config['SECRET_KEY'] = os.urandom(12)
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit-data', methods=['POST'])
def handle_submitted_data():
    combinedForm = CombinedForm()

    # Get image form data
    file_form=combinedForm.file_form
    file = file_form.file.data

    # Save image as temp file in folder - folder will be cleared after scanner execution
    upload_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])
    original_filename = secure_filename(file.filename)
    filename = "{random_part}{file_extension}".format(
        random_part=os.urandom(12).hex(),
        file_extension=os.path.splitext(original_filename)[1]
    )
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    # Get analytics form data
    user_form = combinedForm.user_form

    # Store user data in the db
    form_data = {
        "name" : user_form.name.data,
        "email" : user_form.email.data,
        "phone" : user_form.phone.data,
        "age" : user_form.age.data,
        "gender" : user_form.gender.data,
        "howKnow" : user_form.howKnow.data,
        "message" : user_form.message.data
    }
    save_analytics_db(form_data)

    return redirect(create_checkout_session(file_path))

def create_checkout_session(file_path):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1QPyXYGADQ2qx7ZNbtMyxcHc',
                    'quantity': 1,
                },
            ],
            metadata={"file_path": file_path},
            mode='payment',
            success_url=url_for("causes", payment_status=True ,_external=True),
            cancel_url=url_for("causes", payment_status=False ,_external=True),
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("WEBHOOK RECEIVED")

    # Retrieve the payload and the signature header
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    # Run webhook logic
    response = stripe_payment_status_webhook(payload, sig_header, STRIPE_ENDPOINT_KEY)
    print(response)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def feedback():
    return render_template('contact.html')

@app.route('/scanner')
def causes():
    combinedForm = CombinedForm()
    file_path = request.args.get("file_path")
    
    # Start scanner
    scan_results = execute(userimage = file_path)

    # Delete user uploaded file locally
    if os.path.exists(file_path):
        os.remove(file_path)

    # Render text based on results
    [irrelevantImage, x, x1, x2, d1, da1, im1, imp1, maxdt, it1, imt1, dt, pm] = render_text_scanner_page(scan_results)
    
    return render_template('causes.html', irrelevantImage=irrelevantImage, form=combinedForm, x=x, x1=x1, x2=x2,d1=d1,da1=da1,im1=im1,imp1=imp1,maxdt=maxdt,it1=it1,imt1=imt1,dt=dt,pm=pm)

@app.route('/save_form', methods=['POST'])
def save_form():
    # Extract form data
    form_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'subject': request.form['subject'],
        'message': request.form['message']
    }

    # Helper function to save contant data
    save_contact_db(form_data)
    return render_template('contact.html')

    

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))