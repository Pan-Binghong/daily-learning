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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZECA2DJ2%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIEpmn70jwJFzuTULbzEEkQyrlp80fD2f28PUAyDZaW0iAiEA77u08FVkJLwXmA5Eloqr0H8Nhk%2BFv7dnfufEVTH%2BcSUqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPLE0FrDV7fDblhWircA8j2Ja%2B%2F9ebCeGNzTnsZDphJphOEv5qkZmijnH%2FlrEoDawLc4J21wpfWMc4ko9hK0w2NrhJVNfdgbtDv163IaQH6P7YjDwui3t7Yar7uo38ulqLb2uuYtKcRpCfBBh1vA8ijAUqeN%2Fl6lILfsmFfvqweffrNsFdWsmLAT4dAMvl%2FUU%2FN5Uae26zBGwFEw%2F1YSheXK7aO8gujSo%2FvU0ibIN9pAHT40ayXCrTJX03iSIFOpPl1xHhsbuMPPYh42XVq6KBW6f9%2BjROq6N9TJjrkxOC%2FYdWEMZPcmtkAn5KV58qcmk8AIZU8jx1SqXIovVbljq2RJP2ZXTX0ZN3FLEhBNOVDBSt%2F2NC9hAY9dT8%2FCNnVid71FuGrTh2wV6qshmd%2FeS8OVGmf3GTWDwp9IoduEpGAiePEL0eZBhJN7PSqsFGeh8UX6dugPH3OMGMC4ubsIEQov1iTs0zj00jt3ANVK94lnNpEKhti%2B1N7Qk%2B8TGHKy2NVmJcuTdHwgD420wNFVpxDlGuNTn00TfPNA3qKwtmRIv0hiAVzaHYtpYbhTJSf9ybh9QvXMIsYPj9rQh4UycsS4L38WwGocbDHBz5I5kMvSp5uTwqzaG8EST%2FtExI5dVJb4GWdAkJmicOKMMDQusgGOqUB%2BPOt7r7S1n9NMVSYwmq0Kp6eD0%2Bzu%2BB2979PBGG1a3SqHkajdeZuMHksbKhWuLxC%2FKtQ0Uew37t%2BQ0AGj4kBC0lPEKhohLzkrdFiNnEP2s3gO%2BY34bS9lrfhmwusHwWo83tt47qTEaGqbeqPxutNovaNWG%2B1A8Hch6YAqQH0V7Y6ldXW%2FBcAJ8LuY98HU6cfVMQX1cOiFNLMmPxpwy8ee%2FBK5jG%2B&X-Amz-Signature=df5ecc902c63e8570db8dd792572dbb31542700fa5f13b3fc4741b100e6afaef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

