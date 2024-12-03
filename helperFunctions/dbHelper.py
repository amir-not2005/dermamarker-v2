import sqlite3

def save_contact_db(form_data):
    """Save contact form data to the database."""
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()

    # Insert the form_data into the table
    c.execute("""
        INSERT INTO contacts (name, email, subject, message)
        VALUES (?, ?, ?, ?)
    """, (form_data['name'], form_data['email'], form_data['subject'], form_data['message']))

    conn.commit()
    conn.close()

def save_analytics_db(form_data):
    """Save analytics form data to the database."""
    conn = sqlite3.connect('forms.db')
    c = conn.cursor()

    # Insert the form_data into the table
    c.execute("""
        INSERT INTO analytics (name, country, phone, age, gender, howKnow, message)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (form_data['name'], form_data['country'], form_data['phone'], form_data['age'], form_data['gender'], form_data['howKnow'], form_data['message']))

    conn.commit()
    conn.close()