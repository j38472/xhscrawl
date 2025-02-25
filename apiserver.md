## 简介

官网：http://apiserver.top/

提供各平台各字段逆向的在线接口，按照请求次数收费。

## 接口概览

| 接口                     | 对应平台及关键字段 | 每次调用消耗token数 | 单词请求价格 |响应数据 | 接口超时时间 | 最高QPS |
| ------------------------ | ------------------ | ------------------- |  -------- |-------- | ------------ | ------- |
| /api/xhs/xs/             | 小红书 xs、xt      | 10 token/次 |0.005-0.01元 | 50ms    | 800ms        | 200       |
| 更多平台加密字段敬请期待 | /                  | /                   | /        | /            | /       |

## QPS相关

若对qps有要求请联系作者，作者将为单独您扩充资源。

## 价格

### token消耗优先级

1. 订阅计划 > 单独购买的token。
2. 订阅计划内：到期时间越早，越优先消耗。

### token数充值价格表

感谢大家对apiserver支持，为便于理解，于2月25日降价，并统一价格：xs包月单次请求0.005元。xs非包月单次请求0.01元。之前购买的用户差价已补齐至账户

单独购买的token没有过期时间，可在任意时间使用。

| 价格         | 每次请求单价          | 最少充值 |
| ------------ | --------------------- | -------- |
| 1¥/千token    | xs接口：0.01元/次  | 1元      |

### 订阅计划表

若超出有效期，未使用完的token数将过期作废。

| 周期          | 价格    | token数 | 每次请求单价           | 
| ------------- | ------- | ------- | ---------------------- |
| 1个月小量计划 | 500元   | 100w     | xs-xt接口：0.005元/次  | 
| 1个月中量计划 | 1000元  | 200w     | xs-xt接口：0.005元/次  | 
| 1个月大量计划 | 2000元  | 400w    | xs-xt接口：0.005元/次   | 


## 接口文档

### /api/xhs/xs/

#### 请求url

**POST apiserver.top/api/xhs/xs/**

#### 请求头

```json
{
  //  token用于标识帐号，从官网'我的'中获取。
  "Authorization": "Token cc87ae3f488357cabd786689c4d9d1675ae85b26",
  "Content-Type": "application/json"  //使用json交互
 
}
```

#### 请求体(json格式)

```json
{
  "a1": "194fa029a780aceej3dvs06kum1qwb6r09b0g5ghp30000317563",
  // 小红书帐号cookie中的a1字段
  "params": {},
  // 请求小红书的接口的参数
  "method": "post",
  // 请求小红书接口的方法
  "api": "/api/sns/web/v2/login/code"
  // 请求小红书接口名
}
```

#### 响应参数

```json
{
  'code': 0,

  'msg': '',

  'data': {
    'X-s': 'XXX',
    'X-t': 00000
  }
}

```

#### python代码实例

```python
# 以下为笔记详情接口示范

if __name__ == '__main__':
    # 小红书帐号cookie
    cookie = "xxx"
    # 小红书账号cookie a1字段
    a1 = 'xxx'
    # 请求小红书的参数
    param = {
        "source_note_id": "679469900000000018018d98",
        "image_formats": ["jpg", "webp", "avif"],
        "extra": {"need_body_topic": "1"},
        "xsec_token": "ABREBBrQgn7R-7Q0SFGFY0AdTauA-_aziwDDC3DvJxLrs="
    }
    # 请求小红书的api
    api = '/api/sns/web/v1/feed'
    data = {
        "a1": a1,
        "params": param,
        "method": "post",  # 小红书该api方式为post
        "api": api,
    }
    host = "http://apiserver.top"
    token = "xxx"  # apiserver.top 平台的token 填这里

    headers = {
        "Authorization": f"Token {token}",  # 填入token
        "Content-Type": "application/json",  # 确保请求头中包含 Content-Type
    }

    response = requests.post(f"{host}/api/xhs/xs/", headers=headers, json=data, )
    xs_xt = response.json().get('data')
    print(xs_xt)

    xhsHeader = {"accept": "application/json, text/plain, */*", "accept-language": "zh-CN,zh;q=0.9",
                 "cache-control": "no-cache", "content-type": "application/json;charset=UTF-8",
                 "origin": "https://www.xiaohongshu.com", "pragma": "no-cache",
                 "referer": "https://www.xiaohongshu.com/",
                 "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                 "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "sec-fetch-dest": "empty",
                 "sec-fetch-mode": "cors", "sec-fetch-site": "same-site",
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                 'cookie': cookie,
                 }
    xhsHeader["X-s"] = xs_xt["X-s"]
    xhsHeader["X-t"] = str(xs_xt["X-t"])

    response = requests.post(url='https://edith.xiaohongshu.com/api/sns/web/v1/feed',
                             data=json.dumps(param, separators=(",", ":"), ensure_ascii=False).encode("utf-8"),
                             headers=xhsHeader)

    print(response.json())
```

