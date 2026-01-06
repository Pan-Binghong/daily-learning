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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RTICK3H%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc%2BXn5B%2B2tSWZUjoWX%2FniCrxgY9Gx3nBBi7GLify2%2BBwIhAKgsskkFnxXViPVVDE%2BGLER0q8uwDUdUKZwlMpY3SD0lKv8DCFMQABoMNjM3NDIzMTgzODA1Igy%2F132%2BsZz2AH6Yudoq3APx1EbfExPfmKfWc6Wil1ZO%2BZReTYiS59p2eEnv180JWQxCz2V7NKGWUsiE7GM5I%2BS%2B18eCwzkHfPSEZRbXa0tFsCF0ZQP2nyuUEfWI%2FkXrrvMwqI9opQmjuvFeUUlFAfeQ89BhJ%2FJDLRtsk6m7lpobT0O5E5fMlhlQBAv9RMeilhifckDBjtV57Cf4U2HfvveXSXr7UVIQGuGX0Kev0JuJTUhzgon4qtR5u6povZD5OcbYr2P0cbHlc0Efa8SKA8hb0nW90brs0IPYehxO5lDst43WDGfplsUbuuDB8%2BbwfADgXcPyllr5yK9UxzjncMkMn%2BbUVifZf%2FrvR%2F71I%2FmjnN45ENWtopjsJecdqilFkPqXu%2FgmDM5MuiK8SgNP5Zslg9kp5VUK3H3RO0L%2BElIC0H5ALIogdyHkn1VTOLMyBm0oeM5aG3MgQH7bdMZV6aAzBySGdEiFBire8NVHJpS6bPEXqzs7q7u2sK4HmimyGmINJyQRUDkCACJtc0ErNQD2KlaWpf%2BALgt964nHJkhbHr7XZoWE1KW3zSnKoNrbfHECIVnv9nIVHOm87j1s4ThdSHxw0D5%2BP2fW5Lw8IWjfnZ%2B%2FMr2%2BSAQ%2FqCkpMw9uWb%2Bg4twc86I0VzF2tjDZ5PHKBjqkAcKSiTBvTZcpg7Y9YvdFEZgar%2FR%2BdnnTKTDXMaXFjxROvELs8lgSts1c8FMdTAMLHrEHHXOhOQqRJaem%2BVETCYe%2FWOerIiLQVz%2FX9dLpw%2F%2BVRpHL6XnMkx1pEXhCzLRfiy9MQWnt%2BqKYkYAANDL2rhaLA%2FfTU6oMbdHIy6HqdRChd6yinob1P8U91GYWTR1lEh6lXdn6GcWIpczBXydvINF49Eh3&X-Amz-Signature=d5ece1138fd4e62c77e77200547b4343a8789f36617e43cfd6a20a2c71ee7b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RTICK3H%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc%2BXn5B%2B2tSWZUjoWX%2FniCrxgY9Gx3nBBi7GLify2%2BBwIhAKgsskkFnxXViPVVDE%2BGLER0q8uwDUdUKZwlMpY3SD0lKv8DCFMQABoMNjM3NDIzMTgzODA1Igy%2F132%2BsZz2AH6Yudoq3APx1EbfExPfmKfWc6Wil1ZO%2BZReTYiS59p2eEnv180JWQxCz2V7NKGWUsiE7GM5I%2BS%2B18eCwzkHfPSEZRbXa0tFsCF0ZQP2nyuUEfWI%2FkXrrvMwqI9opQmjuvFeUUlFAfeQ89BhJ%2FJDLRtsk6m7lpobT0O5E5fMlhlQBAv9RMeilhifckDBjtV57Cf4U2HfvveXSXr7UVIQGuGX0Kev0JuJTUhzgon4qtR5u6povZD5OcbYr2P0cbHlc0Efa8SKA8hb0nW90brs0IPYehxO5lDst43WDGfplsUbuuDB8%2BbwfADgXcPyllr5yK9UxzjncMkMn%2BbUVifZf%2FrvR%2F71I%2FmjnN45ENWtopjsJecdqilFkPqXu%2FgmDM5MuiK8SgNP5Zslg9kp5VUK3H3RO0L%2BElIC0H5ALIogdyHkn1VTOLMyBm0oeM5aG3MgQH7bdMZV6aAzBySGdEiFBire8NVHJpS6bPEXqzs7q7u2sK4HmimyGmINJyQRUDkCACJtc0ErNQD2KlaWpf%2BALgt964nHJkhbHr7XZoWE1KW3zSnKoNrbfHECIVnv9nIVHOm87j1s4ThdSHxw0D5%2BP2fW5Lw8IWjfnZ%2B%2FMr2%2BSAQ%2FqCkpMw9uWb%2Bg4twc86I0VzF2tjDZ5PHKBjqkAcKSiTBvTZcpg7Y9YvdFEZgar%2FR%2BdnnTKTDXMaXFjxROvELs8lgSts1c8FMdTAMLHrEHHXOhOQqRJaem%2BVETCYe%2FWOerIiLQVz%2FX9dLpw%2F%2BVRpHL6XnMkx1pEXhCzLRfiy9MQWnt%2BqKYkYAANDL2rhaLA%2FfTU6oMbdHIy6HqdRChd6yinob1P8U91GYWTR1lEh6lXdn6GcWIpczBXydvINF49Eh3&X-Amz-Signature=8c9914a07ce6cf10825f2b0ae602e9029444b3812781ccbbc14ea1bc35c54ba8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

