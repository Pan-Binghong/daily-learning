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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=335114aa87a8caf2670a6d165341c73767810738b47d8558089b4f6c431a110d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=2286bede58b15eabab51ceab82d9851fa5f9b68f11857441efd6a4df8a961165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=06eec5b9bf288bfbb9590056d6c292ed1ba59d4043b6a4ac38cd2b902d511855&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=ed3fd6564025a0cef17b2d6335ad42b849bbeba35572ac19e6be9575098b1170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=8a3c9878216e0753b72e7b62053ad82e23938e174b1fff7b4c8df46040317361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=379f77703528669aec2200791b6ab0e19014f8e569b9c602184dd7e2011be57d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVU5D5J%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHbLasFk%2Be52EqNBZ%2FNLPdammTAEiQ1x2f34YS%2F6uW3zAiAn6q9s8ugFajlpVJad5u6m5DkPIL8k0m0VaRjZR17mUiqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpMiFWD8mMloe0ectKtwDspF59FSuM4CXuPtbE2BypHL6nQWTnWqYYWSIYi1hcqgfEEwVbANoYJzNgkkrBoiJaO0%2FtDSG0Il3lFsOXap98fuCzr2gN0VCGovY6%2FTepRJLrLFvJy7sDIBvwU%2BpVLiOke49JW8mqMYZmaSn%2FnCjC0zCAfzcGl9tFsRGjaaTluk3pDUTk6mi%2F6BlOp2xpE6ywjWUfuIXSej9lpsIEEsEBhqXKwvQN9Hp4Gjc5LHxnofTTsIRjwT%2FIVjeVQCPa7pqBHSbV9%2BZQ%2F0bLvFmyaPu2e1FAHEACen1srtna2un4VNIrOeFYbPucOgT8JfEVeCjJJuVi0a2SQIEJ3PvoFfoWpttXpDGMbbwdusEbcwEQN4l6GvXXrKyIVVaQrNnfnCqQomLnvk47KYOIGGxOviL4MIehglVVAuNukYrUHx9V0scOhTx6htr2NZSu0kU9wH%2FUxFOaOjudo1kkPs9QcBhOyfmQ3GpltgtwdUNHh5iz%2BAB1SMg7YU0vk%2BCzrX0dxK7wVP5JdGJIwdOnC2CYkrYOTwLt2681HoqxhKaDjYDpr9piWI0wPKob4k%2BiQS%2FSlK%2B6mLJvldSVBd%2BewfGMQBWlgSqxkxnNnSc9o1zH%2FNbmZ5OiHhITK4Mf%2B%2FCbYMwxKPXygY6pgFMLjTBIKW%2BFTIx3SsV5bc8jB4Ae%2FydCYeBIhLeoWrNt2oJqQ3AEVMNkTOZbesdpv6VpEgldnbS6Y4BbV8WPlf7np%2FJiicfhDDUTkUjlBRqGgY3N5Mu5guT17pUituPTrG%2FfSzzBbpX2dQqJmjJxhVi88k2vn4pQFm%2FhmUL0Wvy5lW6sItP%2F3t%2FOuWlykG1BYn0FP6aVAqaZfI7DrJQU8rxa9CZuIU%2B&X-Amz-Signature=82ddd1d3a7657fd0eede5e3751bb3dafd6b3a4fa9ec077b58e685535ebc413ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

