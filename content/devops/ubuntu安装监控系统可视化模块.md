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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=0243e999f566471f3331335112e0eea7c968c31af05ea99266be56afd99c7db6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=c13b9d99a368bd4f74c62143b3d885c5d430ccfc6feec479ad789b7e35733bfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=5f2b71f119d40e67b3a466650133de3aceb0fedb73df043743d3b7b50ab8246d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=69d6a4ba0a4cfecbda4de86a385e3a9298bf194c0853e7233b434850368f643b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=962f37f0bfd2b5629757f6a69311ef2d0ae7a97254c8cdb0d3297b8cf2c39496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=4ee783921fc77cfc58701e97e6bbe310630415eb5ec038c56e3d74a53c84fd78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=c07ea20b53bc525adf2b902b60fa35ffc789d60c59535f9e30dcd0ac0379f9dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

