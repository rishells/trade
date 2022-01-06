
import time
import hmac
import hashlib
import requests
import json

#PUT se utiliza para actualizar.
#POST se utiliza para crear. 

bitso_key = "okURfcpasT"
bitso_secret = "e22a20b7312e4fcd24ce774395a974b1"
http_method = "POST" # Change to POST if endpoint requires data
#request_path = "/v3/balance/" 
request_path = "/v3/orders/" 
#POST https://api.bitso.com/v3/orders/


parameters = {'book':'xrp_mxn','side':'buy','type':'limit','major':'1','price':'13'}     # Needed for POST endpoints requiring data

# Create signature
nonce =  str(int(round(time.time() * 1000)))
message = nonce+http_method+request_path
if (http_method == "POST"):
  message += json.dumps(parameters)
signature = hmac.new(bitso_secret.encode('utf-8'),
                                            message.encode('utf-8'),
                                            hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)

# Send request
if (http_method == "GET"):
  response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})
elif (http_method == "POST"):
  response = requests.post("https://api.bitso.com" + request_path, json = parameters, headers={"Authorization": auth_header})

print(response.content)