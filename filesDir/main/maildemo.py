

import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("info.archievr@gmail.com","9826118075@Aman")

server.sendmail("info.archievr@gmail.com","amanansari10106@gmail.com", "hello from python")