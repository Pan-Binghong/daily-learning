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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EYGEVB6%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJFMEMCHw80WBkeHvUMnzuNoaNvKM3BT5UsoXaU%2Fcsq4Z8eZ%2FcCIEHD9hCu5AHQB8WRRMZRZKWeHhvc5emy%2Fmxbzd3iUaczKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG%2FfhjIzKdgcl6ahgq3AOQ8Fp3Tk9uL0fTUBoFFwNHsFrML3Jka2Csk6RTHlVR88KMQDdqJTaoCVSZt0KLEIY2bxQxLhgZK2yyo%2BR6xNtZYbXPmZXzKmmM5L3JGsDcnP1puZfoRcmpXwcMvDY7%2BkgkLRipncul6yzR9bskze1pa21tPfyN%2F44DH3fQeu2xPh2npX7Uc6du76zIqPZmJ6I0HWgupvDOdAwrtCltxrz4%2F0tOGFCr15%2BqMFZy5g4wb4IEi1ZsDm6rOdPdPmpalNQz67ONBLF5AMFQhIRx0aM39jDnRqhviOhlZZGeG9X73caJwoC0i08xexMLXpedwsGnlcJi6LWSKgplN0IWURn%2BFcL1kF0s8yoKgGU4vVsMPF2Qw1p8nlp0upCYXbHiLphV6dwARUgCSjPVVwEpJrrX36zXUorduSi8e0Xz4GKkE9Sxm%2FpBhLploM9ldaac3PEqxhPZ75C8ALKA8iiodYkXODGJfMcjuZPTF50jfD7XsFQe7H%2B6zaan5xDEFcwK0CCo58jvc%2FUbxbWMw6rGzUHdy1uNg8TOhD9HTXWgXz3ArdzOTgz9eTN8RMqxG343D%2FIl4ZzQ9RJsqvx5NY027tteZIJ0vTQ%2BTreyW29ZK8dkBErpxQ%2B01w4400tMozC0zqjNBjqnAVweNFZ2WMySqFwK3OPYhbBtOb3TPQ4iQHOqWHaos2bng8jQxoXFo01hAXRCdFXq5SRc66%2BN%2B3tlchUWRk7mPkHkOT5kHiPXYYqghLfJ7yC9BRQ79Vkhj2eRckT2TpPymIZuGyd4ro%2BKHTOnq0NZs%2F4PAbLU6PU0iQgk8yJWnk%2F7D8y1dv%2FgujlWe6dRVHocfYQyR3eULM0Dn91EdmdT14GRQ1WNG3rN&X-Amz-Signature=f77b4e5acb7b3d92d3f12d00625b5c9ebf432ebedda741c5fc30837d024671c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

