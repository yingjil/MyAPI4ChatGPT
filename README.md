# Download the package from GitHub

```
$ git clone git@github.com:yingjil/MyAPI4ChatGPT.git
```

# Configure AWS Account to install the API

If you don't have US AWS account, please register one via https://aws.amazon.com/.
If you have US AWS account, but don't know your keys, please refer
to (https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-your-credentials.html)

```
$ export AWS_ACCESS_KEY_ID=<your aws account key, e.g.: AKIAU53GUXQ62MUDWKF4>
$ export AWS_SECRET_ACCESS_KEY=<your aws account key, e.g.: WxcqoLjBtutydA1OIInJ/mKe7WmcNt5JYF3oKasP>
```

# Configure Open AI Key

```
$ export OPENAI_API_KEY=<your open ai key, e.g.: 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>
```

# Deploy to AWS

```
$ cd MyAPI4ChatGPT
$ npm install -g aws-cdk
$ pip install aws-cdk-lib
$ cdk deploy
```

Answer 'y' to below question:

```
...
Do you wish to deploy these changes (y/n)? y
```

Find the API URL in the end of the output of 'cdk deploy':

```
...
Outputs:
MyStack.ApiHostUrl = <your api prefix>.execute-api.us-west-2.amazonaws.com
MyStack.myapiEndpointF52D9E64 = https://<your api prefix>.execute-api.us-west-2.amazonaws.com/prod/
...
✨  Total time: 96.34s

```

# You can use the API now

```
$ curl -X POST https://<your api prefix>.execute-api.us-west-2.amazonaws.com/prod/ -H 'content-type: application/json' --data '{"prompt":"Hello"}'

Hi there! How can I assist you today?
```

# Tech Support (not free)

email: jackandking@163.com

# References

* https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-your-credentials.html
* https://docs.aws.amazon.com/cdk/v2/guide/work-with.html#work-with-prerequisites
* 
