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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZWB2HLU%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHnM%2F53tXpSHqR2r6CEbHCXEnN965qEHb8Xz%2BmpeZc4gIhAKplJfmzbGZqc61rAHakXhYlxjwzwBGAaTTp2ZTipKQJKv8DCHQQABoMNjM3NDIzMTgzODA1IgwF52psKyCIMO6on5Yq3AOhwLp50H02%2B4vwKREiiEPSvEJrjg85pMIhxVLLiTLD%2BtsRDo2p61VBUH4LPI0DmIYab8%2FabQaSEGU6URtN34%2FS7fik2gckk%2Fa6ZlLMu35UfxHSLjAKTbAgIYis%2BfIizUNt4VG7OJJn9IhDNkZOPx9mcjFxc2gKLxkiU%2F67JhCeFcMfPVw7NMQZ3xWXonNXpj%2BRrw8lNyNNtZ9sQYoJty9Lvd2cIr0IQQEF%2Bb2dJm9UczRdYBWyGD7QeFs9XTRt0AbHZByRxLlIX4eMFM0NgQcWhl6hNsAJrBWz9gVzJJGsOc2eeQaCZDknolUI5WqBMbBcBrGlAfhRV0chC3fU3NG88DlgbTQW%2B6PSXJI3E9lC2eLVxszwmX3h4LMCBmZnfG6VgSQWRL3AZCLD6hHYwigLha81gRyKfzbb6q%2FiDBCfnWcboP3e%2F5Jg%2BRuEQ3UCscc5SXwYV2BML7w3y4PEf6n1XdBsous34eaDhvW%2FfNowgT%2BMEpAhhD9vnLoDYXVK6eJjB1h5GkTDhsCAKB1XyIsPn9XqDAhJrjdoOQ9ln69sYeW5R5cSv1t%2F01WIe8TF%2FISUlv%2BDcwX6g1mcINAjHTbD%2BX4StDEplJFyD0ma3l5QwGgr7%2BwRt%2F9T9ZwqzjDZsojKBjqkAT0s7ur2vcjNbwgO2wycgLnyFp5ZdxY6oxtDQx%2F48y1FN5fc6LNp13ECRg7O9VCd7ZEq%2BQstJPr1HpROLGiMPewwUkkdmk3jDcM674oCXpc6sisPR1kUfEQOIFEwaqFu32GK0I18PAHHFmDqUmBrljp5NeQKNM64nwfokFN8Pk1zJhGgZj1GAyf8HvlIHRNqIuq%2BbVZVArdx6QVb57UQc%2BYVgQds&X-Amz-Signature=92c64250d8c5d7e874daa2a2a36d48351034579dc47e8acdd2db0d75725b54a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZWB2HLU%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHnM%2F53tXpSHqR2r6CEbHCXEnN965qEHb8Xz%2BmpeZc4gIhAKplJfmzbGZqc61rAHakXhYlxjwzwBGAaTTp2ZTipKQJKv8DCHQQABoMNjM3NDIzMTgzODA1IgwF52psKyCIMO6on5Yq3AOhwLp50H02%2B4vwKREiiEPSvEJrjg85pMIhxVLLiTLD%2BtsRDo2p61VBUH4LPI0DmIYab8%2FabQaSEGU6URtN34%2FS7fik2gckk%2Fa6ZlLMu35UfxHSLjAKTbAgIYis%2BfIizUNt4VG7OJJn9IhDNkZOPx9mcjFxc2gKLxkiU%2F67JhCeFcMfPVw7NMQZ3xWXonNXpj%2BRrw8lNyNNtZ9sQYoJty9Lvd2cIr0IQQEF%2Bb2dJm9UczRdYBWyGD7QeFs9XTRt0AbHZByRxLlIX4eMFM0NgQcWhl6hNsAJrBWz9gVzJJGsOc2eeQaCZDknolUI5WqBMbBcBrGlAfhRV0chC3fU3NG88DlgbTQW%2B6PSXJI3E9lC2eLVxszwmX3h4LMCBmZnfG6VgSQWRL3AZCLD6hHYwigLha81gRyKfzbb6q%2FiDBCfnWcboP3e%2F5Jg%2BRuEQ3UCscc5SXwYV2BML7w3y4PEf6n1XdBsous34eaDhvW%2FfNowgT%2BMEpAhhD9vnLoDYXVK6eJjB1h5GkTDhsCAKB1XyIsPn9XqDAhJrjdoOQ9ln69sYeW5R5cSv1t%2F01WIe8TF%2FISUlv%2BDcwX6g1mcINAjHTbD%2BX4StDEplJFyD0ma3l5QwGgr7%2BwRt%2F9T9ZwqzjDZsojKBjqkAT0s7ur2vcjNbwgO2wycgLnyFp5ZdxY6oxtDQx%2F48y1FN5fc6LNp13ECRg7O9VCd7ZEq%2BQstJPr1HpROLGiMPewwUkkdmk3jDcM674oCXpc6sisPR1kUfEQOIFEwaqFu32GK0I18PAHHFmDqUmBrljp5NeQKNM64nwfokFN8Pk1zJhGgZj1GAyf8HvlIHRNqIuq%2BbVZVArdx6QVb57UQc%2BYVgQds&X-Amz-Signature=a3c66d51ab086a1d970b7746ee4fd092cf9e2b2e5542059d481a4d8343fb6bca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

