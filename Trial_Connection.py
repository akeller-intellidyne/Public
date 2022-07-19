import http.client
import json
import ssl

# Defining certificate related stuff and host of endpoint
certificate_file = r"C:\API\vagwesqlgrcaltx_pki_intop_emass.pem"
certificate_secret= r"*****Secret Phrase*******"
host = r"api.va.emass.apps.mil/api"
key_file = r"C:\API\vagwesqlgrcaltx_pki_intop_emass.key"

# Defining parts of the HTTP request
#request_url=r"/api/"
request_headers = {
    'Content-Type': 'application/json'
}

# Define the client certificate settings for https connection
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context= ssl.create_default_context(Purpose.CLIENT_AUTH)
context.load_verify_locations(certificate_file)
#context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
#context.load_cert_chain(certfile=certificate_file, keyfile=key_file , password=certificate_secret)

# Create a connection to submit HTTP requests
connection = http.client.HTTPSConnection(host, context=context, timeout=10)

# Print the HTTP response from the IOT service endpoint
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
