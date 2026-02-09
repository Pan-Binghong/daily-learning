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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=00a6affe8babca6281b2ddda39a3d1289c69e252f9b8dd737e47cde280cc008c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=bf6676989983e915969f6fe95b93872fc95277e9399452969c394a397c1cfdac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=e4ea759115324bb9eb42c2dee89db6aa8d252aa285db71c0b94a2e1689b8e3a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=48a7f86adc9fd82e7a1f3f6aa889528d17ed6138563943084c6547162779d5a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=60f6fa9e11a1408b7ab88e2f56354610cac70819f40e9f7194a8a1b9146278f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=67fadc6178166b34f453309b695889357284e6592ebf8f020af98c73f8e6501a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHXDD2US%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuCUhY2TH%2FcTnCMZLM3cBSljenTyV9DQZFudl2OUhq3QIgAfd5sdP%2BmPsT%2F4uwVWXeeBUldXS7yKRAXM3WR%2B8QIksqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJca%2BK%2Bebj7S14ILBCrcA84Z4jJa1COy4rO1xSm%2Fyu9%2BRBdnjp6t8v01ImnvY9qG9qWOo4mBWUFBQ7etkUkt3YnSSEZpbi88dKUt1oJxUST9qtDrzXi2VCS4Q1iRcvCpGp7qrR44tQqB1mN9WrxYtrvyr3e%2BCXeQ3Uu0acyK2pY573NtTl%2FsEEG87TUWTihYufmMHq09hvmYFQQa2QA9vCRQ4lFyvqpef10eD7zohPheFkYW5doum8UAZD43YU9djlRM%2BKjdwd1jIjWHUueA%2FGD4gWsWBVpwUR6bqQf1R%2BpSMtyeTiB6xjYP3cUnb4UrmWjue90KFmAcdLsBby%2FtZiodJGhg7%2FM39%2FmvbNFRp8f1pqIdr8Ii%2F5Zbap%2FNoNLcBFM4Z9dU4JMGwKT2pjideJCbTwUczQs7eEh5MYPRZFka%2FGPQlW7BVn1%2BZx7Igb%2Be%2BKwlOtvXurftRRpG7k0bzqG7PAdnNXpxWpN7wiExJwUHZk50A560ievAnpO3EhipYuAXlTIUfC4CQAxhJ7f%2Fbvcy23D03JmIvwb2MXJqC0GeDWylqmACC0m982p0HJ%2Biy%2BviZjX80eADeezFtvZc793ZY7%2F7hjvQ212lEUI0nkYOajDsa8QjKJFvWb02O8IF4NSdMnwg%2BCYFF5%2BeMKeXpcwGOqUBTA4GsqdOJ5HFNZVquYvHBpvGyJeP3%2BCkhMDAO6Ytpob6Oe5pRwadFBlh2DMzo%2BRDeih%2BC0iGyuvbGheNO7mGpvgaD5EbPvcujmpj0A31WBceLwst85nBgJj%2Bu9NotQ9QMNDJ0HPW4KgqL9DaIdrmIdTTO6CwIBm6jov3RaOxLTsR2PqvaIVsZj%2FyGLEgdCYeSsJyVkGUPk0BD3ygbTiLeYX8VygR&X-Amz-Signature=fb43f1e5d8b141a75740a0c8c0f5ff3d0b6d25ca8df8406d5b4b1cdc64a9c523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

