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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=d7d370f3512b087e0d8c8e682a82951bbb3118ff220ad1e69c4ce687bbb796a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=590ca538a45d762e5e783790e4b82ccc227d0b2dfb62538296f588e206cbc939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=5fccc41090788d6745110d490caf28276bbdf0e365a3aea038d19d527cae6fb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=aab72dccd197fadc9be4468be6d916603abdb0409de9278e56838ac1b8d08e92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=f0132d419932eae5e1f4a262bb96231c852e2f0e3f366f68d33cd64df75babd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=809f20c906a9ee19578a13afd774c6f90d29e4bb41a28b029cdc73c35f32cd75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFMAJC3%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWNTO0aiiZ7WHq4M87%2BUAXvTZPKAlKVIkgqLYD3i5EzAIgIfe57%2FnA7V6Xz04KySW5Ub%2F55bTD4f7z4KRIyntEWM0qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT5HPm7JxJ4u4%2FfKircA0nmkE6kpOC8uit%2BKk%2FxAd9WyLbkrwoDZBp68nkhKgvvWK4NHyXMpPlAcPXdMnSZQO21Xu0wds%2Bi5O7ZJI3Is9x9xfhQR%2BC2iAQqQusIL55yVopjyhlF8njUdb8pnpwVt2or4Q74lpMzTrEqON8WLV1f8ov8DeWAE%2BKrHQJYUZ9iekiDEIMnuJ04cAVAfZtpaIkdhN%2BRDBNknsiQxkEUFNYpCf0KHC7QMfQukIun9bR7ng27VvBvTKlv9HzkcfDe3Y2miI9C95cRTCTDobdoVFo5kGuojaLG7xhcG1cYr1Y6TLXn3kBPdLn2dgXMBSh5m0KqXmWJokzRl4Rmjxeu3DZeaJb75NkcIRczXZ%2FBcrlpjDyE%2Fqtc6V0zuYBtzGGIZmFz03xqW7hGNlOby%2Fs91h%2FjUXwZrXoty36hEbgOvjeyPZWntXz3CsrnWg7B0k5SUCiUOUqBoBqDDwtKCh9p38fiH0yWsntVlpBUDKPg1%2FWfq6%2FW4IkJwAOZzuar3oug0g%2F42VYu3nyf0P%2B6iKZSt%2FmtttGzPhqhTmd%2FkM1A62KfqHsaw4703b8sr1wpmm2%2FQajLIRXHtNMjQFqzoRQNDGE%2FE9wgkep%2BCiuramsgK0Km5vBsHTl8hr0OiKmYMLLdtcsGOqUBVNI01bzA%2FhGNUG6QggEq%2BhLycuoH1%2BuIG9731sQ6m5%2FMCgQjCLZZcbpCQiL43cS8eZyt8nH4E7bdDTyiWeBo%2FojVvh8x8g2QXwBNWoQwyk9eyXCUm7cjBXXhmV%2F4zm6en6G8leC13z%2BjMP7S%2FNgbVaA6QWOS6zl68OeN8bL%2BPQv%2FrEKhmK2gPq7zTiM7Yq4pzf3qS0kRvS%2FQb8gLBGOvax3yBM2z&X-Amz-Signature=538dae226558c33b590cc95d86ff8156a290f120d0ecf854a7dea6f793d8c75e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

