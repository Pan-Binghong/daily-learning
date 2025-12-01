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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XXDWCUX%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQC4Ah4YJVG5DixYXhLkDzInibDD1avdRK6hdM4oIiMJnAIgS3zOz4t%2BNpQLQZbubSIt8LjMu53yNOxo1ObSYtrJL18qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyvXaJMNwhNRIUiRCrcA0bc6X9U8dwiOdOOgduleigHjGq9SN7skovRlWeTxXjpJIzfKJQPMUOL9dNJLxhhKN2zH59x8gcLkiq8QHqMvmaxNJj9ZqXFGq9f8JdIh0D%2FzuroLIv%2FhocRwqKtk6hbP42kYQ5Ac9j%2BBv2ZrOykW74pDWHWZ04zdLzTZYo2K1bhwVajhVBgjexGVMWi%2BaV%2B58NKF0i7ttXtxcWc7lxy%2B0ij82YCD%2FDdqGvYYDLpPx0U19MuCzHo4Cx%2FhRdYe9C4VffWNjUUoRbCkSVT8nCpRyNoyqaUtcvz4%2B1uhXm6OyC4KyIujMeyOENIlTWg7f1ykH36vHd%2BmkkTDPxcx96x%2BTmgw%2BHLDEF0%2FVUsdb5iFZsbCE7HHyznSdoouAzJGTG7uST8%2BNcj61gFr1HOT2iMcz47kRFv7I9HiPml4trTzmLswMW%2BrJzwYYUM0eSmEso6HDbpERIzmr1EJ02bWyQzM6lwoHAevGTdri4hxR%2BJI0hTGf15lHew0tyeKCcxmBSF3Hwh0aiD%2FjoLDQxfVPJ7WEWo8367jHYhhg6X%2Bqg%2B4%2BtLkmV0N7QdMkg%2FNeCtoq3QFX4BXjQL%2BjXev34Bocxb12%2BwBHK8PV78e3soVBpVpyYLev4SlKVNdAGE2L%2BEML73sskGOqUBebBSDrhRvztf3BI5AqSeASxUoiJ1QgWsk8%2BIGMzXYy7OQukObXl6JLEl21e7uacgyFLwvEiIJsUn0r4HwaTKuasiG8zvrZC29yCJVCoKe%2F7QsIq4FnJZOekbmV8GqyKwBFVh7UjjJpy0VEqQvQKsBbcav4UGRwadxFqPrCfU3lRFsGG5sSUaFNM0nR7ta8lHYfusdfHuL%2BVhhun1vaqcXwGrpF9b&X-Amz-Signature=d84c47237206284adc1d9978c13b1c40abe017b096abd12c0c488d7a09780bed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XXDWCUX%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQC4Ah4YJVG5DixYXhLkDzInibDD1avdRK6hdM4oIiMJnAIgS3zOz4t%2BNpQLQZbubSIt8LjMu53yNOxo1ObSYtrJL18qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyvXaJMNwhNRIUiRCrcA0bc6X9U8dwiOdOOgduleigHjGq9SN7skovRlWeTxXjpJIzfKJQPMUOL9dNJLxhhKN2zH59x8gcLkiq8QHqMvmaxNJj9ZqXFGq9f8JdIh0D%2FzuroLIv%2FhocRwqKtk6hbP42kYQ5Ac9j%2BBv2ZrOykW74pDWHWZ04zdLzTZYo2K1bhwVajhVBgjexGVMWi%2BaV%2B58NKF0i7ttXtxcWc7lxy%2B0ij82YCD%2FDdqGvYYDLpPx0U19MuCzHo4Cx%2FhRdYe9C4VffWNjUUoRbCkSVT8nCpRyNoyqaUtcvz4%2B1uhXm6OyC4KyIujMeyOENIlTWg7f1ykH36vHd%2BmkkTDPxcx96x%2BTmgw%2BHLDEF0%2FVUsdb5iFZsbCE7HHyznSdoouAzJGTG7uST8%2BNcj61gFr1HOT2iMcz47kRFv7I9HiPml4trTzmLswMW%2BrJzwYYUM0eSmEso6HDbpERIzmr1EJ02bWyQzM6lwoHAevGTdri4hxR%2BJI0hTGf15lHew0tyeKCcxmBSF3Hwh0aiD%2FjoLDQxfVPJ7WEWo8367jHYhhg6X%2Bqg%2B4%2BtLkmV0N7QdMkg%2FNeCtoq3QFX4BXjQL%2BjXev34Bocxb12%2BwBHK8PV78e3soVBpVpyYLev4SlKVNdAGE2L%2BEML73sskGOqUBebBSDrhRvztf3BI5AqSeASxUoiJ1QgWsk8%2BIGMzXYy7OQukObXl6JLEl21e7uacgyFLwvEiIJsUn0r4HwaTKuasiG8zvrZC29yCJVCoKe%2F7QsIq4FnJZOekbmV8GqyKwBFVh7UjjJpy0VEqQvQKsBbcav4UGRwadxFqPrCfU3lRFsGG5sSUaFNM0nR7ta8lHYfusdfHuL%2BVhhun1vaqcXwGrpF9b&X-Amz-Signature=89e6237e74ce16009196be8dd2ed3c3220d6056473616e02d787b61efa3e2538&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

