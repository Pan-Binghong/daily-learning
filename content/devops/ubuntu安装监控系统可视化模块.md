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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=30f39e63dacc25d63a9d0c26c694d79f87d0570868915af2d2ea4ac75c008a71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=92b4ba726cd8616087b45814129bdf95ffe2272e53429c91c26f807af1644651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=38c1636b237cb1d6ca6faa4fee020db7b106c9e5734aadf500047a8dd951e199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=f2d45aecd5ca95d9eca3380526d4d83640805157c6d67d3269a8e36b202b0e72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=9e4a02e7274626510c3a9ea0b6dcc9b2dff40c84da470ff4903725ab8fea62d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=2460bbe81a08277a487d788346f5650aad869b262a795b1bff0ce6fe20c933f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3Q4SK5%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC43vKaOZyJdMSOH5QHT7%2BFn%2B32R4791q%2Fm1%2BcyJ8fUigIhAOX7uL4jppUukcKxg7pGPV6Z2bYHnbCc82LPOqUaFdcjKv8DCHwQABoMNjM3NDIzMTgzODA1IgxxZyp8%2BWTP5mP54ckq3AN4EjQdxHsjObdXmky9tR5PXatdFO3RW5ttI1%2BCxVOCA7MsMWjzVyeLNoV4wwtATrIDzNEhcLxxtdhMy8Sl9U7HpdQWMPfAGlRkbkCfzqnS%2BafA2QSK125DGc3gz7oji7sccp2duJyTbEkNOdOEIJeTQ8Idy%2Fq4snXQbZEh2MIdVj2e9jhwdMzE9tpy6c2VT8LVnGCWfkawgWw9bttactcm3%2BA0vAq9eI7Gv%2BrHZc1GScapSk5d45nV6ex7XCiLie0%2Fm%2Bw3u%2BfCx%2FjfIeEIzG%2Bbgy2kJ1qmHQcCaPl1RWC%2B7TJbP7lg7lKp9rnlEN%2BXfqsFuRgtkvp%2FOykCHzMTZqjchMZfyomc8lAJpbI5uIZs09W2WY1L5xIq1EQCL95dT3kR6NfP0gJLpxp9jDrMgYIhdJ6zsJ5N6SwzLyeKOT7WSlk1tm8A34ANDlth5sNnqe%2FHZLxSTFUwVl%2BtKvuPOP6xpeMkn9l%2BCshBq4wNshtizFz6Deu%2FjJIkrfYiv3le66caMpOaBl7cBu0SbAlH3jyqGX76baqC504CMPURc%2BwvhU7Jrm1NYgRR6IKD1xJ09IvylDS46nM80%2BhBdvzdupJRme4C4eNmsM3w3dcUVd9%2BXvXw8Q2wDxH5S0TxFDCP5bzOBjqkAVXG3VsS27469P67nAHSvewpqc%2FSJCcjkH7F%2F43QjM5Ej4wpHr9mKHjoQ9KzxALdhCCL6IY0ZqgMLVEDRsIKD0tkuF8YJVa6XqdeYIni308Vj55KgxMUeh94i8eApQ8nSCaHNTQ7enCRGsaSvcuwvopRhwvXgFNakilp7izOR9dhfVGRQgPiJIO7161bN5dRmd6XdNu9fswEXqjHaLyoAqqA%2FFsm&X-Amz-Signature=3036d7d76e1679b51c35f53657e81b0230b96bbd12dad9e3287c735fded73677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

