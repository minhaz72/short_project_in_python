import email
import smtplib
print('hi, this is a email  sender : ')
print('====from there you can send email------')
email=input('enter your email address : ')
password=input('enter your password : ')
con=smtplib.SMTP('smtp.gmail.com',  587)
con.starttls()
con.login(user=email , password=password)
con.sendmail(from_addr=email , to_addrs='receipentemail@gmail.com', msg='hi')
con.close()

