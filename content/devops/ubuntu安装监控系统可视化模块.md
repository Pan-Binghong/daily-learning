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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=d9b5bd069fb9fc5fbe306da7cfae1a67d06b9ef32a02f71dc7932c66a105164b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=7cfde76912f88637ee6a5fb19b3a088142166b84a59e8aff9d8a3bc185c2f0b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=97ce556b3022171b0800aad8b010ae3b098bd0ec6a5a700f7ed975d5df05961d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=927f9ee8b571c660fb4f5c8544b067ec69970fdffef2bfb3234b375b0bc73e13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=133b401a3a78dfcbd0c22ea6de4b34c19d5600b44cbc00d31c3fc8230761b8ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=e964aecfcdf38dd16035f63387f4974c724b569fd9c2bd3323f97f11018db5d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBCEZK6%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDprG%2FCk5L9tJANUPnuiPTMahAuYiCE5KmaQRapyaEsAAiB9rbQjXV5QiiSmrl2JwXtdYthMV4F91Ha%2B99NFnPUDoCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMip9EDBXqhiDbqkCMKtwD7BjBmWs32eDqyDMHJJac9ppvzyj8I%2FWcQsKY2tkXaAjI9fz2Wdpvp6S%2B9iQVV7AYHTSEJSbXy3gjDoaZfA03K0yl%2BsWK1kbZ%2FMMTvnVXFkJhHLlf8p2%2FTmmj4s8pOhoxCbROVtNqy4KNp2f6k%2BqL6CCMqMYhmIxayUIfyk2eT0H5dWZxGhOt2UKgFC2azZm2m9tFqzZGTUyisNb%2B8%2FRVcVUB4ltbys%2FVeAgsbYinbSBN4iumV%2F322DTCdX%2B1p3ZcTy8yEKkWzhdGTUASI3t6XEspytVZi2%2FuKuPUmcMH7fn47vla%2F8EY%2BN3CSoKrpejHrzEVV60f3N2h12Jppe21jWLkQuDKNb1hBHsoWh79R00whzvRWq3cGI2y0c1j5vSmyhrwbwLSHdRiGdwRUFEZxnWRJ7UpzN7slQRhffp060VxOF069EaUxULTUT%2F2z2R%2F%2F%2FP%2FizX4Rd%2BsOedUzgZZcZRQtxaeUDYlwkmtNrq0FsEiEbQ8kmtL101edz4x4dHcWlgbkXpyxwu6Mo48kTiRqFMoK5EW6k%2F6izrq3vW4mgE%2BF2xeOESGgekKcyNyOdsuTWZ1Z4NLtaNSq0KkA29UW8XwYmpIwGA264QobxxqJpMshLao8FpkCNTHZKYwjc%2B3ygY6pgFuU0o5eJ8PQ6Ngt4XM0BmqAnzc9cr%2FauQb04sZt8Zp%2BkLMV27We4F3Hc4%2BhL8pGllym6QKD8wqZjJTYukNlYAqXzI%2BIl4%2FIQcVQjNQJ9imwZE2JYYwERYd1U430lENG4M3tjXiN96Ri9LiUHwKTzn2EKJGK3qmz2oQhFtQ5t%2BkQr7MuL6qhXiW5r8RufIISsZ%2BcEytS3XUpRB8MncE1%2BBmxg1UB9vN&X-Amz-Signature=b79d33c4af03ff972cfa9df49140eb7972aaf6517e410278e3ea819cadb96b81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

