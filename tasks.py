import thermometer
from config import *
import mail
import data
import datetime

def check():
    """Check if the current temperature of the fridge is within certain bounds. If not, it sends alert emails"""
    current_temp = thermometer.read_temp()

    if current_temp >= MAX_TEMP:
        print("Fridge temperature too high")
        subject = "FRIDGE ALERT"
        text = f"The fridge temperature has risen above safe levels, the current temperature is {current_temp}°C."

        for recipient in RECIPIENTS:
            try:
                mail.send_email(
                    sender_email=SENDER_EMAIL,
                    password=SENDER_PASSWORD,
                    receiver_email=recipient,
                    subject=subject,
                    body=text
                )
                print(f"Sent alert email to: {recipient}")
            except Exception as e:
                print(f"Had error:\n{e}\nwhen sending an email.")
                continue
            print("\n\n")
        print("Sent alert emails")

    elif current_temp <= MIN_TEMP:
        print("Fridge temperature too low")
        subject = "FRIDGE ALERT"
        text = f"The fridge temperature has fallen below safe levels, the current temperature is {current_temp}°C."

        for recipient in RECIPIENTS:
            try:
                mail.send_email(
                    sender_email=SENDER_EMAIL,
                    password=SENDER_PASSWORD,
                    receiver_email=recipient,
                    subject=subject,
                    body=text
                )
                print(f"Sent alert email to: {recipient}")
            except Exception as e:
                print(f"Had error:\n{e}\nwhen sending an email.")
                continue
            print("\n\n")
        print("Sent alert emails")
    else:
        print("Fridge temperature is within safe levels.")


def test():
    """Gets the current temperature. Acts as the default behaviour"""
    current_temp = thermometer.read_temp()
    print(f"The current temperature reading is {current_temp}°C")


def ping():
    """Checks that the raspi is online by sending an email to the main email adress"""
    subject = "Fridge update - I'm still here"
    text = f"Just letting you know that I'm still here, have a nice day!."
    recipient = MAIN_RECIPIENT
    try:
        mail.send_email(
            sender_email=SENDER_EMAIL,
            password=SENDER_PASSWORD,
            receiver_email=recipient,
            subject=subject,
            body=text
        )
        print(f"Sent ping email to: {recipient}")
    except Exception as e:
        print(f"Had error:\n{e}\nwhen sending an email.")
        pass


def log():
    """Log the current temperature"""
    current_temp = thermometer.read_temp()

    now = str(datetime.datetime.now())

    print(f"Current datetime is: {now}")
    print(f"Current temp is: {current_temp}")

    data.append_data(now, current_temp)


def wipe():
    """Wipes the csv file"""
    data.wipe_csv(CSV_PATH)


def graph():
    """Send an email with a graph of the logs"""
    data.graph(CSV_PATH)

    subject = "Plot of fridge temperature"
    text = f"Here is a plot of the fridge temperature"
    recipient = MAIN_RECIPIENT
    try:
        mail.send_email_with_image(
            sender_email=SENDER_EMAIL,
            password=SENDER_PASSWORD,
            receiver_email=recipient,
            subject=subject,
            body=text,
            filepath=GRAPH_PATH
        )
        print(f"Sent graph to: {recipient}")
    except Exception as e:
        print(f"Had error:\n{e}\nwhen sending an email.")
        pass
