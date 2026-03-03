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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VCXVIGQ%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfmsI4QcwKhjpp3HzUXZRXtY%2FbzwVzzLVlHudNSqHpPgIgdeix3lqv3vhGq62bqmQAPTu4bbtwzkbed7VSFJCflPkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaKKKgAe9zgF4KGnircA1RsXmX46lUTR%2BBd6GNJyQw%2BmeXE9DqDB3S2baJ23fAKNB8XZ4uzwBVOUQ90cgbHk9hS42yRCRVwTN1h%2FE1Wm%2Bikdq6uWwh4Lz1Xp8P%2FrgfdWm5INn0DIsIdxYBnkBiYNP7nDpN4TUfYNgqm9%2BdtseIKAKJyA6E6lt38NYZvIF8iGnj9tlbUREXrlRX7bCMHgcOVeN6sGEHecRA9WAJMbhzmuSs1EE1DagSyv5J5pyrF6pEA0%2BAJzT2oOsGN5KJUK6k%2B%2FYyuuOxC5pwMFiZu3pbo7wB7mvpMt1uX92ZK9NkbUuQZLRoQl9Z0EdsKkn57bZtFWYCmWyMOnByor565q10u01%2FRvzHvnxC8vCBXiJebqgHu0Rn5O3UQx327NFaTx6CEMN7nSoowVc8dzgAHNE08A99%2BzTrNPfsefc7xYZ%2BR1JxhfaxA0Mxz0iieJ3BI0SKOkyPIfI8N8n9acVys3YAZiad5JE0GiEtYuEikKok87x2L%2FOB49LNlZVSbo6o0kYFDLWz3i5JCRD1H4dnKxg7FJY22nETCwt5skwG1pxGYBsWu1w6jbmD0w2xfvOQ5p67RsCq%2Ftf45%2FhUCDfO89Wwhp9RAlubn4n%2BJXRRSXamtfOMTDLTXigFGzfLIMJK1mM0GOqUBuxy0iaUlGkGO7EUhjw8uZDAU6JOd09qINm91Mso3wD8NDzG0KRn%2Fmi9e9lvK1C0w6uM1sFmZjAVTA8Pt83du%2FFCvcZgwuJfbtZEzUiRDOqzCGzabWUzXsoHv87IEGebNexx9QQiBt4f33%2B1pcpcuygpTxyohB0NlbJTGXZUSByRN%2BH7H%2BJJBF9CyBWpOHECFAYjzlZESORbeAI0oY1ZH8iOfbNzF&X-Amz-Signature=ca6a8c76e69fe0cc620fd3c4171f5b6f70230a89b61c802b8fa928e802e066cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

