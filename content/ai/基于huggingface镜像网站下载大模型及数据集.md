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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMCVFY7Y%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArZT3zfK8WTlU8%2FOciiqTm2G0Am%2FIkTFNfCUOC2VSLmAiAClJB57eIn51jK3i%2Bz7T4UZSyXwZ7KGn2moqSzF%2F0buCqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQw%2FLNiBc%2FQxCJpu7KtwDArBl0cFF16KHSXB%2FeaQcvzFtqwrToajWDJL7Hdkpuu3nkIbdEdfZY8ey9M3gZYQ%2Brd9cnO%2BCv5nTNYymAEQXffgW6GTryMzLmCke65XRIhLh1zxLSako48Db%2F%2B3ZOCZVf9BqrvwbEMZsWDZZNgXaB8LNABCHflTgh6tf5lGJSE4y86jrvFRWW9Sp6JkQk%2BczciJlJX6iRnBkkyd817de7vp5lZsEEpFK0eL%2BTmrZdLQPqFS9d3z68ZYqOH0UU%2Faw43o3K5T6ZJ9UcWpk9XpCwGmz%2B0PcN2UgIgL2Ef9CiMD%2FO9T7HoaT%2BckwWVqmd%2B5awPGkQ5SwdV8qpatZIrjpY2x2s4%2FDwxYrtAn47I0tWxHcsD%2BsZebb7sT3bVxwWus%2FSSioC4HBrrWXpVUxrfvNwzQMRBajCUASRbmhG4WZRVmqN7doZTwNYODfOl2VUiFm%2F7vx0ymvfRgnBYnv9HMIfB74hHcj6IRt55QVjHD8RRRZL02sPs01yODh8Fe8e0rT9ALr4%2Bij93pSIz%2B2kio5KZkVbNQGacEOZ%2FC9uGJZ4lhh7W8l1yMeuo1C04270rZtpRJtPx%2BjM7vfyYqZsAYxgUlwZyJiyvZGddzc70syZKp8qlCPaAr2yCzCINMwtrW1yAY6pgHLqy1y1IIKCEMc7i2glyfeeUcwoZYnXJuUbeVYkc4Ih2xvzagjMhyMC%2BzDblfw07I%2BdgHRue0jkD7FbGWCqFwwfcIPrbjZTSpCWUJVLwuiRmk7cDTwuuVUdzI%2Bc0RUWzl5wvZEDWGlVtWdXPjDJErlTv3VPW33jmMv%2F67XxXyafoBtfPxn5d%2Fdug7iyr3F7OmRct8V6ioDK59GBkAvHqNL6QUj%2BeiE&X-Amz-Signature=1646a7a5bcac7a0169ab9ddf130e09d82f2d310bbdd4061d5941aa7e85abc927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMCVFY7Y%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArZT3zfK8WTlU8%2FOciiqTm2G0Am%2FIkTFNfCUOC2VSLmAiAClJB57eIn51jK3i%2Bz7T4UZSyXwZ7KGn2moqSzF%2F0buCqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQw%2FLNiBc%2FQxCJpu7KtwDArBl0cFF16KHSXB%2FeaQcvzFtqwrToajWDJL7Hdkpuu3nkIbdEdfZY8ey9M3gZYQ%2Brd9cnO%2BCv5nTNYymAEQXffgW6GTryMzLmCke65XRIhLh1zxLSako48Db%2F%2B3ZOCZVf9BqrvwbEMZsWDZZNgXaB8LNABCHflTgh6tf5lGJSE4y86jrvFRWW9Sp6JkQk%2BczciJlJX6iRnBkkyd817de7vp5lZsEEpFK0eL%2BTmrZdLQPqFS9d3z68ZYqOH0UU%2Faw43o3K5T6ZJ9UcWpk9XpCwGmz%2B0PcN2UgIgL2Ef9CiMD%2FO9T7HoaT%2BckwWVqmd%2B5awPGkQ5SwdV8qpatZIrjpY2x2s4%2FDwxYrtAn47I0tWxHcsD%2BsZebb7sT3bVxwWus%2FSSioC4HBrrWXpVUxrfvNwzQMRBajCUASRbmhG4WZRVmqN7doZTwNYODfOl2VUiFm%2F7vx0ymvfRgnBYnv9HMIfB74hHcj6IRt55QVjHD8RRRZL02sPs01yODh8Fe8e0rT9ALr4%2Bij93pSIz%2B2kio5KZkVbNQGacEOZ%2FC9uGJZ4lhh7W8l1yMeuo1C04270rZtpRJtPx%2BjM7vfyYqZsAYxgUlwZyJiyvZGddzc70syZKp8qlCPaAr2yCzCINMwtrW1yAY6pgHLqy1y1IIKCEMc7i2glyfeeUcwoZYnXJuUbeVYkc4Ih2xvzagjMhyMC%2BzDblfw07I%2BdgHRue0jkD7FbGWCqFwwfcIPrbjZTSpCWUJVLwuiRmk7cDTwuuVUdzI%2Bc0RUWzl5wvZEDWGlVtWdXPjDJErlTv3VPW33jmMv%2F67XxXyafoBtfPxn5d%2Fdug7iyr3F7OmRct8V6ioDK59GBkAvHqNL6QUj%2BeiE&X-Amz-Signature=580bd48d7a0d5dc7057d1f840d05edd11ef5f0b0d2e45fec2c78f6e7f1ae6dec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



