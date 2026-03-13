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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=625b5cd9bbc62d36f84156d5b6ad0c5ceb5dab00bad84c2a1d56022d8a2b38fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=d47b9784ce6454f0c916cd76a5fe0e713be7199b9916c2859f8004c1806db690&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=f51f3f55e2787c5285746cdc07ff9700b95a7059b900fffb161a63aff6009c25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=c27ba8bb06cff39743bed0a7b16037251a3fadd272c4e8034882948fb5ccb1e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=e0e8ee723c3241b52da75939e704e7a634553f6961f47c3691ea13537910f4fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=b6c984e91e2bda97d684425642d764582dc0846565fe17c828f411aa47aba32e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOGH742%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5STKZbLGU6OLm9kOqjUaybIxXS1oK8qBuvJmqGO8acAIhAPaEzakT1ml%2BK29vJEqn%2F6WzxNhmAr2UGi46%2F9HdVenMKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzapVO04%2F4WTGvKoigq3AMRehwsXVnqjd%2FxorhjF09S5d9BUoLiHLH5DFsEM9M7gFBm4B6wB8go3nFYPHBW45t1IKDK%2Fv55zzLNQIRKAt8ZidxOZRYp%2Fx7PAaPAT1CHdw4XOriEEi%2FpZjTxkbGmTXRvok40VBBEq2Vd2TgKjJoVOyJzvIVVDMwU04Q064X2te5tmzXp1IR%2F0Y3vJsuqibFVnzynB33tiE%2BN2D88MCKCyYGAOd6UdHH4569v4bFYxI8StmtKBhEnDWhxPzTR4EfiLg9I7R9VFal7VyFMxSmDhL7amEX%2F3oEFPkhk8C%2BG%2FD9WMnoz6FvdaBPPBdJfkmXdSN27UE95sv8M5VyfirIGGf%2FUQ2602pVBtbESFtfGwJMKeTlr2EhthuGfSA1kniB8azbjxpbaEpuvKBY6U2lMwVbII4yZ4bNOywKyYKXHwqRl4CZGdbPuiuZxSA5z8kkARMBJwZBl4ZOpHhkDphPZTjZy1QqoVAUljZguIhuxlbDLGLGRyyuY8jz0Lz2HxipqBYQlkVFDtv8g3mi1I4oBP74Iuq3Ck7SQ0VieDUvLrXWg2qaErzXNpKR%2Bkq57aVe%2FujuJzEldngpmOXDmm5obQe5R6pXa1J6d1615qBEdnHHiT4Au3qbWca7NJzD4t83NBjqkAXgGP%2BXOkcA%2Bg37XKByeLS5S1o6ohMtZ5ba3toyCM0t%2Fdn1Ha4OapZNhkuMlb7z8eDzsgQLJ6LMUzX8KUlqOIGQvfi2WDNq3Vgu49YKI4MNczRRaC6dxBc%2Bi8HE8UdLw2iVHCRuc7YiiFokAFd4c5S5LdDI4oYNphn9yCZlqYn4xZwUF9MpMtgXxUlbtJrfPh9jX8536%2FNqJDnJy2vI3rzjXR0Fg&X-Amz-Signature=77284adaf4e40bb7ec30e6223569463571d7e768c69e7482a45e6170a74ba3be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

