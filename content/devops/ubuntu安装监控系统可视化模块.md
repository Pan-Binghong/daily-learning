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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=da8a8ee92bc398e1a0da50ccd4aa67572992c2aefcfc0414528c6284e4b2fc8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=f524f553ce4672bba779e3fb628267c935f4ad4b992524aa598b0e7a2aa41248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=6ffd61bf22048592bb9b112cf0c227cfb61cd8878887b99d5f4ac948198de7a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=5f240ee2186a3194549a41d7785a5d81b13bab6c952f1dcc45dc8e1a2246e290&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=9a23673abaaa6e037997d0c091a195ccb5916168f35d5fb73d9db888e2808183&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=667814c480f9b4f5d7f22370c3835939797841d6c8005038040dd55a08152765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZJ4V6DG%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhIh%2FNgeSqgbatx74p6PARIRxXVNzFQqQ6MbJfPKWhbAiEA5C6XQvpg5aENHC8BuOnbIGMBrzE%2FmQElPksJlqaafw8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDKUYp%2BmwSEJ4KXcL0CrcA90IHUIVZKRnXaMnrhQS7jJoj4EcopSDG3%2BWsqKwGiHTQNjuJpfsZ9utsa6MzHI9NLrXppudqy6fvBO%2FC%2FXxOxQ%2F%2BziAchR3TpK912NsJ9K2H7JG%2FWfa0lt2RhoWOQgorGvvT%2F%2BJen%2FE1vQDzL0As0OgI7fH6VijYmuvUcGU9Jq4m5nSaMjsNok4ioKuGPfZT64NEIqEQijG1PY8j%2FLhNSNY97Fkj0KJtVhRoJsUFEyqbG9nVrbzI367LJdIQ%2FXA6UvPpk8h6W%2BaMc4bUiKl6H7gLiC5PCB9dDLxHkPh2SbQoDYcbhF4MsC0kxGUrb5VLTAg%2FMHnlTxSoA9GEPrQph4Nx7THCGIhkdeQqKYuTcQmarZhKpO68HBCR7o8L8lWC99C4wy9xj3XNB7Eo4rde2Q0r0XFgB0LcqtvQkitgNacd5e9ZaOeqBuBVCwEytJ0SH6EDeGVmC98lBBT7nvfSfDwxER0OXKLnXIImrwXkbd1lt2EYgO54WWdH8zWK4hcJugFvisTYnKpfFy%2Fou5TZMKCu%2ByihPZ%2FwZw1x1au1o%2FO5o4lE0NPxs2evnsnMmQ6GZnIylixIlCQurcB809IGOS7Ok2pS9hZTUhsrwHmv3CoeS%2B8vn9ykzWsIWBiMNfRq8sGOqUBsZwGhnVB2vDh89rCj4tSNPZPkaiblEzG6kjSjO42Vw4PZH0nfT%2BUL3zotEQJTnkLAJRchhbPIamyy80%2Fq4mdfFf4NNrj9380JWNH24iYKr%2F3yepGqa3XYqgNiB44EYRhCjf%2FAYRNbo2h6Dran9umcNJfvXADVPpIWI6njLnr7NhDZS2UG662Pp3GaQeDvctxVIZvYlNiqDne6H3lt%2FpdQRF7cGNk&X-Amz-Signature=33e9725bf3bf02488696ee840dbcee67441b34caa4e8112575d91015a8524d9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

