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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3KN5SEO%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHwWOacDA0Sl%2B5GVyqqdcpDFzpPEld6tgQnHfxyBsPXAIhAKJ51RpcdTa1uiNXgg5tdFbVkdqCmE7m4nRQvlNhGUHzKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5aldAjvtX43rLmZQq3AO%2BxNARk9Ny3J5tMUJKG6go5afDv%2FzH6oxKbV5uPz6Ar4u2Fo03RfPEkFVhLwfbG7LRrObsbhcE7Z0JuccKXaYtZ62razgSs3ap44WtOymf2vxQQCrCmr6xPsXTpr5Uww4BKFTeLdxwUm4h5aOZFW9XUI0VTFYqpobiweOZrzhd9ce5TRnLgTiYHMK7js3GA1Zxbicz8e0yPQcGTNyafxL4W%2Bvor5xZwqitoA%2B4sONb%2FhVCrpOIZXcwYB7N0wnE8z5wr46K%2BurqGIFPJ970VMQ8OiZj9Ns8NmQd7eFYMuAg12uQCMQ95cpCBz6VaRD38tJEf0QJ%2BTvzyywmRza47DhZTC8xTA2GKZEKAiyFgjj0ymo5DgoMPj%2BcmEZMAB0wvlYK%2F1b2h48pws%2F7lEnz2KlTnOaIP5dAN8I%2BdqO1l5%2FQzpaCHHUhLZHS18p1B1zA6ssHpkeWaBnYIv8gQkUV6izJIxwmGJWR6RhiOa4gygRBzUDKcTxPYzcyv%2B1kflFEU53%2FoJ0FBcD3sxNDYoKX3TAESpv2iFgI1OW302OKUTL0fM4dwl1mvlX3SpnGHq9%2FCty581eInVECse3CqDycXIZOHgcjtOfrbn56itpBiMctu2tvGYqil48F%2BfWTSTD78tHKBjqkAfIA51UJ7QY0QIlDauj5mUNtnyuzGj%2BpFkBBtKCstlaEaXc0SKWb0oWmiCQycVx8%2B%2FG%2Fiqv0RqyAdhERH0mNy45O4yvPyu93Kkw%2FfZYBc6X3FHhfus4Q3xSAcG0%2B6ayf3AiJJPF2%2F5%2BPic7yptpp2Bi%2FQF2SeQVRXEKz3v0xQHma49h%2Flxy6hRe2bxyxJlCfvgADiIFbkHqTZ7UQX2Xo4BI6fO5Y&X-Amz-Signature=b7944e1d9458dc3f5311c6384aaf4fce4ac8356eabc0378cebf0b880752bab36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3KN5SEO%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHwWOacDA0Sl%2B5GVyqqdcpDFzpPEld6tgQnHfxyBsPXAIhAKJ51RpcdTa1uiNXgg5tdFbVkdqCmE7m4nRQvlNhGUHzKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw5aldAjvtX43rLmZQq3AO%2BxNARk9Ny3J5tMUJKG6go5afDv%2FzH6oxKbV5uPz6Ar4u2Fo03RfPEkFVhLwfbG7LRrObsbhcE7Z0JuccKXaYtZ62razgSs3ap44WtOymf2vxQQCrCmr6xPsXTpr5Uww4BKFTeLdxwUm4h5aOZFW9XUI0VTFYqpobiweOZrzhd9ce5TRnLgTiYHMK7js3GA1Zxbicz8e0yPQcGTNyafxL4W%2Bvor5xZwqitoA%2B4sONb%2FhVCrpOIZXcwYB7N0wnE8z5wr46K%2BurqGIFPJ970VMQ8OiZj9Ns8NmQd7eFYMuAg12uQCMQ95cpCBz6VaRD38tJEf0QJ%2BTvzyywmRza47DhZTC8xTA2GKZEKAiyFgjj0ymo5DgoMPj%2BcmEZMAB0wvlYK%2F1b2h48pws%2F7lEnz2KlTnOaIP5dAN8I%2BdqO1l5%2FQzpaCHHUhLZHS18p1B1zA6ssHpkeWaBnYIv8gQkUV6izJIxwmGJWR6RhiOa4gygRBzUDKcTxPYzcyv%2B1kflFEU53%2FoJ0FBcD3sxNDYoKX3TAESpv2iFgI1OW302OKUTL0fM4dwl1mvlX3SpnGHq9%2FCty581eInVECse3CqDycXIZOHgcjtOfrbn56itpBiMctu2tvGYqil48F%2BfWTSTD78tHKBjqkAfIA51UJ7QY0QIlDauj5mUNtnyuzGj%2BpFkBBtKCstlaEaXc0SKWb0oWmiCQycVx8%2B%2FG%2Fiqv0RqyAdhERH0mNy45O4yvPyu93Kkw%2FfZYBc6X3FHhfus4Q3xSAcG0%2B6ayf3AiJJPF2%2F5%2BPic7yptpp2Bi%2FQF2SeQVRXEKz3v0xQHma49h%2Flxy6hRe2bxyxJlCfvgADiIFbkHqTZ7UQX2Xo4BI6fO5Y&X-Amz-Signature=b3736603aca3e2e968b3389b6ae45653e12121e7b4b3cc5ec5d03b88b3f23e8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

