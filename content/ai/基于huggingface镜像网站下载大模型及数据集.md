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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JCOSKA%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqqo0SZJHAyUb%2Bsp6cbNdiAPJlbD%2BYS9OzhFZpkPRGkwIhAOpQuaHLJQeKgM%2BXBz4nqA8H3SaaZJvkaRlzzktoJ%2F7iKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvjfmqYDqimVi9YlYq3AOvp7J9SY5DMmRXH6SEuKEvYWpwAwsLW4piKiNmPJYyAg7P8JFv3Dxtqn1DMiT3%2FvfBpZSXGouXCC2LSoviKmMc%2FDhgQzdj7%2BiSYftaA28Ys2LrUnEHVRcOIxsC1QSCLpnImocpBD0j1k7TuIrHjrWwxj9wTBI3J7RtMJ9Z%2BxTFWeeb9u8X19LaCgWmCFnJOdVbU%2F0yKcuNIQPRxsKJNsz7BkmJk5o0%2BPcFqycYcKsIMuabzRs4AXoLmDnSkwy669rCEAmSLEdJRyyCDvLj4ikHxE2v1O0h%2FGTFnr0gFk9vWztqL9TpoyOXAEuxpcHxttS%2FoJQtvLJs%2F%2FWlIz%2BitiX5EW1weE%2FDdG1havFhBXwtp5t33rbOx1kd%2BkJ1eJuuCZ0qFPPKuRU4XHHc2hHg2hvo1MRmqvWJfYJ1GewnNBwqvez229M4YmOVfNeTkXRwQLtm0Rl7tr5IP6ngMHbgYszKmIgIYCd7ZEPoynD9obzptpTKTrBNJGXi2vAau1P98qfDXhcDnY00BbhM5uHBDkWfe6%2BxzL9bJKyaC5hboyirKy2cE0zGRKwzafdhi%2F4H9o%2B0pv98yPi7FYSIzgb7FXF3e2vSc%2FPL2ESviOVS1Jhd9B2cZ4PgnF5rl1OaKDCwn8fOBjqkAcyTLN8sor%2B8x8tMXkC0g7CYpn0F6mnc90ZoPgigi%2FO0JbJ3guLt6Ew2cdbKtYn%2FQnU93HHh37Ixe%2FMh8is%2FYgbjiHIBFulOKfTDRi085UZN2OHaED%2FKV5fRRcBWT0qqbvJ9ZVCplfKgESs%2FSrLG8CkdPMod4dVSs8dJC6m6GQHtA1J5htgi2007%2Ft2TWs%2BZIQc6%2Fe6hreKbOS7cFWTTD8F%2Br1wr&X-Amz-Signature=fd4fe89533485712091a9a86cf0191309345b563d40a19c776aaa70ac3a3df90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JCOSKA%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqqo0SZJHAyUb%2Bsp6cbNdiAPJlbD%2BYS9OzhFZpkPRGkwIhAOpQuaHLJQeKgM%2BXBz4nqA8H3SaaZJvkaRlzzktoJ%2F7iKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvjfmqYDqimVi9YlYq3AOvp7J9SY5DMmRXH6SEuKEvYWpwAwsLW4piKiNmPJYyAg7P8JFv3Dxtqn1DMiT3%2FvfBpZSXGouXCC2LSoviKmMc%2FDhgQzdj7%2BiSYftaA28Ys2LrUnEHVRcOIxsC1QSCLpnImocpBD0j1k7TuIrHjrWwxj9wTBI3J7RtMJ9Z%2BxTFWeeb9u8X19LaCgWmCFnJOdVbU%2F0yKcuNIQPRxsKJNsz7BkmJk5o0%2BPcFqycYcKsIMuabzRs4AXoLmDnSkwy669rCEAmSLEdJRyyCDvLj4ikHxE2v1O0h%2FGTFnr0gFk9vWztqL9TpoyOXAEuxpcHxttS%2FoJQtvLJs%2F%2FWlIz%2BitiX5EW1weE%2FDdG1havFhBXwtp5t33rbOx1kd%2BkJ1eJuuCZ0qFPPKuRU4XHHc2hHg2hvo1MRmqvWJfYJ1GewnNBwqvez229M4YmOVfNeTkXRwQLtm0Rl7tr5IP6ngMHbgYszKmIgIYCd7ZEPoynD9obzptpTKTrBNJGXi2vAau1P98qfDXhcDnY00BbhM5uHBDkWfe6%2BxzL9bJKyaC5hboyirKy2cE0zGRKwzafdhi%2F4H9o%2B0pv98yPi7FYSIzgb7FXF3e2vSc%2FPL2ESviOVS1Jhd9B2cZ4PgnF5rl1OaKDCwn8fOBjqkAcyTLN8sor%2B8x8tMXkC0g7CYpn0F6mnc90ZoPgigi%2FO0JbJ3guLt6Ew2cdbKtYn%2FQnU93HHh37Ixe%2FMh8is%2FYgbjiHIBFulOKfTDRi085UZN2OHaED%2FKV5fRRcBWT0qqbvJ9ZVCplfKgESs%2FSrLG8CkdPMod4dVSs8dJC6m6GQHtA1J5htgi2007%2Ft2TWs%2BZIQc6%2Fe6hreKbOS7cFWTTD8F%2Br1wr&X-Amz-Signature=7eb1e236028f5f11f8ecba96f730d523cd021160fbaf18eb2b1190dcc4c5e0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



