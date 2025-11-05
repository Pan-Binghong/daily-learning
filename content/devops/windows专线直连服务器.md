---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
标签:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSWFR5VJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEdzjH6juCuzrALoTFw5xEsF2eX4wsdJygO2f54WRFsuAiBxx6wO6YRRzmwl%2BBPH3YYGDvLs9klUgN%2FYZGJj7%2BuJvSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuS35Up3kDTkA1i54KtwDxlM3N5FOxm%2FkgfXOZKpf75Cr05grDxldEdjz9Boj5YPvsbdCSWcWY2h0rUZZDpK0Ba3ZBy5pEbpGogEjStnb4De5utaRKTBT%2BvlNait0OVxOOoYtrQza8eAhSyJRqavAomtsWeiZCcyHBec5VNFq6XOMf4x8SVpklZTByylp0Bx6rK5NKGEcYeWx%2BRfr9OXGnNKKJmZVjbXKsjtyHmMXXvB88yj8Qx1mGedr8yGJqTZ%2FaabKm5GkmPwCW8vfoSnc7lZScwR19%2Fmkmy5d6ZM3i2Vucjbq4TyY6gvqkCkGQ5dPzPpBVl1nMkm1WH4zZQ%2BLBY8pWhwtuGRkAXomzIFEArVUw266TQ72lwnxb96TJsJ8%2FrS5dnpEUUUlqenXw6k%2B1JO%2BNVEQCVXFaL%2Bb2U4QtWs50YEYHGwivXGNxrOdxIx2aVo6VGD3VOYBI0dQy%2BDYfvjFmYdoUa1Fjyvcbcj3ukN5mGkxifzINPWNVIaK5Id3k8irx9M8qFhDWFYDi0Yc7HLkgQRHBya%2Fe3PhaNGq9M%2FrBZPdvs1SZdtuxHdZCPBbD8qKi9cFNZukYHlbH1x8NmQLH0TUNZ2vwblsDQ3yzhpHdSU5nWt5GkyFtLbfgLuJPuz2Btq5KM5HMWww5KKsyAY6pgFO7LdwFPfJAf6rW2Zg1kgowi0emjBziVA9oylsUKcD%2BUh%2BP6Vr4maztamSEBIylYhHkftoRTmfu0ClaTf4hgOslXbP1Gn771sWn4hdnlK2DL2hOHvbRkqXifoPRcHARw7w2UOjtTZAuIEA5o6iTBvUZ0VetMhANllRLq4laIqZOVgVyL%2BSZMl8UpSUCcbFvQnbHJkaYcISf9wO9LkK2cOAy4erbVwq&X-Amz-Signature=4e5ef5e67b31e6767458cf7c4352230b45ceeeb30d32b0a6d54489c71b303dd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

