---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RYMNDP4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8Yi7yhPw3eKdwL7EXbiKVa6SiQ%2FA8CwHHskavzv3dGAiByc6a5Ts9Nn4Mbg8%2BGBBGiHS7zvYXDDp49XW573rRVKSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1FFqMOcMCDUU4ILXKtwDdZnS7rgHbuVZ9PWMquDIYLxKh3%2B43fPCGxwMYUzNExZ3cB82Etu2DVR8Cr2rIKTco822fk26p%2FCssNSOKdwlYwG5bTuhGB4DYWZpzLsmS8D7DXzU7OpWDn5%2FGck16E8kfTzbtM%2FN6XWN0QhJCF7qjS9EiZ4u0QduYBCgIsNXoAfNfHTNPrbPA9Y%2FxqkWbTRdjcKIpJVAeYFkgVLFHLWG7P8vZ2WPHvg1hKsJqe8E6ubCS1mrLTD%2FEWfXFzwvcH7X9S47%2BbT8zxblinXvPPUtXMQsQyq%2FwZconrqOptHBQlL4nY8YzMxz5Yn8o1so9gP9FukUjkXonZvjbgXouSe06kle9Z96d62RKA4zRZroQ9CM%2FnMMoZZyYJ7V%2B4LjVLtu1%2BC7r2pCEZNL5rsSK2V8L8GNmL8gEbR9jTPSOV2fnHQYvFtSA5Q%2Buk6OITD3E7YAQmCEAN4%2BKLaQ1I9wjgc5Rf%2BLAdE%2BWeFRHUZLY2u4T7cqTCvZjZnS8Ha4bUOBTInuAi5yp128DDqDkZmEwAGnw%2Fj7WktafTDC0bn0AOcI3v4BryJjhQVBmiYTc8d3qZoqm6adeEYiGa%2FbKOXBQitPUkcr%2BErPbj%2BjaZFJaX%2BhMyX6IsLlRFfKLr4TzNIwtc2eyQY6pgGOaiweb6FwCkqxvpaE%2BhU8LQwHwHT1FUqkwwW84Qw2jgEYiVXUJG2ghwWcS1jt9ii3Wjxv5PGOH20htKHQdv13EXhGfpnfdsLJ3YdXovuOtdWlrYBU5IYec2jGr15X6Dimd6uLYk%2FDc3yRbQ%2F8jODNAiHVeTXME2GEtelHo6l7G7kW7sjygiCYvEDum5dAVxKfUljazhHbFOnDpgGrJP1nmcdZs0wu&X-Amz-Signature=11025855e44698aaf5e952871cf75b08e0183e9b13c2f8250e3c598988c15ec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RYMNDP4%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8Yi7yhPw3eKdwL7EXbiKVa6SiQ%2FA8CwHHskavzv3dGAiByc6a5Ts9Nn4Mbg8%2BGBBGiHS7zvYXDDp49XW573rRVKSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1FFqMOcMCDUU4ILXKtwDdZnS7rgHbuVZ9PWMquDIYLxKh3%2B43fPCGxwMYUzNExZ3cB82Etu2DVR8Cr2rIKTco822fk26p%2FCssNSOKdwlYwG5bTuhGB4DYWZpzLsmS8D7DXzU7OpWDn5%2FGck16E8kfTzbtM%2FN6XWN0QhJCF7qjS9EiZ4u0QduYBCgIsNXoAfNfHTNPrbPA9Y%2FxqkWbTRdjcKIpJVAeYFkgVLFHLWG7P8vZ2WPHvg1hKsJqe8E6ubCS1mrLTD%2FEWfXFzwvcH7X9S47%2BbT8zxblinXvPPUtXMQsQyq%2FwZconrqOptHBQlL4nY8YzMxz5Yn8o1so9gP9FukUjkXonZvjbgXouSe06kle9Z96d62RKA4zRZroQ9CM%2FnMMoZZyYJ7V%2B4LjVLtu1%2BC7r2pCEZNL5rsSK2V8L8GNmL8gEbR9jTPSOV2fnHQYvFtSA5Q%2Buk6OITD3E7YAQmCEAN4%2BKLaQ1I9wjgc5Rf%2BLAdE%2BWeFRHUZLY2u4T7cqTCvZjZnS8Ha4bUOBTInuAi5yp128DDqDkZmEwAGnw%2Fj7WktafTDC0bn0AOcI3v4BryJjhQVBmiYTc8d3qZoqm6adeEYiGa%2FbKOXBQitPUkcr%2BErPbj%2BjaZFJaX%2BhMyX6IsLlRFfKLr4TzNIwtc2eyQY6pgGOaiweb6FwCkqxvpaE%2BhU8LQwHwHT1FUqkwwW84Qw2jgEYiVXUJG2ghwWcS1jt9ii3Wjxv5PGOH20htKHQdv13EXhGfpnfdsLJ3YdXovuOtdWlrYBU5IYec2jGr15X6Dimd6uLYk%2FDc3yRbQ%2F8jODNAiHVeTXME2GEtelHo6l7G7kW7sjygiCYvEDum5dAVxKfUljazhHbFOnDpgGrJP1nmcdZs0wu&X-Amz-Signature=58111878d2daabeffd6e31bc3ebeebb4ed1916d97bbeb2fb720a1a50071fc584&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









