import smtplib, ssl

def send_mail_function():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "yash.test.noreply@gmail.com"
    sender_password = "Skull1324"
    recipient_email = "yashd2024@gmail.com"

    message = """\
    Subject: Fire Detected!

    Dear User,

    Fire has been detected. Please take necessary action immediately."""

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message)
    except Exception as e:
        print("Errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",e)

# Example usage:
# threading.Thread(target=send_mail_function).start()
send_mail_function()