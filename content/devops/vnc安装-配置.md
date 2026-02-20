---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZ4HSAC%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcjRkND%2ByevA0pESpmMAVFT5uVv3ELljjHuCzP%2Bo%2FraAiATjs6IotRXgsYMxgqGVXrq5hoVBq1m%2B1Trlkw1ZjSSSiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FFD%2Bbh%2B7rDpXMKg5KtwD38AeMyOwYqmBMw0w2sAXoeqfs%2FbHe8RdFSde7PrXb3T00bWZ7rp6kJEhPBOmuG%2B9feOyetM8HpnNrvmHOtz5i%2B2ii84MLKVlIj79XSOo5HxAjH9b2juLx2JiDijr2pDfb906qK4ErcivXfGMRhyrQZH9ysMIEf%2FUP4JtbMMPc3fAjhVm3K%2B2OoamIhwF3TwtjjjgtkwHauhpw8IdbGZdl4yfcXY3JgRXNg3UHW5hG8NJcnPizd1S68%2BbZsr34C9cYQIRV71mB5OwO1M9%2BVC0zhjCRMg%2BPo4ucu09fPHywSSQBUj1sCro2tWbEn%2FoFpor8nYuGBWvXXlzImbI2h9M52PdoXV77No%2BSGWZTpgvRPC0w3w%2FQMRRK8N5x3cdwYf953i66rIxG98NCMfQmDher8lhmtqD81mX7946sqSa5aanE588gB2CD9K1wjBD4efg%2FgoV%2FwVx4XvP1ZlM1lMthE6cxHlabj5E5%2FYBTzh8BxRzsW%2FQdc814EMLck%2F2Ptu64hgOAsHYGB%2BPjjhaEd1FNH%2FmTyXT7h%2BEV6Uflbx0yP3b0%2Fy1PbRJzO7zZURgd2UIp8wJFPQv5YbD%2FE0dxx7G6zduEaR%2FUbREhvf1cx66rjayAOZgY%2FwhUb39ZLIwxpHfzAY6pgHoQnND7CObrFvpjuPMzVB78qAdJNTrI5Q2CHTS1FYGBSh%2FYkaFLV5DUgZZJyxw0K5CKwjtvma2j3TcnhJT6jSCaqfDWj4dHzPD8D%2BjgU8k%2Fi%2FyodrrHECKozXB%2BY6jJEDpFatrKcv4W9cb9pDq9PnBPmezMf5l77z2Nhxs8g0nz2nIpNIiU5fK%2BUGxszC2es2aVf337VS0atmKiE7drQk52%2BLPpz7n&X-Amz-Signature=ac8a8605ef2dcf8f7f6acdc6d7b938931d1e7c4c1d9e389ed682adaeba024212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRZ4HSAC%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEcjRkND%2ByevA0pESpmMAVFT5uVv3ELljjHuCzP%2Bo%2FraAiATjs6IotRXgsYMxgqGVXrq5hoVBq1m%2B1Trlkw1ZjSSSiqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FFD%2Bbh%2B7rDpXMKg5KtwD38AeMyOwYqmBMw0w2sAXoeqfs%2FbHe8RdFSde7PrXb3T00bWZ7rp6kJEhPBOmuG%2B9feOyetM8HpnNrvmHOtz5i%2B2ii84MLKVlIj79XSOo5HxAjH9b2juLx2JiDijr2pDfb906qK4ErcivXfGMRhyrQZH9ysMIEf%2FUP4JtbMMPc3fAjhVm3K%2B2OoamIhwF3TwtjjjgtkwHauhpw8IdbGZdl4yfcXY3JgRXNg3UHW5hG8NJcnPizd1S68%2BbZsr34C9cYQIRV71mB5OwO1M9%2BVC0zhjCRMg%2BPo4ucu09fPHywSSQBUj1sCro2tWbEn%2FoFpor8nYuGBWvXXlzImbI2h9M52PdoXV77No%2BSGWZTpgvRPC0w3w%2FQMRRK8N5x3cdwYf953i66rIxG98NCMfQmDher8lhmtqD81mX7946sqSa5aanE588gB2CD9K1wjBD4efg%2FgoV%2FwVx4XvP1ZlM1lMthE6cxHlabj5E5%2FYBTzh8BxRzsW%2FQdc814EMLck%2F2Ptu64hgOAsHYGB%2BPjjhaEd1FNH%2FmTyXT7h%2BEV6Uflbx0yP3b0%2Fy1PbRJzO7zZURgd2UIp8wJFPQv5YbD%2FE0dxx7G6zduEaR%2FUbREhvf1cx66rjayAOZgY%2FwhUb39ZLIwxpHfzAY6pgHoQnND7CObrFvpjuPMzVB78qAdJNTrI5Q2CHTS1FYGBSh%2FYkaFLV5DUgZZJyxw0K5CKwjtvma2j3TcnhJT6jSCaqfDWj4dHzPD8D%2BjgU8k%2Fi%2FyodrrHECKozXB%2BY6jJEDpFatrKcv4W9cb9pDq9PnBPmezMf5l77z2Nhxs8g0nz2nIpNIiU5fK%2BUGxszC2es2aVf337VS0atmKiE7drQk52%2BLPpz7n&X-Amz-Signature=0ab70165232f1d27657254eea5fd48157f9d2c9f8185bb399916c3787e21c207&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

