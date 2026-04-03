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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=df07c2c1a242ac7950e9bd27ae0a125e2396ff5ed4314f98865069ad6346bb13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=86e2f27f550038a130a700eff2f64c76833f2744ffabe664e6b936dd52e0a392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=a44fbe276105e5272ab6930e4483f5a76ea7e273a51a07335de11f6142ccb4b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=0cdcddbe14698f274fb5f7c275f0a6e885dfdeccdbbd2b19856ab204588a4e63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=f020c8d5279fd4ad23619bf7810529c38b9b0ef2646485ffbab5c45011a6a382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=c28bbef7a18de766a81c46246722e5a24cc88f9f2a5ea01ac0ce84af998e2732&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKCDLNXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI1ltf%2BVktoZ3QQgnj7HdY5nYWpAJ6syN3FYJf3YxFewIgbsCLO5P6Rl%2Bz19%2BBznpyXRhziH5aIdcVxphXTpsd5xwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI8U0Hn9vM%2Bv3YdhAyrcA621R6Fls5c9GcSpLpsRXI35b5N6tRUXGvK03twErxtFHK85LQ8D1kta%2F6ak0xDpQpOVrzYZKNU4G9d6fogEOFbdrOZ4gyOBtBL%2Bi8Z%2FpvWiShBvOjwCPgj4d4xKg%2BHrnJaHlvqyn2FBWqWvSmAm57JfGNzbZ2%2F22tuk67dGPpF2FdTxqo9ByXDUtwizpnPS%2FSmuKadXH%2BLB%2F%2Fpx1jQcerf3f%2FV%2FiMcNL%2B5%2F8DEnzG%2F%2BRRH95g8n7k%2FGnIBTq6mDmexs6pKkizpkFTfbEkxFQ9m4LJhyVkDVaoVZUrlRJKRj%2Fl%2FxEEafAc69peGqDu4o1kPZ6rdJUOUokOdtJENO1D%2FoiCrG5uwK9GsagEPP3JL63yjfOFE5HqiNJTRvpvH8GXUSRa297Q9cSiWHbZs82aFtm1swE8PTxoPwqJl3nFo0KU3t69DoQpHYZiYj84GPFsWW1x1COsUF5SQm3mT0mvoD0kdUtWsX3xWNxU8BqjNHFTzFEwekN8YmiBp58V6yF44SjZTJHZzkCLTQGXGY2G5ys43X062rprKWlNtJRvfmMu8%2BYSaUwyRW%2BM2zGiRKX%2Blu7d0Bvco2%2Bg1ncOT4tgWCIlpwztPcSDq1X3zbLrTsUT0SsQAoKTt6xP61MNPQvc4GOqUBL1CM5L84EaYHKvu0ot9TBYDFLBnt0TPnqmC3s3fGVBLDMXw6QCFC9NI0LnG2mtdKnvIAY1r7nVpeBo8GTx09bvBHD9SB8gsThhRpZlaW0ofzokzf8aajDzKNlBeY9Ppx%2BQwSYmY%2FslmmRJtl%2FWd3U5HYO8CedPQvcg0oGD6MqF7LaY8h1HRmioUrwv99naVjIqfRJBrFt2WixD%2Fnv3EQ4o6L7oyr&X-Amz-Signature=6a4fc313d50471bbe547a12173bfe29f427612e60d425ddba8a1303aae35fe5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

