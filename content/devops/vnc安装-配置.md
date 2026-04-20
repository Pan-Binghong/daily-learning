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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7JUSLC%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDSgHzoioNAnhUBURpEU0nVyUyUIbv%2BFMgCokWJwCFJswIhAMD38PeXuO%2B5MZV0bUDS9fjZtPmIWBvps9jdWw6ylXjiKv8DCBMQABoMNjM3NDIzMTgzODA1Igz3dfIcpjQ91s3NADIq3AOtgg233fEzVBuEE7%2BZATByGt1xLZCjM2MTLylhzcl7flTY0NK3hrifbkY2UHjBhJPEG2LmK74Og9ngw00ur40pZrss9XbxAGIP%2BvPiGE6fsteQGq5vULA8arx3Ye7qeQz6WebYllPn6FCV%2FoLv3dgFL2QI0gMQVVKV4ie9DUpK43lDlz2PgoueCFRW%2F56%2FdscmeUqTMn0Jj2TXL4tP2suEFVqNggsp7bkNSijQf2DxilSDzASoTgpCJmAWyFDzFStatxUpKdECTdYwcSflS5iGPQzRN%2Fu%2FxvUTdwxP6GIABr%2FKgqjaCFse%2BZDNOfuddvTsIpabsw8ktRvLzrBw9SewVMKZQrK4EqdYJNy5ndFpac%2B2BMtf90%2BNIwmb4deF9DU9oXaHsHaOXKuAca%2FuRf85wEiakoPwPuKpKc%2FBbhdzj%2FhvHp35avNn4mAUQbDwOZdk51R3alD%2FnETCE8gAGNxQKubBhDBpZtuf6T6h%2BVxQNaTK3tI3SpN1%2BkTHEwP5s1pQU3rxQJY9zeUE0OgYrQHavcghNw%2BlgzRJWtEZj7yOrwq%2BDbI%2B02V6NdTydxUfHYT9f2LyPieoA5dKGGCfHPv1PY0rLEQ69e6roU4v1vHVqMt62pu1A%2FArjqkmITCbl5bPBjqkAforM864US3VwyPetS%2BmxrKD6OIcCxUNhEFNN4ppbkt1gaF4aecFwxjKa7c8wA8mzaInVbe3a15umdymKyeIHVb1EfjYieVGRrsTTYYxBho80opF4qZzRdBwSC0TCyBlLKYkEyqpnes%2BPNJJNLXYzNdwBAo103w6iWadzd148gr7IWncEa%2FqBm4q7K4bi4YlEFb8gtHKl%2Byr8hicrvAFem%2Bxfsty&X-Amz-Signature=c1a7463cee720a8b220e950420a2ca6a436c08ed55d9123db8a19b4de8295aec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7JUSLC%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDSgHzoioNAnhUBURpEU0nVyUyUIbv%2BFMgCokWJwCFJswIhAMD38PeXuO%2B5MZV0bUDS9fjZtPmIWBvps9jdWw6ylXjiKv8DCBMQABoMNjM3NDIzMTgzODA1Igz3dfIcpjQ91s3NADIq3AOtgg233fEzVBuEE7%2BZATByGt1xLZCjM2MTLylhzcl7flTY0NK3hrifbkY2UHjBhJPEG2LmK74Og9ngw00ur40pZrss9XbxAGIP%2BvPiGE6fsteQGq5vULA8arx3Ye7qeQz6WebYllPn6FCV%2FoLv3dgFL2QI0gMQVVKV4ie9DUpK43lDlz2PgoueCFRW%2F56%2FdscmeUqTMn0Jj2TXL4tP2suEFVqNggsp7bkNSijQf2DxilSDzASoTgpCJmAWyFDzFStatxUpKdECTdYwcSflS5iGPQzRN%2Fu%2FxvUTdwxP6GIABr%2FKgqjaCFse%2BZDNOfuddvTsIpabsw8ktRvLzrBw9SewVMKZQrK4EqdYJNy5ndFpac%2B2BMtf90%2BNIwmb4deF9DU9oXaHsHaOXKuAca%2FuRf85wEiakoPwPuKpKc%2FBbhdzj%2FhvHp35avNn4mAUQbDwOZdk51R3alD%2FnETCE8gAGNxQKubBhDBpZtuf6T6h%2BVxQNaTK3tI3SpN1%2BkTHEwP5s1pQU3rxQJY9zeUE0OgYrQHavcghNw%2BlgzRJWtEZj7yOrwq%2BDbI%2B02V6NdTydxUfHYT9f2LyPieoA5dKGGCfHPv1PY0rLEQ69e6roU4v1vHVqMt62pu1A%2FArjqkmITCbl5bPBjqkAforM864US3VwyPetS%2BmxrKD6OIcCxUNhEFNN4ppbkt1gaF4aecFwxjKa7c8wA8mzaInVbe3a15umdymKyeIHVb1EfjYieVGRrsTTYYxBho80opF4qZzRdBwSC0TCyBlLKYkEyqpnes%2BPNJJNLXYzNdwBAo103w6iWadzd148gr7IWncEa%2FqBm4q7K4bi4YlEFb8gtHKl%2Byr8hicrvAFem%2Bxfsty&X-Amz-Signature=b6aa96db24570adae4272ff6bcc21164e91490b2e8613d17920755c6109b8270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

