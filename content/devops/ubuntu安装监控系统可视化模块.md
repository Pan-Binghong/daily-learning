---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
tags:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=c9f2e7858aae749af1e86b62c7c44a37e66d335da939bdc0c106f84311c3ea15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> Prometheus是什么？

### 下载Prometheus

- 下载链接
### 安装Prometheus

- 解压
### 修改Prometheus配置

- 进入文件目标, 并修改配置
- 将以下内容放置在配置文件内
- 启动服务
### 在web浏览器查看

- localhost:9090
---

> Monitoring Linux host metrics with the Node Exporter

### 下载Node Exporter

- 下载地址
### 安装 & RUN

```shell
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```

### 在web浏览器查看

- http://localhost:9100/
---

> What is Grafana

### 安装Grafana

### Ubuntu安装流程

```shell
# 更新apt-getsudo apt-get install -y adduser libfontconfig1 musl
# 下载软件wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.0.0_amd64.deb
# 安装sudo dpkg -i grafana-enterprise_10.0.0_amd64.deb
```

- 操作系统不是Ubuntu则查看上面的链接, 根据自身系统进行安装
### RUN Grafana

- 运行Grafana可视化服务
```shell
sudo /bin/systemctl start grafana-server
```

### 在web浏览器查看

- http://localhost:3000/
- 设置流程如下:
step-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=d06b5d26bd1fe60e130bd6850875fc0eeb4ef4e5168b5efb8205f4db5e28683e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=3e41746d57ab07f5c45d18b20ebe03383f1c385d184e89577b78f33a2fb64a4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=c955ff7ee3037032a8825f1dd67170a30ab6c7b4f91da8e698c873d7eed28374&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=3ce9cfeede4edca5552baef528b46cafcf49d01da2b4546c767fec337bb73656&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=87d6846e3573242fbf3744ab8b25cdbf8c234314a4db7b4713931a784eb481de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6IZTQ3H%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCn9JP%2BznEouEYfTXggtdQ0p%2Fk%2FdbuK56qQx5U0El%2BYXgIhALQSGkqnut2ylrF%2FCW8SamQfN%2FNJZm5BNQvrZvTzKJ5IKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgy8gnoJ96iqRbReoq3APhGaTUSwKzXuAqB2XOfLj1czdEY3rbAsfc1NsAEmaL%2BGu7KK7M%2FG3D1nrvpVXQDy01ZfUzwe1qdBIBYnMOI7N1xJiIjk6JMlmN9Pcj0QKVP5m%2BISQi1xJVtQccricD6dO5FfjxXHt2Vkl2k557Zd6qFfWyuZZMdgV5srZonESlpUVBa1KzP1%2BVFJd1QcePDmiYqwGHzRn%2Fmal6%2F6zuaKwD8cT6OyEG1kSn4rfoUbFUDJKODOigDIk2ogSjRfV7pMV68VhgiAOPSzIdLuTA40rDkHnntYXlQxLBeoX0Mcn6B2ke4O4arDxE8KbkgAwxCU1fPRSHH%2FUoyhW06TOC3pB6MTvxh4n6UNUlnaPqLWsrMSyLnMXHhXBGz91%2FGaZfC7g6vcorOSZeJAeHxAtBwB4GiPNsFi%2FVHtmRekbgS7HGo3Dc14Q5Nf%2FY%2BvJ50vMuEeG8rbKKEL%2BFDpYcYwcTKbJYG3T7t0dMA%2BprGxLnCFjoJZdIzyNSTVYQh0OGr%2F%2B3WdBQk%2BCEKkUfiJEJymD%2F7YfdgBJaeMe52ajJiHuviEnx224TwLU%2BUaiAIEGaLqX%2FjdhWrA1AFZ%2FUntsQQHNvZqKgouekcvNCU4wAUTEiRm0v%2BAQXZaGmst567sL1BjDlgdPNBjqkAagzn2RirrizjamDjZSKJusaDF8VfqBAe2Dpy89M5d7FsM6TPW5MoWHduIOZjOJuSXpRy3Gm64gyvLHAB%2BQOFzz%2Fx26m%2FLUff2r%2F8w6v8l06jR6bIGDi4Tzr9pMl3eIyU%2B6RO4gmfpRdi9v5gIWXxdFOdaHvXVFEHwDGYbusy2pYotwY6Jlu5TaxwAgzrRxEvSLcgcjffWHZmhQXji%2B4OEs7Y%2BY5&X-Amz-Signature=4afeba853c5c30e1e882f2ad351b0376acee73278533f9907b5013dcb6738e5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 参考链接

### 拓展代码

- 安装Prometheus
```shell
# 下载export VERSION=2.13.0
curl -LO  https://github.com/prometheus/prometheus/releases/download/v$VERSION/prometheus-$VERSION.darwin-amd64.tar.gz
# 解压tar -xzf prometheus-${VERSION}.darwin-amd64.tar.gz
cd prometheus-${VERSION}.darwin-amd64
# 配置promethes.ymlvim promethes.yml
# 运行./prometheus
```

- 安装Node Exporter
```shell
# 下载curl -OL https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
# 解压tar -xzf node_exporter-0.17.0.linux-amd64.tar.gz
# 将 node_exporter 工具安装到系统中，使其可以被全局访问和使用。cd node_exporter-0.17.0.linux-amd64/
mv node_exporter /usr/local/bin/
# 运行service node_exporter start
```

