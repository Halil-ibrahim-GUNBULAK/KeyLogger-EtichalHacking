import smtplib, ssl


def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "sender_email@gmail.com"
    password = "sender_email_password"
    receiver_email = "recipient email"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(from_addr=sender_email,to_addrs= receiver_email, msg="mail send \n "+str(message).encode('ascii', 'ignore').decode('ascii'))
        print("mail gönderildi")
    except Exception as e:
        print(e)
    finally:
        server.quit()