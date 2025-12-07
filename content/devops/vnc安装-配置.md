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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHWQR3Q%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2BOY9v4hWTouV9oFYYyr6EKeVAEtKX4McBGq0ABLrHmAiEA81wN8NKs2NchCPdLshYGGcRNRLsEHWAAuHZZpzA%2FBF8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbtCodProgJUcOqLyrcA90pEopbIBs9%2BYb94hH74d%2Bun21bWxI%2B0lkztiQsvGm1mSgXtuoZn0dLzhWbHiV%2FfOaiLSa4zZ12PXUNMHxUZiBSZU1GuxzqLdIoAoAKzBSdzCFphf5NqkeBKEZIN%2FObdWNOZpMn2LrLl6s5809GCirPkNEGa5DgFFEp3BXcydvF5hjISs5AOcuSxpZLt6VbRBNiTxQME%2BH8MxXAkoC%2FAcuA3Wlum5dZ8J%2B7xKS2A6hSTZCj9FZV%2F%2BM9tx2XMF3oC30DpOHfzOtf%2B93yJ7xk9SgZEVeiDLqIXBip3PGJ%2B%2BexT%2BPBTGPGaNbGJKGoyPYjsocNRJBcc4COj3mHlAaw1HApidrFdVOcGkfnITVCH1DHA0WlMB1Pk9p3uAjUj1bUWjz6Uidq5ytPkr5J7CvLT5VPMgeePIp9N6t2EQT51UX0ZwSDmeQfz%2By8h3pAmie9F0uwMJWPfUoxFY43vkC4qcHulFbY66gKXRfkxVUQdYAOX3cdSVpnFRVnm9N5OFStiJLEOc634DXS7G7P0QzEaqpO7pOd3Wevlijb%2BggR4CQs3FJDIDGe4s7j0y1kIs22TRZPlLws8hQPZZ7cgEIs8%2B5ojXFeXOFyZDzHViJm%2Bv%2BF2UN0WoGBqVuHWdWvMLv90skGOqUBJXHVqwiNdKr%2FsVlH7qJev2bRx0GTOSsDJ3yo6bdkvK%2FDtLVGcdTOYr%2Fvwi5l9H3NQE81iWrfoUm590noM7eYBSiEMQbQhB0440tlmQ%2F8pyJYlrn1w9exZRu4ueACQ69ZuOD%2FC5gZTsYqINZGesBX55tNn1e92D9eOCLmdE%2BwqcoCHDyqhOUMnMzhjpe4RdlRXZDWW37RbNI1hWsozfMtvFmdjRBa&X-Amz-Signature=4ed9051360a9bcfac92c36d510420fd00efec1082f42be18719388b3e824d678&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGHWQR3Q%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2BOY9v4hWTouV9oFYYyr6EKeVAEtKX4McBGq0ABLrHmAiEA81wN8NKs2NchCPdLshYGGcRNRLsEHWAAuHZZpzA%2FBF8qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbtCodProgJUcOqLyrcA90pEopbIBs9%2BYb94hH74d%2Bun21bWxI%2B0lkztiQsvGm1mSgXtuoZn0dLzhWbHiV%2FfOaiLSa4zZ12PXUNMHxUZiBSZU1GuxzqLdIoAoAKzBSdzCFphf5NqkeBKEZIN%2FObdWNOZpMn2LrLl6s5809GCirPkNEGa5DgFFEp3BXcydvF5hjISs5AOcuSxpZLt6VbRBNiTxQME%2BH8MxXAkoC%2FAcuA3Wlum5dZ8J%2B7xKS2A6hSTZCj9FZV%2F%2BM9tx2XMF3oC30DpOHfzOtf%2B93yJ7xk9SgZEVeiDLqIXBip3PGJ%2B%2BexT%2BPBTGPGaNbGJKGoyPYjsocNRJBcc4COj3mHlAaw1HApidrFdVOcGkfnITVCH1DHA0WlMB1Pk9p3uAjUj1bUWjz6Uidq5ytPkr5J7CvLT5VPMgeePIp9N6t2EQT51UX0ZwSDmeQfz%2By8h3pAmie9F0uwMJWPfUoxFY43vkC4qcHulFbY66gKXRfkxVUQdYAOX3cdSVpnFRVnm9N5OFStiJLEOc634DXS7G7P0QzEaqpO7pOd3Wevlijb%2BggR4CQs3FJDIDGe4s7j0y1kIs22TRZPlLws8hQPZZ7cgEIs8%2B5ojXFeXOFyZDzHViJm%2Bv%2BF2UN0WoGBqVuHWdWvMLv90skGOqUBJXHVqwiNdKr%2FsVlH7qJev2bRx0GTOSsDJ3yo6bdkvK%2FDtLVGcdTOYr%2Fvwi5l9H3NQE81iWrfoUm590noM7eYBSiEMQbQhB0440tlmQ%2F8pyJYlrn1w9exZRu4ueACQ69ZuOD%2FC5gZTsYqINZGesBX55tNn1e92D9eOCLmdE%2BwqcoCHDyqhOUMnMzhjpe4RdlRXZDWW37RbNI1hWsozfMtvFmdjRBa&X-Amz-Signature=5ba8f6ffecc06118f91aa1f2a13ed8665fc59346143f8589b4bdc1dec58a8f92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

