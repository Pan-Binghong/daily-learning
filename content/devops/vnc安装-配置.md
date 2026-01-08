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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5C4GHC4%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICy8jxZEgi%2BR3%2FbvbvaQIEqX7uscYDbWRiAcXWdDfUPVAiEA5CtbLkonxUqkicg4olIk8S5KLGDDzVOoWZkXpYaiHaYqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1chh%2BMXHZhJHSxiircA8DcFkOOO9TifDBXHDdf7DrvMHDBhgq1rIFofaAm6eZoOm%2BCNkfSE5DNJ2Xc5HV4rhyN28PbOYAfDViuEbIXkFVUU%2F8QEO3TMlG95WxQBGHU5Ex%2B0BV2o%2F%2F%2BNWoD%2BSNrEb%2BX8%2BPCTDU%2BM2JB6wmj6zwb%2BaFS4NZtG6c2x4DmfydDFqzDsW1%2FP4P8s%2B5Zqe%2Bn9I31SlQsWlkpRFgffkhMhiV1Hy0g6%2Bfix%2FVFSsb9s9oOYVbXsiK1NpmljorLpet47rCQILxoztwPFjaOcq1vFSiUH%2B3bHWZRVDTdnpeVHodO7%2BLgXhwTTF9UF43uaDclQIfPToG%2BenpNz4vCG8WSBIK8a9vznL5qFugxkHu2kF9UeJQogRFGJEGRf82m4mNhl5ejBEjGD6Mo2LLbImvL70Wy5MJFf35SPeY6fr%2B3qy5hGtq12BkGCGJNk4gRyKnGlbfnA4qlukNBwn8HpPA%2Bt4J%2FLE98mmjDTJDTXbjAWAaYYGDpd%2B%2FGEH%2BpIt7NYq9riJ0WNthm9szFeDTVqA%2BOQbktXvQomkSYYBNikVlep%2BCIerDyh3yiD9AOVLfHgL7psgjWSO4IqIlzdTldwFRpuwVOog2cM1AC08THoPINqZboRFUxZLxoI47kNTzcMOyo%2FMoGOqUBMYjzeYQQAiOz8PBs3A0s9ZW%2BvedbFfhO5jswmthEOV8Xl4AlFBOw5EhnhGe64Fbqrn7tkkbbFLsf%2FOHR2EX%2FN0zpNbcgL7VLl54V%2BIhl58D1gFjTO5T%2B6irJQGqGk6O2JCAhnkv%2BFHlre%2F5RMa0zryUfzph%2F6UueJ76ucBUUbGAJp7vNddcJ1CkRPXxuJc%2FNvZ8%2BlHDRjrkQa1AZ7e9w%2BEwNgSlI&X-Amz-Signature=332132583e6e9baf10c4b5da0d2ca2ed684027f254313d7f48850332ea4b4ac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5C4GHC4%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICy8jxZEgi%2BR3%2FbvbvaQIEqX7uscYDbWRiAcXWdDfUPVAiEA5CtbLkonxUqkicg4olIk8S5KLGDDzVOoWZkXpYaiHaYqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1chh%2BMXHZhJHSxiircA8DcFkOOO9TifDBXHDdf7DrvMHDBhgq1rIFofaAm6eZoOm%2BCNkfSE5DNJ2Xc5HV4rhyN28PbOYAfDViuEbIXkFVUU%2F8QEO3TMlG95WxQBGHU5Ex%2B0BV2o%2F%2F%2BNWoD%2BSNrEb%2BX8%2BPCTDU%2BM2JB6wmj6zwb%2BaFS4NZtG6c2x4DmfydDFqzDsW1%2FP4P8s%2B5Zqe%2Bn9I31SlQsWlkpRFgffkhMhiV1Hy0g6%2Bfix%2FVFSsb9s9oOYVbXsiK1NpmljorLpet47rCQILxoztwPFjaOcq1vFSiUH%2B3bHWZRVDTdnpeVHodO7%2BLgXhwTTF9UF43uaDclQIfPToG%2BenpNz4vCG8WSBIK8a9vznL5qFugxkHu2kF9UeJQogRFGJEGRf82m4mNhl5ejBEjGD6Mo2LLbImvL70Wy5MJFf35SPeY6fr%2B3qy5hGtq12BkGCGJNk4gRyKnGlbfnA4qlukNBwn8HpPA%2Bt4J%2FLE98mmjDTJDTXbjAWAaYYGDpd%2B%2FGEH%2BpIt7NYq9riJ0WNthm9szFeDTVqA%2BOQbktXvQomkSYYBNikVlep%2BCIerDyh3yiD9AOVLfHgL7psgjWSO4IqIlzdTldwFRpuwVOog2cM1AC08THoPINqZboRFUxZLxoI47kNTzcMOyo%2FMoGOqUBMYjzeYQQAiOz8PBs3A0s9ZW%2BvedbFfhO5jswmthEOV8Xl4AlFBOw5EhnhGe64Fbqrn7tkkbbFLsf%2FOHR2EX%2FN0zpNbcgL7VLl54V%2BIhl58D1gFjTO5T%2B6irJQGqGk6O2JCAhnkv%2BFHlre%2F5RMa0zryUfzph%2F6UueJ76ucBUUbGAJp7vNddcJ1CkRPXxuJc%2FNvZ8%2BlHDRjrkQa1AZ7e9w%2BEwNgSlI&X-Amz-Signature=bf5d2cd93f979a1eebd89c6175f041d421b453f1f5c236e3e33e1a9d00a531c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

