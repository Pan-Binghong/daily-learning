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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=b6ea3d06e132b4d1526aad64b215d730b70b3992ee254fef2e8f065f77bac5f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=8ceb6bb29455551c0ff787eb1d679d1ed13f37beadf172c157403728c407add0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=46d7b4971110ce1f10329acd85d22697e6a9512d82e9836ed9bed1a5a6686315&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=c77ca7e3a9a67c03f9b0b83c19b834c97671230b4c4e28e7f8838c5364129682&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=bdd22f0ec3b05b26745c2621a80a6f8be464d80a61cc80f39abba080596e4904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=4bbe170785a5eff7f7c40848d12cf604e8689e36f560ebcbadd667abaf62545c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQHHAX3%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhAHpbPpCeqSi%2Bdb1hpThNFNG2c60Tiz%2FvTygzDDOpzAiBpGaYHa9ACbUKzN5bN0jWFhkRLOPqETs7saAE3oMdhDCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME404X%2BKpsSl6kM0rKtwDW2ItTtLrljhxcDOEtq4nmKX3ahpZS0oAs6yuN5tFqILea5fB%2BpytoCu4StLSyr4TPJvTCh0uMRB7qxGgT3KxufheJRmU%2FN662d8BGj2ld%2FxeVxMZSGQCnB6Z705AsNy8eTnqaqIPqDJYsPuqF3fl1hwBIv3U7o9EeW9%2FIu2qyZ4g%2FtD8bAbp73fSUU6GgBX3CQYdAlduEqPpCsuDtNHof2nvAx7CTnP%2FHRqNpF76RRRl4iDJOyrA44qXkirBsNnoYYiZ3I1PMOSr4oUOmbRFFEGqJ7q6Wgjzr%2BjbDg0qUw7p2VqHKt5X%2F3bIdoFtrzs50bd%2FYR5OEEFx8wfUAABGBTC%2BYNpsugOsi5FPqnfic6%2Fl7zxkR7AhmA4jo7hNL%2BATiFCwQupdpsb1Drq%2Bp4Sr7e0phrcxoverGUmPtkYuMlukH2Whw7OAIWgliDi0MzKSjTqm%2BT0hLf5Rp%2BbcMkMNbOyuro%2FJbY8pOT6Iua7LGyskUftMt2EUoeHXWy%2FasN%2BkcSgJVuFAbPkAC4Cexw12au3ltW%2Blcs4PEogsl7yqOkuhMVF9GI0AKOmUAfgcYj9YOZQnXIzBib%2FeuKR%2B6OcrsG4VcnxEeSkrKbP0Oz0EP8UtOSqo6VW27LQfokIw4ODMygY6pgGejtC56iDgKpGvtywSGKzEq%2BUtCWjiYOHr9MHk3p5eeQPmM1jlSBBZXI5ciCAbQbWSSJ8qePgaOYeTjRR%2BHlDXYZevzAJ%2BW0Aw%2FRY%2B15B6pCd9VwsJfHeRCmWWlSD56I2PweNQAycrSn1cVtWXNzCkKPfDRDTsACJ3UW%2FQ65r5rpyhAI5SZ9npXGoeOgLdf8U7SSfnuMUAk0eXzXWk9ZHl8cC%2FYfbk&X-Amz-Signature=50aa68997f75568a4ab43905f79a97241321f0a99cf2289149540a107a78ddf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

