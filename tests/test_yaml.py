import yaml


def test_yaml():
    with open("config/config.yaml",encoding="utf-8") as f:


        config=yaml.safe_load(f)

        base_url=config["base_url"]

        print(base_url)