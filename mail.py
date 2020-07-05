import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email(sender_email: str, password: str, receiver_email: str, subject: str = "Subject", body: str = "Body"):
    print(f"""Email settings:
    From: {sender_email}
    Password: {password} 
    To: {receiver_email}""")
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""\
    Subject: {subject}

    {body}
    """

    html = f"""\
    <html>
        <body>
            <p>
                {body}
            </p>
        </body>
    </html>
    """

    part_one = MIMEText(text, "plain")
    part_two = MIMEText(html, "html")

    message.attach(part_one)
    message.attach(part_two)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        try:
            server.login(sender_email, password)
            print("Logged in to server")
        except Exception as e:
            print(f"Had error logging on to server:\n{e}")
            return None
        try:
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Sent email")
        except Exception as e:
            print(f"Had error sending email:\n{e}")
            return None


def send_email_with_image(sender_email: str, password: str, receiver_email: str, subject: str = "Subject", body: str = "Body", filepath: str = None):
    print(f"""Email settings:
    From: {sender_email}
    Password: {password} 
    To: {receiver_email}""")
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"""\
    Subject: {subject}

    {body}
    """

    html = f"""\
    <html>
        <body>
            <p>
                {body}
            </p>
        </body>
    </html>
    """

    part_one = MIMEText(text, "plain")
    part_two = MIMEText(html, "html")

    try:
        img_data = open(filepath, "rb").read()
        image = MIMEImage(img_data, name="Graph.png")
    except FileNotFoundError:
        print("Image wasn't found")

    message.attach(part_one)
    message.attach(part_two)
    message.attach(image)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        try:
            server.login(sender_email, password)
            print("Logged in to server")
        except Exception as e:
            print(f"Had error logging on to server:\n{e}")
            return None
        try:
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Sent email")
        except Exception as e:
            print(f"Had error sending email:\n{e}")
            return None

# user = input("What is sender email?")
# password = input("What is the password")
# to = input("Who is the email being sent to?")
# subject = input("What is the subject?")
# text = input("What is the text?")
# send_email(sender_email=user, password=password, receiver_email=to, subject=subject, body=text)
