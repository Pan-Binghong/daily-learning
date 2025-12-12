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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FJDWXUG%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDOf7YNc2RSRl2X%2BZsPEWreA6Rq1Mu9fo84%2FMcjL9qKXwIgGS%2F8%2F4x%2FabUbM2z%2FtBFg4dfQzfhWZ%2BHcdUF%2Fnj1%2FvToqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMboOfzioJywHO%2BiCrcA6VIX6lWTlDx1Y4mPxBtueeA0rX%2BB%2FkIyy%2BslbWyWSmC6nbYgecjNtzHh0LQvZDwCZz6wzBjNcX2FbLaNq0%2BVlIF6rLFPnsf3Mo3%2FbBQ%2B5r9i8camTIikRWIi%2FcM72eeuuRhPURaq897a%2BVovyQEqoVW7Luw86zYNF58Nhr9iYH0BIsSGz7haMa6vxOXwhOpXudvl%2BeKe4kI%2BLmoGojX7mlR2PkYAdVnnQfyaXgzE2AQKqwLnOBKeyz12K%2BXym28XQ6OdLaF8UEk%2BU7KmfGk%2Fq8wtcSAqBvpzGlNxixP8IyNZyBhaGNkdN67P9V6i1oPLUoeMaFCA5ZGgcymIDaUpK5Xwfc0Li5qAaLS8K68AxdOqLJlMs6Q1DqOAQMEt8ElPcqwDumFt8KNiCrh0%2Fb5%2F5NNNk7hTvCyg%2F2wTEXcadfVKLizCz%2B4laVVfz53D2jZt6LhFFDlMDE6hSzoZuvqec1JjPIuCvCWqChddvYk4JJ5tsIfn%2BqRZbEjQMN6i2UCoTM%2BmvQLxxw%2Bquo%2Fj5VRxyDQx5l%2BGAliPMxwsSzDD3Xo95FFOFIfK%2FgEXfpsyg5R3kA%2Fj21XABuHE3pihmXg9Jsyaz9vThH3ajGrCXAQScgbRRRjPwz4KNbfaZFEMMTV7ckGOqUB%2FofWC0bQCF4y0Z2D0IBUV%2FRgFBPYVElyDSUDGicT5sm9goaRzgNKB2hrRwwP%2FB8B99leO%2BfmpltbVYaMLw9ZZ4U6D0PJfEi3CAcNtlMnpy%2BiC0D8U2ARYgo3e1C95BcTE%2BBjaeK%2BvhMy%2BVa6QEc00RXKTBatlMtASox%2FaeDE460sQwwJBuhabo4ShetmQe4YkIzTrTUJxYWUzkgXAxT6T%2BOlTn7g&X-Amz-Signature=fd9363c358f01846827a652b4ab9f92e80dd7a155af3f9bfeef6bf3432dac358&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FJDWXUG%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDOf7YNc2RSRl2X%2BZsPEWreA6Rq1Mu9fo84%2FMcjL9qKXwIgGS%2F8%2F4x%2FabUbM2z%2FtBFg4dfQzfhWZ%2BHcdUF%2Fnj1%2FvToqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMboOfzioJywHO%2BiCrcA6VIX6lWTlDx1Y4mPxBtueeA0rX%2BB%2FkIyy%2BslbWyWSmC6nbYgecjNtzHh0LQvZDwCZz6wzBjNcX2FbLaNq0%2BVlIF6rLFPnsf3Mo3%2FbBQ%2B5r9i8camTIikRWIi%2FcM72eeuuRhPURaq897a%2BVovyQEqoVW7Luw86zYNF58Nhr9iYH0BIsSGz7haMa6vxOXwhOpXudvl%2BeKe4kI%2BLmoGojX7mlR2PkYAdVnnQfyaXgzE2AQKqwLnOBKeyz12K%2BXym28XQ6OdLaF8UEk%2BU7KmfGk%2Fq8wtcSAqBvpzGlNxixP8IyNZyBhaGNkdN67P9V6i1oPLUoeMaFCA5ZGgcymIDaUpK5Xwfc0Li5qAaLS8K68AxdOqLJlMs6Q1DqOAQMEt8ElPcqwDumFt8KNiCrh0%2Fb5%2F5NNNk7hTvCyg%2F2wTEXcadfVKLizCz%2B4laVVfz53D2jZt6LhFFDlMDE6hSzoZuvqec1JjPIuCvCWqChddvYk4JJ5tsIfn%2BqRZbEjQMN6i2UCoTM%2BmvQLxxw%2Bquo%2Fj5VRxyDQx5l%2BGAliPMxwsSzDD3Xo95FFOFIfK%2FgEXfpsyg5R3kA%2Fj21XABuHE3pihmXg9Jsyaz9vThH3ajGrCXAQScgbRRRjPwz4KNbfaZFEMMTV7ckGOqUB%2FofWC0bQCF4y0Z2D0IBUV%2FRgFBPYVElyDSUDGicT5sm9goaRzgNKB2hrRwwP%2FB8B99leO%2BfmpltbVYaMLw9ZZ4U6D0PJfEi3CAcNtlMnpy%2BiC0D8U2ARYgo3e1C95BcTE%2BBjaeK%2BvhMy%2BVa6QEc00RXKTBatlMtASox%2FaeDE460sQwwJBuhabo4ShetmQe4YkIzTrTUJxYWUzkgXAxT6T%2BOlTn7g&X-Amz-Signature=770a6b60c4b6658a7b34333f4d1a8edfd49a2de7fb9f190bfe70ad6555967cbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

