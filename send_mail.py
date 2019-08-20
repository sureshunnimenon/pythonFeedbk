import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='6178e33a078bec'
    password='8c5ae823e70d3d'
    message = f"<h3> New feedback submission </h3><ul> <li> Customer: {customer} </li> <li> Dealer: {dealer} </li><li> Rating: {rating} </li><li> Comments: {comments} </li> </ul>"
    sender_email= "suresh.naloor@gmail.com"
    receiver_email= "suresh.unni.menon@gmail.com"

    msg= MIMEText(message, 'html')

    msg['Subject'] ='Lexus feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
