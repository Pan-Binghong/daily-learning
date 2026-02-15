---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNGFJTBZ%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDAWq6GX7VMtoUjx9cLUkIG4Q9n1vnStvx0QBgw8ndvoQIhALGtYt%2BJ6JbwFmtGjWtBILu6EopC4K7hvWuSmiT8N1i%2FKv8DCBEQABoMNjM3NDIzMTgzODA1IgwvA1RYepzEoskhS%2FQq3ANbHK151dMvNpNSIjWrJTT5SUmi0aJDt1vCB7Yf5Zm%2BdGFEmPSkavZY8Kp71gTq3190A1hecWp7y2fH7D%2B4sLNWWgP3QDXGC4dyq9TXvSkuPmBcn4d72vRI5I8tlq%2F3gC94OUhNAUJXeV4o5tK3nGNhCkN7HO3oRwWaMz6NdWfmI19kHVvig5qZeJDVD0jFPKu2M5jqfdNfw91nT37H5v1Czt%2B8Ksl%2BICuiO2HcbcPKrUvmTnoVit63CU%2BPG6taGQMrsmvQIm0%2BGYdUvHCZargmsPZ6BHa86LAMM5r9y9EE0Z3G0zFK8WBfgrmvzoiLh2EIJBPoZIkgsZoB%2BFMNPmwQEXIW68blDMN06b7gZq4mCH1%2F9ZMOKL59FUC%2FMKBT0wx9Dmwfsg1ahPFHzYeyVueUom7yHv0FPRXkYWAHsX%2F3prCLaWeXT4%2FyP901rrKV8p1P6i1IiBDveXj3tXE0fCKQ58%2FrsW7QdG55HoazwaNAa%2FkyxUkMneELrPYnlTfxefCrLqukHC4BbsPgDoXTxQnpC0NoapAKauIQeaWe9Jn%2Fsjd5o2LsMIX7ky3nQIgu0WT7Ag0cjuKaB8gktgNo3nKfRL%2FeL7AGC2sBY14%2F%2B45WD6vdI5hp4DeL1%2BA7kTCWnsTMBjqkAdv9oiHP7pUuoANxQL%2BI1PChiw0sLxc17SNaOAIvjih5L%2FLHFuzAHusmrx5NlXnUVXrRnavR61I%2F3T9rzmywiICKD7s%2Bz21LqWiWkWeQguCfp6LwE9%2FK%2BkBFG8I%2BwV%2F%2Btx80pKVQOmLp9DVFk3lHDva3TWb3dZ2tLkTB5%2BBXoNhbwCc2%2FjelIBp6o51GS%2FVJsTa%2FfnOo9Dismo21gfaD4EOfzbaY&X-Amz-Signature=06a16a32c8bf09d7efaa35f9d351354933b5c9f1faec33b07d3c1eb8d5e23d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNGFJTBZ%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDAWq6GX7VMtoUjx9cLUkIG4Q9n1vnStvx0QBgw8ndvoQIhALGtYt%2BJ6JbwFmtGjWtBILu6EopC4K7hvWuSmiT8N1i%2FKv8DCBEQABoMNjM3NDIzMTgzODA1IgwvA1RYepzEoskhS%2FQq3ANbHK151dMvNpNSIjWrJTT5SUmi0aJDt1vCB7Yf5Zm%2BdGFEmPSkavZY8Kp71gTq3190A1hecWp7y2fH7D%2B4sLNWWgP3QDXGC4dyq9TXvSkuPmBcn4d72vRI5I8tlq%2F3gC94OUhNAUJXeV4o5tK3nGNhCkN7HO3oRwWaMz6NdWfmI19kHVvig5qZeJDVD0jFPKu2M5jqfdNfw91nT37H5v1Czt%2B8Ksl%2BICuiO2HcbcPKrUvmTnoVit63CU%2BPG6taGQMrsmvQIm0%2BGYdUvHCZargmsPZ6BHa86LAMM5r9y9EE0Z3G0zFK8WBfgrmvzoiLh2EIJBPoZIkgsZoB%2BFMNPmwQEXIW68blDMN06b7gZq4mCH1%2F9ZMOKL59FUC%2FMKBT0wx9Dmwfsg1ahPFHzYeyVueUom7yHv0FPRXkYWAHsX%2F3prCLaWeXT4%2FyP901rrKV8p1P6i1IiBDveXj3tXE0fCKQ58%2FrsW7QdG55HoazwaNAa%2FkyxUkMneELrPYnlTfxefCrLqukHC4BbsPgDoXTxQnpC0NoapAKauIQeaWe9Jn%2Fsjd5o2LsMIX7ky3nQIgu0WT7Ag0cjuKaB8gktgNo3nKfRL%2FeL7AGC2sBY14%2F%2B45WD6vdI5hp4DeL1%2BA7kTCWnsTMBjqkAdv9oiHP7pUuoANxQL%2BI1PChiw0sLxc17SNaOAIvjih5L%2FLHFuzAHusmrx5NlXnUVXrRnavR61I%2F3T9rzmywiICKD7s%2Bz21LqWiWkWeQguCfp6LwE9%2FK%2BkBFG8I%2BwV%2F%2Btx80pKVQOmLp9DVFk3lHDva3TWb3dZ2tLkTB5%2BBXoNhbwCc2%2FjelIBp6o51GS%2FVJsTa%2FfnOo9Dismo21gfaD4EOfzbaY&X-Amz-Signature=82271b56bf5804eba2b0475dd887480e5a1755ff3fc46c56e40fbccdde4b5ab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



