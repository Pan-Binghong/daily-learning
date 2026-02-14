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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDHJZLJX%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIBCCDtafvW323fW0LnflCaN0tzMv79BqCAUfJEmK2NzcAiBR2L6rugaVXUvqROTUo1APDJdEIvxZqKqatk%2FXwp8tqyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfbFbzGNwWURhS%2BAiKtwDSJs963Bhs3fzD3iSgl3GnnqXNUO8Lxtnr%2BIoE7jbj%2FVxeei%2FoUh72KNfh1%2Flbn%2FEjHZ5Ngfd%2Bion5How300jEJnU3tJWH5IAxLn0WN%2FU%2FfHbd%2Fc44nTndYP%2Bkr61iXB%2BKPpkr2J%2BF29wsJUE3xHb5C91nQue4zfq58H0Cvuj%2FQM%2BKE7MX4M2lPhDqYAMt3rsjDUn2gAux%2B1lWBL3VMiaVRNFjXa3Tq0CgemOtTnkRi5qvJgrnPOunIqKDJxQwVNHz2nYGQTZPcv3y88ZL%2FPxsfy7OEHu0fpKDWnX13NPFoBWkI7qWiqeBtqgZD9wbG6qZuaCKloZS55643PO08oytbUtAQzhNF%2B%2F9pR5GsvA%2FyvBzTSu4upOfdAUmbh2tlUc3dazFX6fcoba%2BHYsB6Lb2%2BwZRC748rU6k0jnkBF%2Fex%2FC8Niq6IKJS9%2B7CmlM3IwAPgY3HayYVBOEMuJYibpjW7Sqp71tsjwThAa8iyYwd3H8gnUuSBXFUzrUcADorM7M74GN30Rlw02icFDBoDInVhc0FR8TkU2gR4YK3Vh7MowVFGLLX3ozAv9YSPfCP8E%2BVBs2qVhP9SqY%2BZm3q%2FQ7ry91qUuqZOh1s0OnyXxhws40GHRnDmSUpg3izCIwzMC%2FzAY6pgEeAgH4ppIJ6Z43OU%2FqqenG9WoK5SbCjB9MxOZGxwDtfloenV4IXY7UoL5hMiQFriY06hY1wD6MqtY48lqbXzACCxcxpZ%2BpAkVFuk%2BspjDeg%2BQ5JAHz7RnsWbZGS32n11TL1O%2Fv%2FOdDNdoxQvGIP4qDoEr%2BnNMF%2FylZ3NWQ%2BMSI0FJqchfhp1uM0R76KkscJRw4AibwQ%2FmNrJsAgqeVucBmYtkaoBaX&X-Amz-Signature=095f7d96b3395a655f4349c2e71053a56b61c7929421829a295f98615b54f2c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

