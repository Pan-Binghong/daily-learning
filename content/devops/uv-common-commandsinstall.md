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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DLYZTEQ%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyWEX9RWfBdPTXIlm527HsopxVGeEIDuey9N62ZfisAQIhANGIKcwOgijZzHAPfB7BKysjxntUq9MKpzpu3uH80RSlKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyb3Dq6UutQAgx8dUYq3AMjmUImeuVheyfg%2BERKXdGZKk321sE8s%2F4tmeDf83QTJWyLBt%2BYPy1H3rLJWIxb6PoEkknInikyBoj9Hk9%2BxMhTC9N6LW3IJwJyQKSIiHrGH37o67TFWfnsV%2Bo87A%2Fxf4Aei0uN2OGigvIPoLo%2BTxWSifv4mR9upKUkU1OgCpEzJgCY%2FQaGajr2FX%2Fcm33nopPq%2FX2%2FzYF5dbeNpkZt6s%2FS6PHwgKGFRoGgtf7gVLZ0exG9gCseqlSl%2BWcqKyECyn2OhgqW7L0sFrPvr%2Fnm976gbtdb5aop6XmZtFkcXCU14I7GPwKlpxomumTe%2F4%2Fx7kcts8iZpTBBSOuHXPW5DoskGBtPIEHCZhAGvAIT5OE9XwKwMSRLZtg%2BMFQSU2M%2FwYn0hPoFHZ%2B6mMSdDFb7ussVPxpNWLpTzl6FsibKpOtN5wQ%2BjkpxEeKBBLQ1zN4HqmDvYZ6EAkDU7iy%2FUfAvuv1WoUOFKQpHLO7NoLc2ADg%2BhIgDa%2Fba%2BOA00hL%2FHqgvtbSDYbIwmr3ZKhjFGGEkTGf3P4DdHHwNGd5v0a%2FvWbmQ9yy6zRpCRMMvQWawr5cQC6sLHobDA2h7ni14kadPkYH6S1k5dICQghDgzg9gu5QCkNRlxLHEnOHgi0BCdDDpgsHLBjqkAU%2FCqy6OImVlM%2BRhnO46NyUjUic81RS9P4ItjJmqzBppKvphnlEe8mu0gNwEB%2B0UoBlbrPMss8Colsy6gbgOrpe7PQPS505W0wHY8QLuuj0xBEQmXxjzkHiERqnrbsSCOzmwocUnU7HrdouDoC0rLg5b8%2B6Cn3YCiv8dorHX0TArTUPFR7IcIhRKfjJNjFkft6AFNSvWOHvex%2Ba8ztdRcZHmUK48&X-Amz-Signature=0dc1acb9337040988932f3d9e6f73ddfbfd5a4ac06dfa4e8c5f192699ad87583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DLYZTEQ%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyWEX9RWfBdPTXIlm527HsopxVGeEIDuey9N62ZfisAQIhANGIKcwOgijZzHAPfB7BKysjxntUq9MKpzpu3uH80RSlKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyb3Dq6UutQAgx8dUYq3AMjmUImeuVheyfg%2BERKXdGZKk321sE8s%2F4tmeDf83QTJWyLBt%2BYPy1H3rLJWIxb6PoEkknInikyBoj9Hk9%2BxMhTC9N6LW3IJwJyQKSIiHrGH37o67TFWfnsV%2Bo87A%2Fxf4Aei0uN2OGigvIPoLo%2BTxWSifv4mR9upKUkU1OgCpEzJgCY%2FQaGajr2FX%2Fcm33nopPq%2FX2%2FzYF5dbeNpkZt6s%2FS6PHwgKGFRoGgtf7gVLZ0exG9gCseqlSl%2BWcqKyECyn2OhgqW7L0sFrPvr%2Fnm976gbtdb5aop6XmZtFkcXCU14I7GPwKlpxomumTe%2F4%2Fx7kcts8iZpTBBSOuHXPW5DoskGBtPIEHCZhAGvAIT5OE9XwKwMSRLZtg%2BMFQSU2M%2FwYn0hPoFHZ%2B6mMSdDFb7ussVPxpNWLpTzl6FsibKpOtN5wQ%2BjkpxEeKBBLQ1zN4HqmDvYZ6EAkDU7iy%2FUfAvuv1WoUOFKQpHLO7NoLc2ADg%2BhIgDa%2Fba%2BOA00hL%2FHqgvtbSDYbIwmr3ZKhjFGGEkTGf3P4DdHHwNGd5v0a%2FvWbmQ9yy6zRpCRMMvQWawr5cQC6sLHobDA2h7ni14kadPkYH6S1k5dICQghDgzg9gu5QCkNRlxLHEnOHgi0BCdDDpgsHLBjqkAU%2FCqy6OImVlM%2BRhnO46NyUjUic81RS9P4ItjJmqzBppKvphnlEe8mu0gNwEB%2B0UoBlbrPMss8Colsy6gbgOrpe7PQPS505W0wHY8QLuuj0xBEQmXxjzkHiERqnrbsSCOzmwocUnU7HrdouDoC0rLg5b8%2B6Cn3YCiv8dorHX0TArTUPFR7IcIhRKfjJNjFkft6AFNSvWOHvex%2Ba8ztdRcZHmUK48&X-Amz-Signature=ad31084aadecb9e76e516fceee556e6aec522fda36c198f3f68cc8d05051d326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DLYZTEQ%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyWEX9RWfBdPTXIlm527HsopxVGeEIDuey9N62ZfisAQIhANGIKcwOgijZzHAPfB7BKysjxntUq9MKpzpu3uH80RSlKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyb3Dq6UutQAgx8dUYq3AMjmUImeuVheyfg%2BERKXdGZKk321sE8s%2F4tmeDf83QTJWyLBt%2BYPy1H3rLJWIxb6PoEkknInikyBoj9Hk9%2BxMhTC9N6LW3IJwJyQKSIiHrGH37o67TFWfnsV%2Bo87A%2Fxf4Aei0uN2OGigvIPoLo%2BTxWSifv4mR9upKUkU1OgCpEzJgCY%2FQaGajr2FX%2Fcm33nopPq%2FX2%2FzYF5dbeNpkZt6s%2FS6PHwgKGFRoGgtf7gVLZ0exG9gCseqlSl%2BWcqKyECyn2OhgqW7L0sFrPvr%2Fnm976gbtdb5aop6XmZtFkcXCU14I7GPwKlpxomumTe%2F4%2Fx7kcts8iZpTBBSOuHXPW5DoskGBtPIEHCZhAGvAIT5OE9XwKwMSRLZtg%2BMFQSU2M%2FwYn0hPoFHZ%2B6mMSdDFb7ussVPxpNWLpTzl6FsibKpOtN5wQ%2BjkpxEeKBBLQ1zN4HqmDvYZ6EAkDU7iy%2FUfAvuv1WoUOFKQpHLO7NoLc2ADg%2BhIgDa%2Fba%2BOA00hL%2FHqgvtbSDYbIwmr3ZKhjFGGEkTGf3P4DdHHwNGd5v0a%2FvWbmQ9yy6zRpCRMMvQWawr5cQC6sLHobDA2h7ni14kadPkYH6S1k5dICQghDgzg9gu5QCkNRlxLHEnOHgi0BCdDDpgsHLBjqkAU%2FCqy6OImVlM%2BRhnO46NyUjUic81RS9P4ItjJmqzBppKvphnlEe8mu0gNwEB%2B0UoBlbrPMss8Colsy6gbgOrpe7PQPS505W0wHY8QLuuj0xBEQmXxjzkHiERqnrbsSCOzmwocUnU7HrdouDoC0rLg5b8%2B6Cn3YCiv8dorHX0TArTUPFR7IcIhRKfjJNjFkft6AFNSvWOHvex%2Ba8ztdRcZHmUK48&X-Amz-Signature=5f96627f5dbeaf33b53f7544cc2cb7de60315757a735dcb145ca4cd9fbea4cf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

