import pytz
import datetime

def check_six():  
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)
  
  d = int(now.strftime("%d"))
  m = int(now.strftime("%m"))
  y = int(now.strftime("%Y"))
  if datetime.date(y,m,d).weekday() < 5:
    current_time = now.strftime("%H")
    if current_time == "06":
      return 0
    else:
      return 1
  else:
    return 1

def return_weekday():
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)
  
  d = int(now.strftime("%d"))
  m = int(now.strftime("%m"))
  y = int(now.strftime("%Y"))
  if datetime.date(y,m,d).weekday() == 0:
    return "Monday"
  elif datetime.date(y,m,d).weekday() == 1:
    return "Tuesday"
  elif datetime.date(y,m,d).weekday() == 2:
    return "Wednesday"
  elif datetime.date(y,m,d).weekday() == 3:
    return "Thursday"
  elif datetime.date(y,m,d).weekday() == 4:
    return "Friday"
  elif datetime.date(y,m,d).weekday() == 5:
    return "Saturday"
  elif datetime.date(y,m,d).weekday() == 6:
    return "Sunday"
    
def return_date():
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)
  
  d = int(now.strftime("%d"))
  m = int(now.strftime("%m"))
  y = int(now.strftime("%Y"))

  if m == 1:
    return 'January', str(d), str(y)
  elif m == 2:
    return 'Feburary', str(d), str(y)
  elif m == 3:
    return 'March', str(d), str(y)
  elif m == 4:
    return 'April', str(d), str(y)
  elif m == 5:
    return 'May', str(d), str(y)
  elif m == 6:
    return 'June', str(d), str(y)
  elif m == 7:
    return 'July', str(d), str(y)
  elif m == 8:
    return 'August', str(d), str(y)
  elif m == 9:
    return 'September', str(d), str(y)
  elif m == 10:
    return 'October', str(d), str(y)
  elif m == 11:
    return 'November', str(d), str(y)
  elif m == 12:
    return 'December', str(d), str(y)