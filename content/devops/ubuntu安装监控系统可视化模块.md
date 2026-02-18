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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=568d68e82cc7320b8a041fc1a3011b93d1cb57ffd966b6b7f75264fc35e79e80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=8f2b02a6682b383a596af67feef7284513f7563c94d35a6e941e506f867636af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=29a43fa6093f3dc50109dd51ae04cf5d20b2c1460dcf0fd0e80f99a51ade7d2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=b3ba79d8a1a1073d8fdaded21a3fe87d26946a4d3c6daf59e59f45c0a6d32a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=9244e4428c2e86506e7a53e0c62898026708ce90c50864ebe5c226a3da38988d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=a1636ae5da5c5bb139f19bb8172c92374ab3454b61ad707ec36f0bac2cf5e1c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDURDNU%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE72DatfOYEZ2MWjbjir5tb1F68OCVrv2E6MyzVaTvHTAiBM9XgafeMMuEG0%2BZkqO07ehjB8Sk1QqkJxbhkuxoE67Cr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMYNyLlmIoedvAM%2FecKtwDnB9lN1uyX8Cf9tKgMp83RtXRZ7xSXKtPg3u0g%2B3R0S2SExLtJjFwVYOG8TF7WYMRvsSRPkLcuLNodL1d4%2B9Us4FLAYjd%2F2pM5H%2FNb9Hv1SkiB4SSYYjUrfwB1VZRQAgcj7zgHHDZUYiD38fxemICO0KKKOK7gOZwJ%2FX1BopoodGzQg3H5OsYavn%2BwlkqXM8J4F3SgZxQx6HbAsaEzN%2BFVFsT%2F2kX6PKntYFPWR8qKPhaJ5VzFM9dG18utSt9Qg7tC1eZqTzpUI9cZjI9b4k%2BzWUegDzHcE23e8rj1jB9vAhGTdTFEvUOUwUesbqVwHh5kvphRocL9wPyd97V4Wu%2B%2B19Whsnk4Wm9H%2Fg6Fbssy%2FpFTtCsA2hTXcjII4v07iMDCTrjc5z4PEv8ZNxX%2Bmvxbv7AG2rE9TIgTEbEsyuYdBqmCSwaZXtzZKYRtzmtA2sAE2oWEEUxtWygjIc5Nly9qFhbuwFbiAqlhiti4Poa4dWgjtN%2BlXEt4Uqh%2BdpmOtX3RRwsUx7OdwTYbPpkn2rOLOq%2FnrTH18Cc3roYCxS3hkrx1fuwuO7SwPZiS%2Bkgoy49pB%2FmLPeplj96lW1YJVpfaO%2FqeQtGl0slv2tuufycVx4WQso%2B%2Fpa74qxClQYw%2B5%2FUzAY6pgGTvE6jh1Sl2t5urD0XfvN30Ol8xQ52MgbO1fGOd5yNBnQeBetpvJg0kgdr%2FkKi925J9lQ6Gh0OksFdbVg1yed7CQJeVFjdWEURVUztc%2FyBME3wqgqmkjuYWfzEazMxWn5PJjaH72RsORFGME62mew0y3gsDrPCIz7k3Iie7KTxAVqRCkwsaUN%2B4qWWXXMkLBZTjzGo9T3Z2k2ttVv0ZKwVvRZkVwfc&X-Amz-Signature=0a5dbd0c38184e4335a981221006f6eee2ec171540a495cd0264dd11a7b2af61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

