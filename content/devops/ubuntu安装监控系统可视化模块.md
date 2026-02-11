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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=32cf1c9c13fb12804873c9b5750247c1d7ee2e628053fd19099cc9d2e2fc82e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=2c5b09a1fac4c761d6b71dcdf619cc2787c337b705956b910c73c656dd94718a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=4eeadb5bcf4c29e991d1ca26d339502aa05e4b2f8c8e674e5556a595cf5e617a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=13789c7d3c5e42b5da8a456f485b8eccec03fb5978e2f992b2131e448edcb0cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=b66b12772c95c8914d2c69a90a3c21149c61e4f476d9bd0fbf648b1db343192f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=33e5567c634bb3ed6c4a14179c34777192e9d9869114d760fe19c3b4e080d953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUOAXLFK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7AnmxeKGOCKluhtzqT9FzRwEzqnNwJeepkLfwZMtqYgIgFhtqNZH24eROgB7SpqfqVlc7uqjFQoGKfAGPtTPh9KEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4IMxlXvyKy5t8%2B6ircA7z73qIBVQ3RnxsCbNEixNlYARRCtBGSIiBouMCSQYBoeeDGrBh27vJ6wYmnvCg%2FAF3imEHHKWewuUGu1bfJ53wgAs9h737tgi7EoKM310a2gCQea3cjpymgXjJ79VL3%2FLnnqUilhEFBSb8x9L%2Bg7tDVP80CRDBCoEi%2Bmibjxf%2F9INJTyPuDnNRsLaIl2x2MG2qdpocFsTZFz7iaqCLnzxqA8%2ByMXIPvY8p9FafY80eGO3k%2BTCm8WRpQKFhC3F2cigUSZGM7wjCpct5k%2Bbl%2Bty4j%2Fr6uynN4z%2FfXD4WqdVAUV5IacCBMl0vxMkt18VCXwQ%2FdM%2F%2BXCrnViBQLLNG7FiShfJcucIRbz%2FPOquOgrcO346X8JjV3Mkp3vl4Wn1i9JKq2dx%2BTkigofwDDajhQW1fqIiDs4FgSgQQgDRMNSueiUKWxN%2BhDfn49NXDxry1LPDO9ZqbizeWVtwGOUU%2BsU90ANYvri%2BDoiFfvcPzbh23FC61mDRwzXbKSlSt0rLRbJ2jOqpr0al%2Fl17vQs7RVwwzohx0f88r97xSUhZ4WwMDxJ00EyEeRJLfrrcRjQ3oW2zg%2BSKTEq0z25lqMZbk%2ByKUUXt2WYluQVYQZYlU1oHllt2rkbupIIYRtuAt9MI7Lr8wGOqUBowGd8KhJN%2FDVlt%2FyrAO6p3t2TfvQbFtYWGrmXeKH6dt%2BALeOP4Zs8%2F4VcJVxLhyiVr8CK5bVO3KnTJBSWmLY6n2EA5OsM%2BL5oOUYuwgTbFBBCcz1Sf4NuR%2F63ONJui3GPWJpo4qoGWFWE5xu97PRlfjKj6cmBLVvAaNng%2B9LGw%2FZ06QjHGen3xLVUWgx8slJ%2FGBMfB7jvc2xN9cn3L8tnC1vizLv&X-Amz-Signature=26f1ee82e77966de2486a95828203f2631a5c1c8aec25553f30880336c0df751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

