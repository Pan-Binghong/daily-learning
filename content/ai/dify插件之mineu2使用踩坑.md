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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6SNYRL4%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQDUe053lZunPaQc8Upw90NyEYFDcNUGz17qWCmCqUSYZQIhAKZIW71e2004PG2QoVjZDjPu1bwjDwpmw0FXVFMrz3rmKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzm47GPf5RNwsSLkuIq3AMN%2BxeUiHBQIPeqzLiyNUqv4ozVyHX6QwEQveFBlLjzqC2iOVz85c0Out5WLns%2Bt3P68lv88IoUGZnP3PEPxFVJYSnB0cBxcq%2FYmtzM5TNmQSuekr1LWcMmXoRUkTTJmwgs%2BVKAgzMOMNbHs32kOnWfzdn%2F4XNI4Ym3SW%2B9Ti4Gsisj6HufQb6W0IYZapCr6c0BM%2BCFuoNLKBYWJk1La79h96OV6tWJuOJKqtChGtwAripI1lofFPwjU1a0r5g7z8ji7Dku3SdksSylAiZNzemKxi7lSiJ7Qnz5pSTUTPbDBmTRBy1nvblu2VnR0WEANJSHx0YsTLJ73C0WLo18Nryc%2BkuPdpsWAONDhgBbwHdOxp1Kkaw4SpBDmBWjdGeXCGZz8vsJYzxaPJwQfXQB74gJHUUNQUu1ewysH1sPWEbpKd2wHQUroGG%2BgzeoqbB0LVCSpAaQaBV9zpgPxsCV6pw%2B%2FaggvSIRX3q13KsA9A3fNgxfuX0O6%2FQIZ9LiuOurzCp6670qqSWdhjAVjdbFt77FRvuQwHCscfPHrMBooRODFmOEEgVIz6U2R2YFL%2F%2FJeyAUjECm4DTPnYp0ZuEyv25ckYtemQJjvxCJGQc%2FKAb36Odsh7eR4tUWojdZ6DDF1O3JBjqkASbh0ea76a2gfufLBp1R5a3BhCh%2BrO2ZHfTWcPZJf5ff%2FocEbC80o6r%2Fr4N40p6Of%2BND4UZa97POsCgNeeW1CoyGi0%2FzMC30%2FlBN9EM7ZLd4o6GbcXRsgKBZbfqUGMlTXnVk2l%2FM0gYlXknpnUm2Fm7Mrmq62%2FZWMkK7EAoLvHzPsvuY5ZInB4eP5h5Ak9mhSPassWm8eSCnjzYRiEAvFXbyBaHH&X-Amz-Signature=7f7d5c378a1bee00d1b5374bb9f51b80210c4b1c92ffd8453d54fb574eff278a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6SNYRL4%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQDUe053lZunPaQc8Upw90NyEYFDcNUGz17qWCmCqUSYZQIhAKZIW71e2004PG2QoVjZDjPu1bwjDwpmw0FXVFMrz3rmKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzm47GPf5RNwsSLkuIq3AMN%2BxeUiHBQIPeqzLiyNUqv4ozVyHX6QwEQveFBlLjzqC2iOVz85c0Out5WLns%2Bt3P68lv88IoUGZnP3PEPxFVJYSnB0cBxcq%2FYmtzM5TNmQSuekr1LWcMmXoRUkTTJmwgs%2BVKAgzMOMNbHs32kOnWfzdn%2F4XNI4Ym3SW%2B9Ti4Gsisj6HufQb6W0IYZapCr6c0BM%2BCFuoNLKBYWJk1La79h96OV6tWJuOJKqtChGtwAripI1lofFPwjU1a0r5g7z8ji7Dku3SdksSylAiZNzemKxi7lSiJ7Qnz5pSTUTPbDBmTRBy1nvblu2VnR0WEANJSHx0YsTLJ73C0WLo18Nryc%2BkuPdpsWAONDhgBbwHdOxp1Kkaw4SpBDmBWjdGeXCGZz8vsJYzxaPJwQfXQB74gJHUUNQUu1ewysH1sPWEbpKd2wHQUroGG%2BgzeoqbB0LVCSpAaQaBV9zpgPxsCV6pw%2B%2FaggvSIRX3q13KsA9A3fNgxfuX0O6%2FQIZ9LiuOurzCp6670qqSWdhjAVjdbFt77FRvuQwHCscfPHrMBooRODFmOEEgVIz6U2R2YFL%2F%2FJeyAUjECm4DTPnYp0ZuEyv25ckYtemQJjvxCJGQc%2FKAb36Odsh7eR4tUWojdZ6DDF1O3JBjqkASbh0ea76a2gfufLBp1R5a3BhCh%2BrO2ZHfTWcPZJf5ff%2FocEbC80o6r%2Fr4N40p6Of%2BND4UZa97POsCgNeeW1CoyGi0%2FzMC30%2FlBN9EM7ZLd4o6GbcXRsgKBZbfqUGMlTXnVk2l%2FM0gYlXknpnUm2Fm7Mrmq62%2FZWMkK7EAoLvHzPsvuY5ZInB4eP5h5Ak9mhSPassWm8eSCnjzYRiEAvFXbyBaHH&X-Amz-Signature=8bcaa51e01996ab745f8c878a0ba25872bf0764023337c10b56e6b6213900ba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



