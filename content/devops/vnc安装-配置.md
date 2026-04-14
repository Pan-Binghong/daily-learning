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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5JFSUSW%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuvFpk4vL0LJbRoBBlRl8aZ2KV8avAcbicjBVI0aFYwIgZeteVuwqUoFsmMOYcDKO5RcVuAjvXytH0jMP%2BP1P%2F0oqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeX%2BKn6VqEWE5ZKjircA4Ufi%2BEtpH7JSysWJzm1df3Fpnt45x20T2rJYrWpSqTogeSdg2g%2FIMK2sh2nDw9kNV%2FEViLCSs5XvvybRquY9l34q61kRJjeafRWqIQGHtdv52w2vIcpsKqV4v970OGb4vgdq9DXJD7E21NxZWaCdFHJm3Z4bbUQn4kX%2BlUogla%2Bo2but52ahIRl1JkjrVAoshdkaCfrzKwRxynPITIwqETpQj0A3XMiPRy9Sn1cKu76W5aBn7Az5ptpV0lsCfStyAFIjgQPsw5pPW6%2FSdv4PAOl%2Bbk%2FZvGUZapBZIssiBYi1dq7M4moDEqRo7nw5X3dfzoiAGKJkd2PZk9E40IhtlWuNxPFv3%2BveH0elF8JpJJWe15HtPXbupnX4tBhfHDhp2THuDRXP7fSxjs6ivePB2S0u3tNTJ%2BbM%2BaprTLpn%2BKwRv3v4gwRZz4O4mIEyYI3GU%2BoRV1bPH%2FPnn4%2FAvX%2FWebgqVjVBnyEwna0nZGKhkIlhdzxwjmAdoYs7Hs6mgwCaNPk%2FMVjsGXuxnPji9QN7JtVi3YkZ6qp34TZuJVrGzzRwym5NPqEJqIbLuqUOTXpwFD8a7ttB0DsMQ1RZ5qCmXdCmAeHanTMnckMqjARsq%2Bs%2FxREyyq17EmkBY1RMO3g9s4GOqUBp2W0xVdG2aN1yPQfEMlAy69cigCjRV%2B9%2BdDpzy0BGhqTWHaXqKJ31grcymJzcIvBRFvSfyqfVzZCKLmmvimqbs74GJVA7UrTd8%2Bqa1EXayPLHklF2ulE6CqG4IpwKlmiqe59ARbQvXNw00ScNy%2BjtDONqrYTK3iKd%2FQEKqYYVlQZc%2FZQ4X%2FZqxoNJ3enFS%2FkZjzARP9MOamHKchaer4%2BJ5RaMk5R&X-Amz-Signature=ed72ba445c6f843582e5ec56a2a4cb77c40d65de025d22b15269721ffa69eb63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5JFSUSW%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuvFpk4vL0LJbRoBBlRl8aZ2KV8avAcbicjBVI0aFYwIgZeteVuwqUoFsmMOYcDKO5RcVuAjvXytH0jMP%2BP1P%2F0oqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeX%2BKn6VqEWE5ZKjircA4Ufi%2BEtpH7JSysWJzm1df3Fpnt45x20T2rJYrWpSqTogeSdg2g%2FIMK2sh2nDw9kNV%2FEViLCSs5XvvybRquY9l34q61kRJjeafRWqIQGHtdv52w2vIcpsKqV4v970OGb4vgdq9DXJD7E21NxZWaCdFHJm3Z4bbUQn4kX%2BlUogla%2Bo2but52ahIRl1JkjrVAoshdkaCfrzKwRxynPITIwqETpQj0A3XMiPRy9Sn1cKu76W5aBn7Az5ptpV0lsCfStyAFIjgQPsw5pPW6%2FSdv4PAOl%2Bbk%2FZvGUZapBZIssiBYi1dq7M4moDEqRo7nw5X3dfzoiAGKJkd2PZk9E40IhtlWuNxPFv3%2BveH0elF8JpJJWe15HtPXbupnX4tBhfHDhp2THuDRXP7fSxjs6ivePB2S0u3tNTJ%2BbM%2BaprTLpn%2BKwRv3v4gwRZz4O4mIEyYI3GU%2BoRV1bPH%2FPnn4%2FAvX%2FWebgqVjVBnyEwna0nZGKhkIlhdzxwjmAdoYs7Hs6mgwCaNPk%2FMVjsGXuxnPji9QN7JtVi3YkZ6qp34TZuJVrGzzRwym5NPqEJqIbLuqUOTXpwFD8a7ttB0DsMQ1RZ5qCmXdCmAeHanTMnckMqjARsq%2Bs%2FxREyyq17EmkBY1RMO3g9s4GOqUBp2W0xVdG2aN1yPQfEMlAy69cigCjRV%2B9%2BdDpzy0BGhqTWHaXqKJ31grcymJzcIvBRFvSfyqfVzZCKLmmvimqbs74GJVA7UrTd8%2Bqa1EXayPLHklF2ulE6CqG4IpwKlmiqe59ARbQvXNw00ScNy%2BjtDONqrYTK3iKd%2FQEKqYYVlQZc%2FZQ4X%2FZqxoNJ3enFS%2FkZjzARP9MOamHKchaer4%2BJ5RaMk5R&X-Amz-Signature=e73a8b3242e19ca4995800c4b943115217ffbf1a87fb4c0920c67027b1cde4f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

