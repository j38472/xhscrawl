## 简介

官网：apiserver.top

提供各平台各字段逆向的在线接口，按照请求次数收费。

## 接口概览

| 接口                     | 对应平台及关键字段 | 每次调用消耗token数 | 响应数据 | 接口超时时间 | 最高QPS |
| ------------------------ | ------------------ | ------------------- | -------- | ------------ | ------- |
| /api/xhs/xs/             | 小红书 xs、xt      | 10 token/次         | 50ms    | 800ms        | 200       |
| 更多平台加密字段敬请期待 | /                  | /                   | /        | /            | /       |

## QPS相关

若对qps有要求请联系作者，作者将为单独您扩充资源。

## 价格

### token消耗优先级

1. 订阅计划 > 单独购买的token。
2. 订阅计划内：到期时间越早，越优先消耗。

### token数充值价格表

单独购买的token没有过期时间，可在任意时间使用。

| token数区间  | 价格         | 折扣 | 每次请求单价          | 最少充值 |
| ------------ | ------------ | ---- | --------------------- | -------- |
| [0-50w)      | 2¥/千token   | 0    | xs-xt接口：0.02元/次  | 2元      |
| [50w-150w)   | 1.8¥/千token | 0.9  | xs-xt接口：0.018元/次 | 900元    |
| [150w-300w)  | 1.6¥/千token | 0.8  | xs-xt接口：0.016元/次 | 2400元   |
| [300w-600w)  | 1.4¥/千token | 0.7  | xs-xt接口：0.014元/次 | 4200元   |
| [600w-1000w) | 1.2¥/千token | 0.6  | xs-xt接口：0.012元/次 | 7200元   |
| 1000w及以上  | 1¥/千token   | 0.5  | xs-xt接口：0.01元/次  | 10000元  |



### 订阅计划表

若超出有效期，未使用完的token数将过期作废。

| 周期          | 价格    | token数 | 每次请求单价           | 接口请求次数      | 有效期 |
| ------------- | ------- | ------- | ---------------------- | ----------------- | ------ |
| 1个月小量计划 | 500元   | 35w     | xs-xt接口：0.0142元/次 | xs-xt接口：3.5w次 | 1个月  |
| 1个月中量计划 | 1000元  | 80w     | xs-xt接口：0.0125元/次 | xs-xt接口：8w次   | 1个月  |
| 1个月大量计划 | 2000元  | 200w    | xs-xt接口：0.01元/次   | xs-xt接口：20w次  | 1个月  |
| 1个月超量计划 | 4000元  | 440w    | xs-xt接口：0.009元/次  | xs-xt接口：44w次  | 1个月  |
| 季度小量计划  | 1500元  | 120w    | xs-xt接口：0.0125元/次 | xs-xt接口：12w次  | 3个月  |
| 季度中量计划  | 3000元  | 300w    | xs-xt接口：0.01元/次   | xs-xt接口：30w次  | 3个月  |
| 季度大量计划  | 6000元  | 660w    | xs-xt接口：0.009元/次  | xs-xt接口：20w次  | 3个月  |
| 季度超量计划  | 12000元 | 1500w   | xs-xt接口：0.008元/次  | xs-xt接口：150w次 | 3个月  |



## 接口文档

### /api/xhs/xs/

#### 请求url

**POST apiserver.top/api/xhs/xs/**

#### 请求头

```json
{
  "Authorization": "Token cc87ae3f488357cabd786689c4d9d1675ae85b26", # token用于标识帐号，从官网'我的'中获取。
  "Content-Type": "application/json" #使用json交互
}
```

#### 请求体(json格式)

```json
{
  "a1": "194fa029a780aceej3dvs06kum1qwb6r09b0g5ghp30000317563", # 小红书帐号cookie中的a1字段
  "params": {}, # 请求小红书的接口的参数
  "method": "post", # 请求小红书接口的方法
  "api": "/api/sns/web/v2/login/code" # 请求小红书接口名
}
```

#### 响应参数

```json
{
  'code': 0,  #code
  'msg': '', #信息
  'data': {
    'X-s': 'XXX', # xs 
    'X-t': 00000 # xt
  }
}

```

#### python代码实例

```python
#以下为笔记详情接口示范
 
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

