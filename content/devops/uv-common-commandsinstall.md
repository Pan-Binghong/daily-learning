---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U27X6DKZ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkg5uDrDaWKrfDbP6G%2F7fdZYnuE1n25ozVEyg2eBR6%2BAiBfRFEI4AxbdFW8qDpO0fmGLaoVJfUJE%2F6DRCkGDzbBECr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMj1kgOaKYa7Z94jPHKtwDnlDh4o50PhsPcHABxUnvUEcLYv9JXWk6MqtWOSJSaAa42YGDCawuyaImpn1zQg5rX79dHFDBzniLIiKtGRLnOLg6InKyt4jREc3JyGqvnlFyfDM444chIhfU3ZUstQBze526xNqOGFciX9wb4todawO5XrKPe%2FTN4c6w9LSDyUfdOqzneuRTnsyMc13cq8%2Bi0TqvaUNYy%2Fn7GGMYcod4D8Z%2Fr5PTd8q9XRugMx0lAXsFcGQESA%2FcY%2Bn7xl1pUUxsIG%2Fg%2Fc9ClZmlqTKvaykETH0W6wMvfEK%2B3z9iLmIvFWXimKYKXj70LsBrZDQIybALTlda%2FCGPyZsIGTyGU01jP0rLsNfkxgYqUeDxGK1QIhkB6%2BXr4DgWzxIoCSeRYkDvsH5KKjmhvowPvl3tHNXwcLChjT1J%2BtivTGM%2BEmYLO%2FwY40z2Ma%2B4tIyy%2BWW2EksDxayhwCfLGHsLM1qBYZSelX%2FejtR1NZf5V2gPS8j0pLhxZYOhyfgjGPlhXqpn%2FrE9LFy0fdxyIoOMfy3UAtdejDHCa%2BTaB0KDeZw2etfUMHwFHf78ERFQXlnt8F73OFYOXDoqd4YiIm1JrB5q2ztGHNEAsmQndJf%2Bgl9wnYaHP96cswKipSr24pftO2gw1J%2FUzAY6pgFXrSFDEaritPlRdCwhLPg52BHkxnqC8Y8MWqVDZYF%2BFqBDoQR50Bv6kBwzm%2BIfraTOGyLJAoazbLKy58R8P%2FBA1XiBPlSk%2FOrZgs%2BQrXRzbourYvdF%2FkYUSP%2Bn54JG4oRqx%2BYenez2BUN5P8K7c92cT4wOWORLpe2KzBGAiJTymxYIi%2FpgqD4IfGcpGqHygyXQFPqVPb6f5THKVnC5RDLFm96Lao%2Bj&X-Amz-Signature=97e454e7b25b66b8d5f9e1f97619c9b66f595c86aaad0454d0d467462f7d49d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U27X6DKZ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkg5uDrDaWKrfDbP6G%2F7fdZYnuE1n25ozVEyg2eBR6%2BAiBfRFEI4AxbdFW8qDpO0fmGLaoVJfUJE%2F6DRCkGDzbBECr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMj1kgOaKYa7Z94jPHKtwDnlDh4o50PhsPcHABxUnvUEcLYv9JXWk6MqtWOSJSaAa42YGDCawuyaImpn1zQg5rX79dHFDBzniLIiKtGRLnOLg6InKyt4jREc3JyGqvnlFyfDM444chIhfU3ZUstQBze526xNqOGFciX9wb4todawO5XrKPe%2FTN4c6w9LSDyUfdOqzneuRTnsyMc13cq8%2Bi0TqvaUNYy%2Fn7GGMYcod4D8Z%2Fr5PTd8q9XRugMx0lAXsFcGQESA%2FcY%2Bn7xl1pUUxsIG%2Fg%2Fc9ClZmlqTKvaykETH0W6wMvfEK%2B3z9iLmIvFWXimKYKXj70LsBrZDQIybALTlda%2FCGPyZsIGTyGU01jP0rLsNfkxgYqUeDxGK1QIhkB6%2BXr4DgWzxIoCSeRYkDvsH5KKjmhvowPvl3tHNXwcLChjT1J%2BtivTGM%2BEmYLO%2FwY40z2Ma%2B4tIyy%2BWW2EksDxayhwCfLGHsLM1qBYZSelX%2FejtR1NZf5V2gPS8j0pLhxZYOhyfgjGPlhXqpn%2FrE9LFy0fdxyIoOMfy3UAtdejDHCa%2BTaB0KDeZw2etfUMHwFHf78ERFQXlnt8F73OFYOXDoqd4YiIm1JrB5q2ztGHNEAsmQndJf%2Bgl9wnYaHP96cswKipSr24pftO2gw1J%2FUzAY6pgFXrSFDEaritPlRdCwhLPg52BHkxnqC8Y8MWqVDZYF%2BFqBDoQR50Bv6kBwzm%2BIfraTOGyLJAoazbLKy58R8P%2FBA1XiBPlSk%2FOrZgs%2BQrXRzbourYvdF%2FkYUSP%2Bn54JG4oRqx%2BYenez2BUN5P8K7c92cT4wOWORLpe2KzBGAiJTymxYIi%2FpgqD4IfGcpGqHygyXQFPqVPb6f5THKVnC5RDLFm96Lao%2Bj&X-Amz-Signature=50a568c618035b6e2648c357167f49dc6b741fe17027db3db45e1753bb782ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U27X6DKZ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkg5uDrDaWKrfDbP6G%2F7fdZYnuE1n25ozVEyg2eBR6%2BAiBfRFEI4AxbdFW8qDpO0fmGLaoVJfUJE%2F6DRCkGDzbBECr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMj1kgOaKYa7Z94jPHKtwDnlDh4o50PhsPcHABxUnvUEcLYv9JXWk6MqtWOSJSaAa42YGDCawuyaImpn1zQg5rX79dHFDBzniLIiKtGRLnOLg6InKyt4jREc3JyGqvnlFyfDM444chIhfU3ZUstQBze526xNqOGFciX9wb4todawO5XrKPe%2FTN4c6w9LSDyUfdOqzneuRTnsyMc13cq8%2Bi0TqvaUNYy%2Fn7GGMYcod4D8Z%2Fr5PTd8q9XRugMx0lAXsFcGQESA%2FcY%2Bn7xl1pUUxsIG%2Fg%2Fc9ClZmlqTKvaykETH0W6wMvfEK%2B3z9iLmIvFWXimKYKXj70LsBrZDQIybALTlda%2FCGPyZsIGTyGU01jP0rLsNfkxgYqUeDxGK1QIhkB6%2BXr4DgWzxIoCSeRYkDvsH5KKjmhvowPvl3tHNXwcLChjT1J%2BtivTGM%2BEmYLO%2FwY40z2Ma%2B4tIyy%2BWW2EksDxayhwCfLGHsLM1qBYZSelX%2FejtR1NZf5V2gPS8j0pLhxZYOhyfgjGPlhXqpn%2FrE9LFy0fdxyIoOMfy3UAtdejDHCa%2BTaB0KDeZw2etfUMHwFHf78ERFQXlnt8F73OFYOXDoqd4YiIm1JrB5q2ztGHNEAsmQndJf%2Bgl9wnYaHP96cswKipSr24pftO2gw1J%2FUzAY6pgFXrSFDEaritPlRdCwhLPg52BHkxnqC8Y8MWqVDZYF%2BFqBDoQR50Bv6kBwzm%2BIfraTOGyLJAoazbLKy58R8P%2FBA1XiBPlSk%2FOrZgs%2BQrXRzbourYvdF%2FkYUSP%2Bn54JG4oRqx%2BYenez2BUN5P8K7c92cT4wOWORLpe2KzBGAiJTymxYIi%2FpgqD4IfGcpGqHygyXQFPqVPb6f5THKVnC5RDLFm96Lao%2Bj&X-Amz-Signature=b018c1996cc480589f1a8d16560b1d2ce69c9a5dcc26a5f8b321bd375d7a5402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

