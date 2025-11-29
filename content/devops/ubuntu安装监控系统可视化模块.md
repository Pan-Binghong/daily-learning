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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=b6ee777dbb678bb49b61db261048f6add605b50a630ea2811f8ad3cfc6fd1603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=c3a1e65b755452016b5951aa566e0fca60032fef75e8e55fd2e74ac2f55c0a79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=22a98a9107487534a556b7a16221edc6ed3345d3c6315a7f9ca8a306f5bbae81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=4c7f18c9eadf20adea1ebb6031b0202bed3b857e46679d784bedd8990efd9066&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=cd13108c94cf9bc06053c7fedd4c2ed010b7da709e550c2dcf91292fed07ef20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=e31feeaf61a7c1c14c64f2ef87670dbe9372ce8033161432645c731ec3953b98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQTTVF4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPWXsr%2FulasmCF5n1H5vIo0kAU6Qm8ZFM4eWPDtEpFPAIhAIz7ImBrJVVwEGlMUAjaORNh3VaV23pipvF6C6xCVtKGKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy75%2Bf7F%2BZv4zTFxt4q3AOsaaXqNkf3ZCXuWcqBzpSI58ViRT%2BySWgqPBnzebVW4718PYl3DZF2%2BFC7AOCYmOTGuvW2Bqf0SN8tK60CkX9w%2BYqCugSkq51vRsK7ir2QmB2oU8htWbg894XckG7LEGjddQfFMdVB5bapv629Gwp3QFLovwBkCKgF2AWy58xMYkbipAVom33KaeTKy0%2BTLjesoCBVZKTYr6gaGVAcNjkU95FNlHKvDRhAKB3LKJ7POp9fOOz3SC8fCgm1%2BlDdNIl%2F9qjuPrnhz132bdv2GM19%2FxMe%2BmqvcAYCm7NVUtcKjghrNl1ajZ57ZujrLfxuv5eGC9Vdaysc6gqlyOtPAuqht0cGfg%2BhLBD5SsFot6%2B2DOiUDERJE0jjShi5BUrx24RQlpjdy63FwjdPrjo%2BppiSTkKBry2C3aR9V8uie1zI651ttsZtDWzhYGUpkAtm%2FGWR3JGCnnQ62ox6eDuzeDojv4AO52ZEIVjC0XkG7tmWxQtfQZeMHjVYjpJZ07%2FkWAwAyhkaOCe9QOaizfltL2DfbaLJZzec1QvAviYFqZJg0Q8MVdQP6esVd51%2F%2F6ZXwKKEo4WsNtQRP0o1Z0O%2Fura4%2BojZxlQe6XV3fGD90n9T8cU2QZwmGuZLYtxzJTCAganJBjqkAZfkZ8YOCzPUoxxTI%2BeXNlGGkl6Tz4XcbgMVgFxO8%2FRWNpi3ETx8sKe9YQUuAtkO88IPGjKEgABGOZ3ZNSY%2FCW8zn6FiubUXYk71JTHJUWxfmhP1NH3VuACYbz%2FvEPKOL9xxCg2u2iyKX%2BfJ1vR8iUrnszfuvdrUiPYzQbyc1qTrOm9u8KL5pLeMsWqMq%2B1hI%2F4mvzmuAZp4kchLPNfX74pU2KIN&X-Amz-Signature=5147f5e8ac1019c39858008a441c35019963c2fce03561493bfe3b21b54d4cd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

