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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=dd102b05bf69ebf71d34efa21c93bbf06d4edc9297a2f1f1387cbf2b453d3d0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=6203cb67b9364cd558503af94fb2c07949ef66a12a9fcf47c95effce95d01fa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=7ed0b60147b6a179ee378be7cf646968bbb623b151cd1beb49a1d1876f6d8e63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=4bbe022e62edd4bbc25a1164bba83c41c8566fcc64efe920fbfe93f5ada4cbad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=2ae102677a86646b7ba767843570c55bac9a6536319f16c27aa85c415e1d7de0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=8a40ed1923e70449c00e3d26926c9f298fb444a50bf54dc9b4d7ce910c4eabc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2GNYK3F%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICD6DmcD10RvdgrsTj%2FTWpWvP%2B6VW9MY3daGi634RfJvAiBsUXLnEnr5Uk4RbtHkVvBskjS%2BIuD42TwTmsyxsySvwyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtz%2BOozapjLKIKG5mKtwDxpdfrMWV3fs%2BmR%2BhgI6r7Qmy1b74JvMHUU8eRljf6tkAbhazaxbD%2Fq%2Bu5%2F8dQhyQKTQlLERr2oj1sJAu1E303ti8VrCJt4CkZYtGM%2Fkzuhe44Y41sQdU%2BS%2FtFvdJB8EO8LKVb3Cuu7VXFHo%2BB76U6Z1NxdWMpzgDThnHFTU%2FW2nY%2FQ%2BHi%2FrJdp3r67r3dI7%2BLZIVlHvYSEVsHHiq4yTovftC9QIXFjp%2Fq09D4mg5oK%2BXJm9VKe%2B2m7x4kFPchjSybZ04fbDLuHykX%2BckBzccN4x4vyLPAQgotsXUxd9kcAOQfezEZxPvcjmvMlETPiVGBmgSZAcG5UrPIjqGd%2FCsGJA%2F15R64NxAywCGgRahmnbVDuu%2FRhqZOu89P28X5qlze8sk2OKbZHR%2Bs1CAlJsII8ZWIRZgfEcZe3ZKU0uwpFOO%2B0IKLOnd6QH4TlCXWKWQXK%2FHh37oMnxaCUxM11i7OTmZ3LvNtkrfwvV%2FJf9TWLYJbWjbddsw58MWoet%2BfGTamQuohleeHAqjLw8gwAWyanHS%2BeRxqH%2FpfbRnPsgZkt%2B04C%2BPl5cEhmKEysHnDf2RujzXVQqmLy%2Fps4x8RUY07IiyoMwf5eUxH6zPGpFv7ZXDvp53XWLe9YEeLpAw4%2BaWywY6pgEoEdIZ2kVNkL4fJ1KoDhV%2BWlHYx0Yd2lZEoFYOtuN9TUsAp797OTCXPqvJ9%2Fs6ttLn4cis%2BbBni%2BOADNvuX4hv25tkBE1eKrgYK26WvIUcFeNLN1LQttj7C5oRnWH6PQSf7dHt6Y2knTQCuObGs%2F6ie8uJugxUAidA%2FRRIrQIh7dP%2Bhn10BbplJHgae59SlTofFa%2F%2FMB1SVu2FdH5o20Hr8FAFw6n%2F&X-Amz-Signature=eb470d5d26664c0f2e14b2b4c660790376250e05dbdc916c451f888226be14f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

