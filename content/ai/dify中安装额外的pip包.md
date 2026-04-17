---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDXGDWZ3%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIAOG3orkkv%2FB6XskZNfoz0jeGVixEfoA%2Bz76cnA9375WAiBaTRo7wkY8%2F83K0V6am6PQtWOaEb0NECqfE1FOKoAYuCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUR0C%2F8IVaoxFuhVdKtwDFQPPwq7jLakUneWg7jAe6f%2BBKv2WQqHHxwOaOS1ZNRlWIbTHzmhrmdu73ei4mJ5FcuINFwxyqIx1hvFI01yVwyJMkbUYy0Us7BlCLGg4K3eqXobh6%2BhPnLMCttGL67cGRJmA%2BerM%2FfzhpQPzU3crSI7%2BJI2FhOM9Deo3MMa1dEn4T%2F2D3%2BfENrrg99Hv89cl%2FGz%2Fv6EdSorjBzg0IZb2s8%2BtMWSB5z3cO%2B3CDHNE2sOAMKzwtr4%2FgTLFhd2Ubnku5%2BDIXMZQbaphS9437Ls8%2BzKqoonm2OI7GEBoUXU1udFKl7KAi8VWD7thnEH%2Ffq%2Bq9uK%2FLCZSUnCDTHHxOPokc11OmkYoO%2FFwHF8BJfjDzeRmKbAJscj%2BMpDeQlZ5HFsHhVjoELi30rt2TzjmPws1veYe0VZT5FN1oDmaPTS9AkCKI2klOP4%2BR9wMLB7z1A9kCfR9yjNXXHsE0qIqZAnXjK3QwazWyG3bzndwExwJ8Jkl%2BhdWjpSE%2FadJqrHAo3DrZQG%2BHPfg2VcIwntdWsos4YifrRGmlow2fmyXgagINe9SjMejsHaS9RGeUBtcAGX%2FMIvdFrNRm42c%2BMWDr2pFIIzUk%2BJXf2mpX%2BEODKh%2BAyuqgqH8tfQwTFfGIzcw1LyGzwY6pgH%2Bj4oFjaiOKiT%2B0EvjfWwe6nKBUSEYUsAc7vKAfIjhH87RzRT3zpDqW64y1HoyguyfL6pH732i7NQnpgycriei6L5rfQCRBqrd5oY70ze2RkhMwVZbR%2BbLu44toKWXB7FM12OY43quwvwDcC7YKLRJKSvoIKLfH0fUoX9PjqXecu64s2zWe0Nt5k1Ur882o9KBUYx%2FYfO4PiTR0Kvmx8s4pQmTc0In&X-Amz-Signature=49ac20f275e617ff57e95957fb279b6515dfce540e74b26da0d891ed80c0a09b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

