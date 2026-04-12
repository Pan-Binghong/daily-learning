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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=7b09a56094591b0f1a49cca0e7a59ab0e38f302bf3f7dfd681a5b8dadee1bab5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=9e075bc4e01dbf5802179cd11aa06aa73ee573c616a1734c2926930180e909ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=e1c009200b5473a9edfc42dc170cfb825c0866adfa0de53bc15b79103479a8a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=25caffce4d48e679b0884ffffc7534baf6fb28f795b6ee7d9123e2b9eecd8061&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=93a25682eb8dbc0f3128fecdf3c6dbfa32ec34338ac42933ddd46b1e894797e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=08ad7a3a3fa772b41e934f65b63aa1099729c2d5ef0160ee0ef5fb3be7dfe1d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDE7MRRB%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8A8ORXhQ7iTq4yU0E2WGoBKVWyKd0eDS3PT9E%2BQzZVwIgR9Kop243hFTgRgyHpjFSPx0PmgBH%2FKUOQBCvtLbl%2Btgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDNp%2FqL8TEfXDxBj1dyrcA87at9rJp38ZcX44YqzWcTUq%2B6lqXqKYx98EdzJHv4NwoOiTMldERT5M61XHPhCzNJS5UG5P0kaf1IjRF26%2BhqPwxQCso%2FhWTvQ8stSUb2LQssP3eA%2FTrIhKVHz5I8HVf6RZ9L%2BnkXYdYAJvxoMdPQmQV04xV%2FTZjDuK53YYN45JkKB%2FazQ224NCQv3c%2FGRLPr8%2BDQqNqqJ2lRyL3wSK%2FG7IlhfP2Y58ltVLIm3V8hOqdnA8WF7meXOvmU4AWeZC5G%2F6NQW3mkPOtopCBkWCUYk4YA%2FtkoS2rXc0tZiKTDgf7iPAH%2B7ZOQAMVQpGQ8YVz%2Bol6aAbd1eFbi7ZgqXrgBps7DhtZkNzQvkvzJH12Ev0h0tgajKCKgEyvkcGSMtUvUdaMPXMPuvQJq7gK4eKmJ5hXQi8x9ZIqemESiDdzbxLvTLZw%2Bs%2Fn4AP1FKwhw7B%2F5XjkWEFKslo%2FQot8NtV5QSPCiMov43T1cxzhLe096VY8AhqH%2BHjcqt9GX%2Fpdrh1StOISW1LHA9WMh%2Fqx2zhK8MwOVXKOTQOwBJuhrFQmCNqcudV5L9rr%2ByWVy9iGHAdrHi1RgngKn2PqAGHyRlVTa62aN2%2Byq41B6LsBiMd1gUGgocufIUZj7H1pQiIMNKH7M4GOqUBZ8O30v5B80%2FJymScvY%2F6nFnQIV0GgykTibFEd1L5ZYMHlpr789%2BEodMzCspKJmWMj%2BTQb14cj3DOL59J7tS%2BzA29o%2B1t%2BJm8Qc1bCGu3EudF9t%2BONjU8E0cBB6DXOPs8tFb%2Blv2uJgpql4oF90l0J%2FKpQP75kvxmcGczBc5yyeVzwZs5qgisfr6jvRQobB7xK5KTEeA2KNWKcJNxFiXrFHoQytFc&X-Amz-Signature=9f00e2040d2babaa705cbb3d1e901ca9f97a5c39b5021de647ee201d7b44ee04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

