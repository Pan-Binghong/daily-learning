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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=ae851a02ec421b127fea910761182e6c612881349cc87a7664c410f02e80e693&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=b9955f89277a5cd92b84fe53cd2c5004c3ea70ba3148f318dd149b83439a0f3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=29084595c1e9a1612b6b45620e0da0b77d5b00c3e99ef8dfe06455ccbba8c53f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=3aeb92cdf59434532aa418abe13cb2ce03686518bc0e39e441e1219bf0e18f63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=12d8fa5a9ae7487e6f5f28ec1723f2c031fdea1994eff5e27def1462b6f0c7d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=7bb11b4fd315b09d988c258dd32e93a18bf80d612f86fc9aeceab1b45a4bd39e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBVTVCX%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDFS%2FC0OBNoq7X%2BZQont%2B8wnoqkJAb4j2aHbj6%2FPlILuQIgBMqVvurebS1J8lN8I26Xz4eF6urvxketX1jfD7cLPmgq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDIh97x5lgeX4LYXctSrcA0wN5CdzhEi9fA8vVR8bdWa%2Fl8%2BZ5pQsHaqXaOFlT09MDrKHjwY4TMzxErzfpCvla2m1IH8Ay%2FaGpj4EvsIMtZKoid3lmAnh5Aqg%2BsdcuwvMBq2Wy%2BVxR1fa4CJi0pklEnw7pGvIeyIV5g8Sze%2BAIrtvoXyn99h7%2FiOXu01Aolp67nlo2gsHeDWFYE2T%2F2ahcT9OidlA8j35yjNt275U8MZ8PlCfDzHJl48FUnU%2B3T%2BNwFPRbvA9O4zpOFtwug%2FpiXY8g1iNIxHopAPXwf4YehAaXWJ%2FvSYfZpAEAU%2FyN%2BgpbuvK%2FPRqLHhSmioUBSGZ%2FKtWM2RdElPUbsCW1YeySR8nGE1naRonDJ2HtK%2B8fqgvP8VEicpNFSluF5JOr4uqLIU8Hd2vd31Kkw8UwUoQ4BWMBJXEKCMNzGkhqmUjsPMKvIpmx1qs3%2BKYgpnA9z8femE0sbVebOB%2BzilKX5TnbHeSs47%2BzowXhDSbw7BpbxGMTfZmw4g3JU%2B5a2e5SqzYR1MM1qtBuivPz6Dm3lyttvNEDBllKyAxyVdtzlXIdxNtq9b46vEITBJqiu5r4rIAW5f2jftNuiBoTj4AbBJ0oqcKZ%2BCGMI5dZT8d%2BuCDjrRVsJh7OXTyETY4ib%2FyMJeE%2BcwGOqUB%2F5qpm7lCMyTse%2Bpjx1jcPdeknJVHsK5fBr0WOtEzNSxCg%2FlLta0tGnIet2lFZT%2FdVTFodF42Qkr8%2FfqN6uR2KFyLPK6c2FDqDvZSBMDbvjuWKNG%2FxJHD4dbFAvQoTg%2BE1ffdWXsqTnNOv%2BjmuXrWHVjhT6%2FndNDrdeBfGnDO%2F2mM4G4dMB1y1I0rwBfndkW3Df2nZRahTrX9P15lmYOsVHraUskA&X-Amz-Signature=596940222e8518968227e4249aacdfd87c9ffc2f7e98aa07cfb0dff64657567f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

