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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=6f1acfa2fef63b63a005c736ff1020bc1fbbf4fa66481179232ce55867fc112b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=f52ab8651d256672ce9b03fe024bfbff3288d145bc36387a2fe0d915b190a123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=8923f41168862b1f708d2738ccc87cc1fc6675d3bb463853874d6123b2268440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=687c9561615ec317039ffc05c771fc9ff312ae0800687e46010031d4f244d8bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=19fb09b030d96da5272fb06e49b3023c30e670c867dca1354975ccfaf47a5ab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=c59c402f844d620d6e2b35822dd9f7725a9829477c54fa0db1e03926d16df115&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK2UJG3U%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIDozGfPgwpormBrJSK5ek%2F4EIDyormnNRMVgcQ9oVz6eAiEA0pyL%2BHiIUc40%2BOVdE02kr74czy4p8etacfXrifVNhOoq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDI4U12OrN2jOChXL8CrcAwYN2yp1bxm5FqK6i%2F13iR8xKmOJSc7pjfIUyzvllIWLHqRGKLPzWpXA2rxep7GFq7V0jnBevmcAyeHuJ%2BqW1rrcRGfsqs%2BEZHf3Mfh%2BQ7gJdMdwI%2FlwgxLYHEA%2FocIE6H6HcWn9StZBhEO9Bsxfw31FK84Z9BFsdXywvEf3TAJGuentdzSGxv2wGWUGT0MqEzZ6y85ktYx2RXVK599Y2ltJH3u8soru%2Bcf5VOS0mj9zAqQa2oTlBjW4M1L%2BhmZJxMDpVmTuEhsAyGssD4cXmM1PXkZrPK1SvgczesKmRDkIG%2BMjL%2BAzCIDn%2BsGpB4WYEOJLncwiBoZlqR6dnhiI%2BNvYxCSO4ah%2F8eK6WFkOfIKxaurAkpv%2FAb8PuiEBqxiZOqo6jw4jzT1l31IlYB31FJhIp2vOaSJHN66%2FcTiXPirwuQPQgYdmU2b9ZsUdoBchyqOffLRsCqzEOeJPJlLOU4kca6mq%2B8NqYHVtUsN%2B5gd8nnvuWqbDX8n59%2BD0acSWYX3ltwqKU1fO0AeqPye0yiCvfjcxbHvWs%2FRR5XMZVX%2FI4UglaeB3OBFVwP253XSx2x%2BuU6QhgZ%2BGPQsmEXq4vQBTxheJoBdgDf07ZcBEoGCumViK7vHhO65fan%2F8MKzP0MsGOqUBNKFU1U1S2RuiyUgV5PwO9uFqha9UGcrOVgYHAZRV7SVK2n4vs4YpqzY%2FdmQTJ4RzQ2tbFCf4j90oDbRo%2BC4faIbLVgTyIEKX0D3b%2BPJJ9NGisV%2F6jziKu1zM6MvK80U9IzeB3fGyeeYTbeqCvxpKkgQx4UQCBIsSrkt2DL%2FTyy1QwtuUfVmuQ%2FrN%2FMg2YpprB2KscnZI4Mn19%2FJ3jmT6cdssCV2X&X-Amz-Signature=62438e8bdeb8c91df192ddd4fb6c1b688b70573551027b68280ee19cf1d0a4b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

