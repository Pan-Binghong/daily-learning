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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=6db0dc41d5a8005e31ed77b3376b23aebd96ca6ce2f4c7dd06446f001bb0ec7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=ad6cb41961e1dd0852410849f085058d39cb36731f51fb280ce962be7e29feea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=ae717147e3d136bb6e364c677cfcbe3351e1a68797fe3ef1dc234f346c03bb4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=8b513efe7110f862175926370cfc4f3ffe1e254e28bee639e2175cc9346f2e9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=13cc10cf23056a7fa0d8d6fa73e78c55eb0752f992be200479ccae324f535c86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=b9c0508fa02400ed1a01b84758cfdfd32c21a5f695fe8f1aaec9e28a032a9b1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHVKYAO%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHrWHQHT07%2Fv9WrR%2BOMbm3ncdIGiOqN1cuOEQPfAP%2FrgIgeP7tBCH6x550SEKD6uB6ivauAh5wmTdMZS%2BuG3CUZ3kqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDIKRwOXkWOPuxHOyrcA47jx9XueVQBEIS4TzaqmUCgip6f7FuTuHXwuW%2BjWKuI5WyCAeTYZWjjdBgWUHjglYjW%2BZrlDh8DPk7CA45HNjBEaeDdAXTMopm%2F8%2FCcZFMZOGgVhUK2cOFzMPMXrdOnYPCUoFCLgjUacKU1bHP%2FDmJEyAXU09fDLi0v5OQ%2BVJ1YOFdC7Td4NLGgdFEknP5T4N2odZIDbYTcQ4NGfZVjz3uQyCxZEh31ZTbhMOTskPNbbDyB0pI4qjNQD44k0lDhQUpeQIa8xR1MXJacXqO5Myn9%2FpOgSn8N6Me1%2Fcr89BsKCPTWJPbMA%2FtsEicilmfEkJyKPoxqYmDuqu5AAWYvqX9RqnCNiWb7O9oV9O%2BWJfR3UoO2qGWune%2FA%2B9irsEJLn1AcM3GyxhF1Rp4VQ%2FzdQJ79gKQ3r862Ap8VKPgiNVKPqYmgQTDcBt9eVSs3VoKtDhj8O%2FXRLG%2FAjcoBF34IPIHUyOhEprg21GkiKR7FSv1Pt7z4SQkjWEzdcI9rjS6pM6GUl%2FVvs5skXP0plZHJiJxaAcnj1j45YWGhSv1dSx5dRPRNpZRCVMz1ooaspewBl0xParaV7UmIu0TbUEh7qVgqrFSDxnG1T7op6w9TPtP%2FJDIWhKvNFWze2%2FiEMMm1tcgGOqUB%2BUBRlof7QMzkI8phmy8cj2moIcP1Mhzgwmk6NyzpYwy%2BKpzQrGBqiAcyNB4o8Q%2F6Abknn7N6fhXjfa58ujqS5zlX6Vix%2FY4sePdHwWIIw19M%2BLOVNZFUdwEdDIjXIvb2ASVhAtSU9QcQnBmXwhTWof1pww1XPr9L0sMQo66de1KwUKpXfKWf3yVWqYHrq4Jtzq8DtfsUr0Jn238qFM8dwZaAPAMR&X-Amz-Signature=4521afd62cb513ef8832652e944be8666afa1a012e57820d0f16d53b1fd9aa43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

