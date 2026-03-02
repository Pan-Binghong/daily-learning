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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=f2bfbfaf8a764e618f1ed3772afa8de2820b317f73b69a0f7837c4aefedea00c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=8799df1e25414ce3a59abbc1c51dca9a4792815e521a8d4a6fe46db1a61b414e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=268690c9f2b4ad4d81779c1a91744d08d47a8d58bd52319e625c904bb588c718&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=e76af5b7614da344fd8389edd57836c94a0ba9dd4bf2d2dce19a43ca30435237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=54dfae7f669d3e3f77db6e835a0debd670894668365dbcad49c1a7632d7f0371&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=aa9218d2d29d7fa12aef96ea67f81da3a03460fb6d95d46a8a5aea48f4b65c9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI76RTXB%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHfqKGhvs%2FiSzJF3cy5sV9PmnrzXEAAB7cnXD%2BinoSmMAiEAzNVomKCjn40VSNo8DHOmBCFlSjSm5l3d1FfB6D5lmpYq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDDkf1s0%2BvBBNVM6lbSrcAwKCgNohHl%2FSQAgK7TpGYxLfrNHBuAH5nXja7gkUtfTE%2BBYxWmojwQGMwScoT9Uz7%2Fy%2B8Dt%2BpmWvRN%2FUyy5AoKiXa1nZ25PM%2F5jMuBTwpFZ0eeaoUBsc7g69EFfg70zF0Tn0PHG%2Bf1xk49HLzwzG%2B4azoN1pmhR7XTGIqwkHwRZcwSj6iLFxwWx5LAYZpPNjqfMdL9N0Q8qu8rDxWI4WngWFrSqGBSadAzEJSrxEayPqZA0C%2BgvMIKNiyrlqZSkIYU06ruCWn5xZjWguZCcucXLdoirhh88oDlsdNYyTiwmKtETQDDX8diej%2Ff%2F6n4XWXRgEAAGMYCJ1OYCebInMAWh6x2yWXXuaWYVYuFA9he7aeAFb%2FiSSIudzoPxayaTnqUojetsz15BKRHgeL1rdgG3gkH8qjs%2BIB%2BZv7ypBMIbDqoO9%2FWulFGevQ%2B95LBHKqJzN46KfJiF1mgFsElbo1rqcNceOrMGq9lLOzNc5iZEUiLwk3w%2BeUplIHEEXkOHHtmUM2PN0b0DPC%2BmyeKBy4O4U%2BBymZ8Z6Caxg3pN7CSFauxL1hMqi2KS4iVsLBk3w5WuLeYgdm%2BNEJrjhbyMw6yWf8Me6QpFJyzyNID8XzEMMnUNu6aDsFS7blzfSMNP9k80GOqUBN1ri5E2y26TqqYKCoNT%2Fe3zguvaZd7GkkXH%2FM4efZQAiqFgarsCsRC7JpRdLZd8hq2SXKkFQ4xK9qa7TvDDmWRMsL1WUGWa1mzYyg5v50uVdxqVMP0CyqjLd3Hn0FYWsp4lO%2FMe0YxBmBqGEAnRhZcFm2%2Facw%2FtxhK95OVlPXnM%2BmDH7IEN834jBoxWk5fchk4T%2Bf9YyCXMmwn44JQeFLN9RNW7M&X-Amz-Signature=acdfbdb5ae73bbc5b488c92590e170ec2eae1a1fe6fead6498854173d1a64d23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

