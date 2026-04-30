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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=daac68fa2ed4879126536465497cf5d675efd56b38e31c2424f6e91110c94dcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=2d3ea4c2be9d5d49e02aa343553326a14d5dc01fa231d4c0ee0372a2139494af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=47c822e8e2a55a5ff5f2f35501ca45c91b0045d3597984264e87aed580d28b07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=d9fc5b9f2698672914e50774b541bb6da7c7462c73ed8174ffe39195c817bcf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=ab0312b8e9ff6be48d6eec33d9447b2a8fe55cadb8f0342fe45f813e7557c14f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=dfbab90f1ac217b864b953e9293e48538209bea1a5160cb278c877a970b0fbe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU6SMAXT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDsL6Z70ii%2BDVVDfhqpNygTdkjy6qBFNsC9birnpbm0KgIhAPQM4fCGMKclUQuCOTOIqt%2BMpqUmoTHn3x5bUuF%2BYxCJKv8DCAkQABoMNjM3NDIzMTgzODA1Igy9pWYWCVT5g0vzcc4q3APVkjgQSLCprBKL0vHpjpCvV9i%2Fvi8CIw8mJd%2BX36lscGTp0tTT6uGgmsw3onrHaeV1qOUk6YSdAQTs3wAqxd4w2CeEFwhNf5R%2FgL2NmqzsjSo3fOcTkA%2B%2FM6oC7HzsKXSEScgTAA3xA9lnGX4Y%2FKUSVcWTyWu%2F8r3LRNwWCuPgxQmg6Nn0S8JUG8WMOS%2BPEhTXI%2BEIhQ%2F%2BuYBRLvY1iIbnpqAX1to8vmytPtipJmIOnX2ejeha5SMmW%2FkVwJDnO1D9zUGJpNfY2FZg7EvOEpr2xqaozfPapweRPzuOoHsWHGX5IjMnshciVQY%2FsyKgGK1lBgYEBHERQv4NumXzIqyfvZf0FbS7wS8uDU%2BbX3mL%2Bg6sX%2BBqDgcLtKkctlwjMMhVpQYuIGhJMZZ7FEeeyIzFBXIBoON256mR%2BMmLPdgNw5gNHbtfWHhJIEq7htZ9ySnmyu6oq%2BES6EZtSlbIKJrSQoubueq0YaaZxM20kCA4ZWJ8pkaN2wNaodplCzB2H6Y7%2BM%2FXBEzViiHsF3PBAb10%2B%2BJ2gHjZ3q3hhS6I%2FD2Pu9X7I17%2FO9LsDg8ft4aSho9hCqG4BwH3toO6dUT1qPaUzLOSd5sCGMCyRPZt5rwNOhvicLhQXsSpcdDNaDC1m8zPBjqkAU0HMO%2B1fGYEjm6zDWlcf8GxHVTI%2Bl0YbhtHGWs6FHJyGBa%2B37gqkYkPJ2BILq5TkLLTKEttdBWIYjd%2F7CB7W6qnDmfTSXM7pwNpT0%2FFX4QAPx%2FlJtw1JOXuv3FSrzVBtVwoJ1FQ2zqJ4iHASflErDE5RPhsfQEN%2BkFMDwmkw7RO%2BfyTSKT5c4VPBGZ53aVtKyhgznu7hR2RjKJxOwgmgqcR7Ebe&X-Amz-Signature=96acbdd0f8b82c3a535874a1aba6cf230613bb6d41184166d72bf556c1d36ca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

