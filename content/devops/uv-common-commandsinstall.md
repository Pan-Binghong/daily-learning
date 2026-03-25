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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDMHF4Z4%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBnA5sKfrBibmZn9gN%2Fnb6014vmAwn3%2Fr7xGc%2BIzs3QRAiB6m8%2FQf%2Fc%2B4s8ZRHLkS89wLqNV4w2ydOniQTsrv8gpxyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad3Px29pYHleT7Z3KtwD0u%2FVI70kfZNPXLG%2BYvYLUYEmPZR9qyh7DzHRzxht8J2OhujyB7B%2BjhStcejMcv3sO8qxOers9JrWMxloMCvDXuNxR%2BYN8v9m3rMJFP62%2FLU1doOBnQOMp3dUt5%2FoafTCkGwMoaOLgjxQod3XkmQO7EwIVoWdIZzqCw5iWHp3gM4SD9R76ibDYDpPYk6VvmhA8H33VbtLnWAYiVVIrp0ZNLf0bMhLoVCdpTc3qBGleAMYu%2FOxmHOWYUg6ii3BGpR9DDnSj7wHjTPZo%2FlDt%2B8VgmK3d4ZnQsxbdtVvEDgBtcphebNmNX1YbJ4tmsGXyRSVSsXXOhXQ72kml9qo3otvoE0UZxd4x9wXFXuU6fQNhmLiXvTq1qQcsqUyszQVzictBMQYFPv1yIwSfmWM63dqGhp8h2vhlpqN2M%2FjqjRcOcG2TqnJm1lbJpGwJ1gpBjzDH9OYOZLysPmOj9LO4NDRLviWsNG9QtYlo6eiKSh%2BRHecXc3BmQO%2FFx00muN9c%2F6lZLFqMBz5cACKIk%2FOd2%2B0TmY9b8DSYiKPD9fAFR1e6rDjNzaHojacX4cjWl6RFGMfTHlqNZ3QHRajdNc%2F5LYT5I160rkwtBZIuaEYeQk1KqaKh%2Bvg1Trk8Pfmdmsw4qWNzgY6pgFrnzRPXNBGjHIkdmJPThLW4fMq74eNzXR7SOpR49GpmIEnD5Mo1DuD2Jml515Zu7L3lIRUR%2FUXf9hmkWQsyLoRmmaUqVEC4inhGhW5uwt7LmG%2Fphi2oAecH3MbMBoRQqVGxbdbKq7k%2Bvw3kRm7nUn1%2BM36y57tIcX9GgagNC2rQTExmToR3AEx0pfJ%2FB%2BAQuN73KKUyPcaSWr%2FaUdKP%2FlNRbBJPd2%2B&X-Amz-Signature=9721f4fa109027902f9de67265e8fc501eb2609450d9a17e7036924f1e9d4d30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDMHF4Z4%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBnA5sKfrBibmZn9gN%2Fnb6014vmAwn3%2Fr7xGc%2BIzs3QRAiB6m8%2FQf%2Fc%2B4s8ZRHLkS89wLqNV4w2ydOniQTsrv8gpxyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad3Px29pYHleT7Z3KtwD0u%2FVI70kfZNPXLG%2BYvYLUYEmPZR9qyh7DzHRzxht8J2OhujyB7B%2BjhStcejMcv3sO8qxOers9JrWMxloMCvDXuNxR%2BYN8v9m3rMJFP62%2FLU1doOBnQOMp3dUt5%2FoafTCkGwMoaOLgjxQod3XkmQO7EwIVoWdIZzqCw5iWHp3gM4SD9R76ibDYDpPYk6VvmhA8H33VbtLnWAYiVVIrp0ZNLf0bMhLoVCdpTc3qBGleAMYu%2FOxmHOWYUg6ii3BGpR9DDnSj7wHjTPZo%2FlDt%2B8VgmK3d4ZnQsxbdtVvEDgBtcphebNmNX1YbJ4tmsGXyRSVSsXXOhXQ72kml9qo3otvoE0UZxd4x9wXFXuU6fQNhmLiXvTq1qQcsqUyszQVzictBMQYFPv1yIwSfmWM63dqGhp8h2vhlpqN2M%2FjqjRcOcG2TqnJm1lbJpGwJ1gpBjzDH9OYOZLysPmOj9LO4NDRLviWsNG9QtYlo6eiKSh%2BRHecXc3BmQO%2FFx00muN9c%2F6lZLFqMBz5cACKIk%2FOd2%2B0TmY9b8DSYiKPD9fAFR1e6rDjNzaHojacX4cjWl6RFGMfTHlqNZ3QHRajdNc%2F5LYT5I160rkwtBZIuaEYeQk1KqaKh%2Bvg1Trk8Pfmdmsw4qWNzgY6pgFrnzRPXNBGjHIkdmJPThLW4fMq74eNzXR7SOpR49GpmIEnD5Mo1DuD2Jml515Zu7L3lIRUR%2FUXf9hmkWQsyLoRmmaUqVEC4inhGhW5uwt7LmG%2Fphi2oAecH3MbMBoRQqVGxbdbKq7k%2Bvw3kRm7nUn1%2BM36y57tIcX9GgagNC2rQTExmToR3AEx0pfJ%2FB%2BAQuN73KKUyPcaSWr%2FaUdKP%2FlNRbBJPd2%2B&X-Amz-Signature=0b35a4e6721d16902236d0a0c73dd1cc21c2fed06b5c1b96100e4e9997a0c401&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDMHF4Z4%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBnA5sKfrBibmZn9gN%2Fnb6014vmAwn3%2Fr7xGc%2BIzs3QRAiB6m8%2FQf%2Fc%2B4s8ZRHLkS89wLqNV4w2ydOniQTsrv8gpxyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad3Px29pYHleT7Z3KtwD0u%2FVI70kfZNPXLG%2BYvYLUYEmPZR9qyh7DzHRzxht8J2OhujyB7B%2BjhStcejMcv3sO8qxOers9JrWMxloMCvDXuNxR%2BYN8v9m3rMJFP62%2FLU1doOBnQOMp3dUt5%2FoafTCkGwMoaOLgjxQod3XkmQO7EwIVoWdIZzqCw5iWHp3gM4SD9R76ibDYDpPYk6VvmhA8H33VbtLnWAYiVVIrp0ZNLf0bMhLoVCdpTc3qBGleAMYu%2FOxmHOWYUg6ii3BGpR9DDnSj7wHjTPZo%2FlDt%2B8VgmK3d4ZnQsxbdtVvEDgBtcphebNmNX1YbJ4tmsGXyRSVSsXXOhXQ72kml9qo3otvoE0UZxd4x9wXFXuU6fQNhmLiXvTq1qQcsqUyszQVzictBMQYFPv1yIwSfmWM63dqGhp8h2vhlpqN2M%2FjqjRcOcG2TqnJm1lbJpGwJ1gpBjzDH9OYOZLysPmOj9LO4NDRLviWsNG9QtYlo6eiKSh%2BRHecXc3BmQO%2FFx00muN9c%2F6lZLFqMBz5cACKIk%2FOd2%2B0TmY9b8DSYiKPD9fAFR1e6rDjNzaHojacX4cjWl6RFGMfTHlqNZ3QHRajdNc%2F5LYT5I160rkwtBZIuaEYeQk1KqaKh%2Bvg1Trk8Pfmdmsw4qWNzgY6pgFrnzRPXNBGjHIkdmJPThLW4fMq74eNzXR7SOpR49GpmIEnD5Mo1DuD2Jml515Zu7L3lIRUR%2FUXf9hmkWQsyLoRmmaUqVEC4inhGhW5uwt7LmG%2Fphi2oAecH3MbMBoRQqVGxbdbKq7k%2Bvw3kRm7nUn1%2BM36y57tIcX9GgagNC2rQTExmToR3AEx0pfJ%2FB%2BAQuN73KKUyPcaSWr%2FaUdKP%2FlNRbBJPd2%2B&X-Amz-Signature=04930df7a0b6465f4b3b58b29dadfd9c46d075d70182e1c2be6cc338c6b6a9b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

