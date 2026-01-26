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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKUZHBQV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIC6TtxTvm1eiw2MGtJCpx6zbuD6%2Bnbr1u73qOGcy57k0AiBqyu6OLNakaB87PbNsjvoMvgaMxOflz1Xgewy%2Fqlmyjyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMAAgDmMic7tMlAu8aKtwDb%2BsbN8yRlYQ2h0Lp201osriGQ7rHG5NJtz6YZ7tjh2DE%2FWBbGnoZ3lfKLH%2FSjpXVSGFYPShJ67iIfGdWnRstLnaXAzhRDT1X9v58O%2FHAdAl3TZjzFm6HKkGtqkw%2Ba93d%2F%2FuG0kvqmmoZIL%2BSXUm4c0E%2B57uKFDFIvCuMVq4ZG0SAqHWDP9Q5gKoltHkUSfIjHpCuKjTiyhhUI3bwvdyyRQ6RC5COV%2FnxKxT4AzQGbop5zpZJNoRsKVBpcJPvlZIb%2BB9YgcmWSzCtUK53eTrWIoV7OQM9%2B%2FlWlTZlOQ62T7nkL8iyrTnaX0z9sT4dcy%2FyhSc91pvzj8dyxDF6t8g7b%2BcZ68Wwgx82kmfwxBnVsVLp4cko3EQcyIhwD6Yw%2Fs4gW2JW%2B%2FiWBy%2FnbIgPPMzCF7%2FHOUrDANeI%2BAdDNhu0NaxTYCAe2Z1XiawJ8OHAMt1jtaDXDfXbj5sdAPoUeuNa5L8iuC7DNL%2BFNdgyMxi%2BAJ3ND1Y26CYf1uv%2BmsfGWfVYYIVj0u9WRQB7Zg9M9SKKMxLC4EVvwS73cfLPVmukaQUNIBCXQZvzL%2F07uxIeRF8GvSR2TMtGzGXdFtpWi9fOH%2B8QplRfb8LIw4IsQCvWSjf3nWZRsfCXAnipx%2FIwhrHaywY6pgHZVZccHhQGWmMPMAYxWZdCnjbUa8nnUdNt5Erbusgq4pUNT9i79e0GrIXory2V%2Bv5Yj6YWakVUHYRFUVf5iRhgPC60WIhkx2RIZeSYhaRvpPntULze9yHnZOamZRyEHh2%2BEHga%2BHV19%2F4nao6FTGifRjcCDHk%2FGfJfqLcvFIPvWaoEftWIKotT%2B%2FYwseCRYw3VxywLAigQCUCE%2BgE6luZO36AWyhwG&X-Amz-Signature=d06f11de32d6fb5bb32a4f4456a4aaf546b4a5907fe9e15ea43d993f3148dcff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKUZHBQV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIC6TtxTvm1eiw2MGtJCpx6zbuD6%2Bnbr1u73qOGcy57k0AiBqyu6OLNakaB87PbNsjvoMvgaMxOflz1Xgewy%2Fqlmyjyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMAAgDmMic7tMlAu8aKtwDb%2BsbN8yRlYQ2h0Lp201osriGQ7rHG5NJtz6YZ7tjh2DE%2FWBbGnoZ3lfKLH%2FSjpXVSGFYPShJ67iIfGdWnRstLnaXAzhRDT1X9v58O%2FHAdAl3TZjzFm6HKkGtqkw%2Ba93d%2F%2FuG0kvqmmoZIL%2BSXUm4c0E%2B57uKFDFIvCuMVq4ZG0SAqHWDP9Q5gKoltHkUSfIjHpCuKjTiyhhUI3bwvdyyRQ6RC5COV%2FnxKxT4AzQGbop5zpZJNoRsKVBpcJPvlZIb%2BB9YgcmWSzCtUK53eTrWIoV7OQM9%2B%2FlWlTZlOQ62T7nkL8iyrTnaX0z9sT4dcy%2FyhSc91pvzj8dyxDF6t8g7b%2BcZ68Wwgx82kmfwxBnVsVLp4cko3EQcyIhwD6Yw%2Fs4gW2JW%2B%2FiWBy%2FnbIgPPMzCF7%2FHOUrDANeI%2BAdDNhu0NaxTYCAe2Z1XiawJ8OHAMt1jtaDXDfXbj5sdAPoUeuNa5L8iuC7DNL%2BFNdgyMxi%2BAJ3ND1Y26CYf1uv%2BmsfGWfVYYIVj0u9WRQB7Zg9M9SKKMxLC4EVvwS73cfLPVmukaQUNIBCXQZvzL%2F07uxIeRF8GvSR2TMtGzGXdFtpWi9fOH%2B8QplRfb8LIw4IsQCvWSjf3nWZRsfCXAnipx%2FIwhrHaywY6pgHZVZccHhQGWmMPMAYxWZdCnjbUa8nnUdNt5Erbusgq4pUNT9i79e0GrIXory2V%2Bv5Yj6YWakVUHYRFUVf5iRhgPC60WIhkx2RIZeSYhaRvpPntULze9yHnZOamZRyEHh2%2BEHga%2BHV19%2F4nao6FTGifRjcCDHk%2FGfJfqLcvFIPvWaoEftWIKotT%2B%2FYwseCRYw3VxywLAigQCUCE%2BgE6luZO36AWyhwG&X-Amz-Signature=e749c7d5671337021d40651ce8edfcf1834ec3841f3fe801896eefe41244a16f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKUZHBQV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIC6TtxTvm1eiw2MGtJCpx6zbuD6%2Bnbr1u73qOGcy57k0AiBqyu6OLNakaB87PbNsjvoMvgaMxOflz1Xgewy%2Fqlmyjyr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMAAgDmMic7tMlAu8aKtwDb%2BsbN8yRlYQ2h0Lp201osriGQ7rHG5NJtz6YZ7tjh2DE%2FWBbGnoZ3lfKLH%2FSjpXVSGFYPShJ67iIfGdWnRstLnaXAzhRDT1X9v58O%2FHAdAl3TZjzFm6HKkGtqkw%2Ba93d%2F%2FuG0kvqmmoZIL%2BSXUm4c0E%2B57uKFDFIvCuMVq4ZG0SAqHWDP9Q5gKoltHkUSfIjHpCuKjTiyhhUI3bwvdyyRQ6RC5COV%2FnxKxT4AzQGbop5zpZJNoRsKVBpcJPvlZIb%2BB9YgcmWSzCtUK53eTrWIoV7OQM9%2B%2FlWlTZlOQ62T7nkL8iyrTnaX0z9sT4dcy%2FyhSc91pvzj8dyxDF6t8g7b%2BcZ68Wwgx82kmfwxBnVsVLp4cko3EQcyIhwD6Yw%2Fs4gW2JW%2B%2FiWBy%2FnbIgPPMzCF7%2FHOUrDANeI%2BAdDNhu0NaxTYCAe2Z1XiawJ8OHAMt1jtaDXDfXbj5sdAPoUeuNa5L8iuC7DNL%2BFNdgyMxi%2BAJ3ND1Y26CYf1uv%2BmsfGWfVYYIVj0u9WRQB7Zg9M9SKKMxLC4EVvwS73cfLPVmukaQUNIBCXQZvzL%2F07uxIeRF8GvSR2TMtGzGXdFtpWi9fOH%2B8QplRfb8LIw4IsQCvWSjf3nWZRsfCXAnipx%2FIwhrHaywY6pgHZVZccHhQGWmMPMAYxWZdCnjbUa8nnUdNt5Erbusgq4pUNT9i79e0GrIXory2V%2Bv5Yj6YWakVUHYRFUVf5iRhgPC60WIhkx2RIZeSYhaRvpPntULze9yHnZOamZRyEHh2%2BEHga%2BHV19%2F4nao6FTGifRjcCDHk%2FGfJfqLcvFIPvWaoEftWIKotT%2B%2FYwseCRYw3VxywLAigQCUCE%2BgE6luZO36AWyhwG&X-Amz-Signature=214054cb9e0e8ab1780125c7c9f7971ba0faf198dc9bbd387944565531cc867b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

