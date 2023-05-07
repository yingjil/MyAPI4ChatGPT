# Download the package from GitHub

```git clone git@github.com:yingjil/MyAPI4ChatGPT.git```

# Configure AWS Account to install the API

```
export MY_AWS_ACCOUNT=<your aws account id, e.g.: 123456789>
```

# Configure Open AI Key

```
export OPENAI_API_KEY=<your open ai key, e.g.: sk-xxx>
```

# Deploy to AWS

```
$ cd MyAPI4ChatGPT
$ cdk synth
$ cdk deploy
```

# You can use the API now

```
curl -X POST  https://v7fs3742y264mkvdybminofc7i0zggsv.lambda-url.us-west-2.on.aws/  -H 'content-type: application/json' --data '{"prompt":"Hello"}'
```

# Tech Support

email: jackandking@163.com
