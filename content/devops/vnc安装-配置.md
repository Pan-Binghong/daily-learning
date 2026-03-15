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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQXYJFEZ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDusZHlmFlRfqNjjkq0zOoiXQaFH4McJ4ax16BoNSlbTAiEAlA6g8boC7d6%2BsfvlfbfS4vh9OMlPl1z%2FHVtNaYkanbcqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrjB%2FhUE1bqiVwsZircAwYD0RYl14N0ANdIKISxLia%2BzVvAR9QryU4SsmTDObY5w86Rzr6asKOotSr0IYAcWf41h4KEhG4rf1T%2BaWzB8PRuTV4%2BrFGtFfymeUdMuvDUxnFMHZNWlkSVXPHqgjeWSocOXum9it6mkS%2B3%2BaV5j84BDM9JyrEK3gsLEBItM%2FcHT5yWEKnZ8uXvG1gQrxa6t4vHgIk6NfFrjgGj5D1O799bSz4bBGw1sWyedXRNHAd3KfqI3Rr%2FeiKgIMg35Q3eql0JcxO19rIms3pfgn37TidLMRA71MihkjsQQHkhed73MbFMNWn4cciAj1N2ry07jl0MYYmc3AvdG%2BAzqmV2eyhuvPWGDgZHoaCqIOeVJj17NavRInJQ8Bf6ur%2FtZuLCul4DqvA6Se3NWnwLzCzSrkJf7xLKAQ01XzVaeOn5tzt5ywgrldO%2FLp9gtj%2BB1u1k6VFKyxlNnpys%2FErnIIF4ryEkX1B1dKfvp6xmeJakgNyCd3MhbzvioBHrrqRcgBnR%2FuqHPtcVHErLiKgZ5QqyD%2BqUuUmPJzQjSRgiY1jJbMFT5xROtzytathmt7znkYbkmIvuLR9ENT3QuaNspNfsWz5EV0D%2F3QiHBAon0JwzJabmqVD6Qbvl4VZvDw6HMLSQ2M0GOqUB76KVKOzHSFmmWBcfKbNPqUXZj%2FO2Y1PbCcIjse8f7ZDX5LSZzhOgI8D0yNhVw3jUcJAvy92Ipl%2BGpA1kZC9lnSfk0M0sGOQ3pePGVwthkh%2Bs09T3Ptk9mxjmCCut0pi5k25RdvOrUzKyPke4A0%2FJBeMxq8mp8nw1OXVaq14QVxoTovc79g61RLiV%2FfE9BHbxLQF6inU%2BDr%2FrZDQ%2ByWuu%2F%2FR%2FEptN&X-Amz-Signature=357cdf2fce8aa0adf970bb40b6ec2abba86d157429a9e2b5113524c848551a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQXYJFEZ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDusZHlmFlRfqNjjkq0zOoiXQaFH4McJ4ax16BoNSlbTAiEAlA6g8boC7d6%2BsfvlfbfS4vh9OMlPl1z%2FHVtNaYkanbcqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrjB%2FhUE1bqiVwsZircAwYD0RYl14N0ANdIKISxLia%2BzVvAR9QryU4SsmTDObY5w86Rzr6asKOotSr0IYAcWf41h4KEhG4rf1T%2BaWzB8PRuTV4%2BrFGtFfymeUdMuvDUxnFMHZNWlkSVXPHqgjeWSocOXum9it6mkS%2B3%2BaV5j84BDM9JyrEK3gsLEBItM%2FcHT5yWEKnZ8uXvG1gQrxa6t4vHgIk6NfFrjgGj5D1O799bSz4bBGw1sWyedXRNHAd3KfqI3Rr%2FeiKgIMg35Q3eql0JcxO19rIms3pfgn37TidLMRA71MihkjsQQHkhed73MbFMNWn4cciAj1N2ry07jl0MYYmc3AvdG%2BAzqmV2eyhuvPWGDgZHoaCqIOeVJj17NavRInJQ8Bf6ur%2FtZuLCul4DqvA6Se3NWnwLzCzSrkJf7xLKAQ01XzVaeOn5tzt5ywgrldO%2FLp9gtj%2BB1u1k6VFKyxlNnpys%2FErnIIF4ryEkX1B1dKfvp6xmeJakgNyCd3MhbzvioBHrrqRcgBnR%2FuqHPtcVHErLiKgZ5QqyD%2BqUuUmPJzQjSRgiY1jJbMFT5xROtzytathmt7znkYbkmIvuLR9ENT3QuaNspNfsWz5EV0D%2F3QiHBAon0JwzJabmqVD6Qbvl4VZvDw6HMLSQ2M0GOqUB76KVKOzHSFmmWBcfKbNPqUXZj%2FO2Y1PbCcIjse8f7ZDX5LSZzhOgI8D0yNhVw3jUcJAvy92Ipl%2BGpA1kZC9lnSfk0M0sGOQ3pePGVwthkh%2Bs09T3Ptk9mxjmCCut0pi5k25RdvOrUzKyPke4A0%2FJBeMxq8mp8nw1OXVaq14QVxoTovc79g61RLiV%2FfE9BHbxLQF6inU%2BDr%2FrZDQ%2ByWuu%2F%2FR%2FEptN&X-Amz-Signature=fc69ea85fbf155f05776afdb172bdf37633e3d1e680189877529efa699522bd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

