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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=bf2ad30ccb99dc0fc29ae44d07c38460906fb0de47e01c68ff7c7ee389561908&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=ea8574218848e4de602541fe8c317e39e13039748fb44ae559b8ef77c7ead297&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=a457474294204377105cd58db3303985616e9b2593ce9d78d3bf2ab4c4764fd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=324eb6af3718cd38e5ff5a8528452bcb6ef144ed5c0b2359d3cd30f9c9130b43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=0cdf15a8423b18742ff2292286ae4b65e1c95f83438a504baed90089f5935a6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=b7e0ccc3a64ee4be225972721dacbc43571589d8535e21a0123b3a4b451e4c9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EBTVR3I%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmB%2BzrpHzuiMv65W1FX6kl9Wq1LqvuHwP8swX7rSfs8QIgZzqqC17g6aAjYw78ik1av3RZvOaZIkr3MV7RIZSndooqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1dYAQ%2Fa1pSyjOlxyrcAyeI7H5YqyNRqv2UrLyxl3jCTus%2BfwfvsVT8KqhmJBJ0af7RmrMEReaKaPOYj%2BEM4vN65SqIz5LdwhnMStt0xBOUDpKWYiKg%2BRX8wnZM5%2F3PWJSAIx8%2FAH6lIAXdj9uFNULHiP%2FGh51TYw73ehcWuqdtvSj8lqecOtOlffiM57Jw9%2BOqmdPmejJSenc4eFy2VqDLMmPYruk%2FEOzi%2F0EOh2YwBATnAncphfmsT4GcPqEiS6MZ8X6qhnE5U2AMkefxuJAT9noYy16QA5iSkXnCo%2BAXDjrQffeXIVYZwUF2O1bd%2FgC1nNI%2Bq8cwkeKEwKmud29Ud4E6GotQyjNHaZxCjQ%2B%2BTksHGXdU7Zbw1rCnorXKuz%2BJn55kPUvEBmJbMLvP4a5%2BcMjd%2F8Dq8lh131%2BxrDd8NhDESldIc4ubrfomr%2B0BlbKIxKCQP8ORI4m4ekgeKPBekgcRDuNk3p07yDJmmzQ%2F%2Bu%2Bq0c5NditePvnUryu%2BDJZaU%2FG6E3O8Oy0dpRzFgY9oFzsPgJMwI6kPVubk8Yuspi5mhDcK%2FJFZweijBjhyec5%2Bbt5XguXiMxGwylhgi%2BpqUwOgjcTI8STuzycvcP%2F4zsnP2Gh6jkOHv4dpUj93QflEAkoHxIc81YnvMJu1mM0GOqUB24JG2ACAg2TdExletJ%2FHQy%2Bfzo%2FBjzzEnnwKse1wD5yLDQ4G69OxU5WmBBCLHeCYDrWhKA0w8AmRxvT2BF6zlCdY8xSxJbZa%2BiOO98lpo0ch3n6MRXLFm9%2FDqVJsS9Xkb1OAX7oRi5KZLw6f23%2FepoEGxuA4d6PDhpK59rzlx9v6kllDd%2F1QVwRqQytd%2FN3boAMI6PBJUycmEBs91RwDH%2BuLmQWf&X-Amz-Signature=7ba02df499add0df7418b1018419ebd7c4bd44d4721e6071b4aa24604f063530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

