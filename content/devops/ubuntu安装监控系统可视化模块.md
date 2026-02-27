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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=cc0159f627d4d63f5a1c1b94a34ab85c64af494d24a57ecc08f19706ae668750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=321701a33a9b513a5414c0fe239b097d11e9c85a36b2447e7a5a4cd1dedcd830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=3758e4da809d5ff97c1a67ef9d02d0d92122068e7bc4a67c02a34c4b984c2366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=c484a0180dad173a25268c7f5d4ffc370e1a742d7bf0403430410ab4a9ac0692&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=f8bd3d549122ba9a435c470e0319288162a7b6effdcc7dcba3652b95d802fe13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=39b95197aa1f83564d8f9594732108d41654de02083f35556348196419a838ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GUZKNV4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCYqOZrnVFeXTMEdNcStxcjGo%2Bb8WTqN4DeBcWc34IFQwIhAIL6YBac9WTEDxydJ987qlUT5NflhIfJY%2FGkC%2FJs9CfNKv8DCDQQABoMNjM3NDIzMTgzODA1Igygf6BRq%2F4q9ct8IgMq3AMoveTzdNJ8r40qlwmff%2F0ZZw2%2FEOk4SGZpUsO%2FPlIQq1UCNI81PLFRUnm%2BJt676L0BsHZM2Q2BuARYABCAGqfctSA8e6KT6%2Bi45Wslm5eT8oLqDJBM5PvOG5xgDLtu53zYnRuTAPJ5vy%2FcuE4xquHBixOnb6UobgY%2BqICOwx42juqp9KRRVIgL2WbyucuhYPVEBJHjusX6XCI%2BD7uQJnAmsckZSYo9oR1%2F8RHkkedhxLz2ytdgJdLwwfmaQa66GaTyKTDS4XH3m3ANfNJbsNTA5rgklHgIXbiqZ%2FQBQDaTd3Z7lq7UUsJ%2BwNes1wA9tNB%2FVOxvmBUGPfjZCBn5QG%2BwAWYvaDDgagQ0gY9yXfhLZllBCKMapMGKE%2BtMaixC25Wwt8dVUkqySi6S%2FMLsIKDrN4C3oPd1rtpL20a%2Bgc%2BlfhesRzkuXYENCzYPVft3F%2Fyf%2FcauCr6MRBlwt9AdEqmMeyB7cA4ThpqI%2FKf4PSzNjW4ONvYhJ3Wr606bPPt99AAecVzHxy%2BRUkC7ga4jCc%2F9PNWsFqWXWQiLqexdrP4H%2BgDJNs7%2FcTnsHZzF%2BA9RMJr8UKOMvCtMxVlydREjDZebQ%2FhtI0s3W8VEAC2JQzMGSAyjr8wDg0T7d3dKdzDihoTNBjqkAZMySnVSB50wT3%2F%2FdVa440zQzHtKpA0W1FnBR29Dy9QeopIFJpKOXql0vJMLHJ9rsQwzJJJyxJO3YV%2Bge2CYW5VDzJkwkpgdCs5AJs1swusd10T2Z8k%2Fpw%2B01tcXI95npTs2HZYhNJPCQV5%2FHLhbqtlheKszQ9PD59lbVOR2mximqlljkBb8EtN9ZcUTv3HR2%2FI7YIaGtFbLiFncux4tWvd5MehF&X-Amz-Signature=79108b0a96e69592db6d3e8fa89e25a47d778508844a36047bdc7de35ffb7a14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

