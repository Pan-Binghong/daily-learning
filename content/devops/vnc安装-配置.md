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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLZMIZ62%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDHPqDoXScjqI1UiobdQ%2Fdt6JQVeSrwgzwR6oFscnU73gIgaROpPrBql%2FMyaVyQNGb149UrQveQTWzE9fY57c4TPRUq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJzEUN%2BueNbBIIaUcSrcAzrfdqZGfakBXpsmCI3OOiaYTAjMnhDEttF2wOR%2F57IPlSGtRrYRCIZ0I96rvt3H6C3TI7JJuqq0VQ3OfJiFTznMgnuAwmrihRkR%2FSQn7cWU4neS4f2vTYx50P0A4RX8irErnKPuuAeYzy77x0vHLscygX1YGdetJjmaPkmyMziNXZw5r1PoWB1MJpcsfLW1p9w741DBfEYM0vkwt6Cf%2Bb7mBmEMYA9dnJiBTeo7GO2hRX3%2FetNZtu7%2B%2BiryXdrsFs4QAoURZZouIZ2KbcafClFGGuYDjjlNTpih6YGJtAzWin4nShDldQazMAYd19OSSG3HLvmAN6i4%2FWt%2FfJCPBbKXYIwMqUZRMoU7zbmQOMVvNly57PrdFIzyx%2BBRg%2F9Y7OFaTM3sU%2FpwYtysjEO%2FeETzOtFQrk%2BrzLThIsekcekh2EkhMGZoTBYAKn6pUn%2B03EBAryjqYH3qznW7EQA%2FNeo1Sh%2BOxHsUFe7lFikjgIH%2BybCzG4a4fZFjzBHyVb1oLZScv9gl%2FayWL0HwGVrTRqqMJWfypxEPMhjHk2M5A0M%2BPI3Kgf8C3fvIypPPOAlKrgT54J66TgSPSut6PtkqXCCkgLgoAznUcTvBuOzFvreRHwgygRTMA%2FFZnmDHMJGezM8GOqUBuRNEm8Mkv5qMb6PqWbiOm4oQYZrbeviHF0WSZw7%2B89TsWWQXcBa33PuiBZQ635Y%2BUhBggDdoJoSt2wHnAIgF%2F9GYhvmRmNSJZ4%2FNXo%2Biu1ArMq%2FAv0o6R7QjKJQrRSTeoK8WH81BUmTUjUhKIE9CVlwUORyMlEXtVYCibJGCdS8zHI%2BI8tRZvDXXAtsaiXFRW33H5SzFtey0ibMIfLzlb9Cty4qm&X-Amz-Signature=3d6e169e64a8db220fae47e635c0f055ef0b947d37f79b4f9a0e172ac26edb98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLZMIZ62%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDHPqDoXScjqI1UiobdQ%2Fdt6JQVeSrwgzwR6oFscnU73gIgaROpPrBql%2FMyaVyQNGb149UrQveQTWzE9fY57c4TPRUq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDJzEUN%2BueNbBIIaUcSrcAzrfdqZGfakBXpsmCI3OOiaYTAjMnhDEttF2wOR%2F57IPlSGtRrYRCIZ0I96rvt3H6C3TI7JJuqq0VQ3OfJiFTznMgnuAwmrihRkR%2FSQn7cWU4neS4f2vTYx50P0A4RX8irErnKPuuAeYzy77x0vHLscygX1YGdetJjmaPkmyMziNXZw5r1PoWB1MJpcsfLW1p9w741DBfEYM0vkwt6Cf%2Bb7mBmEMYA9dnJiBTeo7GO2hRX3%2FetNZtu7%2B%2BiryXdrsFs4QAoURZZouIZ2KbcafClFGGuYDjjlNTpih6YGJtAzWin4nShDldQazMAYd19OSSG3HLvmAN6i4%2FWt%2FfJCPBbKXYIwMqUZRMoU7zbmQOMVvNly57PrdFIzyx%2BBRg%2F9Y7OFaTM3sU%2FpwYtysjEO%2FeETzOtFQrk%2BrzLThIsekcekh2EkhMGZoTBYAKn6pUn%2B03EBAryjqYH3qznW7EQA%2FNeo1Sh%2BOxHsUFe7lFikjgIH%2BybCzG4a4fZFjzBHyVb1oLZScv9gl%2FayWL0HwGVrTRqqMJWfypxEPMhjHk2M5A0M%2BPI3Kgf8C3fvIypPPOAlKrgT54J66TgSPSut6PtkqXCCkgLgoAznUcTvBuOzFvreRHwgygRTMA%2FFZnmDHMJGezM8GOqUBuRNEm8Mkv5qMb6PqWbiOm4oQYZrbeviHF0WSZw7%2B89TsWWQXcBa33PuiBZQ635Y%2BUhBggDdoJoSt2wHnAIgF%2F9GYhvmRmNSJZ4%2FNXo%2Biu1ArMq%2FAv0o6R7QjKJQrRSTeoK8WH81BUmTUjUhKIE9CVlwUORyMlEXtVYCibJGCdS8zHI%2BI8tRZvDXXAtsaiXFRW33H5SzFtey0ibMIfLzlb9Cty4qm&X-Amz-Signature=2a966ede1fdb5e77f1633d8a0d737a7e828b935fe03e8efb64cf7b3aab6c92a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

