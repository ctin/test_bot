from storage import *

def OnPayload(data):
    message = data.decode("utf-8")
    print(message)

def GetUsers():
  all_users = []
  for user in Users.select():
    all_users.append(user.email)
  return str(all_users)