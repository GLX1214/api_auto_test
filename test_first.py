import requests

def test_get_user():
    # 发送请求获取用户ID为1的数据
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    # 检查状态码是不是200（代表请求成功）
    assert r.status_code == 200
    
    # 检查返回的json数据里有没有'id'这个字段
    assert "id" in r.json()