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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=1df4c9fcfb0bf91b555f95cc074c7bb9c32597901233515c782157c82bc4ba13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=b85b1f9be9d47db8a37f9ca62affb6e4942094f85d4ce01553e4fd76a161aa2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=ae023feb84947c70bb2b41422a5d98c04f018e94af12e41cfb4057f4c82233d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=01635888f66ac456f4753c191fc7479cc9c846b887680ca32816637875452592&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=21cc2fd664861ce64fbb0c0df9042346b63e27978000c0e7856ea7a9f48830ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=84907c8c22f0902a5569f34b9187dd1ea54e9cc5d2240ce0648896e393378ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7HHJM3%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIGxDkeSmeUWfFq3eIzQaWLdNOx8nluZZ%2FIr3AUfq%2FTZJAiAzuHYBr43LF7fiD5b6TPQprqFn4gFD0CsXdhMDmK0F4CqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9UHFntNYlFAzFXubKtwDdmPR%2BYSV5gmBDYgw%2BfYqMPAeavjYzOYmDcS880nKNkl8Z%2F3bZvuepy%2Fo5%2FSyxyerEAURhOoR8QCNkBpXoC9yBWIMV9OpFLehLGpb%2FzGIF1B%2BW7z8ap%2FaOP3PLVeslZkgE1lZf8ppsAKjoR0dzMCAnYmBqj1TPh4h2ML3qari3%2FKjJWuKsFYi9ewuxxIAvGPhQZYck2dcGYWM67eL0nl5bpYoPNwZGTajrh2nQI9BWmJ%2Bbuj73qRLSDgei3Cl%2Foj72hk02F4F54XnrQ7X9FBhFU4JRx2a7gGIj6bpYdIND%2B8H4NEt5aiImCrJ%2FcEhapOFD%2FBrI7vIfxWCE3nARiMoA7E0afmDJcNPnlxqWaS4%2FNAkmgPt5FkvKUk%2B3XzlxP1xrC0FO%2FAKg3LWC91%2FAsCNL1Ap4T8e0r20Gu2UbpN8a7CPf829q0vwMkAlrfF6xy3LPRJMkmrIEQ%2BszTNt7Cem0rHMKVwFp%2BTWRlkNwq5K8AiNWhduHfaMulQqLw8mcAx4zz17qVK1fAF2XCWm%2FlZ9zmuMaNDByN9AiBSNzUjA5uby3N%2B0OhKvX15SHkKI0%2FE0LMd836KIYJ6jbxRokNgsF3YYefFE6I%2Bu7%2BAOIhfvuD143I05I6GVQ850qRcwupK1zAY6pgFH7%2BLEpvgqBUseHl6fa95eu%2FU2c4J8j67z8TJSavi0Pokw4h9VIlGKc10%2BWDE2oN0lyKBvcxn6f94lIRgb7HBOM5F61l5C2bQiLCKFq2adMZndr0ADEqNIaeHsDRgBTI5z3BjjeOJY7rZYqSs3mcW3bluKJuW0%2B3irirD9Vrepl2pLvc49tiZ1Ed3h%2FcwCKdHQ%2FNnV4BPRu6TiepRXy3TLgysSr9lD&X-Amz-Signature=f70d6e8c98c84b95bd4a36d446ad0c9cc0ce1257d7f9cc546357ff9ca804b7fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

