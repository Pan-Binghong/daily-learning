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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466572WOTL2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6RccqQiStBRw0sNgJVHqGhI0u1qfj%2FK%2BfX67Yjfv3QAiBlThW%2F4S384o9bl%2BkHDcTDxEsJUGvauGWln3K7cnv4ISqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4nMpicqnQajzHHAKKtwD0iT6e56csVFzCivD%2FwReNCVsNyHJpzbmoyEL%2Fu7X31J5aYeI0exgChbRnznaR0ApYNIguOunRVw8IGJCh3gkkDvvaHeWRU5e1tSqvHJcCaF2fsZmcw%2BHtnJ8JLCJQCOBSRr5x1Nl4vHm%2BL3xB2LSMNiHdfmf9LoaWfhnOQA0DJhwpSFj04aIl%2Ffz21j8HbmqfoOIG8jJYymA4GSvSvGgcil3bN%2BoizRovekyd2fSPxvbiaiH6iX7HlvWxIFrqjYUZu1aPkXWTkd6RlNbkbMbLLE%2FHyAjF3CSlyRGASQ%2FOqhgFfkNtj90MAiEiteXkjzdOtXHkwIWTF59ZmqhuGGliFDLTQcGTQSR0MK673QaWm2hyebmbxwaLskerMPomv13OnspvhbK0EcHvdlvpLjIngS6qnhLqtX%2FduL8sam52vKbIW5NaHVUvYC6%2FHIg9%2FVzLsvgf7drQtHyX5YBOIjrNSJG%2FqKBhs8UUz6cNNurBAfV9oicGimOqOz1EyS%2B%2FTbW4nX8T9lgm5vpfo1zpOGVMBTW45RT4ONhZUav3PbIVjlxmYqPe9e4vldLLgz1MtCnAWaLeAxqHkwbTzK5oypir8mM2K3W9OA7VDEdIs%2BksmQfpb8CpBj8TKWlAxowrZawyAY6pgHIo5jTIyXy6LX7ITtfselfSgcntl60AqmZf4YnLhLRuKP3fhpDp35ymk1rsdaaKWFxiEubLtOC7NkeQhFZsipbpJon7F6a3r727jAYLJRAaccwW88EWtFx4VZIg051ybzli%2Bqt3wFopgxNehnLnpWnL5PghTgQJH7b9fdBSA2XKnBfyUe%2F8sAgr4jbix2yzkPGxMHzluc%2FdIVnmVOXFWU8F4KmptFQ&X-Amz-Signature=8accb435e09fe7b9e0fde54e86b3cdc0b32d8e34540f9c90b99ea18390e9d617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466572WOTL2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6RccqQiStBRw0sNgJVHqGhI0u1qfj%2FK%2BfX67Yjfv3QAiBlThW%2F4S384o9bl%2BkHDcTDxEsJUGvauGWln3K7cnv4ISqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4nMpicqnQajzHHAKKtwD0iT6e56csVFzCivD%2FwReNCVsNyHJpzbmoyEL%2Fu7X31J5aYeI0exgChbRnznaR0ApYNIguOunRVw8IGJCh3gkkDvvaHeWRU5e1tSqvHJcCaF2fsZmcw%2BHtnJ8JLCJQCOBSRr5x1Nl4vHm%2BL3xB2LSMNiHdfmf9LoaWfhnOQA0DJhwpSFj04aIl%2Ffz21j8HbmqfoOIG8jJYymA4GSvSvGgcil3bN%2BoizRovekyd2fSPxvbiaiH6iX7HlvWxIFrqjYUZu1aPkXWTkd6RlNbkbMbLLE%2FHyAjF3CSlyRGASQ%2FOqhgFfkNtj90MAiEiteXkjzdOtXHkwIWTF59ZmqhuGGliFDLTQcGTQSR0MK673QaWm2hyebmbxwaLskerMPomv13OnspvhbK0EcHvdlvpLjIngS6qnhLqtX%2FduL8sam52vKbIW5NaHVUvYC6%2FHIg9%2FVzLsvgf7drQtHyX5YBOIjrNSJG%2FqKBhs8UUz6cNNurBAfV9oicGimOqOz1EyS%2B%2FTbW4nX8T9lgm5vpfo1zpOGVMBTW45RT4ONhZUav3PbIVjlxmYqPe9e4vldLLgz1MtCnAWaLeAxqHkwbTzK5oypir8mM2K3W9OA7VDEdIs%2BksmQfpb8CpBj8TKWlAxowrZawyAY6pgHIo5jTIyXy6LX7ITtfselfSgcntl60AqmZf4YnLhLRuKP3fhpDp35ymk1rsdaaKWFxiEubLtOC7NkeQhFZsipbpJon7F6a3r727jAYLJRAaccwW88EWtFx4VZIg051ybzli%2Bqt3wFopgxNehnLnpWnL5PghTgQJH7b9fdBSA2XKnBfyUe%2F8sAgr4jbix2yzkPGxMHzluc%2FdIVnmVOXFWU8F4KmptFQ&X-Amz-Signature=de0bce9012268bdc57a5062412ad55b51356eeaea8043f2e7b7a795fc9da1b33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

