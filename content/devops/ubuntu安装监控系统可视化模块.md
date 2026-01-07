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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=5114dd92e7a7ae7158d8e334eb95bfc24c274b8afd1d9ab7db9a25594d2a9fe0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=64291b85a3fc822efd693d6429b3248dcee71d7dc0a31c28e5354ff2f8ca8a48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=209222571fe8b36ced8b2ae49bea9d506036facf8e35f2d5d2a941aa3a2f064b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=b0be78cb2b060d677431a4a6cde2bcf419e311d7dce8b3e596f9a13d98c62612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=24e025da3fdd419fcc32052df2100b99101a921c7e4ff99f99eca0132bc84e49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=3773f55c054ee1933867c46706153c66674164fa69403be7b90342093ae5a78d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV2P5AZK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE1AkG1Nc3QeyraO1o5Jp5wp7PUvOWG2BkT1nhr%2BP1IRAiBCB7OvZIfMN6oQABI%2FbF%2BSv%2FoUuCStW%2Fd1HJDvD8w8air%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM49NSW4Qf3Nb%2BuHmEKtwD%2BB%2F3TYzLHkmnZFtWM%2B9tVC2juIzBvsNLtzxHibhTbEpul2aNSdZ3kpp5YgewckIQH1T3KH8zq%2BRFmXYr6Y4tElYKS0yOzz%2BmDXL0dEO7nsHzBn%2FT5VAdw8K35%2B5VcmiUDxWQJVsLxRAGxH94Uw%2BgBmMl4jpsOg1X%2B6iUQVlvx3Z2Rd9ipgg5cghLWTfDGG3%2BPKOgBOY0V0fBLQkyi0Zm%2FKqMhWDq7oS0W2STbxN%2FaVbDIepdN2DLRfZ4w%2F5hQUJ4R%2FIaWjNNDGsvyPVGro3yYZEJIBdsLEIR4iOIhEFoUHNUENNN%2Fgrk%2F%2BCoM%2FT0DTslSswR4KElTCfmolRsGnL4QRJFbfvqUzQsZ88m1ZtpeFbnLe6TqyqMT%2Fsfpg6153razGmVL1UhLgbUeqzNXnkFVJljTa0syvUvPyPwV7wE7oF0%2FlUAjI2nzlkXYt67MA1eC2S9WvyGtY4TzHdPrzccGzQsp76A9WBYnRMzU10DKRuwgTWytvyiScM%2FOjTcPkdXyu5Tp5%2ByEdl7f4BK%2BeEARBXJ6XnF%2FyKgQnGGNdp41%2BlTFU%2FY2ZnraREWKklIVCO6vJ8G3pBQz0f%2FeoB6WKoQc%2BMrF6KFo6aEYgrtbOR8uDT3zAjS%2BEzVryW7RTMwjY%2F3ygY6pgF265w91WDtm4TVyNGxqaoFfxlrxy1lzLK2huLunHrTLX1m6FQjnN4wBeAYww6k6P9k2xqBFxKfIeI3hrsCeUiZ57MYhya2FCigF3P8K838w7Ohikbb7SruR9n1JhkrpXn49uOEmLSTBc71yVkLhC4NYgoeKe7cxshA9dcIkMfms1ZFih9X60DaUqYm8km4sef1VCV8i27nxooAr6pAIxVp4cua04ZY&X-Amz-Signature=53b70a61f3f4f8401f9221a51763f143bbc9f96c5ef3689c3432adda1ffbfcd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

