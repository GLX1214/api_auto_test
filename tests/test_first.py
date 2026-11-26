import yaml                                       # import导入yaml模版库，用来读取yaml配置文件
from common.request_client import RequestClient   # 导入请求封装

client = RequestClient()   # 把RequestClient类实例化，然后赋值给client变量（对象）、


#with：自动关闭文件
#以utf-8的编码方式打开，打开config/config.yaml文件，然后赋值给f变量
with open("config/config.yaml", encoding="utf-8") as f:
    config = yaml.safe_load(f)   #把f文件里的内容用yaml安全加载出来，转化为python字典，然后赋值给config变量
base_url = config["base_url"]    #从config里获取base_url并赋值给base_url变量


def test_get_user_1():    #定义一个test_get_user_1函数用来测试
    # 测试思维：访问存在的用户(id=1)，期望200
    response = client.get(base_url + "/users/1")  #调用client对象的get方法，传入base_url + "/users/1"作为参数，返回值赋值给response变量
    print("实际返回的状态码是:", response.status_code)
    assert response.status_code == 200  #断言判断返回的状态码是否等于200，如果不等于200，则测试失败


def test_get_user_404():
    # 测试思维：访问不存在的用户(id=9999)，期望404
    response = client.get(base_url + "/users/9999")  #调用client对象的get方法，传入base_url + "/users/9999"作为参数，返回值赋值给response变量
    print("实际返回的状态码是:", response.status_code)
    assert response.status_code == 404 #断言判断返回的状态码是否等于404，如果不等于404，则测试失败
