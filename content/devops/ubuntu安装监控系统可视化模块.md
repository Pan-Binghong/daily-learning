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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=fc5851f472e01f91e5856bd1c068794e7b9dc6eb9901a60b384c276195a1e2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=ad431f43e9c26f5f9386539ff4b1588c677ddbaf236cacd92a364bf12de6992d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=7e8bcca37f2c814583029f7a0f0f2e589149814da8ab14351035bbeac0fd94e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=0960dec38c4645cd9e95bf69355d18c8169e06ab46d3d101c89b1862c2eb274f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=2eee71610eddb919e0ad4101b4217c79f8f6cdf7b37e6dbffa5c67e9073514ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=821c5b1601f4a96147ebb2ca8772e6af141e09eea85eadc217bc4cf8da85ab83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMVHUUAX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtThvDUU3rNHNqOxsvk8oK%2B4BrcFLj2HqdEahpHsJG3gIhAJYPI9mM%2F1Tmju6QwUyTa5wF2BKC9KPpf%2F9e3WjZtseRKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxR29R1Gx4UWhqI8Rwq3APeG1bw6uA9rPZI4zh3f1dunBA5jgp61h5ZQXK731uYikcDzPaxi0ZfCFF%2FKwq%2BhTGTdMBBVb%2B%2BBMMGQHskyoTKKUaOpEI1gQCVO7vIgpsJ%2FcpUdqTI4UjlT43hcxCGW3E8dq70Y0aEawMQcB8w5J65P4wCgpt7fdEJjLcMh%2FydphgSTdOj%2F26wBOUvXoWUF9LkPJKTU%2BpGDqPXbNLcEDeYTINEF1z2vG7myXn1%2BVR%2FMbEygAGxD6RSyQk3CGP1WeTJP1u3PenPe34XJ1Nuvvsvtjy5UaneHE0VASQGmzPS5O83tySF3K1LVcG019uBxTGEsXx8gWo7tOqA%2BEpyzAKs6Evylykrt%2FcW7%2BbDXxowgiV%2FLlpVxtHPh0Kr049KEv5TtM2CbTNvI0hPUAqYfBb8EwM7wU4BcHkEC%2Ft80kqMdthcMDOmI7p4kcTRdOr0xGmqHuNXWgHrlsBwCQCsNvyE532JBzSi3rjkBxYXfYWOnKbpqJMElaOdfYOhJd0%2FdPKBUl4mLlkbdvnOSwIpLN3%2FJLc075nOXkgWxVdLnaAr54JrlaM4LAP7Is40TNHgBX0Is72VTEbf%2FR3OKjc4bpXDYokdazbnWsbO98L1gIaxXjp9vRbD4nsLI3N0szDl9LrLBjqkAfe141%2FEx%2B0QGo0NdhRD1SxzCHvF7VZffigSgTF8AgB3DV5Wnpouz4xXOMNzw4SWS15OFTSH2MDUKdg8Bs5reU4yYgxPgjzkmI%2Bwj24G7nbyh5t3kdFgW6OzpZnDk8uKw0Dq2KR47J%2FIJZe7fArbuvebv7jYtztIar1qL6idp3SR2Xi1hpY%2BBoDxx7OGmP%2BosrdbNgcVi%2BR%2FpmVxLBN%2Fuu0p61vI&X-Amz-Signature=8e0639c30e006ba4599de8b4c3519cabb56f400f5746f4602f28d628e987b97a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

