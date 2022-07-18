import http.client
import json
import ssl

# Defining certificate related stuff and host of endpoint
certificate_file = r"C:\API\vagwesqlgrcaltx_pki_intop_emass.pem"
certificate_secret= r"*****Secret Phrase*******"
host = r"https://api.va.emass.apps.mil/api/"

# Defining parts of the HTTP request
#request_url=r"/api/"
request_headers = {
    'Content-Type': 'application/json'
}

# Define the client certificate settings for https connection
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile=certificate_file, password=certificate_secret)

# Create a connection to submit HTTP requests
connection = http.client.HTTPSConnection(host, context=context)

# Print the HTTP response from the IOT service endpoint
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
