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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNTMVTYQ%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdx%2BM3Bilo3EupptaObSDIdNh%2BkN7Xjr22v%2FeJk6itFwIhAK1lBkvl0oZ7oaMNThLbGgxEbrUqVBHRzaoCllqX%2FvJ1KogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHW0kGmek1x0%2BQgK4q3ANqEfj%2Bh9FQb9%2FZc6u8sr0D5J1a56OL2EMTMgN%2FG58pdgWkZV%2FXXBuHGtStau0vcCLZ5RBKX2sYu4AU5m9ru5E1Uc3xPbJ4DLMIzNtUKSANNjBQ2w4Y7HQ3vtq9durrV2A9kzkLhWsigjKmwPVYvXL79U0%2BcbN%2B9mcRFAKzk%2Fe%2BCsGsrIJC5hTntSOGDY37tUWE%2BzCxCJh%2F5mEMyad%2FCRhhzqbe5SX%2BhhwmR60v9eaRKnPEaGsVsRytYHOJ966%2F422R%2Febbvx0KPfg%2B2MyXJbhaMX%2Fh8f6u%2BcPqAr6C3uprVHo2gFukfSWc9JgsvEM8D5NfncBbVWXfU%2FLDJNBGz00YwvR0RtfuQyTYhRVnZdSIF3XB%2BtuuOXL%2FfGPeElp1xqaf1VsSNa6j0xmfFqUKM37rpYuxtSu4tZzF4JkQ4SVlnB3%2FXA8L%2Fk6NCCCPw4FZD80sIr39%2FZxba0HDYxoNmNzCkdXql2%2FNhTvRhHq6hiZjxAY8F4OwilEu9oHppWaRLHplzGqVHrItKOla%2BwHEblGA6jVFzLW%2FcJQVt3b5RvLB4Vi3OwNCqqHGExWpSIXixGYDGr2oshomVC6DJQfxmjPsg7FTyueZWZ7lmrDgRooZdbBjqWibTm2dCodSJjC81o7OBjqkAe0bip7IExqcOm%2BcPtcY2nrvFKzjmBh7SUP76dcrPEmEsYcJ9BaUZDmGviU3cxscT2wR1Dax%2F5X%2FR5mJ9nhkRJIlx6ZCWnuGHKWD%2FyOr3qoo%2BJmYgEPesh6a64SM7%2BJnN38xCnSHtgyukOoTMBQS8SZSZtxLjXnLSEZDPxS96wQuL7AaxC334XKVHWJpc02%2BN%2FOw1OvHtHjO0hQtbkHmgThfVO0H&X-Amz-Signature=4fab99d8e3d59db137050fbbb248132a65c33d6cc5329a1281bee557b450820e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

