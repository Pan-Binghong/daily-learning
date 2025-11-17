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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=a2a744e9b9e85c4f9e5f36619a3b89ca4fc4458c30a5c183afe8f7d7d4465f99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=936a84f62b56aaf9e240d866503b9c0214141af7f87ee53b5d22e2a5754c372b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=3c306b90e9a6633f12e0e55e91f2990b8a7c6af964ba5fadd8f28fc0f9c58016&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=691f749f7a64d9a94624d462e5e18790a68ee166d31eefaeda270f2ad8ea576a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=d271f15f28866cb1324d21a6507c91dba2a6bb5d1d5115cc3dc201998f7f9318&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=911dd7ba30e715cb3aa925c7b6c98b8259dc7b7d890f20f646e7f4e3318cb1df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SY2QYPBJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2B%2BzTZPDIcbNFawClmmG9%2BtlLlDyX1ImR7aFF6STad6AiEAngHbU%2F9wB%2FV0n3z%2FtWW4g6OzcCeO%2BzsSLwBB6FOIsYsqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE1AnSNN7n3I4S2kESrcAxZoBX%2FC%2BKoLyDdgAbbbPnPAag3%2FbrxMYVTBoVvfHYPBHQCT8ts8HwMXOb1tKjIzhM%2BWir05gUVSvYD38UKc0lcKX7WnN%2FEg8WYsSDUAhWyEMAx%2FHL9%2Bg2XZ1UZ9yu57k8ndqRnSnEq1I54Uo%2B0CdEzL9%2BivOQmA9xzM%2FAQmWnKH%2Fq2Oa%2FZPhIj%2FNWxKJOr3Ss8c5fjUqTT1CmwI6ooUU4rqCa8P9zSV3qf9XhTFRHc9LngMz2Gfhs73cuyA6G%2BSfWAM%2Fxlzi2Vn3GvbUrK88hlGigEy5x%2F36QAX%2BC9i1YraCCCFA2wPyCWwssC2DiAW1jebX%2B3z6bZfmjRFqTI%2FEr%2F0Db1n4A1%2FcpJZt98l5YA7V82aSd3MbKOeaX34%2BBLDZsG9KbYgQP06x1wNAWUcNTmoiMpl7hZ68KdKoSxSGL23JJDdUj61aPBWi1q7WNa9fCdlfGMOPe4DZ%2BxXkqoEN4zIx1nU%2BSryRmq2Qen5DgmDqNqDBiWcHXOneuDE9kBMdYq0QsnoF7rD7NudrXj1rZ1r3h1LLdOLJyu%2FCZhWy3zo2eBvnR8t%2Fv%2F1OGVGtGltKbzUSE15Kd1rbEVr%2BuS3tzHSre0b6vrRzuAH%2Ft8o9UC8mFmVvv2DQ5bpbNkGMP%2BG6sgGOqUBBqUsYZh6LZcgi9PJFIUhms%2FVgJY95Pb8E0C%2BSCyX1ZrXt7c8s1g8LXTFhBBZkDev1xZqNNMdV1%2Bot0xLpDLQKDv5iYH7uxItcVKdN%2Br9xNjLfPgkE8862OqNWg67CgYwhvXJakObkFhoEmazJtr30O32XKFoRRCPODAlN%2F7%2BQLPnphVUSF6LuSwJSyvF5z6IEVWW15ulDrmVN6I9TrcUSE0itAWV&X-Amz-Signature=1a25eea2b0a1adb970310ca27fd3d7c258c7217426493c6f33f2776c94b6a71e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

