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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=4a3d6453aac75d452b61af73df5bdcf6000f2c5502e78d3a03391bfee2171d9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=b988455a4bd17743ca3a784474287177d59318c898010506c6a8ac7d1f05b0e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=3260fcfb81fa0bf5fcf1a93bd644d3adf3afe072badfe1188b79b3a56186a815&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=0c4d6fc9a5f59f93c4330103eecce7f02977f92233b7274f6022f1db43361fce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=bb32d77dff4ea87b73502e64164d1c39b645a1c58f5e8b630af3114e406e5f9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=a6270037949e10a858772d5153388de8d5926affef0e1a7c08d59caf9e3f3fc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4G6DPHV%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXS98KOvYCYAEX3XA2kt%2FUzn1sVCvi2zy7Aizr4Wug3wIhAM19O61lAClGSwgN2wNMjYmmp5%2BEUXgvp%2BdzkwMILj%2FYKv8DCFsQABoMNjM3NDIzMTgzODA1IgyrxlpTr60xWCDg9mkq3AOtvDy03IXvbAhZf7js23y6SbnquwWkq1h6kdXr%2BNpBkkkOKRxukrBo1%2FkOEC%2FJDIjVIHsT5B6Xgouem77Tm3H2CADBhDOGb4xNS7DfeGFNnww%2B0QTawmah4exozQnTvahaHggiiRrt1F%2BdK8y9cwVtg1QY%2BIMcmyL9mwyMZ5Gh7aA9%2F6qCxPZ5VPwP0K1bFdzCvT93lAVPDHu7ghZs7lg8OYsolGYfM5h%2Fp3XVNyf%2FzyT4q8WqrmxItgF4ua2d3jkYpx5z%2Fu3fEvN1sBjlDrMR7hY7godqY9dokF0kGYDkLqoR5oD60mNJogyxgeqTOpdifYCAMG8CRvi4kvdBge%2FZU2yg8AVUuo7QobdWLlkdZAe3m5g26%2FayDWOKUy2K2Wrvw%2F0YCwsxw4is%2BIyzh0ohgYIL647xPXW7F6YT%2BsrHl%2FkKc3l3Kvn%2FxQ85djpFlOG4k5exLc1k3mEmuFU09y5IIX6PPg2%2BfSwxM9LtorPBDvUDKvIj8nK768YXPoIx5ZooL1zXGRIZG8t7dQq69QrXTQA0HtkLR8l7yYE8bG%2Bx46H4hWTfhTns9Y6FyS8i%2B6tZ%2BZ%2BW%2BOe4vPtICpquDBGCDd4O4dQUgadEAjsLwshSQdsDCq8jiEUgB50I5DCtidrIBjqkAVrqrAb0RioQF7XtuB77zMYpXb6n2UJn7EJusHYbiO72V6SFJRJ8Bp%2B2DjvZMlB758tZNI5H1s1BaSWdHP%2FS4UW2An%2FhHncUQSfTn8DiGIK0KUiuhNy8b0gws64mpPf0JTlln6kyFUKQQiSNlCweGg2CSRe2qxyngLcIkFBJ%2B27id2IoGR0b8iwaQnXhp4ef102goslwJiy8F3wfJi7i47DbDvgA&X-Amz-Signature=592494bbc6f77c7b0693c6911c49cc575e495a446802cbce02638bb86ed22931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

