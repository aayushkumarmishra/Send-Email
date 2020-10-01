import smtplib
import csv

#Code_Start
def get_credentials(filepath):
    with open("credentials.txt", "r") as f:
        Email_Address = f.readline()
        Email_Pass = f.readline()
    return (Email_Address, Email_Pass)


def login(email_address, email_pass, s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("login")



def Send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    Email_Address, Email_Pass = get_credentials("./credentials.txt")
    login(Email_Address, Email_Pass, s)
    

    # message to be sent
    subject = "Welcome to python"
    body = """Python is an interpreted, high-level,
    general-purpose programming language.\n
    Created by Guido van Rossum and first released in 1991,
    Python's design philosophy emphasizes code readability\n
    with its notable use of significant whitespace"""
    message = f"Subject : {subject} \n\n {body}"

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.sendmail(Email_Address, email[0], message)
            print("Send To " + email[0])

    # terminating the session
    s.quit()
    print("sent")


if __name__ == "__main__":
    Send_mail()import smtplib
import csv


def get_credentials(filepath):
    with open("credentials.txt", "r") as f:
        Email_Address = f.readline()
        Email_Pass = f.readline()
    return (Email_Address, Email_Pass)


def login(email_address, email_pass, s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("login")



def Send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    Email_Address, Email_Pass = get_credentials("./credentials.txt")
    login(Email_Address, Email_Pass, s)
    

    # message to be sent
    subject = "Welcome to python"
    body = """Python is an interpreted, high-level,
    general-purpose programming language.\n
    Created by Guido van Rossum and first released in 1991,
    Python's design philosophy emphasizes code readability\n
    with its notable use of significant whitespace"""
    message = f"Subject : {subject} \n\n {body}"

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.sendmail(Email_Address, email[0], message)
            print("Send To " + email[0])

    # terminating the session
    s.quit()
    print("sent")


if __name__ == "__main__":
    Send_mail()
