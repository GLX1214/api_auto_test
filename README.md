# api_auto_test · 接口自动化测试框架

基于 pytest + requests 的接口自动化测试项目，支持分层管理、配置驱动、数据驱动与异常场景覆盖。

## 技术栈
Python 3.10 · pytest · requests · PyYAML · Allure · Git

## 快速开始
bash
git clone https://github.com/GLX1214/api_auto_test.git
cd api_auto_test
pip3 install -r requirements.txt
python3 -m pytest

## 项目结构
api_auto_test/
├── config/config.yaml          # 接口地址等配置
├── common/request_client.py    # 请求封装类
├── tests/                      # 测试用例（test_first / test_users）
├── data/                       # YAML 测试数据（W2 加入）
├── pytest.ini                  # 测试目录与默认参数配置
└── requirements.txt            # 依赖清单

## 当前能力
- 请求封装与用例分离，配置与代码解耦
- 正常场景（200）与异常场景（404）断言
- pytest.ini 统一 -v -s 参数，clone 后一条命令运行
