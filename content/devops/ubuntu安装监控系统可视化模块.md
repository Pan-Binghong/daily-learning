---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
标签:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=d3da21513b7ebac49e336ad585e2e8ab4055394fbb4b75812794330d1887aa35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=f6af42dee3160568fc43103ee5bcf5348bc69460245e55cde0a2bec88400b75b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=bc872097aa11ace5cfd12e328331a8210bb31d25c5dd66114425ab2eeae53ff4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=dda548fd95c9e6af7cf878eacdf5f3f64b1497b64190bee5668ca8683f87cb49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=534d2b7d9c69a85ca699f4c6b6ba8f1fbca016871e4e2c59b3f4134220e571e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=f32ca9e734b12d41d4bb9ed4e211f2d51e697b135df629eef4904e3dd1757653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHQKL5F5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2DFaQqswrXncmCSHWsWV9OjxRb2kop8UqrIXFQzvSGgIhALC2ZeBKQpBlGsooXAjEiVIl7%2BLEzUrw%2Fo6Q7qGYDSy8KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx3TB3XqCLtidy046kq3ANmTPwZiavgbWIqZCWQmOnJQuwGC9w%2BTZnJEbgUjzV0tnvVKXhvr8njcGHnOmQPhVNj1vf2SwOolrOs96YgmQlHD2puryDx29oBfaRicTrJXGhyI%2BjAZII60R4QB1XQGiCKYpZc49UThjhdRN287oA4Tp8GTfYA0uIuVcTx2etEbMNbjk9jLPSdqFn4cqt6z%2B714L2A6eqS9N7%2BxXMLjTtgSQDFKai9PxZNUWQ22XQxjwvrgeegcssoJ48IxJ%2FTu%2FDn1KLeDxP2ihCBxeikMXCR0T%2F5maPSZwycQFG23GYyzCzQZTfdt%2BOpDag0MEgzMp0Y%2FaGbhuul8vlisvgHEtDGYemCFMmiKv2n9JblFg8Tg%2B5%2BX08AtfTr3I0BEPac1sUQQxxti1Q6h%2FXHPei9mVmvmtjM6CD3YQgEFf9IaVEvmOkeBKZBNf5iCVHcCXFgkFNTU0b7ImZu%2FiwEorkYm4HDFvFQw22ONQ27D5aVsC50XDfXiILMBs%2FMLp9TE95HHEgzIiD3dg6FpfhL22ctVbks7ywpBuqvLE9JF%2BT5U5WoHs%2FfQeT97GjoWlp4v9ee8yWMYg4keACwwv2Nv8cWuwLvGXAQUQYdAYRaQPS0DJKPhnEnB%2BqxvDTkft2uYjCwoqzIBjqkAXKTT73v%2BEiHGTAVtv%2F2FEosoth%2F16I506emUqfMc5Zw%2BIkAX28SYPKaYcjMCNSszzE%2B1KCQPtptx%2Bb0BluHfmkD3fgVcJV6StQoR6an2caFibQH5ltngLL6GvrRZNJUZFAXe5CCdmGxX0ywQh6wlSB%2BbnKcNWL%2BP8CXkJFf2O2B9ZBxwciDWaf%2FgwRXUpcTEbpz%2F4jX1HkWXdIfdh7PBFig2PwB&X-Amz-Signature=80dc41ef0ab10856597641f73714218a982fd6a207eb4961f02fedca8b0e9cc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

