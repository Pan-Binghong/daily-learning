---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
标签:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBWPDM4E%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnciHWnY0irQNs8niUAr5swLOvlD9YlI3Wic1i8EtdIQIgIfp4x56NMLl40k60c8037YDV%2BYC%2Fhj3tVYsIfRr5re4qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7T8kTmOqS9TjopESrcA4ynGobX5OIyt%2BvfT6OZL%2FOraMAYo%2BthzcbJt1gpalT2YR5mwr%2BCfq4ZYzbZjfiz8MLmmDf%2FsPedDZkVP5VaJxOkkeG%2F6cIPSPMYtnDCcYrIrObJUHW%2FWIwssQbsjIH3zlyZloNFULromfCASsqTj2BPgak7Shu1SmVPisRmwtjQz7%2FHjhsnmLwodmQORXUErRAPek%2BQEvCjQu%2BjrqM8UpLOSdqs4i571DFn2nVVhB62TmcybhtO%2Bl%2FPXSEkowBiRPjXprYNCBFSA0pL3q%2F2TuAqZW7zC%2FOwX0BGr%2FS0%2FL5UwZv%2BGipcxIEiDLvUxH15y2TB4%2BFjtFvzXP4j%2BZk%2F2Yy5WInD1b1l0JH0hllKWw1QgzkXqMu%2FiTlW5bmBbdND67i9cb%2B21ziFbrgeqYnvoZNS087uvROYGDeeOLpeYo%2F6gPRgRrY7XukFK99tG%2FLh%2BJy%2FbGWusspS69nj15fNhUgARtUhUzWsyKUiKw5eG9bwzWS9nySVATZoUoGnqb%2Ff9ms5W1JdqXsVcxsNwAwK%2BsT1Nqyf2iwZIMN4s6PFPHfZgRFxCFsMZiKoZw9qr8qHIPZpTIQ2%2BS7CXEjMmqaXQHI9kZKsacXOwGvBKe5vdXxIiIanlbhMn1naERJEMNmirMgGOqUBP6lHYdnle%2FTrKCkuYtJbyG%2F%2FI4ct%2FoGmsLDz4PlVgkZUY5dR3DF7iAsNyq1PCeY9llU3anyViGVwkxTxPH1dF1xkQ9igamNlHzrY4ptyyeroboh%2BkoLifw9zqFXG7qu0Ee4%2BjGlaefcMMum08ecoUpiHKv5uDRBNcjNPkx5Axb4dcbvi%2Baz0Sk1hoWnFr0m56ioJhQAwu0cFlEFB4B7nq2zk5V79&X-Amz-Signature=b8878560c42a3246eb7a2b55343e51859a5b1153e9c42c1a498d5f5ae41d5106&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBWPDM4E%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnciHWnY0irQNs8niUAr5swLOvlD9YlI3Wic1i8EtdIQIgIfp4x56NMLl40k60c8037YDV%2BYC%2Fhj3tVYsIfRr5re4qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7T8kTmOqS9TjopESrcA4ynGobX5OIyt%2BvfT6OZL%2FOraMAYo%2BthzcbJt1gpalT2YR5mwr%2BCfq4ZYzbZjfiz8MLmmDf%2FsPedDZkVP5VaJxOkkeG%2F6cIPSPMYtnDCcYrIrObJUHW%2FWIwssQbsjIH3zlyZloNFULromfCASsqTj2BPgak7Shu1SmVPisRmwtjQz7%2FHjhsnmLwodmQORXUErRAPek%2BQEvCjQu%2BjrqM8UpLOSdqs4i571DFn2nVVhB62TmcybhtO%2Bl%2FPXSEkowBiRPjXprYNCBFSA0pL3q%2F2TuAqZW7zC%2FOwX0BGr%2FS0%2FL5UwZv%2BGipcxIEiDLvUxH15y2TB4%2BFjtFvzXP4j%2BZk%2F2Yy5WInD1b1l0JH0hllKWw1QgzkXqMu%2FiTlW5bmBbdND67i9cb%2B21ziFbrgeqYnvoZNS087uvROYGDeeOLpeYo%2F6gPRgRrY7XukFK99tG%2FLh%2BJy%2FbGWusspS69nj15fNhUgARtUhUzWsyKUiKw5eG9bwzWS9nySVATZoUoGnqb%2Ff9ms5W1JdqXsVcxsNwAwK%2BsT1Nqyf2iwZIMN4s6PFPHfZgRFxCFsMZiKoZw9qr8qHIPZpTIQ2%2BS7CXEjMmqaXQHI9kZKsacXOwGvBKe5vdXxIiIanlbhMn1naERJEMNmirMgGOqUBP6lHYdnle%2FTrKCkuYtJbyG%2F%2FI4ct%2FoGmsLDz4PlVgkZUY5dR3DF7iAsNyq1PCeY9llU3anyViGVwkxTxPH1dF1xkQ9igamNlHzrY4ptyyeroboh%2BkoLifw9zqFXG7qu0Ee4%2BjGlaefcMMum08ecoUpiHKv5uDRBNcjNPkx5Axb4dcbvi%2Baz0Sk1hoWnFr0m56ioJhQAwu0cFlEFB4B7nq2zk5V79&X-Amz-Signature=4d2b0399ea6edade88d60abb3d22da0f158fc5cafa7cb95f1fd400571bad052e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

