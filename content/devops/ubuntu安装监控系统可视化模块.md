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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=ba816c416192c3109f8fbdb3bf3f40c8ba1d87f78a89ced8dc44153434ab7123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=40fb522ffe4ea1d9890b00e4611a99b2de4c52ea1e993dbe3d7c707a3ff00d67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=0461be36f773921fc909a16211b94f85da1a087669b012975c6d2cfad10e3b19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=a5c85dea163a9b56c5b77c99857c4bd64c06a2fa5d91d17b592c067225259d44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=1e1bd5dc07ae47f2b23039febe02719dab2e5ede4e5708734ca395f38b2484d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=fd3cf29acf5e09aa4db8276ed909ad085e53e8de90af6c904eda9c34d2f9afc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SR55U3L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDroNaadugM8tsQ7TbWAlvc3FBHBZYkb2xMt8GVK8TKmAiAJyvuYx5WRdERztTkVaCmHMz3AXfyY7eFFfUCuFWY4%2FiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9wRcItQx%2FkllYu0uKtwD%2FTgQU6EQuguXvbmsnBKQ4PR%2F3FHUlRc%2BxaRd%2BdvipyWpuIfXjGB5U%2Bq60aWl0u0ylv5pVeNs0FAlefKed8VhamLhzttBhXK5pLOta1CvOf7ZcSGKLV90%2Fq0YNDfjjMBY6tB0ggh%2BrpHrykTSwbMzGGemF6K6c8I8qeXKM%2FP1KLzwWN%2Bq%2BaE6RHms3xWSidlUuec0FfTmIvYag79hb6GIMhXOLcaFK2n50rQY%2By7GFfBhDYLi%2Bk5bqIFX%2B64hol41iWYXh2HDmJBpamjE9zuzt1cKnBzijslNgxqg2SaQD0DFz3N8jUlDniwpSJmLLKHisONg%2BGL67NuGG%2FwZ31c4OcGqePdv8dFo%2FoC45izJVPLsVz91B7Msbq9s5tcNfUHvbM4PhPjj08mUWL80%2BZHPjpwF1M3Ct2fjVPcpYjGccnZ93blPKz9FQlWxBPGS0SJnhSr17PIce8HSs6BB1PsT3mPceyTsNj1v%2FaLNnGwy0AZsrh%2FgvlsBQQyS%2BhK948wn9axfagAWv8s8zsLiAMvdbzaj4ILuR3UddccoJXNW5dByhFYGjUy%2F1FLgvmomo7dUNCkgNlSwWyRVXYLPdg%2BHlq47uIF847kDYfRjT8vbuupV%2FmuuQXS0e%2BIrTuAwy%2FGvyAY6pgGR8aJGBQKeM14l9lipbhmCEWiExhkS5MW3ynDXUGsXjI2XDJRcOQYEr404uyn1%2BTfWLyd9hfNOqh4GQevvVvQnMCJZ3HJCan2eu9XzUkRk9shPC5pxKDTC34tuLIYbExsTzdK5Ofo1gprgdduvnPg5sFFLIsKTla0j8rgXVzQQAtdZa8rWWlC5DAvo%2FcTPO5CVDTmFraOJGTQUY%2FBAelmVCB6pECgZ&X-Amz-Signature=beeee9e8766f76186c2328d9fc8dfc55733f75c1ec01ce84fcd05f10d300bdb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

