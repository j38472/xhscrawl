import json
import os
import re
import execjs
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-b3-traceid": "a31fffc0ee4f5d8f",
}


def getXs(cookie, api, data):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "xhs.js")
    with open(file_path, 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""

    result = ctx.call("get_xs", api, data, a1)
    return result


def sentRequest(host, api, data, cookie):
    xs_xt = getXs(cookie, api, data)

    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    url = host + api

    return requests.post(url=url, data=json.dumps(data, separators=(",", ":")), headers=headers)


def DoApi(param, cookie):
    api = '/api/sns/web/v1/comment/post'
    host = 'https://edith.xiaohongshu.com'
    data = {
        "note_id": param["note_id"],
        "content": param["content"],
        "at_users":  param["at_users"],
    }
    return sentRequest(host, api, data, cookie)




if __name__ == '__main__':
    # 向笔记发送评论demo
    # warning 该js逆向只能用于改接口，如需其他接口请联系作者

    cookie = ""  # put your cookie here

    param = {
        "note_id": "64e1d603000000001700f40d",
        "content": "hello world",
        "at_users":  []
    }

    response = DoApi(param,cookie)
    if response.status_code == 200:
        print("Request successful:")
        print(response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print(response.text)