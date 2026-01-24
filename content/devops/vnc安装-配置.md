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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2G4ODGE%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIGsI6q0TBPBspf006nSwco5IN3r4QbRSVV8dP1NuVd4PAiB7Z6hn1szE3J74%2F2wc7U7jTH%2BSHvsiS%2B9SD3Yc169y0yr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMG0f3BOKQIYSabDkKKtwDEuRvkDJlvAQbGqF3UZ4dO%2BCth2YC8YidPQohjDi0ah8Vg6q9oUPaROuDoXagIGTodmHORt22q8cezYRkXFxgZr4oGeBfHOUEw5QUZbKSxa47Mu63Ao%2BOTje2COXX6sqJ6deOxoxK0NknRi66A%2F3v6FW4pkr9JJg1X7YQ0SDhdoI%2Fsam5B2xubhaNh%2FG88Ws2%2B8ULNBQPVWpbQaO1hbdUNxYLgPMIko%2F1U3wljD6RmgER9aS3QQb9AIUEoT4b089oobgJcaDgqhlf91QTI34zuCN3wEqlImxyGmjFXQ38wifp2Hw%2FjmcK8J9v5pe0OmzOP8BNZ4VihibaD%2FiTGORhEQf%2FkYQ81TcVxRXsyiFYryBaC2iLhJHg%2BrypoSi9G6cyv05QIlsiDbed3LL%2FD%2F5Bi9S0C3KhQI2VJuYFkgDWES%2FKhRYNPMr482pB%2Bn%2BVyaVGWCikgRv1RF7DqreSVqbuZV2F3Ax1RrupSBissiiFZVT5kHStV6yh0jI2a7zv9nNl01Gkvm6DCUMO%2Fdp6dPF07SaxH40kPs4XH%2BFXjQNoUMsirzVTqrz25la3EJBk1kiVFHZTY9LZwdNXpv%2F8FduePGtdLLwsUwBgBT6ZAB0dmtVtEA2BJ2oSUxjl7A4wtM%2FQywY6pgG%2F3JI6gP3J%2Fz5CJa0n11c2rhGTsw4Ej1TzUHCH5rjDrdwMZf1YQcTY%2BxtYv7zE8CmjAWEdJdAV3yzMDziOIDYMRJU50TtzyP%2FuEO8QwOqv3xDioIFSPxctzTIFW77BAcggFUaPXbXQtaHyCd8M7B3SqwCWVYqPSFKUXGBSarrRfbXxPfTfJ88aio9HZs3VR379GUkzsc1IqZESEIiADYCI6nT2qNrr&X-Amz-Signature=5a173b9148320a0ab9259c85491b299bab44fbe9161fcb91fd93883c8a7f411c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2G4ODGE%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIGsI6q0TBPBspf006nSwco5IN3r4QbRSVV8dP1NuVd4PAiB7Z6hn1szE3J74%2F2wc7U7jTH%2BSHvsiS%2B9SD3Yc169y0yr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMG0f3BOKQIYSabDkKKtwDEuRvkDJlvAQbGqF3UZ4dO%2BCth2YC8YidPQohjDi0ah8Vg6q9oUPaROuDoXagIGTodmHORt22q8cezYRkXFxgZr4oGeBfHOUEw5QUZbKSxa47Mu63Ao%2BOTje2COXX6sqJ6deOxoxK0NknRi66A%2F3v6FW4pkr9JJg1X7YQ0SDhdoI%2Fsam5B2xubhaNh%2FG88Ws2%2B8ULNBQPVWpbQaO1hbdUNxYLgPMIko%2F1U3wljD6RmgER9aS3QQb9AIUEoT4b089oobgJcaDgqhlf91QTI34zuCN3wEqlImxyGmjFXQ38wifp2Hw%2FjmcK8J9v5pe0OmzOP8BNZ4VihibaD%2FiTGORhEQf%2FkYQ81TcVxRXsyiFYryBaC2iLhJHg%2BrypoSi9G6cyv05QIlsiDbed3LL%2FD%2F5Bi9S0C3KhQI2VJuYFkgDWES%2FKhRYNPMr482pB%2Bn%2BVyaVGWCikgRv1RF7DqreSVqbuZV2F3Ax1RrupSBissiiFZVT5kHStV6yh0jI2a7zv9nNl01Gkvm6DCUMO%2Fdp6dPF07SaxH40kPs4XH%2BFXjQNoUMsirzVTqrz25la3EJBk1kiVFHZTY9LZwdNXpv%2F8FduePGtdLLwsUwBgBT6ZAB0dmtVtEA2BJ2oSUxjl7A4wtM%2FQywY6pgG%2F3JI6gP3J%2Fz5CJa0n11c2rhGTsw4Ej1TzUHCH5rjDrdwMZf1YQcTY%2BxtYv7zE8CmjAWEdJdAV3yzMDziOIDYMRJU50TtzyP%2FuEO8QwOqv3xDioIFSPxctzTIFW77BAcggFUaPXbXQtaHyCd8M7B3SqwCWVYqPSFKUXGBSarrRfbXxPfTfJ88aio9HZs3VR379GUkzsc1IqZESEIiADYCI6nT2qNrr&X-Amz-Signature=25747f16d5876b9a6a9599fba040f07dcd3b3436ff51942e35a39b671137e6a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

