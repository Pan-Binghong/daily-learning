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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=4c490f68ad73ea7e9c2ee6b37900d3c5f2e0db2289627626d15c4476428dfbfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=e503f871f52365704aea0a89fdfd8433169849eec54c1768ba3c88a9d1b4e497&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=f5aec7aa0ead53bc76b7e7015dc039baee17aca43f36d92f790acc11fc90b6c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=e99456f3f89ef746b1480af14bfc3a79f4309f322a7e8e55c8a6fa5988a7f477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=9ed3946d716b37c608f5dafef953b51c8e4e0a39bbf0f99782eb74b45daf17a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=56027abd0b451bca726421fbc36a308739d2757b9506f38acd2e6347867e1568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4A6BIKE%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6xbeGfoAJng6FP4Fz4hyhQ6GpwbWA0DM4LF1Acu3oWQIhAPGm7rWYehbLIMZ10n46mXwNp5eUh3uFf6BOUw%2FE6lNBKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypGXxfjmJeKclynvgq3AM5tCnDjWS2njLUdzpixgoT5BmhNKnrR%2BPkcLfbMJwML8%2BVVHBDOPrGvV3mwA0swHvHegY%2By4yUfSHkj1DwSiCyG5mLTFaz3Mnd3s9%2FnuzuLs%2FSZJcY6RulmzA0qWeOOAMx8vuD6LVrYyMDCYgl6zu6hhygUi1cy7S4Oq1XcIxRCZbzACVeidrIVTX7Ncc5lSCODKmxwlppNCpzVa%2BIedBTHTOqqQhJu5oWg4L5gGLBFFdw2WxilnFqhm9GF2dtr0zjjOJJMKs4We5pA0WRYDAvUUGp27xRPGiVSoU9x0sTSrDcma6SgiRfg6fQ9qVhhYUjTTXbbrDElE7P2DX6NGHdY3Yoyl6AkN9IkCLVTtN%2FTIRURensW16I%2BwA0ZvlxoanmI%2FLcCzmb1Kc4sy8C0%2BhyCo%2FUqqE0AxPrDdYP5JUETLJxhqKnDV9h9BH74zlNDKfsCMSei0R7V6MeB1C967YlNAaXyld8idJFqwRQWrfgW2IaBPDAPcKSqO6RGe%2B9eiGxwGq2qoGqDl4hWWKI25u7Fi5hJ36j%2F%2F6Jf2XlGDL4oicii5lPXMFpIoh2QcbBI37%2BYSPuV5%2Fysx7qGoj59yOMEJjv128RT5UAOOxRC2mq3TUq34%2BRqv2C4H43mzCjsMzOBjqkAX%2BDBNoXiGq0HKZOI33rDKCte%2FkBn1YcYrgHTEU%2FSHLbgzCNSMdoFXk%2BS7Ahp1QXvdC6s9JHIqLnZXHYFTwcURxlR94HcOhmMGRKYmvGcYiWv83WrSiQMl3BJxPi1myP5BK0%2FgfFzddempPjlDYQ%2BWtLYeh9%2F4kbsGvWqiINK6%2BUbcag2IYe3RBdehn7SHaBhZPApXlK50iN3Qfr2HFQfe4BCgOr&X-Amz-Signature=ef49d28ffdeb7279ae22b81ddc3a2e2d1b4ee78a6163e8a45cccf7cbb2faf7ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

