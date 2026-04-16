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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAIM6IBT%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrWapKbUSLHGs%2FWq%2FWBpwpAuDbkW%2BeraMrgqq5aSv%2FqAiAMNZNj1fpuMogbvyX2YAysL6tfgbeZULnIrHxUW9wuVCqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh3ysLoGtzbxgg6DJKtwD%2FILO0jfmE4%2BqlET0p4zEBkVkywgQAbbpxkybnbUE4m%2FjFBRAu7LHoZW8BApjZvEetKb3xIsn79zw%2F0pD%2BrTUSf3dA9BXsCdip2f3FW7dQ5AsUX5X7pJjBCFaudAS1BX8%2FoYjj1%2FvuiackZe7HRZ1hjIT%2BHmJQDCb%2BLAN179MwHZykuEZ9x%2B%2FuiI8aVDLHxJdS5P7OPyrjBIexbLAgVQiG2QRKTs3RZ5mvb7BMZBqPrMY88chXJZKlFdjuXmh14fXQMdhZ5B5mBxEOwJQSK1WWkqN%2B8aa48CWE9yl9%2FmeRKadMXBJyK2OldWPeuoLcMt6TGgpTBLRS9KXQEii%2BWRpj%2FJeGx7dkjxJl%2B8u9XVnKv7b0MogTjz1jIYMzj8FXuXeuZeDhYTQso3TbbE2ZfPgjceukzCNtwsYLAxr97i%2F2rEMeO73URoHbK%2BJF8QekiRYAPugSsLxBgGSnlLWCvBUGZUlK%2BvOjpHQmERkMig2t%2BNjKMCaoxNlJiBSjipMd4YmqQM1x0TCeaJCoifaYYeb%2FfZ0jG0VVCluugqZHty%2F9%2FasFTwNq9Gp9uTSrxnU6x2cvolJgB2pxHjfWu5kqp04D%2Fny3t5pCfyl4KVFolbzYmL4HDunGbCoBpY7Akgw6MSBzwY6pgGWbHPenM0eW2OaD1gSKsmInsSVrieSH70%2BZHxBmBigX3KDiv6FpqThnmmkOy6HuejHgFL%2FrLPL75BmLt4AlTEaIULnsnd6iVGuXF3SzAJTxORgy02tE%2B5GJGX%2BkjxDFIrF0wrS3ovdC9sYV9ChWQP8t76C50SLKFysK%2BnzlQ7wkyi9iYomu2fwaeM%2FO20qcBEYQnpusH03pqn88WBkgSL3MuaOhVlO&X-Amz-Signature=d2b69e6dd9978c149bb21546c45552107b99d147b4c0e4fd1ed26b1a7f075062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAIM6IBT%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrWapKbUSLHGs%2FWq%2FWBpwpAuDbkW%2BeraMrgqq5aSv%2FqAiAMNZNj1fpuMogbvyX2YAysL6tfgbeZULnIrHxUW9wuVCqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMh3ysLoGtzbxgg6DJKtwD%2FILO0jfmE4%2BqlET0p4zEBkVkywgQAbbpxkybnbUE4m%2FjFBRAu7LHoZW8BApjZvEetKb3xIsn79zw%2F0pD%2BrTUSf3dA9BXsCdip2f3FW7dQ5AsUX5X7pJjBCFaudAS1BX8%2FoYjj1%2FvuiackZe7HRZ1hjIT%2BHmJQDCb%2BLAN179MwHZykuEZ9x%2B%2FuiI8aVDLHxJdS5P7OPyrjBIexbLAgVQiG2QRKTs3RZ5mvb7BMZBqPrMY88chXJZKlFdjuXmh14fXQMdhZ5B5mBxEOwJQSK1WWkqN%2B8aa48CWE9yl9%2FmeRKadMXBJyK2OldWPeuoLcMt6TGgpTBLRS9KXQEii%2BWRpj%2FJeGx7dkjxJl%2B8u9XVnKv7b0MogTjz1jIYMzj8FXuXeuZeDhYTQso3TbbE2ZfPgjceukzCNtwsYLAxr97i%2F2rEMeO73URoHbK%2BJF8QekiRYAPugSsLxBgGSnlLWCvBUGZUlK%2BvOjpHQmERkMig2t%2BNjKMCaoxNlJiBSjipMd4YmqQM1x0TCeaJCoifaYYeb%2FfZ0jG0VVCluugqZHty%2F9%2FasFTwNq9Gp9uTSrxnU6x2cvolJgB2pxHjfWu5kqp04D%2Fny3t5pCfyl4KVFolbzYmL4HDunGbCoBpY7Akgw6MSBzwY6pgGWbHPenM0eW2OaD1gSKsmInsSVrieSH70%2BZHxBmBigX3KDiv6FpqThnmmkOy6HuejHgFL%2FrLPL75BmLt4AlTEaIULnsnd6iVGuXF3SzAJTxORgy02tE%2B5GJGX%2BkjxDFIrF0wrS3ovdC9sYV9ChWQP8t76C50SLKFysK%2BnzlQ7wkyi9iYomu2fwaeM%2FO20qcBEYQnpusH03pqn88WBkgSL3MuaOhVlO&X-Amz-Signature=82c1d29c04cdfa601850ff17536d15013f0030d74394b9c3905caeabd464c6dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

