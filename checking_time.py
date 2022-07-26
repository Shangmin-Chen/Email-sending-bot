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