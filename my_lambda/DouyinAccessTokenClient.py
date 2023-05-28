import requests


class DouyinAccessTokenClient():
    def __init__(self, config):
        self.config = config

    def get_access_token(self):
        access_token, expire_time = self.__get_access_token_from_douyin()

        return access_token

    def __get_access_token_from_douyin(self):
        response = requests.post(self.config["url"], json=self.config).json()
        print(f"Got access token from douyin {response}")
        if response["err_no"] != 0:
            raise Exception(f"error call douyin to get access token: {response}")
        return (response["data"]["access_token"], response["data"]["expires_in"])
