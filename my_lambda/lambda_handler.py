import json
import os
import time
from functools import lru_cache

import openai

openai.api_key = os.environ['OPENAI_API_KEY']


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
        answer = call_openai_with_cache(prompt)

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
