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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=83f43521e18504809df0a7333fe012257be7fa265c728ca99f1bba9b7d622bb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=ebe4580dae2ec837be142a1d31721741fd982fd8186075c115532fd159ac00fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=b8acd84656e39b041ca8838980fbdaa7dd662252cba0feef4d17d3364f57afb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=aa0c1f07cf53bf505331ff4419cb782857489be0c680be239a3c6eb308d82247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=9b2578055b2410fb9d4b4937af8a184ffeec8144dc17b01eabb5d67afc91e904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=1e26d67ddfada4e59923555092b017683b93355f399cc751b12b8fb3963dcb56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6WM6R4%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxmrTZgf30ZhYqkn8CPxjUC9gpIuYYefZXm%2BkRDpJHAIgayxesAVFLHrWiJMVFgl%2F9xsckaH8RTONkKn6VfCA54Aq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFkl47mkXUs48qMRxSrcAy5BYiKDl8yXy4CbVcpz9zbCOEWzB0lERg3pZoy69V5NWHULDdbUw%2FsbIyBQ3DLTM8Pect3s6xY0%2Fsq3GnMa9cMq628wBI%2BqhrB%2BEuUo7sHuKsuOiV4yEFscvsVVANaor8s6Liz%2FhdS7sB8LNwLsNrhqfu%2Bjmh4YBZS8tIsMbA3tLioAoFrepEmeE3%2BqcwxIs%2BWMEQ5qKncRwX0vle8SoNv7Anlu0vFFoAWWfzH%2BYvWEWMgrH0dyrQl5JiO9sUA3OOIbdQVHVFmu3W4uCdnogeaprEngMf9400hvfhbDTXu0sDt7XXvw8n3ac0DT0uJRFlnWeaDazuko1aTDJNFcAXq7wkrIo5h80iXJpBrK%2BHYleS3fZrH3tpMHB18pqp6e9n80L9elYxrOtj2WFo7zBGCV3CKs5GE5NPbMNm42qxPPhz2dPCEQJ2VtL%2BzovUblgy9RiNQ9tHgRQkTJfnRmxH99V8Ytg5x%2B9ePr1vp9BiTEgjr74pN2jGo6ZlfaY7OyxQVyEpWyIl%2Fo2vRwLHKhha5lDVinltfgGWsmAAK%2Bf2cAZUy5zBkvhKNnV%2F6WuLLpRheAMAhFpTC4CJtn3gDLVanTSk1Y%2FMok1CXvqxWMBjtsgcvC4XDCTF23R8G%2BMP%2FbjskGOqUBRRH7eXQ7L7Q16ol4vdqBWBqyR%2B6Txwb3ueOzyhHOh7oRbkYWMZhDaDEob0K45zClyZDfDxl3x%2Fl6rSUpzFncNUUPS5QhJw6JJDZZ7pUvWbdMRIVMGJZ58RDfAJmNY%2FBqR3NWL9ftXfPw9%2BOC3JJgsHbbARhSAzudjKyMuWkDIoZNcVSjFbCCQyLuxSkpqKUmJ6ccZID7eIGXoEu7wuyP2aEgUVNI&X-Amz-Signature=28b47fb6bc8a3e322ad9689cb4a2f14d4be0dd90e14a69315b6d6c670ee39339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

