---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBSAPI5O%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRDqfg4hyotQBKRPeNVrDJa%2FhyfL7agWZf86DCeQr2gAiAhQo88L%2FCN%2BY9KYiIYMLvA50gOq6le%2BXsYApYPt96WZir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIM%2FksEwKOLQZ30NnKIKtwDiL5E6tQk22EayfinOgOGxCJkwa3z446wjDAJFwVGCnTJIP5DCcXBcJ4%2Blut45DL2R2A5cykWGeeId2xtpEdkCck4GO84FYmzWxl1RdMpqN%2BYjxgiRmOFm7qwsAVotJ0cJYxQQ8bA4Om4QnS1OXca9KiO0sW2s5ru2CtQmMcWgkJAZLljqghfS%2BnKt0Bx3OltCwf3791qAtT6ka9ujq%2BsW%2FVZIkvFSpY%2BC%2BZoXozEPDD1e1M7L9rY%2FI0pkPq0ZZ9%2BDDhF939Crs0KjRdQn3dWus%2FZd4jSe1cgZkDSvF2%2B6ideJp6VrVcuaDVZXX54Ej3iNR5Dr%2BvpkjBGk6%2F1lapWfOa1xxJtvk9guww4%2B3OLig5NV3b%2FJ5I0I8Ghgj7N19JANBULxrned3k4Dxy8XpWTnPXCKu%2BeneYRTxIQbN3xn0vvYLVN%2B3grH9LaUw%2FXPsgZJTcXq1vv7fRQAhaUKU1LBxq7V6ZnO3xBFNIXZJfHp5%2Br4B%2Fr7cnJ6u97j6ouU%2FYzeoZN32mbrWSwZ8bnci%2Bi4%2BInr8Y%2B2Bl5AUnQ4Xrtor%2BScMkcVDpJTfb2rwIsNxq0Zs6S9gDFDiIJvJwnAawKvr40jf5zH288%2FFm1djEauwZ49DxJ5zJj8XC6gg8w3%2BvBygY6pgGlrfc05S92454FxayIMw09migYTL3M%2FZtyreeS22nGU4IEqYiEz3Q3zreaonUUOamwSWq2%2BaIV8t1dpathWnpZ10IQ5zP8CwlTre4vnj%2BGWlnAyYdQCEwZJUv%2BphNsX%2FPbEoHnsGw%2B22TfeJ1T9%2F6uj%2F3qawkviRk6AX%2B%2FBJjJIaj5wZNhmQemXQzGrSfIq0tdNih1pGpYsdYezjf%2F6JqGHqBJdtlZ&X-Amz-Signature=beb92529c7b007557a08e3b7ddd509a698d82a67b666d5b758d93140af594677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBSAPI5O%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRDqfg4hyotQBKRPeNVrDJa%2FhyfL7agWZf86DCeQr2gAiAhQo88L%2FCN%2BY9KYiIYMLvA50gOq6le%2BXsYApYPt96WZir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIM%2FksEwKOLQZ30NnKIKtwDiL5E6tQk22EayfinOgOGxCJkwa3z446wjDAJFwVGCnTJIP5DCcXBcJ4%2Blut45DL2R2A5cykWGeeId2xtpEdkCck4GO84FYmzWxl1RdMpqN%2BYjxgiRmOFm7qwsAVotJ0cJYxQQ8bA4Om4QnS1OXca9KiO0sW2s5ru2CtQmMcWgkJAZLljqghfS%2BnKt0Bx3OltCwf3791qAtT6ka9ujq%2BsW%2FVZIkvFSpY%2BC%2BZoXozEPDD1e1M7L9rY%2FI0pkPq0ZZ9%2BDDhF939Crs0KjRdQn3dWus%2FZd4jSe1cgZkDSvF2%2B6ideJp6VrVcuaDVZXX54Ej3iNR5Dr%2BvpkjBGk6%2F1lapWfOa1xxJtvk9guww4%2B3OLig5NV3b%2FJ5I0I8Ghgj7N19JANBULxrned3k4Dxy8XpWTnPXCKu%2BeneYRTxIQbN3xn0vvYLVN%2B3grH9LaUw%2FXPsgZJTcXq1vv7fRQAhaUKU1LBxq7V6ZnO3xBFNIXZJfHp5%2Br4B%2Fr7cnJ6u97j6ouU%2FYzeoZN32mbrWSwZ8bnci%2Bi4%2BInr8Y%2B2Bl5AUnQ4Xrtor%2BScMkcVDpJTfb2rwIsNxq0Zs6S9gDFDiIJvJwnAawKvr40jf5zH288%2FFm1djEauwZ49DxJ5zJj8XC6gg8w3%2BvBygY6pgGlrfc05S92454FxayIMw09migYTL3M%2FZtyreeS22nGU4IEqYiEz3Q3zreaonUUOamwSWq2%2BaIV8t1dpathWnpZ10IQ5zP8CwlTre4vnj%2BGWlnAyYdQCEwZJUv%2BphNsX%2FPbEoHnsGw%2B22TfeJ1T9%2F6uj%2F3qawkviRk6AX%2B%2FBJjJIaj5wZNhmQemXQzGrSfIq0tdNih1pGpYsdYezjf%2F6JqGHqBJdtlZ&X-Amz-Signature=17edd520ca4f902a001da9a37944a5def1344701b2c2aa2385e1bcdd89755640&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



