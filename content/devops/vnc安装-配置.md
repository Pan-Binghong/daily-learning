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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V27TQZVC%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4XL9z2vCWeQXXHHrcTaYx5YEbd2%2FYPjjQvfxJ4SyDXgIgJYQtTyAIKobc8B6Ws%2FV3H%2BCxjraWR%2BzjV4LbQupjtUgq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDN8gvqtuNUNToLMhsSrcAzZSER%2FHG7TvihYdZTN0MCVHlCkN1GA4yoGzb2TSFBKz0SEDQ89T0dtVX2xZ1ob26rzp5rYoIvpD%2FE1W1aTQWfG26ttGkc9ZXwLcgE8ks8ZnPz0esMEGMWEm2RZBWJgdYUwthSdWSfTBXDpXbs0UCnL7hh%2F5312RN45cXZCXDr2uwEGfdx72a%2F9tnkFwuzQuLzRZtsWb78o6xQ2guuqkM9eCfAEm0nqXBbiFdkNz3ifa1rjyXO8VChUaliB%2B18ON6Tj%2BfFuKHUVYjvrk415egwTQV6qu7xfwchIZgE0MywmDrXq%2FZsr5kBK0tX3LWUcJiaHEFtF49pOI1S%2F5LbFGKZdL%2F8JUTuUvwYdbN3gPD6iF0AxXOVPXa%2FDhNSlvy3QM3znJcHlTVOVfbFAbR9a0Iq%2F0DWTCjPCIuydzQ%2Bzme3bDTzBP683uwnMBTsK4qeTvrdDzXldjDNSgy%2B0%2FDqKzRQoAAoz4D3oM%2BWv%2BqC%2B8RPx6lS31rAbUrTuyW1vp%2FtLiSYUlRW5BnCcviup6yt%2B5UFpZpJD1yzFSFxmfjEjwwiHmtumVUDe6Omn0y08HlwGxKnXgK%2Bv6Y6kCO4U%2ByC7T%2FAgj7O%2FJ6ouPHme3X0feMfc7nwRXz3x3Y%2FTfP21TMMqNg8oGOqUB54FjwbxY9DL8HrN15N8j72xT4SCQkHyNP92tNq8jQszHKRTgRa2zwZgoV%2BVcSZe92jOoZgCOsEoWRXr22sT7LWXP%2Fm%2FHTGxJn9wLnM9xqnzhnpQ%2Bn%2F2HGwRcVn2kl62dIJlf9eTTkedRm109277UOHjuOedpeedhT4Bi8%2Fcz6JOwLEGBFjr27KCp9LJGhysA65eXq%2BOrpdx9PuHS5UcKx5j16fof&X-Amz-Signature=0b622729d838fb878efc81cad08e7fa5e729c695d30a7036fe9a9702e52473d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V27TQZVC%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4XL9z2vCWeQXXHHrcTaYx5YEbd2%2FYPjjQvfxJ4SyDXgIgJYQtTyAIKobc8B6Ws%2FV3H%2BCxjraWR%2BzjV4LbQupjtUgq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDN8gvqtuNUNToLMhsSrcAzZSER%2FHG7TvihYdZTN0MCVHlCkN1GA4yoGzb2TSFBKz0SEDQ89T0dtVX2xZ1ob26rzp5rYoIvpD%2FE1W1aTQWfG26ttGkc9ZXwLcgE8ks8ZnPz0esMEGMWEm2RZBWJgdYUwthSdWSfTBXDpXbs0UCnL7hh%2F5312RN45cXZCXDr2uwEGfdx72a%2F9tnkFwuzQuLzRZtsWb78o6xQ2guuqkM9eCfAEm0nqXBbiFdkNz3ifa1rjyXO8VChUaliB%2B18ON6Tj%2BfFuKHUVYjvrk415egwTQV6qu7xfwchIZgE0MywmDrXq%2FZsr5kBK0tX3LWUcJiaHEFtF49pOI1S%2F5LbFGKZdL%2F8JUTuUvwYdbN3gPD6iF0AxXOVPXa%2FDhNSlvy3QM3znJcHlTVOVfbFAbR9a0Iq%2F0DWTCjPCIuydzQ%2Bzme3bDTzBP683uwnMBTsK4qeTvrdDzXldjDNSgy%2B0%2FDqKzRQoAAoz4D3oM%2BWv%2BqC%2B8RPx6lS31rAbUrTuyW1vp%2FtLiSYUlRW5BnCcviup6yt%2B5UFpZpJD1yzFSFxmfjEjwwiHmtumVUDe6Omn0y08HlwGxKnXgK%2Bv6Y6kCO4U%2ByC7T%2FAgj7O%2FJ6ouPHme3X0feMfc7nwRXz3x3Y%2FTfP21TMMqNg8oGOqUB54FjwbxY9DL8HrN15N8j72xT4SCQkHyNP92tNq8jQszHKRTgRa2zwZgoV%2BVcSZe92jOoZgCOsEoWRXr22sT7LWXP%2Fm%2FHTGxJn9wLnM9xqnzhnpQ%2Bn%2F2HGwRcVn2kl62dIJlf9eTTkedRm109277UOHjuOedpeedhT4Bi8%2Fcz6JOwLEGBFjr27KCp9LJGhysA65eXq%2BOrpdx9PuHS5UcKx5j16fof&X-Amz-Signature=edd23ab7b65158c22104ee5a891b3cd19580f1683f87123aecd0d396a20476da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

