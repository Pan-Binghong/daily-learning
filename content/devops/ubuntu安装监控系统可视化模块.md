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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=0f74fbe1088099775d8cec2b93b9ea611c09e4c18cf14811876e0faa39e3f2ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=723635a56b868886431a1e21b814ccaf7c9c1cd66ec5ea60a723073e2bf2ae11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=2be1854b0a5f0433bb3751ad6e84f4555bb3ef558755349ffc6f636df4ff457e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=713f403577ee51edcd6aaf15fc57c6fd41651d892caa781a595284bd143dfa97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=9b29a935576e04d54c8945040a792d5b05b1febda61b536635116f19699e6540&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=7d49455edee1300c0a365a2b6efc84aa61a2ec25cd18927a8717627208d712c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXXZAN5D%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCUvB%2B6%2Blj4sefLFJg6a6RE748RiDUl7KgNWQrH4nrlPwIgdP0FhmVlRDUCG6Xq2C%2FWP0D4svKLcpZD5%2Ff2gRqCbpwq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDMgnyzVpwJqC5WiPpCrcA%2B0nu3EEZZYUuYlYk4vCjiDPqhALVZnd5jZXMrUSVwkyLm6ohOHSQIWqk8QatoxCcsh05NPagZ%2BOfnVn54Nj%2Bs982tx33AGTncuL58aZ9oDwaXF8CswRkNe2P9N%2BxSd0L%2BoAA34mR1fa18Lh%2BNuXdAnpmmVG42Jba9JdDlALHMVC0JxtvO2nwkRo%2Ft%2BBj0BG%2BjDTjc0qirzL6%2B%2FuMy0FXyYLfgg6KWitNmQ19Rl2Wy4tTFda6XtN%2BVOMZo6PgyBijFWKvmUHQnV9C6IWwV3yjAmaJmwxo3bVD23s7QT1qRJTDmT86ObUlQ0avmqhfrUvivQx4Tz9p%2B8j6SPI4hwiYcUHgx2pOEhoyj8Yr0Afo7Dhw%2Fz9X8onpB8aneCVAiJVUOF1Z0aWgJwktIhp29THC%2Bg43OBxb8aZS%2FqYnANW1BiLvD1bvmnHf0thK4y4QJIzxxw7KwVNp2UjPgoy8XigLCb1m9q9oPSDvWnttEg5OGF4SASfbd%2BrJJ8RapVvhrqDuMIb13aKPSgM47QeJXRbHQLjvNVT87b3e9WXucNL8796jkITNu3B3OSbS8qctpqnyvTj9IKj%2BAEklK0%2Fr9BxJnvrM0U%2BDffcw8zAFCDFzFQsDRxDq88s2gPLnTwQMJCissoGOqUBiSvU5aB54y40Wn485qid%2FvOUxTG34Ff6Mlgo6jC%2FEiAJsqN26qJ2bNurJ%2FN1pLOV9alBUIEyuv9nfWLeB2PMHQJABF%2FfKIgqk4K%2Fk%2BRpNYKnhg072klnMH54E1hGKIDv6wKLcnkZOx5jdUqDmdafhqnXw%2BdCngNsS3gizJfFL%2FdlG15bTtx6djxsqs8BTItMHcTVT0%2BtauUyMxQMmT5%2Fo3Uo7HPv&X-Amz-Signature=7f3253a4f232427a5b1ad1ee4e33f76bcf61045eb54a9a9fdcf0ffc95d0d28c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

