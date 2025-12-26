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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P4D7TAO%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlcjvyDLxEfzFzak2KwWQNPkoTU86cDSA6nE9jKCaYyAiEAymLufIO0SWdgeHT%2FlKXOO%2Bok3%2BjnssLYKO%2BP4UjA4aEq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDOI%2BYCv7LXk92VYNjircA2NZOT4jhNQHvsHi%2ByyC1jjhypMJqrP0YcZB9p8DzxuqGJGrG1l6cD7zQ%2FrTz5Q02EDSI94AIlrCJPwWaDuaakccpTwrwHEhP18%2FQILbhZ2ezGF1qjQ3r%2BXextDRD2Sv0wsVD3m0rs6JBK%2Bd6lOZk0rwoEWvSudsU3BMuXw%2B5r1aoQF2yTjN4NCJTamVIM3x74Czdy87jYGBRXcb1PWKJLpoYPaiivZwkwCoqOzJeFa5omHefvNWKN%2F79NCIeDqAAj4RZseRcJmkdvCYMZHIsl%2Bxs1HdXUdhC8sbdmMo74rGrsKvg9RbNq%2FAgzMLZAX18gjJI6Pn%2Bvwf5v05q%2BLvXaaIkwwIYDzEkEWAZFJN4p5rJvQMHFzK7rjsVFS6wKFOw4eZ01ZTz%2Fjp5y1AeQfK%2FEIxpqZCgzkuRwwxbI3Kg1goD9TtSOYl%2B95008z6zfSKJRZVaJcWlxBx1zplsuXIdNBXX%2FcdBAqj9k35QL8mxd11xFq%2Fq4yVS1vtn%2Fjr3Bk29jeaqxuHL9rM0KTWq%2BbNGNNmERV6J9nwcRzOhpXFYsu22k548vaZQBymk7S66RhsKHALrcn0U5Wa4wG%2FYMPCYokGqP6Zpw9rjDAmnzq8Exm%2FNmowqWK9ZoM%2FyvMbMKDSt8oGOqUBjQAD9wjlPKPa2KLn%2FHdRLGuZw7CuUmP1fQwjPSgG6mBud8OhrbOIVqyeZKQWiXzaR1bCcF2GBr9%2B0MZ0%2Fy7yA7Z1IFMYhnap2rJI98R8Jie5ApWALxryxmo%2BvSONugyQwgg4u8aXg4F4UfF7IQ3HjI88FEs3EHp%2F%2FPWG%2BWZ0llejGGn%2FlSLuBEDM3NOsmM2R63YzenybewfrMU8vKuyUJuWUZi5s&X-Amz-Signature=0a1ba028824488b12a1c6519fdf10eeb5e9be87087b09e636a0357f9882054f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P4D7TAO%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlcjvyDLxEfzFzak2KwWQNPkoTU86cDSA6nE9jKCaYyAiEAymLufIO0SWdgeHT%2FlKXOO%2Bok3%2BjnssLYKO%2BP4UjA4aEq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDOI%2BYCv7LXk92VYNjircA2NZOT4jhNQHvsHi%2ByyC1jjhypMJqrP0YcZB9p8DzxuqGJGrG1l6cD7zQ%2FrTz5Q02EDSI94AIlrCJPwWaDuaakccpTwrwHEhP18%2FQILbhZ2ezGF1qjQ3r%2BXextDRD2Sv0wsVD3m0rs6JBK%2Bd6lOZk0rwoEWvSudsU3BMuXw%2B5r1aoQF2yTjN4NCJTamVIM3x74Czdy87jYGBRXcb1PWKJLpoYPaiivZwkwCoqOzJeFa5omHefvNWKN%2F79NCIeDqAAj4RZseRcJmkdvCYMZHIsl%2Bxs1HdXUdhC8sbdmMo74rGrsKvg9RbNq%2FAgzMLZAX18gjJI6Pn%2Bvwf5v05q%2BLvXaaIkwwIYDzEkEWAZFJN4p5rJvQMHFzK7rjsVFS6wKFOw4eZ01ZTz%2Fjp5y1AeQfK%2FEIxpqZCgzkuRwwxbI3Kg1goD9TtSOYl%2B95008z6zfSKJRZVaJcWlxBx1zplsuXIdNBXX%2FcdBAqj9k35QL8mxd11xFq%2Fq4yVS1vtn%2Fjr3Bk29jeaqxuHL9rM0KTWq%2BbNGNNmERV6J9nwcRzOhpXFYsu22k548vaZQBymk7S66RhsKHALrcn0U5Wa4wG%2FYMPCYokGqP6Zpw9rjDAmnzq8Exm%2FNmowqWK9ZoM%2FyvMbMKDSt8oGOqUBjQAD9wjlPKPa2KLn%2FHdRLGuZw7CuUmP1fQwjPSgG6mBud8OhrbOIVqyeZKQWiXzaR1bCcF2GBr9%2B0MZ0%2Fy7yA7Z1IFMYhnap2rJI98R8Jie5ApWALxryxmo%2BvSONugyQwgg4u8aXg4F4UfF7IQ3HjI88FEs3EHp%2F%2FPWG%2BWZ0llejGGn%2FlSLuBEDM3NOsmM2R63YzenybewfrMU8vKuyUJuWUZi5s&X-Amz-Signature=4182845ddfce294cbc9f3a041352f8c860a2666b3f28fa43db3512cf8450e595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

