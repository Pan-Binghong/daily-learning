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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AM3IVVN%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZigmepKfT%2FonHVoRIz%2Bj3Zl74%2FBLq7oitmslYIR5IPAiBEyu0NuBOIdxx%2B%2BhwKs%2FLmZ5rLn%2BsKMxhzJjZdxbeDESqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM7YNHoJ75Vfbc6%2BWKtwDQcfGOKKXrxNSsZvI%2FhEse%2FPlMQpXv4kKjGKbWe%2BpwxUiQuFsS3SyKT0BIY0ViTFvQ9I6ZD0BrpECd%2Br7eSG6CdeQOfuZROBYY1CuYYfYrYtQj4mRhqsmtUFx9zINAKvpEPA7hJSOaO3M%2FwJvSlcoihh0OLrOBi3KoYgtIvt6VwfiNoWow9gp06A8MWTx%2B9en8W3Cj%2BxqqkJZr4R7rmb36d%2FsTAZwJ5LX5YXAfsGGDjnabDPGu1apQs6tNLYWdJ1hNPFRVbXdxqMWxrCUzOVOcwhMcV%2F0ZnG0vF0vtGmujvE%2Bda3qhqDaidGyHBB%2B5KAGaSB2PdybHtcKAXuVyVpRBBplSjmA%2BJkWQbNMYVdvOBX2SNA1mq305JYZBKaFwbGLlmzZqigNm3aD0QCzieyoqIk8ilaBGXLiHZZI%2FolfYx55xbJ2muPXc%2BLBgwgHGd00Zeb5crfoC2mNqUKQMDuf0tCqTT1LG2rQkwkrHqjzuhizHcsq%2BSjXceEckotXPsYOCK62PrRVMCIjv0gORVRFqXqetWQnvAn4zOO1uOIrADeMEgF2Z9cH%2BlpLGvXJoM9KkpjjRduh6qNx2%2FWLknFaqMLVBX0iqmUXLPDlYqiyQuAnmv6uzkGlVxO8RIww7cvpzAY6pgGbcupF6V8j7Xj2%2BOvaExeLqsivx0Z%2Fyc6nfPYok6Vmt%2BGRKL%2FXjX1hcyxdZwNPbe2yrIu6NxlB6vFCnh%2FbI%2BRwqC2Dpvbu6XiV4sLcmtzicrjI5VY%2Bz8RU0tRlrz30ntZeJ7TVvm47%2F9dsxunS1Z6w255nflL2UjvyUGeBb5k3G%2BQ9SXIYuW%2B%2FWdc0roh%2FHSacXVEDSqtQlN5MElkNS55Y388OB%2BM7&X-Amz-Signature=4a009aa92d3970f37cc0e09e458921d0b5e7185c810266e6747c193e0f53f1eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

