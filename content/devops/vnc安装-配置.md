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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7HVE4AV%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCA12JoCXZu7dab18rTsC%2B%2BerecXKjNS%2B8AaJIk7z9SNAIhAOF7K7dHPHV6yj%2FDBenS1VYQ83WpyxahQ2GvPInV7qa5Kv8DCDwQABoMNjM3NDIzMTgzODA1IgyMu35AM7ULyWVLfRsq3APg%2BPg%2FEOBinJdmB5zDsGjCoaG9jMIrcnvAgkPRvWqWadjeeku59snrJt4ASeQyqwe2wRbTzczgWY0XSTJ8C%2FVcfwlXOi0q3PbzVnm7wC%2Fa9lr0hM1Nn5dqI7bU64MvdOsfPQAdVANTqHQBB%2BCLTYL2GtQQQoNNSzTgiYvwwRXjOxlfAsh7heoxHtWg5Xo3G9fIPaXBfoSsAvJFckHidEQ%2B5udOGkCXkJLXT9KhzZ4xbkwkHCCg15EOVqikfzuO%2F4I07pJgm67%2BZAS5kYyl5KP%2F9AMopJOPV55x4yx7QYlv1fLUtmHrOS3WoQy5pgn2kwkBP27GiBzi3YDWdhzTlrlqHxKas%2BMv803kt1ox4VuMo6fSVNtkMNclPAC9uyAd1o%2B3koTmYBahoNbuemR05tuMAX0DD%2FP8IVDggtsDb%2B7e11LPK0K7LS2mLkbFkwk%2Fp2196klWD3pKO4SOQGxpocCROjJ51wuTB21De8PSJIHWED0%2FTMIp8d9OuIdfa1ges%2FI%2Bj7NuqaN%2B6NHDQkGOMJPKqlGek5eLPbNDxYivKnPnIiAlYCOOXfxw5pAq3u24JNFpduggM2DCiZUSNfTx%2BxSOBDLLLez94QlhdXZQazBuTRRbuF%2FcLktsPO92cDCJkb7NBjqkAccJFlSZonogEl4ovjn2rscBtbniFAHSC0RYjeyfi%2BxzR%2B%2BhZpy5H%2BtrWI5cRE4DZbDb7KmndXszwHrCpoPycH%2BLI3X0sEjgetqb3v9MOXIXBWl9a6mzbbZVqHBASycbl9S60tbbq61AgV3YPN%2F%2BY5tIRVrqz30%2FbM3xtWgelUy57qab0UX3ytYbRVo2Hr%2Bn5ffjYlRwWLbV%2FS%2BnkIuzFtbUP%2B9Y&X-Amz-Signature=c4b7e0adb8b0d1a19944be48c369e1a415be21f6a5978e89941db9039fb4d798&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7HVE4AV%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCA12JoCXZu7dab18rTsC%2B%2BerecXKjNS%2B8AaJIk7z9SNAIhAOF7K7dHPHV6yj%2FDBenS1VYQ83WpyxahQ2GvPInV7qa5Kv8DCDwQABoMNjM3NDIzMTgzODA1IgyMu35AM7ULyWVLfRsq3APg%2BPg%2FEOBinJdmB5zDsGjCoaG9jMIrcnvAgkPRvWqWadjeeku59snrJt4ASeQyqwe2wRbTzczgWY0XSTJ8C%2FVcfwlXOi0q3PbzVnm7wC%2Fa9lr0hM1Nn5dqI7bU64MvdOsfPQAdVANTqHQBB%2BCLTYL2GtQQQoNNSzTgiYvwwRXjOxlfAsh7heoxHtWg5Xo3G9fIPaXBfoSsAvJFckHidEQ%2B5udOGkCXkJLXT9KhzZ4xbkwkHCCg15EOVqikfzuO%2F4I07pJgm67%2BZAS5kYyl5KP%2F9AMopJOPV55x4yx7QYlv1fLUtmHrOS3WoQy5pgn2kwkBP27GiBzi3YDWdhzTlrlqHxKas%2BMv803kt1ox4VuMo6fSVNtkMNclPAC9uyAd1o%2B3koTmYBahoNbuemR05tuMAX0DD%2FP8IVDggtsDb%2B7e11LPK0K7LS2mLkbFkwk%2Fp2196klWD3pKO4SOQGxpocCROjJ51wuTB21De8PSJIHWED0%2FTMIp8d9OuIdfa1ges%2FI%2Bj7NuqaN%2B6NHDQkGOMJPKqlGek5eLPbNDxYivKnPnIiAlYCOOXfxw5pAq3u24JNFpduggM2DCiZUSNfTx%2BxSOBDLLLez94QlhdXZQazBuTRRbuF%2FcLktsPO92cDCJkb7NBjqkAccJFlSZonogEl4ovjn2rscBtbniFAHSC0RYjeyfi%2BxzR%2B%2BhZpy5H%2BtrWI5cRE4DZbDb7KmndXszwHrCpoPycH%2BLI3X0sEjgetqb3v9MOXIXBWl9a6mzbbZVqHBASycbl9S60tbbq61AgV3YPN%2F%2BY5tIRVrqz30%2FbM3xtWgelUy57qab0UX3ytYbRVo2Hr%2Bn5ffjYlRwWLbV%2FS%2BnkIuzFtbUP%2B9Y&X-Amz-Signature=d8cdf43701fb66e4856f6da81170bcee146e17f23cc443ff06bc3a36e72aa918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

