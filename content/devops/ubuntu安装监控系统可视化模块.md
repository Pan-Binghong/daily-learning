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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=7a271c59531955ecddca078d33a118768c487f6a42033d3f3cbaf8aaa7e75022&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=a503d9b5e02327badfb0a849b8acdc8dd2389b1acd331e80dddf451f5140eb8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=c78702be9d4c30f8c94ed83da57d043b1bee89e227786a3438bada3229d02b8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=54af84368a0af41479f853a3464dc8d518be2246cc84a3552b009db25e755e88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=55a86a205f73ce53c4d85a9c05aed3d39bae929c638718b40683bb7ddaf5a7f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=aaf6066d3e27435ea5d6267dd7fc62d2aed8b1b3321b750c168e653281fc70d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBEK27EY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCGsC6JPle0Y03%2BZxzMxKW2u8Q%2Bl8wCE2wBVywb%2BZ7iTwIhAInDAWRq1iyUf1ghlDcJSLWPWdCxdPY31JAqFB45eCHXKv8DCCIQABoMNjM3NDIzMTgzODA1IgyJAeTyOps%2BPfWa7jkq3AOc53UijbvAK88D6eUYvUkxD%2F9K7%2FGeKpJ8td4Tn%2FkZeko0%2BInuIJzaVp56z5BgJxIiU5s0Tc6vL1Pfc4S3wN4%2BsJmbsP7RkckQ%2BhS%2B3IL7hOuM3cDk6cPKg%2BAxLDAnqaDxZj%2FdN30WErixZ8itI3xlof81%2ByzV0DdNuyLtoEqch62PG%2FOLpCuuEy84FjXmUko24GX85LWr4Q4%2F8OMQwDIIClfW7VCZc%2Bzj%2FXFKPh4qE7TJr%2FvBO0%2Fz6OUdum1wAZ7tUB4rnwfnSmGdfquvEkWj3Bf79M3srhRfgQuII2lU5BmEL5xsX6WPlMhF1OmpCvPxEvtceHiC1yLvKxYw7YOfpMz1mKjbgOh2Pn78fiM4w8W%2Bjq8ij8SEfswRRn8zA3spqdKLPxQwNhMzcaB%2BPe99NVpdm6TUOGvvSOwS4y%2BHNZJEOgi1MAesS0agaCuf5Q1Z3UKdQVx1qc%2B7vfKfeObNGIYjD2DEeHu3xr0XNlV7RVGN0fzQ6bA82euwFBrScMgFsltHyse1RvPyeX%2BLuXXADXPzQsZlqIrzjxy5AGWFoLNf%2BlAOCcHznfxppJEscIcSIy%2FWuYoKQCZZGsJOyD0NRoROSdnR%2FfsQh0gmQ3huyzPmjInUBkaDCO292zDFlL7JBjqkAVovQ%2B3KyMCXZ8XlL97gRx3%2FBbsjrCtQtpVa5yFKGz8%2FCcDWxgtVHTNFr%2BBg54xhObe%2BggLKpBt4cGqUuRImF0CJbFiYBCQ0MydRXAuKXv7KsxwHNTZP5w0ab3IkLug%2F2KR3foxj98Pb1GYNVlw3T6s%2BLQinjVHhmKir2RFprnmHkC%2BLkoha%2F0TX%2BW2EZnC4nXUUlP%2BPVCE81mcTRFQE1a9Y1YcK&X-Amz-Signature=1f86d550744bff49bfe0cd56881eb9b45c5dd84dee21b3bc02e8ce958b5b6cac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

