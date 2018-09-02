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

# How to host it on my own ?

1. Install AWS CLI (https://aws.amazon.com/cli/) and login using `aws configure`
1. Install AWS SAM CLI (https://github.com/awslabs/aws-sam-cli/blob/develop/docs/installation.rst)
1. Create new S3 bucket for uploading SAM packages (either through AWS console or using `aws s3 mb s3://my-unique-bucket name`)
1. Clone this repository
1. `sam package --template-file template.yml --output-template-file packaged.yaml --s3-bucket my-unique-bucket-name`
1. `sam deploy --template-file packaged.yaml --stack-name my-stack-name --capabilities CAPABILITY_IAM`

# Automated Deploys

This repository is deployed automatically using AWS CodePipeline. Whenever there's a new commit to the master branch of this repo, AWS CodePipeline fetches the source from Github, builds it, creates a changeset and executes it.

To see how to enable CodePipeline in your own account, see https://docs.aws.amazon.com/lambda/latest/dg/build-pipeline.html

# The URL is too long! What's the point in that!?

Yep. I understand! :) Ideally this should be hosted with a really short domain name but 
I'm just too lazy and this is just trying out serverless

# What can be improved ?
1. Test coverage for the boto calls using moto*
1. Check proper URL format with protocol (the redirection does not work without protocol) 
1. Handle errors such as key not found and return proper error messages
