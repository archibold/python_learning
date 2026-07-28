import smtplib
email = ''
password = ''


with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=email, msg='Subject:hello\n\n to jest wiadomosc')
