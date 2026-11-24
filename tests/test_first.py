import requests   #import导入requests这个库

def test_get_user_1():   #定义一个test_get_user_1函数用来进行测试

    #requests.get("https://jsonplaceholder.typicode.com/users/1")
    #是请求网址中用户ID为1的用户的信息，然后response是返回的响应对象，里面包含了请求的状态码、响应头、响应体等信息
    response=requests.get("https://jsonplaceholder.typicode.com/users/1")

    #assert：是断言，作用是：判断一个条件是否为真；如果不为真，就抛出断言错误。
    #response.status_code：获取响应的HTTP状态码
    #status_code = 状态码
    #断言判断响应的HTTP状态码是否为200，如果是200，说明请求成功，测试通过；如果不是200，说明请求失败，测试不通过。
    assert response.status_code == 200
    