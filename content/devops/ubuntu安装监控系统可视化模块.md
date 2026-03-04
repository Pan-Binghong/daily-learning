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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=632057f69f46c00b530072a732707b411130f66da199835662d6fdbe3afbecc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=05fdecd335d2e923fd8275ba4872f00936525d18b58c973cb4ff40394333f1da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=4531059f1e51a2ef92bce048b7b70d7a226d48e2497e01c9593c6665cec4b9c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=2ff99792df3c4bceaad071b2dd96fcefd8c9dadc2def8070690fd3d5356bb89b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=705b18716716a99fcf044b8e9160e869a95dbc128212a1bd85ce3201ec5d2848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=6a80542e8260c1b9542864512f60fffea3fecdc8dfc0027d1395697cfade6135&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVYKXGP2%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDegR2CVNzMReSlcqsPap1xIUhOSfVGjpwsMe5cOgf0jwIhAO2SXYaJw%2BLEzphi5St77W70QFCDJyuAI6taluh8COxlKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZx479QNMpsnMYIaMq3AMYoKztEB34YPPEEsayVBtanr0R1DyRq7Yyfu86DZDjSciFnDB%2FUHWHP224tQQBR%2FiSpeOyfZFZpbnLiP1vG7RozPFQbJXDqlbUdZckabGR8JvhRPFuHFF0S1WEyGjJB71B03uXskVy%2BtzHhKTOj2lnmp%2FCEX8t8QZ9cMc4IdfrxwXgXcO0BigufZxNDs6DQ8p3c6BCJmQP98tYhvltxlsQa9DNs%2FxpnLW4aH9z9H574FtegzGBP47wITvWGOndVqpxHpzX1cclVn16h0D0SbnReTQEJj%2F6fW%2BhzC1i8AvTS05hpJ95KRzA4%2BMP6cubNA1yKlpThABeBH2qwT9by1hJ1tSnJeoE1Irndr9lD%2B%2Fg4%2FkYgIYDl%2FNWOqjaHMhS1QWw3EKDVwqH9xYp%2FjUXqGK%2BwR%2FvOAe0kFYJMC5jNIoXqLDuKn7jlGk9slMp2TEGqUDI6gSnOsWLomuws7%2FtJDBqy%2FNvoymNmuDg595X9nj16SEalFHizrR83S7zbvUPG6RoEPyg8C4ZS9S5stVQRoj%2FaZoeO8DumrIsgDy7lQskq0IJkr5dZfI6aP7VteQ%2Fnh3zpEcOPX3l%2FKGlL4N%2BCDwVBfaZvaK7E0RQOzIDft%2F7EKqx19nxTshQ6xWDiTCRmZ7NBjqkAblmzyeMSQxH8KLl6yETXg1ieuEOdtpcGUh5BeBZRy7CT%2BqF4WNtKHs%2BM%2F2m2vvGazwXDvQvR1%2BwVadHYoanw827ZFKn96125qL%2FOXjJBEInNybWAq7ntmtKL%2B1mpP8TD3OEh%2Bji64p0ttKYVYHBu4FTXseUTlSitnjKNyvVE5sLqhOB4y7uRupc9UVJsvH7Q8bPdrOp0jjU%2FXrYJ4uKhbSSKOzs&X-Amz-Signature=084cdd39e6c53219b1cbb810c92a098daa435828d850eb30f9a9cf6090f9e973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

