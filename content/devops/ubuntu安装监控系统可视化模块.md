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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=6feeee1b82daab4abc55562cb655e58ef70e2c14de1f4b718fb3acffbf118ae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=09f918e153b1035946aeb8e3bfd4fb9e95ec58dc741dbcd8fcc56b9870beacf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=9fc9193de44c86475580205e1855ff055beda712cc4f87745959b605aa0fe083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=c556ec02c5306e40105cc41ff44441d5c22cc1954aaa63c4b219bef68f7a685c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=b1ba7a4c9d8720dccdd9f2142cbb3922f4a676a62f1cd57d5ff55451bc942cc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=4bcabda2d25e91f446bab3cb21afe288941ed0bcec4b189f245f062092d047cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO52AJKC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIAaWL%2BZQiGP%2BS3BLVNMgXZx0ousIA5tMT2uadgcnMw9JAiEAtTzB1Gf3n57Px4PmQab0UitGaHqZH76eU6aYwCyIjZsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGg1QKtOWBYjd8WrryrcA%2BXKtnkmfvS2ASVUQUlz3LGn7S4HqUiTH3pnC0NgxWwb1wlOAXCVfrJlnPW2NJ4gYhiX7ujbXAaeSCrFKa0YSy4vJes3P4LjPKwA5j%2BDN9G3F9Ci2VSZcbc0WNGSbVxP15DXT5vN9%2BkBH6mhpTY4IaxlRF7fc6ezd5ofzzjyJQpUN6nao0nFJMb9DQco6yzzxoRsdH7Dv5VH6jW8U4jcfZ6Y68RZ2KA8c9IOrxmepb3o%2FJDW1h5Mq0jJDxooMR1LAAcPwgXzH5UPOk3eHBeCd0J5be3uK9eQy1UmyIbu%2FAf8WehHNltbhGTwrHXJ8HfgPVwFP5Zp1X8vBPkKXs%2FG2upKitXWyALiU7vPv%2Ftqm28cj5TtCAKg5lP%2F%2BGTQrUZE1EJy4FUWrNRnWSBJJ0OzEigwHBuYGrR1igBZXeXrwhchHANGa32g0n7vypd18TCP1GYSeCVudj7uLvHCueRH65kOAiYpTGqtFPRI%2BpxoELCWaxGRqn1BFEDupP%2BcoZqoi%2FK3vV0BO9Ejj1422fAtFe5ofLn%2B%2BT8OT9JmfrXrZaxX7QWEOsMLPKlvsPg1zm4lTeP6%2FXd3bPbNrtOJ6OYgdjTU%2BbJziD%2B5a6X1HHL7nAVTX%2Fg9kNJxjS1xvCLUMIi%2B3c0GOqUBMwcq9jRVC4NDxca0VdS2Owv4nuIlV7oM88pNgp2eE6hV47mvHn3G%2Fea4NDi3VG2wO5bjX3j%2BJ2T8wWuloOdXRH98HxV0r4lnD79AUBIrMNAfEvI1WZp33xknyzEFhQ9aCKgSZyXubLPYBQ7n3UaeDGVJ%2Bh3mZmABst4TALUtANLcMw2p3wotzpenOU8ukYTbdnNelc1tAFIYhaHEsa02F0uavxJL&X-Amz-Signature=5fc9b1732b49a224e9d43d51bb3d9d895462f7e9f33d083df5e71bc135db0a1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

