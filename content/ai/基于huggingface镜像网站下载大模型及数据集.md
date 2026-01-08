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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA3DUI4T%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHEJKnD%2FgfrlWtmpTU4Db2C0X2%2Fxk9fODV2ITdu6XOfqAiB95xQNeQs8%2BTr2lE7EguoTrmAbAuOuh1kZaLpiSvu8ByqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFtBKH18JHTQwcOrBKtwDKlcXFfK7remNMh998uDsoP5NxJRkYnbZO%2Fb36%2B6osDi0ycd2%2BC0oN0cUNafwCJsOeRQwxNu83OptG0JLfTd5%2FuWNQ8wJvJjV6wkxdIkj%2BA6dQcZbmMU03yaE8KJNPjhAXcfVvk6qrxLuPEMO1l%2BiLAWcv14KpsXD8MpDq5E5hPjcipV5yBUp46xeiCAeo8C0giOggiGOYVYw%2B43xS2UK%2FB8DGu3zsFvhFF55hjynXmNB%2BiljVM7g8THvNltsUaPXtGaRVYR3YAM8X5m57dTMJFUApOXiuCUIzhMYSZyFgFtmsJvp%2F%2B6%2BEClUbSKR6u%2F%2FvVhL%2F%2FTvvRzKcHpk%2B0LZk613P3%2FdcXsChK8qkmDAau%2FQGJwd6qCyqZBN8x8iS510FZWubA4XvW%2BPDu7xfvMaS24qFD6p%2BrJ5gcUh8JzOTtuGitlA3dls8RlgjK%2BrOFTkLnb2GSmrdMoJ07%2BhfTE%2F%2BhtzEKxsbos7CAdc%2B%2FH47eKrFyMPhhhDP35B4DV2%2B5LLxlKqqOoZ3yzpCqJ70LMD0oo2bgemyIizJyALhRQl1FUqoyFwaD6%2BTC45F%2BQHkSBgX4YZsUiN4xP21uZI2263cbYJqLfa%2FA2ADNk%2FaAmm9MtlZ3rGhQXjlGf0M9owh6n8ygY6pgFmybcYSqZz%2F5%2FVeq1e1x0ut0q2dOdsILC6u4gj9P8X2llew1UbTaqunejrmRbDjlixfVgy0Az5isAqT2Xh5i6puEVtU7aYJBn7zbLjkbiefXwBALva9n2KA%2BMbrMgpG4cY0I9N1t4BKto7NzLZz8XODrIUkO0CB0D194qMbz7p%2BHuajQuVawdkh%2B5FvKVm%2FAV2%2FhRqeTOtpzP9jIOSi0riGfGAliqn&X-Amz-Signature=bb09cd11548646fe73c7d262de1565071990f6488b8fffbbc94d56e85b5fbe12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA3DUI4T%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHEJKnD%2FgfrlWtmpTU4Db2C0X2%2Fxk9fODV2ITdu6XOfqAiB95xQNeQs8%2BTr2lE7EguoTrmAbAuOuh1kZaLpiSvu8ByqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFtBKH18JHTQwcOrBKtwDKlcXFfK7remNMh998uDsoP5NxJRkYnbZO%2Fb36%2B6osDi0ycd2%2BC0oN0cUNafwCJsOeRQwxNu83OptG0JLfTd5%2FuWNQ8wJvJjV6wkxdIkj%2BA6dQcZbmMU03yaE8KJNPjhAXcfVvk6qrxLuPEMO1l%2BiLAWcv14KpsXD8MpDq5E5hPjcipV5yBUp46xeiCAeo8C0giOggiGOYVYw%2B43xS2UK%2FB8DGu3zsFvhFF55hjynXmNB%2BiljVM7g8THvNltsUaPXtGaRVYR3YAM8X5m57dTMJFUApOXiuCUIzhMYSZyFgFtmsJvp%2F%2B6%2BEClUbSKR6u%2F%2FvVhL%2F%2FTvvRzKcHpk%2B0LZk613P3%2FdcXsChK8qkmDAau%2FQGJwd6qCyqZBN8x8iS510FZWubA4XvW%2BPDu7xfvMaS24qFD6p%2BrJ5gcUh8JzOTtuGitlA3dls8RlgjK%2BrOFTkLnb2GSmrdMoJ07%2BhfTE%2F%2BhtzEKxsbos7CAdc%2B%2FH47eKrFyMPhhhDP35B4DV2%2B5LLxlKqqOoZ3yzpCqJ70LMD0oo2bgemyIizJyALhRQl1FUqoyFwaD6%2BTC45F%2BQHkSBgX4YZsUiN4xP21uZI2263cbYJqLfa%2FA2ADNk%2FaAmm9MtlZ3rGhQXjlGf0M9owh6n8ygY6pgFmybcYSqZz%2F5%2FVeq1e1x0ut0q2dOdsILC6u4gj9P8X2llew1UbTaqunejrmRbDjlixfVgy0Az5isAqT2Xh5i6puEVtU7aYJBn7zbLjkbiefXwBALva9n2KA%2BMbrMgpG4cY0I9N1t4BKto7NzLZz8XODrIUkO0CB0D194qMbz7p%2BHuajQuVawdkh%2B5FvKVm%2FAV2%2FhRqeTOtpzP9jIOSi0riGfGAliqn&X-Amz-Signature=8cfb6dc4f25b00217e6194b5fb34f35548c8db2176d68753cea936a36ab412a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



