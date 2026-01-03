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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W7LYVU6%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIBrIG6ueLGJgnco9SGy0VsDpB%2BuRrlDyBKOw9MDKIeNoAiAPds4287m2PhhY3p3Pb0dzhwDU2X1Yr3TlEHjuKN%2BEwyr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMgq%2FdrLpO538TEGxgKtwDUKcw5GuOX2NJxyjs1z5g%2FYxCKNBrKrTjBFGclUPVYzIccc3TTxm4uzQfQR20rZcIHp5ubLiAf42g4jV%2BbpMhe8Y8Rh1UrlX94pVJmkhl0R%2FOYEG1B04QF%2FSoqOZD5qIt%2F3jQngqsxFk1fdjvf98113gxXWhGaeXSfV8TPBgDknh1dNa%2F%2BNxU2HfJ1nJayjG4dqaTbC6qNkRTFRYap9L5rwzK23LNcqFMRT%2FuQAUXC0lAvB5UhDsa8NoB17jaf%2BIKpHRwr%2FeB95jznrZDZ%2B2pXjNtmC9sn%2F2fTOzAEd4R8s9VYfO1fza2EQflhO3DzH3H8MkSIOtYybAFUkFXS9iwswJ2IrobbadHfNsX%2FYM7wk7jlxd8JRXmZi0R0Jvz1PV57MYmJ0iNZkLM%2B9LjXfMhAlvgPzOL%2BJUPP%2BmGlTBT4%2F6%2Fn2oSca0oIEcD%2BlMFbwyt%2B7R7LxVVP6y4aJLcBWQGy799nutcrHVAbg2B5dfWRIz84mlCWIouaTEhyJRNQBxjkIimb4cSdlxokZciSCU7H%2FhRIj7aGT0CHKQztab7AYAefaEMK8GdbE2GRYWyeZmlGonxuLLzsk7wAqBJA2E2l24uf3vrZEHJo2kh1pi51jXG52QE6BPrMtBJZX4w9O%2FhygY6pgGlAzYpx2b86Y9jCpPbZaH%2F1jVGUJe7jQRPa2ga%2Fv9QNW0OHYbAXQ2pfRAAeb3LiJTIxsKV8%2BNt6Cwf9zKpy0G16l4rLiA732A6sJpHDsAEbJTDvV5mS4%2BD6qmVRrCoyzLbXSXrjIzHNQeTjKi7UxJuK5i7%2FFoPD6%2FAUT%2Fmn%2BGbqtdZnxiytp56ghk1cYI07inb4fV6DiPs%2Bd8f3GDCERzuuv9rhAxW&X-Amz-Signature=e6b4b6345dca66e197a29c0ab2bd0fb3d70cf58539d1684c12471f5d7a155ed2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

