import smtplib, ssl

def send(email, message):
    # send an email to the user
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "#####"
    receiver_email = email
    password = "####"
    message = """Hi there, this is a test email from the booking system. {message}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
