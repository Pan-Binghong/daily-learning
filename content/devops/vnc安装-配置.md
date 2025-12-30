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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663G4LXAW%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFR8Bdcpc%2BrbUPGOF%2BmE9AESx86wFb1X6o7F8jWKNxyLAiEApQm22f8dfKValZvTt2wqCTayIIMMLrhx7BbZaNV1aVcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLiEOwXLKa2Ak23KESrcA0RSv3OsIuPmwr9ki7Wykch0ianAq8u%2FmdDwHqBSYXaFyJvCD8wc0aSxAUomecf7P76uHDHQhv%2BDSqINECXwPdDmEQ9AoCu4KU3vuN8bt%2Fv%2BU%2BXFr5DpT08CJQFieUchesqiFsvgOrQYakJVS46m0WY4USAL9E%2FlsLri51CIpiqutWT5BK5h4NTtBTdgNDuuEG7nycVn%2BOl9mq%2BTNl52mpxOge5vZsD2P%2FDi38FeEwwK0eRx1EYT%2B%2FbiTtEyhQ5a9PcmNhoszgIvmkqLAgwESzLH%2BX6MHOYIbXGgSJjyCIh95d9PMOKBs9UcOH%2BW99HQBiGGmi98XA%2BdxBwJQ1%2BjXFQJtSF2TQleLkZHfMtcJGsV7TISALttD7lBLYCmnQLcnrd7Qwk2PwsAIoKEYn3iWE9fvAVD1aZPw9WWEKndtZm0mRzmIwUhZEPH2c5C9T1B0n9cMwvGhNzKrnVheBst58FWQixtx14Gp8TU6tuRvB65CPNhFMQKY0BLZmZbVgZpuxRtNx75wY0klewCaUlE7zO%2Bp2Ar%2Fjlxp6m2Ox7gubr%2FpjSi0L9Dh8pWX0FErqMRrdCWo7T35kOPHuFdbnhFmvhXdzAfSlCncnVXDKi3DAXfmVxbzv%2FZmRcPgTCwMOrVzMoGOqUB9gtSPuY8LHLJDsCCrjKNFfz2600TBtaY3hWB719G2JBfR2%2BKfLrY9OOqRD3YOGTVHHJMR8raauuSR19L3fQtcWbwRVND6nreL1qKKLluHMhkinhRoxgYECem7Ty%2ByDlftPw%2B3ikx7wwPyTDyVNETDeXYfUciQP8vL%2FHpcDrWPLf8fJpSNXasCPX5Tg4tFK9XKSNgr17ra64A%2Fam7pXzpSqki%2FCLa&X-Amz-Signature=75351794b0fd665afb35df0ea5ebc8504470fb29ea2b9fb71a559118ae6914ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663G4LXAW%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFR8Bdcpc%2BrbUPGOF%2BmE9AESx86wFb1X6o7F8jWKNxyLAiEApQm22f8dfKValZvTt2wqCTayIIMMLrhx7BbZaNV1aVcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLiEOwXLKa2Ak23KESrcA0RSv3OsIuPmwr9ki7Wykch0ianAq8u%2FmdDwHqBSYXaFyJvCD8wc0aSxAUomecf7P76uHDHQhv%2BDSqINECXwPdDmEQ9AoCu4KU3vuN8bt%2Fv%2BU%2BXFr5DpT08CJQFieUchesqiFsvgOrQYakJVS46m0WY4USAL9E%2FlsLri51CIpiqutWT5BK5h4NTtBTdgNDuuEG7nycVn%2BOl9mq%2BTNl52mpxOge5vZsD2P%2FDi38FeEwwK0eRx1EYT%2B%2FbiTtEyhQ5a9PcmNhoszgIvmkqLAgwESzLH%2BX6MHOYIbXGgSJjyCIh95d9PMOKBs9UcOH%2BW99HQBiGGmi98XA%2BdxBwJQ1%2BjXFQJtSF2TQleLkZHfMtcJGsV7TISALttD7lBLYCmnQLcnrd7Qwk2PwsAIoKEYn3iWE9fvAVD1aZPw9WWEKndtZm0mRzmIwUhZEPH2c5C9T1B0n9cMwvGhNzKrnVheBst58FWQixtx14Gp8TU6tuRvB65CPNhFMQKY0BLZmZbVgZpuxRtNx75wY0klewCaUlE7zO%2Bp2Ar%2Fjlxp6m2Ox7gubr%2FpjSi0L9Dh8pWX0FErqMRrdCWo7T35kOPHuFdbnhFmvhXdzAfSlCncnVXDKi3DAXfmVxbzv%2FZmRcPgTCwMOrVzMoGOqUB9gtSPuY8LHLJDsCCrjKNFfz2600TBtaY3hWB719G2JBfR2%2BKfLrY9OOqRD3YOGTVHHJMR8raauuSR19L3fQtcWbwRVND6nreL1qKKLluHMhkinhRoxgYECem7Ty%2ByDlftPw%2B3ikx7wwPyTDyVNETDeXYfUciQP8vL%2FHpcDrWPLf8fJpSNXasCPX5Tg4tFK9XKSNgr17ra64A%2Fam7pXzpSqki%2FCLa&X-Amz-Signature=c82d3ac8b6193aa1844129a9619735900a7e7b4b8a496176fe0bfa13b3201376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

