---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4XIGY5M%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQDMopGv4HjlDo9Ixgy0UPdCJbja7fJeWUCuvgM6l28pXAIhAIkoxm8TLAr3Ox%2BPRpP4GoBiIJY1wFZe28yRr5FtJoAQKv8DCCIQABoMNjM3NDIzMTgzODA1IgxZtfp9nOYzYEIEGYcq3ANehMGIVsFZwLhwnPONBOG6Fa1Mbf2fgJms0fmVC%2FPDrFSPBEKcvEZD0RF3xkFwpwJMvivVsdLE46qOOdbybOJyULMbVHq6an0hhMF6wxzXWA%2B4X618%2FiZblIZYUtrXxsiNLMCAl%2BE1ut7amI2WDnZPyWMcid9LQG0drhEgL5fnQtNN%2FH5Lk2I69eIYw%2BBOgvQ576e%2BUlZ7JFBA7pxSRbcy6uZ7vCduGmrQT6DeXHZRP7M5vJnsBFATAwIhmo8ZarAzb1Kgnf8Nn9XMkAOktAYKuDY%2FQWPafryxXyCglHNx0jr0U0jLg5BgXwYXZb6YLCXJPoAkdgzKqagLiLaxzYQ6f%2B9mrot9kdQI3OWc52qxIUgIR9BvJO%2BSg4YJPkKQSWnn52H9gJ%2BssCv7EZ%2FdDWPURligUXyOYR7AsqUyxaMH1y9W04O9%2FYgwJFub7nrhhiIAdYTijgxUy8MnXZ3tVKLKdJ77oThec7jqPa9ca42qeNmFJYR8Sk4DG1y2zgrGa%2BEuHtw5dGVcRQfuf7vDEoeYDAwDyeV19wmU4Tehs7jJ2gmwPwR9DfBV7QZDi5v8s1s3HSSWpuK8N5BO07vlGWmpKlGUGCkTQjwjvUwwnwk6YTi%2BzyA9ARUCJ8MfljDblL7JBjqkAe%2Bl1FAtPovaOYggXwHs7Br5KuNf5Ngb17CZuWbSYS0BOeXrSf17gxUwuzB%2BN1gXSb4neR3BZAbRpRD%2BOzjc9tSmxmp1sX6zE9Ti4CEpawrUCb%2BuyGUBD4FbwL%2Fzm9FFYHo4NBZhK4cMcK0NSUrXNrwfN4%2FSnQKbxH%2FuQV94ZSTWxsg7oisaioKRuuLPeVWiSqS5VCwA1IlCUIjMzHiB4b4X8zTI&X-Amz-Signature=fcf9d44486031daed8bfa71916020e8db18e0910de058631fd80dd909d86702f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4XIGY5M%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQDMopGv4HjlDo9Ixgy0UPdCJbja7fJeWUCuvgM6l28pXAIhAIkoxm8TLAr3Ox%2BPRpP4GoBiIJY1wFZe28yRr5FtJoAQKv8DCCIQABoMNjM3NDIzMTgzODA1IgxZtfp9nOYzYEIEGYcq3ANehMGIVsFZwLhwnPONBOG6Fa1Mbf2fgJms0fmVC%2FPDrFSPBEKcvEZD0RF3xkFwpwJMvivVsdLE46qOOdbybOJyULMbVHq6an0hhMF6wxzXWA%2B4X618%2FiZblIZYUtrXxsiNLMCAl%2BE1ut7amI2WDnZPyWMcid9LQG0drhEgL5fnQtNN%2FH5Lk2I69eIYw%2BBOgvQ576e%2BUlZ7JFBA7pxSRbcy6uZ7vCduGmrQT6DeXHZRP7M5vJnsBFATAwIhmo8ZarAzb1Kgnf8Nn9XMkAOktAYKuDY%2FQWPafryxXyCglHNx0jr0U0jLg5BgXwYXZb6YLCXJPoAkdgzKqagLiLaxzYQ6f%2B9mrot9kdQI3OWc52qxIUgIR9BvJO%2BSg4YJPkKQSWnn52H9gJ%2BssCv7EZ%2FdDWPURligUXyOYR7AsqUyxaMH1y9W04O9%2FYgwJFub7nrhhiIAdYTijgxUy8MnXZ3tVKLKdJ77oThec7jqPa9ca42qeNmFJYR8Sk4DG1y2zgrGa%2BEuHtw5dGVcRQfuf7vDEoeYDAwDyeV19wmU4Tehs7jJ2gmwPwR9DfBV7QZDi5v8s1s3HSSWpuK8N5BO07vlGWmpKlGUGCkTQjwjvUwwnwk6YTi%2BzyA9ARUCJ8MfljDblL7JBjqkAe%2Bl1FAtPovaOYggXwHs7Br5KuNf5Ngb17CZuWbSYS0BOeXrSf17gxUwuzB%2BN1gXSb4neR3BZAbRpRD%2BOzjc9tSmxmp1sX6zE9Ti4CEpawrUCb%2BuyGUBD4FbwL%2Fzm9FFYHo4NBZhK4cMcK0NSUrXNrwfN4%2FSnQKbxH%2FuQV94ZSTWxsg7oisaioKRuuLPeVWiSqS5VCwA1IlCUIjMzHiB4b4X8zTI&X-Amz-Signature=c04bff4585977343e77480014adbe38d90d72d205c3e63324973bf73083dd5a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4XIGY5M%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQDMopGv4HjlDo9Ixgy0UPdCJbja7fJeWUCuvgM6l28pXAIhAIkoxm8TLAr3Ox%2BPRpP4GoBiIJY1wFZe28yRr5FtJoAQKv8DCCIQABoMNjM3NDIzMTgzODA1IgxZtfp9nOYzYEIEGYcq3ANehMGIVsFZwLhwnPONBOG6Fa1Mbf2fgJms0fmVC%2FPDrFSPBEKcvEZD0RF3xkFwpwJMvivVsdLE46qOOdbybOJyULMbVHq6an0hhMF6wxzXWA%2B4X618%2FiZblIZYUtrXxsiNLMCAl%2BE1ut7amI2WDnZPyWMcid9LQG0drhEgL5fnQtNN%2FH5Lk2I69eIYw%2BBOgvQ576e%2BUlZ7JFBA7pxSRbcy6uZ7vCduGmrQT6DeXHZRP7M5vJnsBFATAwIhmo8ZarAzb1Kgnf8Nn9XMkAOktAYKuDY%2FQWPafryxXyCglHNx0jr0U0jLg5BgXwYXZb6YLCXJPoAkdgzKqagLiLaxzYQ6f%2B9mrot9kdQI3OWc52qxIUgIR9BvJO%2BSg4YJPkKQSWnn52H9gJ%2BssCv7EZ%2FdDWPURligUXyOYR7AsqUyxaMH1y9W04O9%2FYgwJFub7nrhhiIAdYTijgxUy8MnXZ3tVKLKdJ77oThec7jqPa9ca42qeNmFJYR8Sk4DG1y2zgrGa%2BEuHtw5dGVcRQfuf7vDEoeYDAwDyeV19wmU4Tehs7jJ2gmwPwR9DfBV7QZDi5v8s1s3HSSWpuK8N5BO07vlGWmpKlGUGCkTQjwjvUwwnwk6YTi%2BzyA9ARUCJ8MfljDblL7JBjqkAe%2Bl1FAtPovaOYggXwHs7Br5KuNf5Ngb17CZuWbSYS0BOeXrSf17gxUwuzB%2BN1gXSb4neR3BZAbRpRD%2BOzjc9tSmxmp1sX6zE9Ti4CEpawrUCb%2BuyGUBD4FbwL%2Fzm9FFYHo4NBZhK4cMcK0NSUrXNrwfN4%2FSnQKbxH%2FuQV94ZSTWxsg7oisaioKRuuLPeVWiSqS5VCwA1IlCUIjMzHiB4b4X8zTI&X-Amz-Signature=9e9356f27ddf146ad1e387a4900ab1819e4e793c44870fba731f187dc46b84d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

