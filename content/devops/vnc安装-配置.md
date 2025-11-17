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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUR4W65Y%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkZA%2F%2FVK76ygdBBgzzcdX2opB4eCuJOwuIwi0Udsu7ZAiEA8B2R97%2Fp2dBVG0442LOltx%2FzqrAJjJEJvFj%2BUhkm9E4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNe3Bl%2FLcn5uY6QjeircA6rHt5sSFBMdhJrYB3dv3tr6pG8k0oiZ%2BfmtJBg2DWzzhUoLJuRVgbAFNGZOZ4W0sV6A3lDoCU3V6y8kLpPjqvH3CqG62KofJ6zBzzSlBTvWokFGsZqVRMl9B3%2BfzDRps9TwxYbjClp2uoYhw%2BhriTeKBfTin62S73oskF369GR8HUuInzmpVH2Wknn60vebSAd1nFhUE%2Fui04UtSz6fFl9JzgVvUvUNghq41UVszZCURxnXR13Z6fg%2BdGh%2FpfQlCkEj0hz1zv5GrZ3x2hTA8v8Mmu15Bqs7p9hm7pWGetE2yrz%2F7w%2FIJ%2BBfeWftb8Qir1aQd8D5%2B6Nnxczkv0deHQrPPP5UriR%2Fk7UqggutblQAAtuP9YO0DZVZv8CHb13K36WsXN0R1bNV5PaWeG%2FOaKz3eP0AIWPqTWysKDo%2FC1SYBIYX4OaYa%2F8f1b%2BVpS8R3K0dC7ifFbh8kJ6p%2F75dAfRp9bcPYJ%2B1I88h3AxTsWK6BgmVzeOn0wVzSUSWt%2BikDlcoUCOowTN%2BxCvCO%2BC5XbPdLwGyjvyhgu7OQLGg5uh6pRdfdTeroKekQqGCepkyZx3qhSP47iN%2ByO27vY7UpT6f08kx%2BDboN7X4Ok0zqMl1%2BvBV4aDOQSep0pgQMJOH6sgGOqUB6gkOlhtzGuSq2bIO2ROM%2BdqGikFDBFItKtEzNT0yll88HLFvl9hhrI8Pa3VEOdgcVBCViIXq%2FcB4b924ii2cvWLkDZQqo7pn8xlCKRW92BMLVT%2Fu4d4f1H4sU9B7Wn1Th5sbRd83hFjNNAqAPHJ3sHdD7CL2Rxz0OjpP5T2ivhcEefzzwz%2Bm0UG3UDkzArhVA3q2klnftnRHya9D2W8qOzz4EJFH&X-Amz-Signature=76f1cfdc226451063def8e72f7eb19d41076cadaf7591b1ca19abab7894f8bf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUR4W65Y%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkZA%2F%2FVK76ygdBBgzzcdX2opB4eCuJOwuIwi0Udsu7ZAiEA8B2R97%2Fp2dBVG0442LOltx%2FzqrAJjJEJvFj%2BUhkm9E4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNe3Bl%2FLcn5uY6QjeircA6rHt5sSFBMdhJrYB3dv3tr6pG8k0oiZ%2BfmtJBg2DWzzhUoLJuRVgbAFNGZOZ4W0sV6A3lDoCU3V6y8kLpPjqvH3CqG62KofJ6zBzzSlBTvWokFGsZqVRMl9B3%2BfzDRps9TwxYbjClp2uoYhw%2BhriTeKBfTin62S73oskF369GR8HUuInzmpVH2Wknn60vebSAd1nFhUE%2Fui04UtSz6fFl9JzgVvUvUNghq41UVszZCURxnXR13Z6fg%2BdGh%2FpfQlCkEj0hz1zv5GrZ3x2hTA8v8Mmu15Bqs7p9hm7pWGetE2yrz%2F7w%2FIJ%2BBfeWftb8Qir1aQd8D5%2B6Nnxczkv0deHQrPPP5UriR%2Fk7UqggutblQAAtuP9YO0DZVZv8CHb13K36WsXN0R1bNV5PaWeG%2FOaKz3eP0AIWPqTWysKDo%2FC1SYBIYX4OaYa%2F8f1b%2BVpS8R3K0dC7ifFbh8kJ6p%2F75dAfRp9bcPYJ%2B1I88h3AxTsWK6BgmVzeOn0wVzSUSWt%2BikDlcoUCOowTN%2BxCvCO%2BC5XbPdLwGyjvyhgu7OQLGg5uh6pRdfdTeroKekQqGCepkyZx3qhSP47iN%2ByO27vY7UpT6f08kx%2BDboN7X4Ok0zqMl1%2BvBV4aDOQSep0pgQMJOH6sgGOqUB6gkOlhtzGuSq2bIO2ROM%2BdqGikFDBFItKtEzNT0yll88HLFvl9hhrI8Pa3VEOdgcVBCViIXq%2FcB4b924ii2cvWLkDZQqo7pn8xlCKRW92BMLVT%2Fu4d4f1H4sU9B7Wn1Th5sbRd83hFjNNAqAPHJ3sHdD7CL2Rxz0OjpP5T2ivhcEefzzwz%2Bm0UG3UDkzArhVA3q2klnftnRHya9D2W8qOzz4EJFH&X-Amz-Signature=466e3d44ea644bb86ac44821ed3de5bd48e179332532c0aa179232818927338a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

