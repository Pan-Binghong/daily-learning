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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6HPPDOG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDGjGWI2t5lPrtBaila7UwbhRofd22BE0iwydFd5psspwIgXGLInj6kzhUyo2zYcBLil%2BHx7bB0uB%2B7BV5YQlHefe4q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDIlJbFxhuisp0ALXZCrcAx0cER1qHjFbkn1dAaNP2NkrSyGvBPirelWY1C0YllfAPP7S8P3XigTFvoGgap2WUax9vgY0YxgjayqbboQCqr9zU80axzFwFV%2F%2FXivsEj0vYNgUujL9hKmRx7%2FUCEWEbQRnEBE04pqqBhy5sbUPy3xbcTY0XaqgVR52q98n%2BYLjCxoddNXnz9XsmmW4jVmS8pFOwY%2F9ix7la6qk0TSq4Z0AkDsoclGtWuiMFd5au7BBYl04OpClksUgt8b0PPp07%2FJW23StCCqHsgaW5IGlT44j2YBqLIWBn0OjUY7r69%2B0DnLSz6N7DbDUeTKUU7WZg68uWEIC6yttJQqiwXXazfYZbtww4hz3HZUPxKQRhVETAcOBfq5XaTVjxGkEnuHsr9caTzdQyJzRNp3LThRAhyJJymnba0GdfabdesnUiCHG%2BHGSU8rhuAnOUP%2FglCb%2Fhbpa%2Fii916Xx%2B%2BeRJspAXZMLLs%2BKKPG4K4PSR4gxfjaiFXjV3yAumbCItz%2FrZlhTICSFTA7HoSSHIYV0%2BPbhf%2FtqQluoWe22KUHfYlGlmcBeUgs1p3M%2BFRSannFLLmC%2BaHaPknSkE%2FTGnYQwnGOydQFOhzz6G3V5WQNYF0om59NK7iMmsm%2FkudR6GjDlMLCe%2F8gGOqUB26FZ7nMhWg%2BCg8IQIop4F2oyntXwA1l5r%2FcCP7oqRw%2Fe7sQ16M%2BiEM8NxDIPQh0wFmUCazt6Q3ITvPjF5nqYhnwvCCP4ZJCdgWx94GUTMzyYoPMWP118gC4EZUIeyANdibIYZU7bxuhLycI9QhdiXIpDBYPzz9ELpK2XXi1CZmZkYzNf06ZSMpPIzm%2FBUGBItV3gDaA8Ro9xkkaN6fkPxrsjeOMa&X-Amz-Signature=b0396d87d839bead72a42795c23011ce4d05bff28e765a172d6aabf077079d7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6HPPDOG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDGjGWI2t5lPrtBaila7UwbhRofd22BE0iwydFd5psspwIgXGLInj6kzhUyo2zYcBLil%2BHx7bB0uB%2B7BV5YQlHefe4q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDIlJbFxhuisp0ALXZCrcAx0cER1qHjFbkn1dAaNP2NkrSyGvBPirelWY1C0YllfAPP7S8P3XigTFvoGgap2WUax9vgY0YxgjayqbboQCqr9zU80axzFwFV%2F%2FXivsEj0vYNgUujL9hKmRx7%2FUCEWEbQRnEBE04pqqBhy5sbUPy3xbcTY0XaqgVR52q98n%2BYLjCxoddNXnz9XsmmW4jVmS8pFOwY%2F9ix7la6qk0TSq4Z0AkDsoclGtWuiMFd5au7BBYl04OpClksUgt8b0PPp07%2FJW23StCCqHsgaW5IGlT44j2YBqLIWBn0OjUY7r69%2B0DnLSz6N7DbDUeTKUU7WZg68uWEIC6yttJQqiwXXazfYZbtww4hz3HZUPxKQRhVETAcOBfq5XaTVjxGkEnuHsr9caTzdQyJzRNp3LThRAhyJJymnba0GdfabdesnUiCHG%2BHGSU8rhuAnOUP%2FglCb%2Fhbpa%2Fii916Xx%2B%2BeRJspAXZMLLs%2BKKPG4K4PSR4gxfjaiFXjV3yAumbCItz%2FrZlhTICSFTA7HoSSHIYV0%2BPbhf%2FtqQluoWe22KUHfYlGlmcBeUgs1p3M%2BFRSannFLLmC%2BaHaPknSkE%2FTGnYQwnGOydQFOhzz6G3V5WQNYF0om59NK7iMmsm%2FkudR6GjDlMLCe%2F8gGOqUB26FZ7nMhWg%2BCg8IQIop4F2oyntXwA1l5r%2FcCP7oqRw%2Fe7sQ16M%2BiEM8NxDIPQh0wFmUCazt6Q3ITvPjF5nqYhnwvCCP4ZJCdgWx94GUTMzyYoPMWP118gC4EZUIeyANdibIYZU7bxuhLycI9QhdiXIpDBYPzz9ELpK2XXi1CZmZkYzNf06ZSMpPIzm%2FBUGBItV3gDaA8Ro9xkkaN6fkPxrsjeOMa&X-Amz-Signature=1c68c4d6057a25573af8840dfadb33a406d87e1a5f160b2a436d02cbd3fdd883&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

