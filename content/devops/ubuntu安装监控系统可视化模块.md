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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=6232d754287710f57d49561335125dbf5af0b048a1b55cb213014235373aed0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=62a84c5e3061b36c6a384663af6a9632c59babfe8944723c0850fb29f443171d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=9ba77174c2e2011ba9d1d21f26e488dbe06f8fddb18b6a029fde796be2647d84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=cab1ed53d12ca6873123cf2c8fb0a7ccce97fce4214a956638c1e3b6793f3f73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=0f6c3b9df991bf16edeee5be2ab82fefded1339a0dcb0294e60d8908d60506cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=b491bb6c62e8b9138349481acecde0b702402df07078dfbb114385659a8d677b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC4W7KSF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCMxrQoGacws4rAQ3n3l%2BjYwJ78YRXL8yfUP7xBwRA7lgIhAInusxnRse10rF6d%2ByGhrjFEi2%2BNwtf%2BWPLq3YO%2BlGhRKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjHRHVCyHYlKi970Mq3APkoXBszbjhB9uECGBgbdjpSRbu7hc2iPmBRw3I%2BMT7wleFzmOXq3D08CmLgWfpfvpbmTI%2BwbHkWfT7k33bCSD3gYxOZqF5HIWsRyMv9Cov%2FDRsf%2FnJ8qzDeNTIW6v%2F2gXQgkAl6sTPx43kdLRkjlmMbc1eI0bqbE8Ras33onICHrabH5%2B5MQ80DkC9ieQ%2FUcfE7rhpCPVLbFLJPYblwc78x7TBW4%2FBBxYzfUcF1D%2BLl5cOW%2FB0YFOUgjq048uaZlLujJQTrh4JkL%2FOQ5eH119fWuRFQVkp6Q9xIdPFs%2BUvhvT%2BTipPvZ6bf1hqbPgjNhQMRveJYwwmFI9l%2BeYAbiRSfWWeYARo9ue3qukhHXR2i73TDWvX%2F94ulVa591kMxqJgmctNY7kDm2iGLzG8ik4Maf1xt4N1ybhyDwl2cHGKIhMS7%2BgTa%2F3H0baav1dmZX2CMxrVCX9BJtLqamaiRhezcpOylvZpG2bmDJKMbPCW%2B1OIB3oR8Tb%2Fahc95zV9uPHkEkaMrloIKLe7BEoj4FGn34c0ZoJXcvx5Q4MXCZALfwPTVMIPgjFmzc0KMvaB2iHfWKOROUJ%2FB6JX%2FIE6p4cNz9jgi4%2Frt9xwIQWqkyVUdyxsgDllIFxDWjctEzCk1K3JBjqkATVuNCFTd8DEMmNHAanEXyxlvxb%2F%2Fg64SWgCOvdzcNgZQUqCZMfsUNH5rKQeHO6Dd6IQhPiMcW8XKAGsC8xng1rv3y%2FDNpSxkmOW8etvxmLVp2eI85VXQJyFiddgyhO%2F4zJF6szoiFIowWwTk5bX5sReUuJ8IuB37%2FnjqWzC1hXzahQ6rGm4OvX4j3l3Z2t66zl02DfDG9bE9ZpRbmaQek1C%2BZ4V&X-Amz-Signature=37b4a15f36485aabc8cacfecfffd4746394ce2e18c0f3d2b2dd836762172df4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

