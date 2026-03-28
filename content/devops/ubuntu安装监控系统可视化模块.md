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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=3937d753b0e9ef222e4a7cea6e615138843fba9a86ed3663b6b851434924b2fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=67255ec3f90ebce9d4cc19250355d828c64dbc7938d5e29fc79dbbe424ad9ab8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=4d599975ba49f5579e0ae5a340849f2252ad41bd9d0446aea0dbce0849979d3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=fedf2507af0db5e38ca5713a474203435ad86535dabf03cbd4a06e8348f650fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=61feceeb69a45041efd0a931135f544eafadff1158eb0cd79cf3e0e2666b4e14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=b4219a592f6d5f74454f17e091f138ddeba1ee4c293d3c8f18e967705edc2c47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZM4M7L%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIExuKTWo9cX1RLXAR3%2BwL%2F%2BfCBkS8vO5rxXD76i44YcjAiEA67vwEsCttB1QsbceSaYbFaeU9Iga1ynl54nhReINX9sqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLZo1UHq1wNn3OwaxSrcAzlWTu1MUUTej4Z1giq5IchcJwGajEmk%2FSUtLVfIiE5CZavcnaOqe2NKa7s3A3fnL0qyKBiRwdf0S%2Bt%2Bc%2FSCqBZSche7uJnMO0Vn7cSY3TgSTvqS4lP9jP%2BKUqVFP6%2BWaVsmhNkefkhLx13lLJWNeNPqnxw6qcJ7D078CxWCdwVQ4wfTOUFruYIJEt7Vf8PQU50dV3v6uS3oYCjPW9gH2nlgR5lpPy%2B58d%2BRJ8zoGXm4pdRSrBgYSQRMuFsvxtTR3%2FJV4c18%2BVs02yzX%2FFybayujZVd69Jc91gPMkc846CDcgl2fLf0bt4YM5Kh0m36yUpcxtUsRUJA0TiBBQcUh4hsec4fIQrnnvxMG%2FTycA3Qxn7RF4H4O9qnr6cgyeGS%2FXX%2Fre11j4%2F%2Bfwt%2FzUcDJ4CI7cf7r1zVdepD7G7jfxHOPnJuPwtSLS0B%2F3Std7uhOtuI%2FBLUlkthzZ6L%2BA0yJ5sYaC%2FL3rYupC%2BCKziqTtcet%2FuZKsoz1OCJ4Y%2FEJnqhtXBI4T6UinZgssidYnG0gPKLBZqqa%2FzNOsaYNpNcW%2FRcKrSVzBXm4owBGKocMQUc%2BycKa7GSdJhWXJlQmkPLHc5sWjj6R9rOR2DUzbxCX%2ByyB2vMEId7Aiw1NzeUKMLHsnM4GOqUBqNRe3imxHHrxo0s%2FmFq7%2F7tx3iIT0Hs3v8UB6cu%2Fc6r%2Frqv5odLR%2BgGN4WObnEYBv%2BA8KMeYk9r0pPM5i2FF5h3NtB9GM2IBGUtscgzNqhC7ghxCSDgjf4FaB2XpBxkz21xa77tev%2F8g1SXhV%2BVB6dhL3G3XGlkB4%2FBC%2FRGc33JmUaDNHXOQOoNJPR2Sdx6pAlmPlgi0kZi2cRHMPHUqdkSsmN%2B%2F&X-Amz-Signature=a88f6e108b7795e15730ae4f111093c41249ca0ee0b4019f96d6ebdc7ffe4cac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

