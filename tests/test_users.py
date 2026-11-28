import yaml 

from common.request_client import RequestClient

client_1=RequestClient()

with open("config/config.yaml",encoding="utf-8") as f:
    config=yaml.safe_load(f)

base_url=config["base_url"]

def test_users_1():

    response=client_1.get(base_url + "/users/1")

    print("实际返回的状态码是：",response.status_code)

    assert response.status_code == 200


def test_users_404():

    response=client_1.get(base_url + "/users/9999")

    print("实际返回的状态码是：",response.status_code)

    assert response.status_code == 404