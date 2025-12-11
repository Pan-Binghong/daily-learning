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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=bc78aa3662cbedceccafc39fd57f819de69c715343e3d1f105b7b4c66ac44260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=ead6cbceb917757c163ac33f62cbe48f8e46ad8112e7ad326413f97505b67381&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=b6c3b2fda0229e427f97a8afcf222a9705790517e923a87ab4ffb00327343ff3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=01c6beba8b0531bf3c1dba528019ff9ecf8db5434543e69671768797c5ca7474&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=1f413b2d139b7069399d9e2b86673bdd1204d1d93a2f739b08c0376ddfb92d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=e85d98706889689a332f3e583f80c89610fa2da1b1ab72b8bab3c22bc2c999de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVRLP26J%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG94D7kJVzul9sN2V4WmD6pea9WvbJMw55anF8XiumWoAiBUc4daj%2BBpbU0If0V8Cgm2C1czsLOIjSp3nIjn0GXC8SqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLm4wPc%2BbniQENOjfKtwDXxwJH3nzWL09%2FPIP1eCs7Ymksq4gLbxmPbpYy8IDEcnrmqMBkgrBmEZszAKk%2BioV4EGQtka0srQ2aGKjSs0M2bjXadEKQDjI4UpTJ70Hn5z8O%2FZe2IoCTtTnXjo8l999TfmiJ2tJEoCyJ6%2BL2b9muDYqfA0OEJmmXGV4uCfqUMtj74CBYjnpT3SDNvN3g0M55Pix67z4GxMkui745dRKu6qUbiafNJF2bSR794Yk36AQVkV8M%2Fr2NhP2S2J4mNLbLKHkX8r6MplIU0gQXiv7JsWDklvXdK0%2FNuh%2BHpsCGy85BsL4ucvG%2BtGSEsIpkSLDvyNUgt9cjyfCVV%2FzEvM3k4lh9HYfg%2FrJUxt5P6ZTf3JmVj8qDTXlwDO%2B8R%2FDJaLpnkhdJpx56UuRHW9%2FgTD28VlkH%2BISaWpJN9D5q6AQt6SzViJJj2mXrSM8ZJ%2FM95VoS%2FtxbnoxX6xXRL%2Ftk%2BVDalrkTENzeDkFDXirJAw2wV8eJQ9danh%2BAV3yBODS4FsO7kDHxp7mueCiWaAr9a7NrGoHCvqC5101Rq0suxQwb3uKLtHL46XvZI8DZGjAppSw6Zy4Yq5rXCa7P5rpspUedsz3j9PCTJM2zKEfhj6CCXC9rOfHGZTCwRmq%2BxYwhrboyQY6pgFeDa98LDQtSi%2BIAEELZWOeAWMI%2FOoAmQZXB1LSeYUQSnsrgn1WXJqbrJdpFvSetYrcCmXG0Wp8cUtuR%2FeW1I3xYv3uaGDGE8dXLfBakMZa2BQFBJd3nQhaSSMnAK9WUc0gLJr%2Bi1UyLwekqmL%2F5EXZNUjCZlppoReyJYkuu%2FRGrBFCZicXy0bbRzD8nxlqpmTcUS85iVvg35hrekAhUS5rAgjvTo6N&X-Amz-Signature=a0898d42606fbb2925f13ee6fb26ac658f8da0bac2533877a1d4814662a2787e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

