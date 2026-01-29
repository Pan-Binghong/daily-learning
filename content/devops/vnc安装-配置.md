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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6R6IDZ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FY0OX4Pl7stR%2FSW7TfNJK8%2FcXDFrGEN26QA%2FajCYsLQIgSHn0frX3tmLHP1LMI31%2BmjmDnv6bSqadduBXurixDFUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDELvrAMzpiOSiMuP8yrcAzGd8PgaBX%2F6cvSeZmAUciRCbFgJgg6cNELRfg6e0HHpCB2NXNHuuC03rxncbv62qE20erQ%2FlrkBZM1qeDFQJtpxg4qoc1j3ov%2Bs%2FEB6d14HbXI1ZdQNWOt2M0nNGR2J1xA77bznsN%2FoOGwnnCRpv%2Fe4jhNa8jqM%2BOcbTeVl9Qs5wWX9wYgoVLs%2Ff6XqsHRtb4Np%2BUvTmAcyGEu6H3AbakPCMAPyo4p0FENIS9QDh1ONwy13Z4i1nMOQQcV60nsBYYB5qXBU3oK0Cf4%2BS0wClfsOzpsYcSvNZdmjPo8kFiGe2hSD7L%2B%2FheNekW5q%2FybezZYCpQdrx1pm3ChqezJ2Vabjf5qFflio9JJBWUyagV3TMnBcpH1gaIpyHoWZyAecF4rsPzd38rKtvZpNB5KNYC%2FmBN8O9dCaPJe5jG%2B8N7nCvxG9FZVj82oy9d%2FXYducYFFILch42HgBYMJzvZ8Gb9E5Hp6HvsrfTZCcR7rVO0m8PKtX3UArRHyuFN9RNHzb2zwCL2Gw8%2BbqUNYmUVlOerWESkJm%2Bx4GrBswL6eddyKFJzuQvQ63k%2B5GTT0dFw30TjpnYp2jEFOermjrF9hh1tWXVcwtDRGDilmxyJ9I%2B0Is5BlhUiktkYZEQo64MN2h68sGOqUBO12sY0lphr32%2BlPACR2W1V%2B5NlhhXh7wokFxPEEeAJkwfC92uqFLi2UaSfxUvduZTzhLgytoRyKzosolEZC44Uw1vulEYmGFzVOebIoRnoDR6v6ll2GdCnJUI0mSLaJQP0QEMOPNDwBOkUTS5lc5FE1UnR52nFX8Z74P0PX92%2BdqJQGrhbAswvlIrBCXDzutHRd8Tf9FvfXvZA9qMtdKB5EH3lH9&X-Amz-Signature=742d8ba691b5449934acfa37dbdd5eb9e0e03a46ba7f8d9a7b41bec82f6711cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6R6IDZ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FY0OX4Pl7stR%2FSW7TfNJK8%2FcXDFrGEN26QA%2FajCYsLQIgSHn0frX3tmLHP1LMI31%2BmjmDnv6bSqadduBXurixDFUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDELvrAMzpiOSiMuP8yrcAzGd8PgaBX%2F6cvSeZmAUciRCbFgJgg6cNELRfg6e0HHpCB2NXNHuuC03rxncbv62qE20erQ%2FlrkBZM1qeDFQJtpxg4qoc1j3ov%2Bs%2FEB6d14HbXI1ZdQNWOt2M0nNGR2J1xA77bznsN%2FoOGwnnCRpv%2Fe4jhNa8jqM%2BOcbTeVl9Qs5wWX9wYgoVLs%2Ff6XqsHRtb4Np%2BUvTmAcyGEu6H3AbakPCMAPyo4p0FENIS9QDh1ONwy13Z4i1nMOQQcV60nsBYYB5qXBU3oK0Cf4%2BS0wClfsOzpsYcSvNZdmjPo8kFiGe2hSD7L%2B%2FheNekW5q%2FybezZYCpQdrx1pm3ChqezJ2Vabjf5qFflio9JJBWUyagV3TMnBcpH1gaIpyHoWZyAecF4rsPzd38rKtvZpNB5KNYC%2FmBN8O9dCaPJe5jG%2B8N7nCvxG9FZVj82oy9d%2FXYducYFFILch42HgBYMJzvZ8Gb9E5Hp6HvsrfTZCcR7rVO0m8PKtX3UArRHyuFN9RNHzb2zwCL2Gw8%2BbqUNYmUVlOerWESkJm%2Bx4GrBswL6eddyKFJzuQvQ63k%2B5GTT0dFw30TjpnYp2jEFOermjrF9hh1tWXVcwtDRGDilmxyJ9I%2B0Is5BlhUiktkYZEQo64MN2h68sGOqUBO12sY0lphr32%2BlPACR2W1V%2B5NlhhXh7wokFxPEEeAJkwfC92uqFLi2UaSfxUvduZTzhLgytoRyKzosolEZC44Uw1vulEYmGFzVOebIoRnoDR6v6ll2GdCnJUI0mSLaJQP0QEMOPNDwBOkUTS5lc5FE1UnR52nFX8Z74P0PX92%2BdqJQGrhbAswvlIrBCXDzutHRd8Tf9FvfXvZA9qMtdKB5EH3lH9&X-Amz-Signature=62b2a0b9086a0be7bbabc7cf73c5581ef7f1f9b79fbe141eb5b5b068ff7d9867&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

