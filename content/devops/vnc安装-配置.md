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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBIQOQIM%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFdrYx6q5KCEhr3lF3zR7kXemkKqJd1HJ7uUeWr4ASToAiEAyxYq2wNSb%2B0Jrd4emdMSBhG%2BZu%2FUEyYH25DJV%2B3lrTkq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDGSjsEod5rOKIlY15ircA03YjRlX%2FFxqpxpY1CCdnCeRvONxhTVmtcFDjtyy%2FWOeZ4pq14CePz97aXe0XtmHKRu0EmdI2MJI8zvwwgkiVFRY6BGUey%2FyJ937lBaoXzWy30hmkEO%2FaLb0aoc1SNLeEQm3noCf0k01Xj1c3MSNYTXgMuVC1KPBbXQ7OnUO6z3aiwmEO5SqB%2Fw4RKvgn8RD0GGEofZVuNNsP8tC%2BdaCItwB3NZzHiTzO2gQBFvrw9sPteZPGOL%2BEVnzISWW97BaDaThEY9bS8QuzPkeTBRbJSwV0UN2FwBZpz4duGp4TjZxBhn0DhEaePZmoWHrLrBC9C6jSsrHlrHC04h%2F6C4hHgPeauJ4lX4V0PORz6UAMmnrQQXPwnW%2B72qdODzYVGlbu3o2kO5wvAtI2gyyciY1aG9rvIAbbihmq90orHKwV%2B%2BkqeijE%2FwMXQC%2BSF9JjKZqd3rtYGv50Jhc0fM%2Bn9wEuEzyAIundzJMGl5KPHf9tBLbOuHsc0Oniw1NjtPHtmxXKhSufYqt1qHmu0PR9yX8%2FvJ0XS5NaqoRDhSqIu57Z40fGlSSJWVwNSg9f1afg62vSf0TNK%2F3fGunKxB390%2Bg6etHoXgRoiVvbXSKE%2B2D%2BoFeGWaK6ZDkzH4OQGTVMNCczM8GOqUB7fploCdaZ2XYLtlTumG29DCXp9Hpw5igCBNy7aNMxM0KaChl8Rv3z%2BpnEfkazj22hJZIxGsIT7AOA0EqCx%2F7%2BuxNzyhYBp90LBTZDL%2FEWdbgeIhKYJxV%2B%2BbKzrrPNNZx05j7TjLsSFwQXoCaf8N4Dt4YOXuM6POedhmxVco9VGKkak5XkZEm%2F5jN7L6CVNYnjky0sxht%2FRdmOe2QUT1xw4j9GsOW&X-Amz-Signature=6f8f3e7620fc3fbf61bdf7404ca5782f048c95d9a2465995c4c0877d04bb74dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBIQOQIM%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFdrYx6q5KCEhr3lF3zR7kXemkKqJd1HJ7uUeWr4ASToAiEAyxYq2wNSb%2B0Jrd4emdMSBhG%2BZu%2FUEyYH25DJV%2B3lrTkq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDGSjsEod5rOKIlY15ircA03YjRlX%2FFxqpxpY1CCdnCeRvONxhTVmtcFDjtyy%2FWOeZ4pq14CePz97aXe0XtmHKRu0EmdI2MJI8zvwwgkiVFRY6BGUey%2FyJ937lBaoXzWy30hmkEO%2FaLb0aoc1SNLeEQm3noCf0k01Xj1c3MSNYTXgMuVC1KPBbXQ7OnUO6z3aiwmEO5SqB%2Fw4RKvgn8RD0GGEofZVuNNsP8tC%2BdaCItwB3NZzHiTzO2gQBFvrw9sPteZPGOL%2BEVnzISWW97BaDaThEY9bS8QuzPkeTBRbJSwV0UN2FwBZpz4duGp4TjZxBhn0DhEaePZmoWHrLrBC9C6jSsrHlrHC04h%2F6C4hHgPeauJ4lX4V0PORz6UAMmnrQQXPwnW%2B72qdODzYVGlbu3o2kO5wvAtI2gyyciY1aG9rvIAbbihmq90orHKwV%2B%2BkqeijE%2FwMXQC%2BSF9JjKZqd3rtYGv50Jhc0fM%2Bn9wEuEzyAIundzJMGl5KPHf9tBLbOuHsc0Oniw1NjtPHtmxXKhSufYqt1qHmu0PR9yX8%2FvJ0XS5NaqoRDhSqIu57Z40fGlSSJWVwNSg9f1afg62vSf0TNK%2F3fGunKxB390%2Bg6etHoXgRoiVvbXSKE%2B2D%2BoFeGWaK6ZDkzH4OQGTVMNCczM8GOqUB7fploCdaZ2XYLtlTumG29DCXp9Hpw5igCBNy7aNMxM0KaChl8Rv3z%2BpnEfkazj22hJZIxGsIT7AOA0EqCx%2F7%2BuxNzyhYBp90LBTZDL%2FEWdbgeIhKYJxV%2B%2BbKzrrPNNZx05j7TjLsSFwQXoCaf8N4Dt4YOXuM6POedhmxVco9VGKkak5XkZEm%2F5jN7L6CVNYnjky0sxht%2FRdmOe2QUT1xw4j9GsOW&X-Amz-Signature=66e5aa728896cee888b7516c854b95b39f7ca8f9aca1cd89243a60df00166361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

