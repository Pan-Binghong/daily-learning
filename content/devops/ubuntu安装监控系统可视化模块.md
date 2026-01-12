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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=8d4be18662f707843dd0798998f991c50417595191878acac6983bb9164c5937&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=1cb1893e2abdf59814c5529fcd825b816c1f064692b938d77f9b19583b816478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=6a6cd258c8d400b50b4577fcc8ab91d0e5e48da9e2ef93ea3f687f0e2e6a04c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=fa2833dbf631761fa327ebe7a5cf1ec0285b9fc929d215b7d827edd32928d8a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=197021a6010c28acb9ab7063a32ad1d11f5340b766877a05dc13d16767bd1fdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=3ad284bae596c723efda9ab09765404d482d2f5bcf3c84581e6db71688865766&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3BYDXT%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQD7kCun%2BGjHNMId5F44PlqQVVqxJadRchDE%2BLVXRIGp6QIgfhyffBzC7AJoVwFgnqb9qOkcyxKMmhABqp295Gna6nEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiCpw7tAsi6jtFlxCrcA%2Fql8w0M9y8h66LEk57fHVsN5Z3ko28zqMCAAkYKH0P8fKbm7kMpIyij0z3sby%2FeLCuy55BMfmCYSOoC9cr2vG8sf3Rk3XdZ4bYACVKyuDcsjhKmJjgUmjoj3ZS4ZGaXCeDexsB86egA7A5D6urdpbke2ubfp9ca83P1w8F8Zt1awsj7Q9jbklxpJTCJAT0WVrSJJJBjaKjeSQo5boAD5fRjD1BJzvNobDQta83CA5xQL7kD38CDsyV%2BlhOVPyIYKUMmT284CsZ4L%2FnXPo8NgE0lEwwH%2Bws8Th1eYXlPdJ5%2Fg6QlggsawCV2X5EWCFaPyE4Rmk7%2BaGCkDhBOnR32O%2BHpYk8c%2FSfAuAE3Iw%2Bp4%2BagfgNr1GvHXIcrCZpaZHju8DJ7zNCXqwhIYjNm7hiI%2FXORqc%2FgAa%2Bplz%2F7bShJ%2BIOXdhNnUPfND8slteJsCd%2F%2BuA8hQtzRO5%2BisNnbcjjKi5rM%2FsQFpU8qk3NHdwlZSRWncpT5NBdRUSDpv4zkuRKJcpkep5O4LHPYvAbaX9RJ62BkYG%2BYQdCeS6fXvB1j62EDWxKd1O24wPn7jrV36A1InZq0XJ%2BygmrkdBUTRYoo%2FeROoq1VSKimtCcq1U4VMVlZciwUfpMIYywu9hqMMLj3kMsGOqUBiYYXJ2yA3OSWdtoPW3RhcUXwP0v%2BAgpLlLJEhis92Fhxcsap%2BB2q6vvbJ%2BF%2BsCK19sssAeA%2BiDLgERCtdxk5EA9qkNn3jV32wPmalkzLJz3Fgt%2FsTd7miNKwIw9qSb33MJkH5Fm%2FD5anjNdkoG4KFpVWC1oQP%2BlRImtvWiYuEfAAluXfvH31VQMt1yrlVcEpxpz4BZfcDSYtMLSTkfHvm16jXW49&X-Amz-Signature=dc68664b4f37cb7a836ec8cac5f7c3ea2bfbdfdd180986a4b0102b6addfb231b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

