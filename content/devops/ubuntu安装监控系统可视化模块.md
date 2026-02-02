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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=713afd942e4e1a9827ece53866191fcdc31771c871d2544d7a0ae248a31e9ac3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=b2ad548dfb8dad617d2ad1e39cad4f8595e444862f6de31b317a85eb69fc9f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=37fdd8354bdbb574e20232904fe99e03f06793e7ff18a98afe952f67a430ba31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=bc9f0093e337eb120a578f9e4582c25db0aba1248917fae65def73011e3c39a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=61c1a073abde5c6acd0b4ae0a1732ceb06df8fefd942d9167405893f8f397cef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=32f26441c79cc42d918f4a0edc4a4760795c71c1dc7b845369b099c93f013c5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSUGVCK%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCsWTJLzunN2RYDfY7Ld2HEUE%2FO%2BsyxZugy3UP54FasBAIhANoj%2BLxn7Tsdz%2B9iHfoFsytg7AC9PLHoNHvndWOaU6i5KogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbKTAToAEV%2BOVHQksq3AM8%2F%2BA6JpuwspNg2o54tLmYKnqFRwq7vhdtxBDzUm6qVb9Q7FKV%2FeSUR3xuZ8vN2oRUWhYwXjiNYMUtkel%2BjgU2AGOr5YeKLOy%2Fm0cequ4OJEeQi3DYi7D6PSBwdLZ87pMZ1hzoLwuxsv0%2BZuLHTxXkcpgRTmZ3SSR9uAcZXyg4tO1m92xXNcXmA7eQuhJDIviUO%2FtgGDDbMeoBZxr2j6NfC38x6ZN9l7mDIgRYzpYo1Wf9vxb%2F%2FCDwysHbFoU5PtKZg7RJspL%2B%2BjOJdBA4ggkxO50X2wgWJxeJUEFJ9Rd%2B9%2Fq0%2B%2BqdfO5KgZAfV9OYxhsvuvOw2x7G21aiiHgwYET%2BwR0uRNuKi42FIrljxPqtVJ6R1zeMEGheO3uos4J1NzQkNNrRjCZTVUYFXbjgkeKjwtSZVL%2Bq7BsDNXO3PpmQCrGBg1ehb5j9Ft6j46Zm%2FL087NTWdhWInjFSXjzCEwfTKbzZJA00V2l5HG0RfZ0jNw5j1xCnFO8H3Q8J3V0lGDftk%2FYyxvEanDIJcB7bJ2ff8seS8Dh%2BUnsGuasjyv%2FecXRxsvYRjr%2BTyqcpCD7H%2Fx2Zaswcj%2BbJD5X1IqHW7PO0Eskf0Opdw9D%2FdnRmi4a0Yi27queW%2BswNrMdayzCtiIDMBjqkAUTb0IL66MM63onhEAUU0BeqGBjRm3V5loKN9XokSoYhkOOxxImYKn%2B1zmaKEaqUNSxlxW6XlAZjxj6HBHD8pWArZE8wLNJCKtOtG3OzZCj1TZYhqKCv4f9nFWppy%2F6j7AjWiqf4%2BTXPygXu0kNpniuakdMwWzn6PpvEV3ZjxK8x%2FYSCV4wfyje5Jf5289KTZpObAyfhjVV1yMz%2B5Cqu0pBaZ3rF&X-Amz-Signature=7ba7df48a08a712d5119e9f52f7558dab7d18ae648ee197bde9c2a431e500d60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

