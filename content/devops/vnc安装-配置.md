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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW43HLSR%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE%2Fq%2BPN08AUycV8KhKkYrGFfNbywsl5GJqy9pYR8nyrUAiBmy8gBXXfgY4Bsto%2BypvcM9bAmYMY880a%2BWeOihqMuPiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM76WQocW%2FsIGkulvQKtwDxiXurNa0mHa42bYF7u68%2BLngyxJd4KS98H6r%2FQA8RirVjIwRqvcc2cWxLUwz0svFrA9yeKeLy8TrQSOT3bTTt6CdhQUGU0J%2B79%2FUU10flcNG7is0VKh5TsfBoIYTh7SuSP81Z8MqXdg9LbdfAGiZ7qd79PkolBwMSZnR72kLWBB8f8nZDykCr9xeFvn1M%2FbO6tlJdzJrydT%2FBd04t2cMOrAcGGsndG7oqiBIPMDrasYB4TUWurK%2BNQS%2BfFtdksSb7N2J3WEaA%2BUfp9TznluaAkbsMmpzF9LBEzU%2FYsUQ29djGMl%2FrcdDgt1pZt%2F6DkfC9Koy4c7lcPCNr2fyDnEwMdg%2BQvvvEfxhI%2F94O31XpdcEUF8oUS4lZ4oxiaIO%2FoaO0Dp2OEIt97bXNJkXztzu%2B%2BhGjd0rgv%2BV0zMvcfFCjrAV9lTkug52wJvzN2eGqkcGJG%2BvJ9dm2FZClFRngyrTGmMRjhWu62elVG%2FcB4hYgCidQyRprLMhc8Z5a7hD1r%2BmlaIhAvu0mWDLhnDypOD1zoryKsVi8Uyy%2BqpZKOeqtoAkWiqUux3TVvI41uGOwX%2FAp%2F%2FeojXRg%2Fuqs4uSCTY2VLbnG5QLhUGhI3fOEYGHYckjRmvtTB4azFktfDMw%2BbmGzwY6pgGIJVU7UkNp93ygXnyLRq6fRMFwnKpGUBcgXiHxRiSloXQ15JoHi6AYZt9laAui9X6qYqxxK75xSpIm69OAHyTTKNOR%2BaQ%2B%2BFdQ3xjtXQ1LVJb9UJzZB7BbW4wcVYEQhmKlXjX%2BqLfmQw9Rq%2FP0iCiwFjRM81SCub5dnXbYlhOeDSZJz9mC7nO%2BkrN9r%2FFzoSbElacyiHxk8LInRvuunmYDzBSWyRov&X-Amz-Signature=500c595020a1ee96f16357b3f94cf7e5fd9758f3b7e023553fcddb10e4dc4475&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW43HLSR%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE%2Fq%2BPN08AUycV8KhKkYrGFfNbywsl5GJqy9pYR8nyrUAiBmy8gBXXfgY4Bsto%2BypvcM9bAmYMY880a%2BWeOihqMuPiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM76WQocW%2FsIGkulvQKtwDxiXurNa0mHa42bYF7u68%2BLngyxJd4KS98H6r%2FQA8RirVjIwRqvcc2cWxLUwz0svFrA9yeKeLy8TrQSOT3bTTt6CdhQUGU0J%2B79%2FUU10flcNG7is0VKh5TsfBoIYTh7SuSP81Z8MqXdg9LbdfAGiZ7qd79PkolBwMSZnR72kLWBB8f8nZDykCr9xeFvn1M%2FbO6tlJdzJrydT%2FBd04t2cMOrAcGGsndG7oqiBIPMDrasYB4TUWurK%2BNQS%2BfFtdksSb7N2J3WEaA%2BUfp9TznluaAkbsMmpzF9LBEzU%2FYsUQ29djGMl%2FrcdDgt1pZt%2F6DkfC9Koy4c7lcPCNr2fyDnEwMdg%2BQvvvEfxhI%2F94O31XpdcEUF8oUS4lZ4oxiaIO%2FoaO0Dp2OEIt97bXNJkXztzu%2B%2BhGjd0rgv%2BV0zMvcfFCjrAV9lTkug52wJvzN2eGqkcGJG%2BvJ9dm2FZClFRngyrTGmMRjhWu62elVG%2FcB4hYgCidQyRprLMhc8Z5a7hD1r%2BmlaIhAvu0mWDLhnDypOD1zoryKsVi8Uyy%2BqpZKOeqtoAkWiqUux3TVvI41uGOwX%2FAp%2F%2FeojXRg%2Fuqs4uSCTY2VLbnG5QLhUGhI3fOEYGHYckjRmvtTB4azFktfDMw%2BbmGzwY6pgGIJVU7UkNp93ygXnyLRq6fRMFwnKpGUBcgXiHxRiSloXQ15JoHi6AYZt9laAui9X6qYqxxK75xSpIm69OAHyTTKNOR%2BaQ%2B%2BFdQ3xjtXQ1LVJb9UJzZB7BbW4wcVYEQhmKlXjX%2BqLfmQw9Rq%2FP0iCiwFjRM81SCub5dnXbYlhOeDSZJz9mC7nO%2BkrN9r%2FFzoSbElacyiHxk8LInRvuunmYDzBSWyRov&X-Amz-Signature=c73d247cb7a6527880aab84e09e257f0139decc87204aac5aeca0f663daa66b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

