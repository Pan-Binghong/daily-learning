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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PF3ZDF2%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEVL6g%2BT%2FJmQJ6eNa0uJbLJX1fw5QFkDEwXIOU1HtfaSAiEAiuryYOMkSkN7Sl2KDBqlDEkTU%2BsopaqTqVVbfurbG6QqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPF2JNZAWByq4nVRRCrcAzIZaPdBcDiq%2FRUu59zz8ZXhkHVHN8NOEkUQi1UyFE1eOjZdaNg4dKoZNUbzMN4raUZxIhxMGmO2E5bxMn1HxMqNzn%2BGeLZmxgA3nHUzk7JxSIN07%2FZOhFvb8tfz0A%2FUbno6gqo2Po%2BLXPWLLAk9LR4VH4OE0iz3igGB%2FjgTmvrJvw%2B%2FiykmCmxd7xmEZu5lZ7kFColZetxI%2BdvkPyJCltVRkncUHMaBIUHzcIFtH8sxGbTUr8rFfd2oWfJxYgsk2ZuijTdO2zh8tfzMYYvG1IiJncC%2Buk1Mw5kLot0Sj9hegXeFfG8xRBtBYTPlmMg%2BmFIA3M3Z2QLaXmxlPqXyYOJTYHBrFtritoZn6NuPKfjwr%2FZh55%2BU5oRpMiFAyGav2G%2BHB14Uq%2B40E6ZFrXV%2FxHNhy%2FjBeB2LGn9HN%2FNWf5LW2Dhf5DspsndMYlRVojinFn2%2Fvxe%2BeptGo3%2FTB1wy4ZyhCXeCXS%2BWpTFBPjesYZV3oIljkzabEJf6rLuR7kq2%2FseD00mQNtbS5F%2FvfXXmsbIelkTTb1zcSUJjDrt96bHcrmfYIWjc%2BlEzxkp21W1g8wTaGDZcyMwvBsCnXzN%2BZqxJUqyVX6eld2%2BfQgszG6K55iGAmHptm4c%2BBRzyML6kjc4GOqUBwEYeqViMBlRaFO%2BhT8hHmsW53hgTz93dPGlGfeyE7MuCow4O6fqzQi%2F4MGDqh5QveUYdrH7R%2BPm6PMTGsn6k2ps90aMvdUoYu9Rqknr6guolVvPn8llKH4p63zOv8jyUo4LYHZaD9935W%2Br%2B1QmGM0PJQSmW8%2FrNkVu9u3%2BPzthQ8Vy6qqwmBbYdFIX87TBd00354ekVBml%2BeMpAPklaMAVO9AU0&X-Amz-Signature=0ad9775009ccb022335dcbe135ae2a2e237351efcfa1b21f65255f0b3c868b53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

