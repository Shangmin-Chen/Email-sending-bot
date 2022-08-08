# import os
# from email.message import EmailMessage
# import ssl
# import smtplib
# def send(receiver):
#   password = os.environ['password']
  
#   sender = "syepscreen@gmail.com"
  
#   password = password
  
#   receiver = receiver
  
#   subject = "Daily Health Screen"
#   body = ""
  
#   em = EmailMessage()
#   em["From"] = sender
#   em["To"] = receiver
#   em["subject"] = subject
#   em.set_content(body)
#   context = ssl.create_default_context()
  
#   with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(sender, password)
#     smtp.sendmail(sender,receiver, em.as_string())
"""above is SSL"""
"""below is TLS"""
import os
import smtplib
from email.message import EmailMessage
import checking_time
def send(email, f, l):
  weekday = checking_time.return_weekday()
  m,d,y = checking_time.return_date()
  EMAIL_ADDRESS = 'syepscreen@gmail.com'
  EMAIL_PASSWORD = os.environ['password']
  
  msg = EmailMessage()
  msg['Subject'] = 'NYC DOE Health Screening - {}, {} {}, {}  7:00 AM'.format(weekday, m,d,y)
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = email
  
  msg.set_content('This is a plain text email')
  
  msg.add_alternative("""\
  <!DOCTYPE html>
  <html>
  
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>replit</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  
  <body>
  <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#f4f4f4">
          <tbody><tr>
              <td align="center" valign="top" style="padding:0 10px">
                  <table width="650" border="0" cellspacing="0" cellpadding="0">
                      <tbody><tr>
                          <td style="width:650px;min-width:650px;font-family:Arial,sans-serif;font-size:16px;line-height:24px;margin:0;font-weight:normal;padding:55px 0px">
  
                              Hello {} {},<br>
                              This is your <span class="il">health</span> screening status as of {}, {} {}, {}  7:00 AM
                              <br><br>
                              <table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-radius:4px">
                                  <tbody><tr>
                                      <td style="font-family:Arial,sans-serif;width:40px;height:60px;text-align:left;background-color:#173f5f;padding-left:20px">
                                          <img style="width:40px;height:40px;padding:10px" src="https://ci3.googleusercontent.com/proxy/8_ZwdScHDKrdI755kqeJ02COxruey833H-8cZJYvVEsxeaP0Kg52y4IpnBI0QCBzX0d8Ujlub7d2bIgAKG3-frnxC_U5qDnvNawleGq2HcU1EoFO6w=s0-d-e1-ft#https://www.nycenet.edu/ui/apps/resources/graphics/user-circle.png" class="CToWUd" data-bit="iit">
                                      </td>
                                      <td style="font-family:Arial,sans-serif;height:60px;text-align:left;background-color:#173f5f;color:white;font-size:18px;padding-left:10px"><strong>{} {}</strong></td>
                                      <td style="font-family:Arial,sans-serif;height:60px;text-align:right;background-color:#173f5f;color:white;padding-right:10px;padding-right:20px">
                                          <span style="padding:5px 10px;width:100px;text-align:center;display:inline-block;font-weight:bold;font-size:12px;border-radius:10px;background-color:#ff8d1c;color:white">STUDENT</span>
                                      </td>
                                  </tr>
                                  <tr>
                                      <td colspan="3" style="font-family:Arial,sans-serif;border-right:1px solid #ddd;border-left:1px solid #ddd;background-color:white;border-bottom:1px solid #ddd;padding:40px 30px;text-align:center">
                                          <div style="padding-bottom:10px"><img src="https://ci3.googleusercontent.com/proxy/7nRz04sx1RiCSr000InlPG4PQiKNJ8t9t6rmv46WOzdoDBFIZ16nWGjHcfm0Wu2rE_nF9z81p58YBomcv6I8Yd0boidA0NfQ0okR0iik9UJP4U1jSgA9kym1eHc=s0-d-e1-ft#https://www.nycenet.edu/ui/apps/resources/graphics/check-circle-green.png" class="CToWUd" data-bit="iit"></div>
                                          <br>
                                          <div style="font-weight:bold;color:#28a745;font-size:20px;padding:10px">Cleared to Enter DOE Schools and Facilities</div>
                                          <div style="font-weight:bold;color:#28a745;font-size:28px">{}, {} {}, {}  7:00 AM</div>
                                          <br>
                                          <div style="font-size:16px"></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>
  </body>
  
  </html>
  """.format(f,l, weekday, m, d, y,f,l,weekday,m,d,y), subtype='html')
  
  
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      smtp.send_message(msg)
      print('sent to {} {}'.format(f,l))

import threading
import numpy as np
# this alogrithm makes it so sebby can go commercial.
url = "https://healthscreening.schools.nyc/home/submit"


def insert(data_list, code):
  threads = []
  for i in data_list:
    fname = i[0]
    lname = i[1]
    email = i[2]
    t = threading.Thread(target=send, daemon=True, args=(email, fname.capitalize(), lname.capitalize()))
    threads.append(t)
  for i in range(len(data_list)):
    threads[i].start()

  for i in range(len(data_list)):
    threads[i].join()

def execute(data_list):
  length = len(data_list)

  threads = []
  
  a = float(length) / float(15)
  print("a={}".format(a))
  b = length // 15
  print("b={}".format(b))
  
  if a <= 1:
    insert(data_list, 0)

  elif a > b:
    b += 1
    data_list = np.array_split(data_list, b)
    for i in data_list:
      t = threading.Thread(target=insert, daemon=True, args=(i, 0))
      threads.append(t)

    for i in range(b):
      threads[i].start()

    for i in range(b):
      threads[i].join()