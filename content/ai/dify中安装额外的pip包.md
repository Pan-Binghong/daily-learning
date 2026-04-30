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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GOVQN5M%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICovQfbH2WU7HZ3M9FD1FW8ewgB3Qn6KSjlmzzw%2BJE85AiEAvzV9BLUCnhtpY0SQIVmOjNG77uFZZguEx56NXlQIrBcq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDANtPjgmwSgyaDWedyrcAwsEsKR3fQGoB7AlPXpvvGuGd4nwTpe%2FvAibXnl%2BRzu7b1XoxZ3t90n1D%2Bc%2BhVLRRamXSycY7EDnH3zKLImaghQLwQd0Q1oVSFaup7ZYH1EyufBAwz2pVONxrjeeaxJNsBVjoG8ACF%2BHqW1bdp25F5Pim3JocL91ENhb4NkB197W8Qpkfo0ajnUewLVtLy%2B5nDzCNBemNILAkQKMTWKFS1fILHU8hRUiw1jJHv3YNg5DiwSZ2RQTUvCAH8ItXMvHk2kvMPqN5qOJ5LAS5MY5Zqxe0HvPKI0bfuLJc2Im8UorlMoJlDqKEDdo02ynr6N5d8OCKEF3wZcuqfQ0UuQTQQeflE3c3BQh5viKtyuesS1YM7nKnmfl5K2zkVRQ2PN6igAi5ySS%2BZ%2BdQm1a7HbUD3Smvvt2dATtwrbtgx2KRzwviZtDbFEyOcQT%2BPwf4jBLi7rsOkIDD7r1OJb1Z54eS224sTmzp57MAKI9WyRE2kcCoOoyZNN5pdxyDWlIJLgM6aAKfgzZT9RxiKDbPNHVwVhReAu%2BMlscuCOaoBSgizLEBh5i4VyXm%2B9E890CssQsc3fWgVeHh9AZ1qksYjzJuETMNb8mdOfE5BCtTuV680Ojm1F5jOAUZLnMl93eMLqczM8GOqUBQp1X7xNgMq2VyXhu%2BxOQEZp4W49Abw37dAPVTKS4z7yi%2FsQfDN8G4xT5NPsiL0Wv9bqC43GEMjX24vIPHlShvV7Mj%2BQCg0hwpfI%2BA19zqTvkhpbQa57Cy4oy9U13qWzswYHZz4APpHJKypL7oSZbtFvP9r1s72vQScO4eBUAyse4Hb2c0b80QSci2R5BVpi8DNaRAvCsO%2FPLxyAjTFIKgAzJaFly&X-Amz-Signature=c311c6c6e591753d546d26f6af25046002a605468df879aea05713c5f39b20bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

