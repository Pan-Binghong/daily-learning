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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=6c2e416e2e8399e58aa7392a7c42dce5f5903a01ad394f64ed65e171708938c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=fe246bacfc38e891117d32f5dedc4391676dbe4d5e0b93d4187de935dac61065&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=3ba803345845ddab46937de215379b66e4cc500e84d0a82b4fbcf85c27831ce5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=64f5d660fa3b800f74b1309624139e9a0cea5d92379bac1f4e8765451136127b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=62411d06328e874a3914c4fe0f9e8a4d3c93171c7950a152617487ff2ab0e9b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=2c1f67ab44f11823d320bb6277db7afd01cc6358c3c5131f2e8059eb881a18f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3EUOGKF%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSVwUlzfgO%2FINPof17UoX9wq8bJdiElPnmIOxfQ9HiIwIhAJtt2LkYOdgOEGrUON3IO9q9Ub84kcbmT4%2FhfdbU%2FPRjKv8DCHQQABoMNjM3NDIzMTgzODA1IgyEqqAMuO3YxIAgRN4q3APCJj2s98X2JJJx3y0M7eKI3M4A3bToHBySYhdjNZZr%2BGCx6uvknUK00RG5nlyZgpP8DeOBEjO527UF1JKjQ6xMAnuQ%2F02QevgncgOrLv8WdzCctlyJzY4P2TI7DGIFSKv9VjuhCCM0QbkoUcHTG3RI8KgPsIgkveEWLCUybm3kySL0YEes3wC4Ka%2BTrlK2a3P3J3mmR6xzu%2FFQfNzOfLqj%2FvRywwjZA5j6TgW3jAtwNmZREiwu4iDRnwDepYf387WJpLCqORf0MXz145njxirDtUOqO7VxJ0F0SaY771BncGfIM2taXGtZfDINYTotrWDmz4KGAtCgO%2F0Z9yFGvqhfBmtmk77fqfvE%2BtYkDh6FmSHFufpk5F%2Fkg83nUv2and0usTWqH6XDNsejfHesJAVLXnZ0sDg3JacI4PAItXV6WcrEllfkoTv9BZKQlZxzRA0CJmFfl%2F1jY0uGyK8ueV9P2BhLrvuYYz%2BfBO%2BiFXNqIUlXOzHG%2Bkb1n0HUU7OYHBHz%2B%2FkrPL%2BNyxaK9vL8KG%2FDfzW5bmqoppA0GCnU7%2BePr8WQopPFUkFaKW%2F34CAiIrLk4eXAgxkj%2FymuopQa5jjZOZDQDn15JZnh2Gfr3vlvpWQFbGiR1UKq7JkDGjC1rqvPBjqkAWnH86Udi5FQQ282Yjt0%2Bdeo0lwkAFbr2qzLPHH0njAv%2BvICT1X3ne8pm94%2FgIMAzCQgiLjAj%2FMmF1L%2Ffjk%2Fp71mWkwmjekJ2GFytAWnuF%2FPDrs%2FifCf3Tf6CL4dTWKwb2d7DDsoLUMOa66taD4j46KmCjYW36dMGP5h7lI%2FWjReNP7EJiMOZHKKQDJtCxOYM5OMMNfoDN1u50A3KMl8PXspShVh&X-Amz-Signature=58f26090ea8587b5b916c91e55c648de9e87b3e92fc259343e0afb0a08ddc480&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

