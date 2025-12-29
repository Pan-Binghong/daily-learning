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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=bd548486b091059bae08839ee0398e6927dc8da7814257ebfef7364612de2b7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=89909e89e40b4c22e3e9ec056c083dff1ceb0c5808cd607e44a1b6b79539788e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=6dd21fa960630ca2508e6b4856d65c991c1dee68727c26fc0c56e0a93d88ab94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=9a60f99d91e6be4158dad42246f80dbe3c2b3c64aeb1755591d81d1f3b9ce75d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=2b2b255bb5d414ad0321baa32c5980a838e8da9c0350dc6a91e5dbed115f8e53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=8b87a2c24a192607d9c4f07e09a9bc23f59b9bee6705f07cd8fd981c1f6d2629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UD2V4FV%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDem%2BD9342M0%2BXqnEu4xvvNggY8Hu2yKUtxOUWADIxGiQIhAOAqrmZLLjJXLqy3H8gpOwiHJSjING7iM5TydywFDgNGKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzYYP4SXhlFG0oYXwwq3APE8gxnIz4Qr7VT%2FPHShi5Oxho2DMget4tzxLtIaRoEgO0KJ%2BYMuDGCbkVH%2BJxddEBwAXjvI6HFiGkXnQ9JhmUjRHIU7MKGiy%2Fk2N1Pubi97wPiNxIdEm3y1sf%2FXJceDLMsY8yCVcW4TD7wzrVKH7b%2BxNgIaDaNYrSjIVTsQ1%2FG38G026mvDW0wSXGtIfOSmb9lfh873fq6UBTbxqYNxYjWEvYdyBKGQ2E%2BIm8KaDrlDKdVFvrHe6SaMfdiHG5yjv072azJ%2BGIzcacJticqHmYUemWy4ObbOZsiJjsd9ODSLwxk4URVDES%2BFPg3Qfh9LMGCX129V62Q6AWGaJd0xm4iw21M3m9XyJ3f5cU5mQuPBukE%2BlU2Qo0FNu1CEUIN4zTyRNdR%2B3sgRZimmbg6bOVYLUfXPmaHL4EZgsv6afXWCA%2BUBk6EDQbobgaBXIN5iGe0e1UZ5eE0GqVJgR3DAXy2m90fWz4q54XHFuub6yw5f6iTWPVC5DoDbmmv%2Br3UP0kCS6I5KWLlw%2F8XF5b9VEUvwtCA1xCwQznE4KA0og3Zl2bT7wmPLeCXLgz1oHv6f4%2FGsinzbKoHxEiX1E%2BAmZNX7m%2BEYgeA9D680KixwHT%2FR52n4cBySUb1p3CIEzDdmcfKBjqkAQ3fkYAw7r5MXBvkvHXxU0VCtCOsY745e3sxEdQKYXg%2FzvqxugthZH2GZPx0xLmXh8JKgNhXBWIGmzAOfNENTtqoZ0ozmisy75e%2BreCru0xhk2hMGLEzMqQOZ0h6PXkgsAtKuBhsQpgxxaN9VDpdUL51J04QLf1QFWgBsneq0CmepdaU%2BaNhpqrGvTdNGYYVGdNbCeLJE5%2FSomvCYjktqMrM%2FOia&X-Amz-Signature=1884f2fb19d139723e3187f8a809eebf2c24224e9a8f6ac9f45eb25c33981344&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

