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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U7L5AUG%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDoxOveKoWpd6jrNX%2FJcp%2BRf%2FvPM7gqF8S%2FqfqtsI%2F7CAiAkuAjftUOIGCY6lYIEKLAIR3gH8QVu%2F3%2FocSTWc%2FFMwiqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtMXGJcd4vMMnnmL%2BKtwDdO0tYpp8Bf7aJlvu8XV004VOwrCnL6OOANIaEcKJ1wB6ksDvW1ZG65kzdQVqqJCs1IgxpSTL%2BntG1kVtNxCTxMMQZFbEIMomUQSI43rihdZrM1zugZDD%2F%2FdCHPrcJzzQ5XVJMhI3mQ1oqvz%2FmUHVo6ZHLlpijr9iwxIfU4GPMAHfCpR68Gz8oz%2BFjiRWumz3Agmh9LnKGH9VpXs6aRD9nm%2B73ToolgmevxVV1HJZ62oAiKVX%2BZTFOAW9bGUnceGJ8TBW%2BDjBf7UTfsal8AK0TGkL5R72sh0YyvkapriXrx%2Fpw4Th%2FyqgzQxJ2LxVipgCxWckm50yjIOSFkXZ5ByCrP6V3lXxvd7up1i2S4g5sDuFRjSW39jkUUggBDN6SuHCwVy3BsWi00jyvF1jKbii832nDTAEOsy7f852spW%2F2bJ%2BPJT1sUanYuuIweBX2dwB1c3%2F9sOaCT5wF0L4gxB3djglRIUJADZ7P2tuw5s1EURAPR8AswpbOgMyUdCGUlz3RycWOc0J6Ho5ju8jztZF%2ByVAZwnBYB%2Br7mfHj2EdOT5vvCkRBh7matzOFVpOU5GCSo91PZHKAOy40dZW9Am%2F%2FKr9P5YdGmQdbLYRaHXwC92gWtaIW0gUFSyNTdUwhpC2zwY6pgGxKUwSe%2B%2F6ZofaYlDld6FOqNLfgBYQije2ocEht9lSEk1cgGNFDaW1HIxiw3dDz22VclLbt%2BnjugKragNI%2BTsS7qskBN23FQeslbHQBh%2Fkh7ujiF2kFqJ3nRtXL%2BYfCmRCR2DiXy3BbNBN4I5vcKNeWwy%2B6JlNN3lhEm1SgyUfysixdB6WBTqa%2FSjoedqbVs35KNSda6FRCqIDkf5TZ5hrJUyTuzuT&X-Amz-Signature=b4545b2a4325609bbc8eabbbb36770a4ea710658e1d216adad25af2c71053992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

