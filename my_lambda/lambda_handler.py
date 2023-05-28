import json
import os
import time
from functools import lru_cache

import openai

from DouyinAccessTokenClient import DouyinAccessTokenClient
from DouyinConentCheckerClient import DouyinConentCheckerClient
from configs import DOUYIN_ACCESS_TOKEN_CONFIG, DOUYIN_CONTENT_CHECK_CONFIG

openai.api_key = os.environ['OPENAI_API_KEY']

douyinAccessTokenClient = DouyinAccessTokenClient(DOUYIN_ACCESS_TOKEN_CONFIG)
conent_checker = DouyinConentCheckerClient(DOUYIN_CONTENT_CHECK_CONFIG, douyinAccessTokenClient)


def call_openai(question):
    print(f"ask ai question: {question}")
    start_ts = time.time()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0]["message"]["content"]
    except Exception as e:
        print(e)
        raise
    end_ts = time.time()
    print(f"call openai cost {end_ts - start_ts} seconds")
    print(f"got ai answer len = {len(answer)}")
    return answer


@lru_cache
def call_openai_with_cache(prompt):
    print("call_openai_with_cache")
    question = prompt

    return call_openai(question)


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    body = json.loads(event['body'])
    prompt = body['prompt']

    try:
        if conent_checker.check(prompt):
            return {
                'statusCode': 500,
                'body': "输出包含违规内容，请稍后重试"
            }

        answer = call_openai_with_cache(prompt)

        if conent_checker.check(answer):
            return {
                'statusCode': 500,
                'body': "输出包含违规内容，请稍后重试"
            }

        return {
            'statusCode': 200,
            'body': answer
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': "something wrong!"
        }
