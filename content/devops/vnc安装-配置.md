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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEB74YPN%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC9Sauyq842po%2FYxHnCgPVqlKT0OhIZdGe8UijnxG2hMAIhAOeiqRtU5hk%2Bt%2FwNnQNnZMYY4dOPWvqXNQtdN6PKMsNFKv8DCCsQABoMNjM3NDIzMTgzODA1IgxC853%2Fz3NqKX69QaIq3ANkIx54FxWNO5hVaPoTM6EmU3JlKyOn3WrO%2FxZj1Ag%2FvlcyQJaWlgJQRFvsL4YgEqzOuwLK1%2BA9ikhIMdRgOt5h5PQI6EDMjcBAj0n4%2FgRpnyqKtqUEOzT5yBxNGOHIBPBA2vXQpyS8ph8pWOGzCINwyptviVTrmBAkPXFsQk6giNyo8NbHBRAOgFr0WF8Ht%2F6Rcwp37W2b21CmSUtzsU%2FdvIAYpXxUeSzKxlR2isPPzljoEHufK1DtYIMNDqTAnCTYNyVTN%2FauDzfAyEtJlUrzZGikvqY9ijIbyv1H1fc1jgxlPH0is6lQmF5q%2F%2Bhk2S%2B3mH05xSNSoAgaBYv%2BHVtOTYzK1G6Zy4W1zsf86QZiLp67YZg1MzOa5iFThKW8vj6Zkz%2F8TOk2dv%2BmtsjiHd2mpJBkyt076JhUOt%2B8Qr4OINg0DyG3QC5w60iOQbHQcWpXgg%2BGy64NxGBNPnelnoWeu4Cnp1cEGCaWsKLXO8eWZoEVPW3fmhVo3MFIKPeMcBcVWn5DV3JeCuYvBO8%2Bhofy9fcKEXhLhxyovmnXsJq15idRv16qA12Na4fmnrt19duWrSFnSMNQwmpwCf4om8%2B0GdZaOSqxyst6PTC%2B%2FFtRe%2BCtE2pL2sNh61WTrzD3mqHLBjqkATKD%2FoXY10TCcIeNvI4sPRGWHSIko9aeQ7yEbh3xgTQtdmiHAkl1H3Dx4gM34ShP%2BjlLvII4sEAFVFuDGx3xNdfPzIRuqwaIAMt5CWkY5W20YpHQ9gs3F1Mv2CkxRdkNayr04gOVfQ5tGP3TZVA2qWZ4bOOJOlpFtkFEkPTAqOVycot5OpLJtzPTlSlPjfmfxBeKL8640YMOZ4TwjRyDu1AwDqLe&X-Amz-Signature=0811a5999c53aa9b6b97ee8a1a59eedffc2df562184af40f7770ae9e50c2b7f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEB74YPN%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC9Sauyq842po%2FYxHnCgPVqlKT0OhIZdGe8UijnxG2hMAIhAOeiqRtU5hk%2Bt%2FwNnQNnZMYY4dOPWvqXNQtdN6PKMsNFKv8DCCsQABoMNjM3NDIzMTgzODA1IgxC853%2Fz3NqKX69QaIq3ANkIx54FxWNO5hVaPoTM6EmU3JlKyOn3WrO%2FxZj1Ag%2FvlcyQJaWlgJQRFvsL4YgEqzOuwLK1%2BA9ikhIMdRgOt5h5PQI6EDMjcBAj0n4%2FgRpnyqKtqUEOzT5yBxNGOHIBPBA2vXQpyS8ph8pWOGzCINwyptviVTrmBAkPXFsQk6giNyo8NbHBRAOgFr0WF8Ht%2F6Rcwp37W2b21CmSUtzsU%2FdvIAYpXxUeSzKxlR2isPPzljoEHufK1DtYIMNDqTAnCTYNyVTN%2FauDzfAyEtJlUrzZGikvqY9ijIbyv1H1fc1jgxlPH0is6lQmF5q%2F%2Bhk2S%2B3mH05xSNSoAgaBYv%2BHVtOTYzK1G6Zy4W1zsf86QZiLp67YZg1MzOa5iFThKW8vj6Zkz%2F8TOk2dv%2BmtsjiHd2mpJBkyt076JhUOt%2B8Qr4OINg0DyG3QC5w60iOQbHQcWpXgg%2BGy64NxGBNPnelnoWeu4Cnp1cEGCaWsKLXO8eWZoEVPW3fmhVo3MFIKPeMcBcVWn5DV3JeCuYvBO8%2Bhofy9fcKEXhLhxyovmnXsJq15idRv16qA12Na4fmnrt19duWrSFnSMNQwmpwCf4om8%2B0GdZaOSqxyst6PTC%2B%2FFtRe%2BCtE2pL2sNh61WTrzD3mqHLBjqkATKD%2FoXY10TCcIeNvI4sPRGWHSIko9aeQ7yEbh3xgTQtdmiHAkl1H3Dx4gM34ShP%2BjlLvII4sEAFVFuDGx3xNdfPzIRuqwaIAMt5CWkY5W20YpHQ9gs3F1Mv2CkxRdkNayr04gOVfQ5tGP3TZVA2qWZ4bOOJOlpFtkFEkPTAqOVycot5OpLJtzPTlSlPjfmfxBeKL8640YMOZ4TwjRyDu1AwDqLe&X-Amz-Signature=f319b56735149a7a38039ee603950b1bf02edfb8fe3d7bff5180b07cf7f57f81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

