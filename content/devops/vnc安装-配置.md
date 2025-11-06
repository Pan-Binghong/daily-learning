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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4USO2XD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy6v2fO7IqI%2FAsOodl4OgIEU8GBQ8OKdhy556vGcjycgIhANNSOoN6jYMgBt1MEbyfB0uRlpUfk%2BZtjM24iPuFTezVKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGG1a4v8sng3C4gEEq3ANLuU3hX1XmtksX4ISgsVBwvXSRqfXX8x3%2BJg1cnSMWZ%2F7%2FC9BHRbBdanCvwwYG9kSQrLDQue%2F%2FMz%2BPRKaZWkd3Eas6irJWEmPXOlpZ12AoDVJ2KDQNvlKu0kNy5EUMSeNUpoY67tgz2umnkWZ5geaIn4MiqHUrIdS1ZkFJqbAGymzvzP0tnO%2BeqtKrndiOXMBGemujt6y%2FT5txhxpPfa5hhFxs%2FSnyQPCblhVF91Fv9xgjMBD1uwDdZv3togP6ExR4zNxv%2F17aBqveX%2FJqRA%2F0JzifM%2BIA42IGoPBaqgBEssIL9uDCorz0MP0JL3U5FHPrbH%2FXmRo6w9VgswGv7kkbH2EQo9U2OjvSBsRMPWJoFJ8xq%2F4xE5C38Uan0I2wDHCmpz9vTHcve0Xpzmh%2B%2BEBKLOnRqSfkZP3pLz1xXYlbOk4nodmwJUABTjG7r56%2BwaSGjyIB%2FCOFUF4NfNGIqznqgf8XbjYR3TiFKrR5Nf4jWs4IHdy6ryhKP0nONnHpEurImYJJQVaUgMhfgfPpS1VHKjYhZuDx8Ng8hjZ8dIvcQHQlTFBCgYUxvReLJ%2BIg2sVG8OX4rJnEEXyQ5xRqykdk0hyPQZOQSF4ae4imxryOBIidWUbGf%2FfdyTtDszCK8q%2FIBjqkAbH2LuFOi36AwIX1OC5XQ%2Fh0J%2BPBnKcaGdKWgvrTte8QSZ%2BCgK5ac2E4lHQOOfIHOC%2FSlNewZrjC3GjFrFv6dHv5Fh1oLbIcbg6yP%2FA6exCs1Zq47Z5q3Th3%2FCTJETBcphmDONJXOj1X8DfRD1RkSo2rw0liNDxT%2BjT%2BkFCFgHpkib572rkfoOHcqvitjEc9cTypPV3GaldehPw8NgcOXhbF1Ocv&X-Amz-Signature=6dfc17e0d3f8c989a518c8c66b814269e6065dd626729d08de739d5ed5162aed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4USO2XD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCy6v2fO7IqI%2FAsOodl4OgIEU8GBQ8OKdhy556vGcjycgIhANNSOoN6jYMgBt1MEbyfB0uRlpUfk%2BZtjM24iPuFTezVKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGG1a4v8sng3C4gEEq3ANLuU3hX1XmtksX4ISgsVBwvXSRqfXX8x3%2BJg1cnSMWZ%2F7%2FC9BHRbBdanCvwwYG9kSQrLDQue%2F%2FMz%2BPRKaZWkd3Eas6irJWEmPXOlpZ12AoDVJ2KDQNvlKu0kNy5EUMSeNUpoY67tgz2umnkWZ5geaIn4MiqHUrIdS1ZkFJqbAGymzvzP0tnO%2BeqtKrndiOXMBGemujt6y%2FT5txhxpPfa5hhFxs%2FSnyQPCblhVF91Fv9xgjMBD1uwDdZv3togP6ExR4zNxv%2F17aBqveX%2FJqRA%2F0JzifM%2BIA42IGoPBaqgBEssIL9uDCorz0MP0JL3U5FHPrbH%2FXmRo6w9VgswGv7kkbH2EQo9U2OjvSBsRMPWJoFJ8xq%2F4xE5C38Uan0I2wDHCmpz9vTHcve0Xpzmh%2B%2BEBKLOnRqSfkZP3pLz1xXYlbOk4nodmwJUABTjG7r56%2BwaSGjyIB%2FCOFUF4NfNGIqznqgf8XbjYR3TiFKrR5Nf4jWs4IHdy6ryhKP0nONnHpEurImYJJQVaUgMhfgfPpS1VHKjYhZuDx8Ng8hjZ8dIvcQHQlTFBCgYUxvReLJ%2BIg2sVG8OX4rJnEEXyQ5xRqykdk0hyPQZOQSF4ae4imxryOBIidWUbGf%2FfdyTtDszCK8q%2FIBjqkAbH2LuFOi36AwIX1OC5XQ%2Fh0J%2BPBnKcaGdKWgvrTte8QSZ%2BCgK5ac2E4lHQOOfIHOC%2FSlNewZrjC3GjFrFv6dHv5Fh1oLbIcbg6yP%2FA6exCs1Zq47Z5q3Th3%2FCTJETBcphmDONJXOj1X8DfRD1RkSo2rw0liNDxT%2BjT%2BkFCFgHpkib572rkfoOHcqvitjEc9cTypPV3GaldehPw8NgcOXhbF1Ocv&X-Amz-Signature=c601159daca68851feba719c187c2b9f7858cb8828a5479ba5f99d5aee6fe216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

