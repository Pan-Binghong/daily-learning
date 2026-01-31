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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=3df0ed842d1ac651e96e633668928ab56e3c8861f42b2235144fec098d3ddf99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=2f457716289020967faf36002ed0d87d482eebb4c04cf270d9394ebd9c44ff29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=00f65751072f7ddb497de7116e52e76a0a11849135236d6d1edbcb644b00f4b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=c843ba23a8e24b0a637bc3b1d77ce7899d64c29b0cd9a035f17fc13a17bd7905&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=74d8e86bebf02668778edd9b9d49825fcbe5e69b92011e7e2536aef191f54fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=eb23a698679fb41c8489cb08cf6779f62a1c1125e028ad553135fdefdfbe26b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTFQL5YP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0L9A%2FnZVu5qj14sntg7yMH8%2B%2BAK5W6bm0NPqK45ipECIFXNRtWLbT7brz1M5z6KCn0jjAtwQ9BhySTcQBAe%2FYLzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz06GxLyo%2FLpGfRs8Mq3AO9eiVHJoL7dxPDYAigB60vsBIVEy1LzgG62Uh0qsn6uKO5PbG0e30Ziu6WAzR7cbbNJ5iCM3Ta5iTHaOKr%2BfP4YKnffHfOlOb9dU%2FcBi5S8umTGdxiTcku%2B2jOHZZ1DIDA69lZAoW%2F%2FDopaYLekzlJlJRFR16VWnb0hj2TNiuDRvvYfVoO2tz%2FM8jypRXq6DCPPuHrdXSVkZXjWJTJOAmjNlM7E9KF1e21O8VU7A06zPf1P%2FjPUmKjKDFQW71aOCEMuLbngSOqKfxIwqF6hrlVTgnkf7Uk3CwS6DJsFwAho6X%2FLUbUn75BmQXhQAotBajG3JRCKiXDPT%2Boe2HrhvObazyJ0p81Ruh2j%2Bi%2FA6q2Wksio8t%2B8TOUi328tzQvjrbfpmjbPrmAGkewv%2BATPpwtfKB6qw4QKJKGmI6YnrEMoFTeY%2FK8RUDyaCZp4GBuWrMqYrcwS84KjjpQvDh0WXqpge6qrHS7fcy2N%2BzN%2B6q1lkqcv%2B%2B5DMePE%2BUHvxGgFeksYEmDteBsv7SQM%2B9d60ZdYTbmZoROEHaCLL2YCL54WdAbO%2Bg2ISvhGCt9AT4sxuCZwplPq3u%2F3CImFmxBnAK%2Fi1Lk5aElFNXDmNDuA4v2JB9uXe09t9TMKeKFSzDjy%2FXLBjqnATI9Q9UN%2BbSidK6Z2lZxyRaWbgEPe2E2KJ8GG%2BymugkRE807My0W1BEmZUMmxh%2BjnZObTqqqRfBfudufuStASIEGALGApTAcMvUuEXrKs9ND5YB8UG3wyybdo3UQueVreD36N3BP3H4Hgl0io3KlNqMsFmYWR0PFz7UpdHPr8a4O62a9s2hw2698M%2BCi%2FJHeKWM3Xcm%2FLQx1ZixoLUxf0rGebct4nPft&X-Amz-Signature=9bd61ce8534c08d4567634848ad5cbffe54b7a2f62a09ca219bdce2384b3738c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

