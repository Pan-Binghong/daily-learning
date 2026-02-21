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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=5861d594495aee98f10f16571f0df0c9c1be0d8400fa99c938923007ed286455&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=3b5496ad864fc2b5235e7483222bee48fc27e1dfc5c0a62c0526ec0925caf50e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=74477569fdca7fde6be5a6e348008e2a201f850875e35f3e855bd98a1e92afda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=58348f9aea9897b6d74119158b25303cea538f59969c43c3aa4c7a50fbf3b226&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=6978baf3fbfac2314ba0bfa26fdd99ab34f0415ead551d34a1961b10f7e01b64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=35d05a04b17f669584b6fd6c1abeb602ef78929ef0158a657de2ad55f6afdce1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V67C54W%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRftwknl%2FbTOTErzVOu3swIT24R1cJeKCk0YVUaDqWsAIhAMPALTy2PVg3nvEC%2B1tnaKkh9NnmWPXBkThA3v96DNblKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRIsbJFDZZPhvzKI8q3AMZQAF83EgzRqKxPbMbo4iWBYdC8EBKXkwVwbUZTW7DBFZoOYs605gHPWGs7QSnYerqbnn%2F1PLNoL%2FORKOyxBOBytaKnUYDXj4Rma5ajUafWqqPEivR%2Fz3ku2KIHpbeEQtfAmZZn0oY35iNdXwwh6vU%2FJyfAyWZmCR%2F9sTe5j3%2BWUr%2BemTT3IvSUh8SzJvnCBLmcY%2FUIOHiSHgnlnFY4r%2FT7cOZxbZh2y9c%2F2XvVdSzlA8hYUqbO3LhrnoODV%2Fk7OHxfZ%2BZANBPpK0eOI5rIDnswkYBZNUaprEtSP1xrfKPSwlk819dv1d40oxcvWg7j1kKDtKwKLO9V50cguX3TuslD7JSNXq2vWPryzIdNXYAR%2BMLPFxLMrB9wCW3eBFTuuX84BXbG4iZabZgKDTd4zf%2BepbIZFWizKPoGrTDZKaEwJqGu2bnakc1O%2BuQn1rHew%2BXSAIPZB27zwCzo45SX6OHDqWDrR%2BT2yYRvJ81TnUMd8osRGAf9x3IwQQYuKlX6Nqp371WCWvBfyCWheTgSULIrn4m9OjZdSuaAyOt2bC2J3eZKzj8HUMVlhY68HZCEVSgynh4HX32N8UoFkiDCn0zAqk8RYqJhp0o5xxtm%2B3QuaoRJeNnZcqML7njVjCwvOTMBjqkAXXy2PucuBf1acgvSN%2BxyIuOJ0KcqEGxeP1MlE2pyyY5ET983nf55lIk4ZYmky4w7T01rRqTTIsv69TDnToNaA1A6XhozlaM9XcmxmLKkSr3mb9TD7jTrScvGeRCroEMmy%2FWNoi4Q9sISibG8ftVJ9F5CQXJwyYezpCSlLZQwqll2ieegin7Rg5UIHcwTIajZRjGVqW4e5rdgSL4jh3noX1fYWLb&X-Amz-Signature=d6fa41d81d44acf4c3a76886d00b862c727da6a1be13f988baa325a9a07265bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

