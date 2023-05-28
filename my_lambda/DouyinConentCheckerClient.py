import requests


class DouyinConentCheckerClient():
    def __init__(self, config, douyinAccessTokenClient):
        self.config = config
        self.douyinAccessTokenClient = douyinAccessTokenClient

    def check(self, content):
        access_token = self.douyinAccessTokenClient.get_access_token()
        header = {"X-Token": access_token}
        response = requests.post(self.config["url"], headers=header, json={
            "tasks": [{"content": content}]}).json()
        print(f"Got content check response from douyin {response}")
        if"error_id" in response:
            raise Exception(f"error call douyin to check content: {response}")
        for predict in response["data"][0]["predicts"]:
            if predict["hit"]:
                return True
        return False