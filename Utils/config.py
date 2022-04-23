import json

def get_token():
    with open("config.json") as f:
        token = json.load(f)["Token"]
    return token

def get_mysql_host():
    with open("config.json") as f:
        mysql = json.load(f)["Mysql"]["host"]
    return mysql

def get_mysql_username():
    with open("config.json") as f:
        mysql = json.load(f)["Mysql"]["username"]
    return mysql

def get_mysql_password():
    with open("config.json") as f:
        mysql = json.load(f)["Mysql"]["password"]
    return mysql

def get_mysql_db():
    with open("config.json") as f:
        mysql = json.load(f)["Mysql"]["db"]
    return mysql

def get_default_prefix():
    with open("config.json") as f:
        prefix = json.load(f)["Default Prefix"]
    return prefix