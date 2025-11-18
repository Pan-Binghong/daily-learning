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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=d248be9c0278a6f21415564828779252fbc52f388ddab300a2118dcc5ff4a9c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=06ffeeb159a872411036327e435e5f9c0d629bc76c9c0906675bff56d2021ffc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=0e5fb67401135b019e295528f58c4b0b3cdaaf19b9d4b57f93873a226e62c86b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=1bd43e8a2420a44504296ccad67afd86edfd82d7d95899f89f6a623b7bf67e9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=427444dedca6f9aeeb20345e75b5aaae15f88b65bacc3f52b972724c2381846b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=21f054b2158dbbe7b51aac47295a21446af01892a3664f430f2776bdf85420ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C2GGWEQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHV8%2FB106Y9Uvhcy4h65xktl7XQsW10%2FJ2S1AfGCld%2BmAiBRrHAmUgwYQIX9dCX1uTMIjCSiDvRjtn8IZ6hsFghlISqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhRnTx8pkGXdesykZKtwDEtFdqY5EixmzFeo2mHbEnsAp7aYa4Wb9lX1lwY7MXKvuoNCdFnuN1In4PrC9zOegrdmVaoxSdK4IwCIfMnb4Sj9am379CrWU32gxHd4j0aaP8AfydfRWy8Va8hNra2xOYIaAAp2jn1U1NlDFge7jc7w64TSV9BLcoRMInXh3udDOXxckgRxJUfyh9lyUjPlyxp7vjnICmesbmhn7Hdq8IZq%2FzG3SrFOmx8JNYM2WxQUl1u47OD5WZW4Viq1apnvdTZcz8jfxFnRlsGATKuZA90KznkcUOuhqPBMzvNwpdzFr7p3ZkIC41GycCq%2Fx4QB91TR7td5jBhbr4bfu%2ByTFRlEetL%2BIPLkcrBGV5KVaEJ6kR4DS8xKMzKN8Sotu7EXl1nGVKL6XXZo%2FW8Xxb7Njl3qLbjOIy9a5BumEiWOatOFjmEgvaQ7liecQGaTwzsdswrBfEiuRGhRrhhA9qfDG%2FLpYWChqpsJm8fU61%2B4CDZSoaz1phGRnVF9%2FhI0cRsziGVwKLIKyNbZQFEK8a%2Bjc2LWNEnRvhBDKsHqgvRVhM0y8%2BHr87xUwxil8cJpWN1O4Oo3m5l%2F9ukNFjKam8EpRF5ChTukQuWGSTCpcgM2QywJtc%2FIBa6ZEAfEX7HIw7pjvyAY6pgGQMznZGfFb4fRXNz0brG1yR9bFVnbdjKlfytlFtPQI20KsTHHHKVTAMcYEpGaDspRXF6IHj48Wlw%2BUU%2Fn5wVtyHHI9C6gJMiCMo%2FCgJdH%2BfG49ygx6TNfRVnS7b2gP0iLZLL1S%2B58HcPhyPIR7fK46y%2FfVtp6ahQ%2BxAeClEPSD6BwftHjmk9nZ68bQuKxfIu%2Bre3IN3T2iU8Eqw2LvRVy0HBJcC9Ry&X-Amz-Signature=a4ea2f3eb751bd7584983e69d5d8b61abc5090bf848a5a445affe30c919090f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

