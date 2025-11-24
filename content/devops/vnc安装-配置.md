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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBCN54ZJ%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc37do9a8znHNbWvXAVg%2BU8V36rJjBsJLmIJBrvz9K%2FAiAJuwHP%2B0j6YqeE3BmuUMwdnMkOVBtYVJ0ZicdKBcZetSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM%2BlaCRVp05tCU3rsbKtwDY3pPWJ5UvO0DuC%2B9K6Zolfvw%2FhKWQVTiQjJcLNy%2BDDPpc1hB%2BfRisxYzZcrtGIESFi4%2FIgfjaAWdXtURd9l1Wr0KrJKTUksoi4uUYnLLo%2FvxW0b%2FI97y01uCSDKJlmvDNbTbpazKvUeqYNW2HaJSJBCo90orA%2F8JAfUPhtYJHLUjTdG764g7Ale1AhFVUJOfn9MW6mnrSJ6viy4zYBreZb75DJXaMr3L5nU7acBBv45ib3xnrxVJWTJLVurbCdqeNxpIBUXALkFR3jVQUZOIlvOtQNOUHZ3bWbSZmIXB1Pm2XcJkXF2J2qHO1AkaiD6ZltfnxO3MPUlPt%2F7mKkAFeZT2Njynpes61eWd%2BkwCpALEnD%2F5x7pypgh4MUKewctIuZbjst2cnK5bt6knVn%2Fbz87%2B5tvvjpfnp7HfOEOzqN2SQoC51BkPVFE632ubBmiYz%2BnmDaiqBMlkXlJrX4DynLOOxUVoNz4%2FH6iHQfEkc%2FJPFLAfycZDAtl%2Fhr1VDa59MBfim4Di4FxyzMCelElCajsBk22ByWCZGUbDIj%2FFK5CrCNNiMwhdqJ7E6Nzxos8gkVUgP8xGeoClfjrYKuXuIdQFmRfcasL5WfXd795rea39v2V5GZYXYJD%2F3XIwx9yOyQY6pgG7HHdM93DvRQGLsT6%2BONtG1rZXpR9Aa08t5uY7TWPQnA9r1FH4dK2JSGzCYBPIRJ%2BbgfKPTboJR85Dn9aQiLFBHIKD48dJx9mAcpOMq4DtA58ovMlij5fZdgysE51l0NmnvG%2BS%2BTJc1ok61nfGRp1IId5%2Fu1%2BuaoG0wUF0D2YYF8rAV5ljOBZZDL0zAFlNWnTVf43sbbtfwvvd4L1gRRP48Lyil65K&X-Amz-Signature=ccc3102a590a089fde24e61b03d1060071816fcbb5f951c0ecae2ba14715b733&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBCN54ZJ%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc37do9a8znHNbWvXAVg%2BU8V36rJjBsJLmIJBrvz9K%2FAiAJuwHP%2B0j6YqeE3BmuUMwdnMkOVBtYVJ0ZicdKBcZetSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM%2BlaCRVp05tCU3rsbKtwDY3pPWJ5UvO0DuC%2B9K6Zolfvw%2FhKWQVTiQjJcLNy%2BDDPpc1hB%2BfRisxYzZcrtGIESFi4%2FIgfjaAWdXtURd9l1Wr0KrJKTUksoi4uUYnLLo%2FvxW0b%2FI97y01uCSDKJlmvDNbTbpazKvUeqYNW2HaJSJBCo90orA%2F8JAfUPhtYJHLUjTdG764g7Ale1AhFVUJOfn9MW6mnrSJ6viy4zYBreZb75DJXaMr3L5nU7acBBv45ib3xnrxVJWTJLVurbCdqeNxpIBUXALkFR3jVQUZOIlvOtQNOUHZ3bWbSZmIXB1Pm2XcJkXF2J2qHO1AkaiD6ZltfnxO3MPUlPt%2F7mKkAFeZT2Njynpes61eWd%2BkwCpALEnD%2F5x7pypgh4MUKewctIuZbjst2cnK5bt6knVn%2Fbz87%2B5tvvjpfnp7HfOEOzqN2SQoC51BkPVFE632ubBmiYz%2BnmDaiqBMlkXlJrX4DynLOOxUVoNz4%2FH6iHQfEkc%2FJPFLAfycZDAtl%2Fhr1VDa59MBfim4Di4FxyzMCelElCajsBk22ByWCZGUbDIj%2FFK5CrCNNiMwhdqJ7E6Nzxos8gkVUgP8xGeoClfjrYKuXuIdQFmRfcasL5WfXd795rea39v2V5GZYXYJD%2F3XIwx9yOyQY6pgG7HHdM93DvRQGLsT6%2BONtG1rZXpR9Aa08t5uY7TWPQnA9r1FH4dK2JSGzCYBPIRJ%2BbgfKPTboJR85Dn9aQiLFBHIKD48dJx9mAcpOMq4DtA58ovMlij5fZdgysE51l0NmnvG%2BS%2BTJc1ok61nfGRp1IId5%2Fu1%2BuaoG0wUF0D2YYF8rAV5ljOBZZDL0zAFlNWnTVf43sbbtfwvvd4L1gRRP48Lyil65K&X-Amz-Signature=a73a38c1f3e1ae7ab69bb0d60092921dc5e96f1829e7b61676e62683e9b894bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

