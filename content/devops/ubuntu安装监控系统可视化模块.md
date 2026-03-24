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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=fba921780f6a6402da81ed307ef58362d42b79d7310c1402eb1b6580ce47e8f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=0c011df7fbb05cb05706983a9d618fab069673e9afe6f8ef90b4566a39ac9041&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=afc847b101cb9dff10454c4867e737527ea904636efc62523a89e285b9981fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=f890979acfbbb20eb7fe3be38fec60a6e8b2abc0ce23e1adec825ab245098ae3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=62de9b7fd2df01e2c2e710a1869d1b4e336bcc9693e0db492dfa412045dacb7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=2cc4d4422c2cc8fd2935907e51fdf641e96a35b670b4e67ac45488c7487a9bc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V24WP6HY%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEb6jZEV0AceB0mx6zpu%2FmXvWcTgRbPjqf8xqNXNFTbuAiBW9jukmcgr%2F0xtJZQImY96sq8CnoUQzkjT3xdciDdiOiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbVttyrFXE1FIri5HKtwDZZViPU%2FcqJaRontT0CO%2B2XA%2FC5cDRHb6WV8%2B5RzoMajKbwBGu%2BdKBTKIYta%2FUu0kl8kU1H15ozZoWEySpERSilsWOXPHmKHgN%2BZE5reTJVkXVb8KFccmrJf0aPmU53oZ7JJdgHe%2BGRlDI9WpXfK9yufGHGbRJV82eSvvHjkKoovw63U3J%2BrFwfd%2BTp01SnXY4%2BxhZCvz7%2FoZNlQRW52FL5khgGeNGGebCZb65J4DBn5QiVeSZBJRn9W9CNG55EtrLNfssf7tSLLtYTRCjrcZ7wTGtYINZiaQ99sD3ts8Fmru49UNhRJXm4yUyctpoGad1gNRW2Y74iJDfmq4%2B6gj0ICHYvSNZhyc0IrGLkR4QlLxQdU6uXHv1EiTp6x2CIItmntmQAY4%2BLagq5dWC2kLTdySSlyBa7z8l0gU%2BzQHCCrg2Ko4XndDhr6K3urAVEHRdJCeL4wQAgakTPHGQdoKZ0a2oSyRDFSpjCkGPzb8qRt50CqV%2BXKz385u4xY6axWvmdlB83LEpQ%2BLCfm6Sqtc60BEFIAcETSMZOVCF2GqA7n1dqsR9OPOpaLJhZH6zZNYezSSQxx%2FwcR%2FT01YmhSe2MrHEGsUTIXAC2QDB1BE8gpg9nqWD%2BB9ic7%2F5lAwgPSHzgY6pgGd9HxXYGe9s%2B6QU0wtHD1wssDLKYo26fDFXxBBGfMlHPLZRWFYGqEqXOLj2F6TCN%2FvNq2GSaobvs6L7%2FUMEFzLsHnyX0DwcmRHhOfDJqgB%2Bg7Mm0zRauw4jefW0M4FF2NQepR%2Fuww%2F9Ntod9BCVWiSq79rfXdxwEN71HsAb750Vy7%2F9PmMkaTSed%2B6eA5zINgLbNSGIwsBq0cpC9O8OjTM6ysO2nnl&X-Amz-Signature=638a1cbd776ef1dc6628c8b5f2c3d7fa3a82f3a1e2a512643ec9045bbabc76eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

