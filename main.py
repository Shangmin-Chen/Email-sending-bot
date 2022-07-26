from keep_alive import keep_alive
from replit import db
import asyncio
from checking_time import check_six
import algorithm

# this loop will be async
async def loop():
  # this segment is to see if theres nothing in database, wait until someone posts something into the database.
  while True:
    if "database" in db.keys():
      database = db["database"]
      for i in range(len(db["database"])):
        print(str(i+1), db["database"][i][0], db["database"][i][1], db["database"][i][2])
      break
    else:
      await asyncio.sleep(60)

  # Constant or init variables
  cool_down = 0
  
  while True:
    if check_six() == 0:
      # it's 6
      if cool_down == 0:
        # init run
        try:
          database = db["database"]
        except Exception as e:
          print(e)
        try:
          algorithm.execute(database)
        except Exception as e:
          print(e)
          # make it go on cooldown
        cool_down = 1

    if cool_down == 0:
      # ready
      await asyncio.sleep(60)

    # if ran already at 6
    elif cool_down == 1:
      if check_six() == 1:
        # this makes sure that the code runs once at 6, and goes into cooldown. Once it's not 6, it goes off cooldown and becomes available again.
        cool_down = 0
        # no longer 6
        await asyncio.sleep(60)
      else:
        # not ready
        await asyncio.sleep(60)

keep_alive()
asyncio.run(loop())