from crypt import methods
from flask import Flask, request, send_from_directory
import pandas as pd
from tabulate import tabulate
import server_handler

app = Flask('')

@app.route('/', methods = ['POST', 'GET'])
def main():
  try:
    jsonRequest=request.args.get("jsonRequest")
    tblfmt = request.args.get("tblfmt", default = 'plain')
    loginRequired = request.args.get('loginRequired', default=False, type=lambda v: v.lower() == 'true')
    print("[I] Login Required : ",loginRequired)
    if request.method == 'POST':
      payload = request.data
      if jsonRequest == "true":
        jsonPayload = request.json

        dataframe = pd.DataFrame(jsonPayload, index=[0]).transpose()
        payload = '```'+tabulate(dataframe,tablefmt=tblfmt)+'```'
      print("[I] Payload: \n", payload)
      server_handler.OnPayload(payload)

      return 'success!', 200
    else:
      print("Get request")
      return 'hello there', 200
  except Exception as e:
    print("[X] Exception Occured : ", e)
    return 'failure', 500
