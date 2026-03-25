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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=c3dbc7d1eb4df7eb6525b1e2960d29c0a9312187c9312f516fefffc3d9bbfe47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=ebe2751d9df66c1607d24247417c04f317b05f27322a8ade51b2d22f8f1d87c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=bef516460e283ebbda21bd875c94a6875012bd143322b093844b661842f213b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=40d9631268b7e4f6df013411f181e4f5437c0181d738dded8b0d14d020137bca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=cb947031c51732b7c2e925c1b3fe2e0ecfa29a9c2d3dcb263e79ea7e8b78a8df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=8614b0af50e6868b2dea6424d595717fa9a8383dfb55aef2895b8d1426756fec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNEYBVMW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpwzphHvkcN%2BPC%2BJ8tCTDh6M6vVlOs%2B66Nj6%2Fl4UVGDAIhAJrL3wEqvYSvvlgcMUg%2BpqKnLn4MhqOA%2Fiia5AJwdvHyKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMQRJJ6VhhQIvIvjYq3AMPBxaGU%2FrXrS0HzyUrUwq14B6PPSMHcr21Bpkk%2BOPImfuNlZnL0xH7Ke40i1TjCtlnbvrcfblS%2FMHgBeoeQ%2FVY4JrOw55dcfvAmXBsNCCWBRj%2Br6FM02%2Fp7s6PXbl4qlIazamsOJ2%2FQhuUP05%2BnGJG402pemNxlMTiSPo8snv634q4NDXrfFwrYUFcqNxyztC5rT1g%2BB0Uv5KsodMSKDuSP8s3hc1%2FCxNupl7vVwTALyjcozc1gwHRK42ysGJfuDml%2FgjKtBEsxTyf%2BCGeJmehlkduDIYSivyVjkHk3IcL6k2TX7zLNq9acv6PoSL3vWpTEKnIvefz%2BqTN0GU8vPrMuWqpMvKBSXVIHGggUG%2FSRW8QMl6eNpyaR0vAqG%2BypAID1Wy9jFRSfDve4Gl3uNOos98lMCX%2BthDprXVWvpdqS%2B4KSqfn7qB45cCbcM5vSX7WtwACD1p4aRATMtHkkvoUZWFoLL44gW%2F%2FM6nBpBtsf%2FH1vOip5GZAKENP%2FmnWUaUUyTTnNR4VoSQYpbo18k%2FHWanzrRWWMZeF61erH6IgGLzn4PhWCxjI8wUbkPsv0PRF0374VjvtTAN7Tu6iQpqj2nCE%2FibKVEhUcoY7UBP4RGeBszVm%2FzMGqQRqeTC3po3OBjqkAVqH4q2LxrYIPdsev6zaJhX%2FHzzp759d67PEOtzrLSj02WhLrAdlq2xxd9aU%2Bzny4UFeTZFKKWnYSWTwIhKuMz3F80RM%2F%2Fl9F82RswoRe5ddPrj%2Ftc3SaeiPK9mJCql%2FX26XHSGabqZWlA1Pwi8RBB13E%2FPYBa4zBfITLy8%2FBAmJMNV6n7odCmDteqB8Mblkd72mtawDSpd0NUBP%2FHaLD%2BKYpHLQ&X-Amz-Signature=64fe657a77265d20dde978ec6062f14787c83b778517b39c80fd06327d1e531a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

