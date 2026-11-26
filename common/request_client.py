import requests   #import导入requests模版库

class RequestClient:  #定义RequestClient类


    #定义一个get实例方法，接收url参数
    #self是类的实例对象，表示当前对象本身，可以用来访问类的属性和方法
    def get(self,url):

        #返回requests.get(url)值给调用者
        return requests.get(url)