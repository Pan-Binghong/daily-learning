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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=8e1e9376350090625e04353dd5d42fbc88148449e7448fa9375a41e29b46a963&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=c76acd6a08355c6d9cfb359a408bb7898e0c7786ca6eea5a4e420610fb8c52d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=c36723de32dbb31b9f0c327ef6cf74277025c0efd5896c9b6f08ef5cdbc45548&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=898f8c7ab5b7a1e2a9374efc87ffca4112961d6cb9aa27077d0d971d7434fa7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=376d8d4ee1bd21bab5f942a5cda3a3ace36f6f98b153e39f7b30bb5ab8c7b67b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=e30fdc45ad8074e19260d3ba6fbc355e69662807e3856788880983e2ece1760d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664COUUM4%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC5yF9KVdFULKWGKgCoHyW9pB9hXWI%2BTdD7epNs6E9FGwIhAKQZCiRH2bdesE8c9f5T20QMDNdY7OCqKTdifXl5BiDaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKAL7X02WXxhck2vwq3ANM5KTuLJnv8%2BCt3mqb%2B3xCJTnN2zMRq07l8nffRZqbqOlmFwPdXmpxjX5Of60DSvJXsnHBILXY24TNquNo00%2BPpjRbC3hrRJ5VWlttjFP%2BxKWG7iwLc0IpmEEnZwA0HN5T9iohN5kxIRE10z%2Bw12p5VUXXr3TBDU1QfPL239Kd84BP5T%2F3LARhokfcAyJo6jxQZHm27%2B87AXUoFeqtJlJcwHg8Zze%2FKQQejlZw6pvadXjSzLLitrB2dJhGyyJvUFZsLrdtlx%2BMtGcA034s9dbNxamkuSuBtsR5%2FiWXxkYYlSpu6p4knR0E9haSlNqYtEzpencWIxKMwlkU9aAVJq0VYT%2B8ueNLuKI2nb5CeOPHSlrNPmWiVjPKkZT56vIRgsjQxOybDFNMTH2tI6fKDi3janq3PHT5ws0CysM12ZwR%2FZ3vGHyCRCj5bePvXqOUiQvn3g%2BF2bl8S1AwwC99rmAfDLYuyyQ%2Bueygy9z%2FMIFQc%2BL5PH%2BNWDKACNGnnMDcYTztfu9nyk%2BcQ%2BKCQyexspw953m8c%2FzIHK8RB%2Fwta%2BfWrMBnwrRIeoH3aJSvC4ciCG4Fi0M2JjcKBLfePgCByJl2xUGGoOuo311w2aFBAjDA1NwtICGSQQjkUmydijCSwOPJBjqkAVFtjlwbr1xowNrPafEp1jG8Gqn6o01uLz9vRGgXCOmD1B9%2BGOUnCyV0Vn%2BVepqSlT8Vs6zh%2FFFW5pGECuvH25%2BeeXf%2F7pZts4Gnvth2eEeynjPQBlnseeugphv05kKNnkeb4L%2Bkzch3WkstWJQXZAu3uxXmB1SxXEFXAm321YniPPp61KD8FcnUUZ4s0IH9BJ5qBQ27V21hC6ay8QvsEMny%2FoJQ&X-Amz-Signature=5b4f03d9945477577edca915256137c73034eeacd6174b4499748c40ae96b023&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

