import os

OPEN_AI_API_KEY = os.environ['OPENAI_API_KEY']
DOUYIN_ACCESS_TOKEN_CONFIG = {
    "url": "https://developer.toutiao.com/api/apps/v2/token",
    "appid": "ttbaedcc5025d2e24701",
    "secret": os.environ['DOUYIN_SECRET_ttbaedcc5025d2e24701'],
    "grant_type": "client_credential",
    "time_out": 7200,
}

DOUYIN_CONTENT_CHECK_CONFIG = {
    "url": "https://developer.toutiao.com/api/v2/tags/text/antidirt"
}
