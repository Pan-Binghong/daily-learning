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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYDDRGBO%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZTTOre5LA2ErJpMjJPNbK6kI2oLaHsw%2B31Bh8Qzs7EAiBQfxlBQPZ%2B1BLqyW138td70MiYgUn2jFmK%2FrhQvTv30iqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgtBiHcfPVNfXaeK3KtwD1DQwTPm06%2FxPgZFb0jJpw96fegHXt6%2BH6xUL6p7%2FDyEkKfE8sVnG86U2AATwbJqBRs38n6Nzw5GWPk%2F5IPhJME1HQw5n1i6tK7WobObm%2BH%2BuHrPDHSc6oMrvM2e7kztGIUKv2TJ4T4anNvQbf5WYD13WVheJPRSmeyJcanXZ%2Fk6BOPmXL80q9Viuf4oZS8b7McwbvCAdlfKuRkFoggo4pnF2Wf9GT6ufqTgE311NyYnNUYoXX4VDldNsUlTrgkbja6U3j5XrM54hQDWzDzEUIoiPln6k7rEOOaq8Rbey%2FeReDqRmLNBswxb3vkvTIZln1BsHH4wsUbAES9Da%2BbcmF5PkpDPYaflDXuVEd1ygLxfIfq4XhNZYg3DlDOro3akvx34X0eZGLhgr1UOYAIy9Bo0d7JkoGKK31frHuNEFnJxHtUDEBuTrVOd6htg%2FeRU%2F1jFTSC6g9mzjAilvTwCjfpaQwqWHarYu1%2Bnm5fV6U5EP4qppVcuIkaIxosX4tMh20f55lne%2BA0M3t7ziqxBgsvcNT1ARxEqTALKWG5VM%2BFmGnq3iyI805sevfjawCo4JM48khb5F8nVTQ0kCU6%2FSXxN2d0hZzMfYLhFGDJb%2FfME4b5oIfx8IXteTUaIw7rSBzwY6pgFiJNSCsbmUA17QvRRoB4NFPyhRjHN2qNCHHZkAoaxtHfRVD4a0WGUBDy7UdUVUKzCxZorAU5JBT6m7h4fiO%2FunzEd2ZH1suu2NV9PvbFSqVGEd7ut8UPSUz1ShMc%2BSDlNtxQjMWQaIXDYMl7vChMPz9IXdarGrQLPNuMDS9V2aUINevVvYTxjavHyBtC8C4%2BMhxmGApbw3A6RK5vg813Kp4WEbU7v7&X-Amz-Signature=fbbf605b3843846194b269935896c20a02ce2ab6e24e289de70ae25c233b6eba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

