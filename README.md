# URL Redirector

This repo contains a serverless (AWS Lambda) URL redirector  written in Python 3.7 and some tests (more coming!*)

# What serverless features are used ?

1. AWS Lambda functions written in Python
2. AWS API Gateway for the API
3. DynamoDB to store the values

# How does it work ?

There are 2 endpoints.

1. `POST` to `/submit` to create a url redirection. 
   This generates a unique `key` and saves it along with the submitted URL to DynamoDB
   
2. `GET` to `/{key}` to redirect to the stored URL
   This finds the record in DynamoDB and returns a HTTP 301 redirect to the stored URL

# How to use ?

I've hosted this on my own domain `api.ranhiru.com/url_redirector`

Use Postman or your favorite HTTP Client and send a POST request to

`https://api.ranhiru.com/url_redirector/submit` with the following body 

E.g: 
`{ "url": "https://www.google.com" }` (or your favorite URL including the http/https protocol)

This will return a unique key in the JSON

`{"key": "OJyRIBhiD7owsQ"}`

Replace the variable key with the returned key and `https://api.ranhiru.com/url_redirector/{key}` 
and use the URL wherever there's support for 301 redirects.

E.g: `https://api.ranhiru.com/url_redirector/OJyRIBhiD7owsQ`

# The URL is too long! What's the point in that!?

Yep. I understand! :) Ideally this should be hosted with a really short domain name but 
I'm just too lazy and this is just trying out serverless

# What can be improved ?

1. Test coverage using Moto
1. Check proper URL format with protocol (the redirection does not work without protocol) 
1. Handle errors such as key not found and return proper error messages
