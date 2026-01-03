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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWRNDMSK%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCiarVKHVq8Mfa4EVpjob6ZFqOedHyWS681FmBUN2Ir6AIgTjKB%2BdAcQbQFwnUTGGyB2R4UvRqf2g6tj2t7hmE16Mkq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDHZjevU2jN76TNLNiCrcA2085g9JNDYVG2fWyNr2npPngB2iPj3T1bMZJkH8LfVksIElMsaBORlNi%2BNAYgphATcEYU3jaalyAwd1eLk5jg1Fzy%2BlXr%2B47RZNhbOpkRfBLiltym2KnoLiTSRDj5xWAlAOaMAfsvb%2FPqSczQYKz08CZwnRkqePGzJPTf%2BkjW2JXaFKAAEl1ucfRntxzdv8pLOELf6chqFgPTk2AeFP%2FeKUbxwzk2SNkd95sx3nuhhAjHVyVG%2BQ3iSIUpm8OVqpMlV7tcJYQ3xpxljapGJC2qO237V8KMLQ9I45o40JdtAx7m%2Flziv2UUvdZ4Ggwv%2BQt7S5aRo9T%2BbC3MCJ9%2FfX%2B59wRxcKwE3DgWfm9CiOJvOigHlvx%2B%2FLigcARZ9t9U0boaZbQav1vN3gNFxdGXHGXL52XelRsAU9ztEYQVJCHgc18VxUoHXhnTH%2BbDYcAsw4XF819anfWgepRRcUrxe1Kqtv9FwDUHDJI%2BGnhY3OKkV%2FntIa0sC8Stlwv93%2Fyu1v2Gn6szZAJE4%2FJzPTWvymsFQqKXGyKZSZCkTxv%2BbXMS%2FcT0SAtxMhBOALVBiUiQ0uHXFyzJ0hRPFyIuOZ1PHKh5Rwx6uWSlQGeCG6EQVxxF7LBn2lABEhh4V5YOa8MK3q4coGOqUBss0mme3u2jEzxoJ3SeqLS5Wx%2BlRLt1IPBSdAOtaroiVhscfwfa5u3mfE3%2B9x%2B1QWdEOmSC4xQtNKaJlykHtOHJTeFWnb%2BZ%2BTPjW23CZs1zKtbZMdg%2BeeQ2bnA9tXA05Z%2F2dgKG5bTn8tF%2Bn%2F9BFSzw5e4qiMfBUTXtmlwcmBs513vh7TaDlM6UJWq0uvTiNS9BYOEY2Fa4nnwQb7CnEgvf8MPxIO&X-Amz-Signature=812dcfcbae3c244814547d4ecb8538e85d03bfc7677dad4ac87083d08008acf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWRNDMSK%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCiarVKHVq8Mfa4EVpjob6ZFqOedHyWS681FmBUN2Ir6AIgTjKB%2BdAcQbQFwnUTGGyB2R4UvRqf2g6tj2t7hmE16Mkq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDHZjevU2jN76TNLNiCrcA2085g9JNDYVG2fWyNr2npPngB2iPj3T1bMZJkH8LfVksIElMsaBORlNi%2BNAYgphATcEYU3jaalyAwd1eLk5jg1Fzy%2BlXr%2B47RZNhbOpkRfBLiltym2KnoLiTSRDj5xWAlAOaMAfsvb%2FPqSczQYKz08CZwnRkqePGzJPTf%2BkjW2JXaFKAAEl1ucfRntxzdv8pLOELf6chqFgPTk2AeFP%2FeKUbxwzk2SNkd95sx3nuhhAjHVyVG%2BQ3iSIUpm8OVqpMlV7tcJYQ3xpxljapGJC2qO237V8KMLQ9I45o40JdtAx7m%2Flziv2UUvdZ4Ggwv%2BQt7S5aRo9T%2BbC3MCJ9%2FfX%2B59wRxcKwE3DgWfm9CiOJvOigHlvx%2B%2FLigcARZ9t9U0boaZbQav1vN3gNFxdGXHGXL52XelRsAU9ztEYQVJCHgc18VxUoHXhnTH%2BbDYcAsw4XF819anfWgepRRcUrxe1Kqtv9FwDUHDJI%2BGnhY3OKkV%2FntIa0sC8Stlwv93%2Fyu1v2Gn6szZAJE4%2FJzPTWvymsFQqKXGyKZSZCkTxv%2BbXMS%2FcT0SAtxMhBOALVBiUiQ0uHXFyzJ0hRPFyIuOZ1PHKh5Rwx6uWSlQGeCG6EQVxxF7LBn2lABEhh4V5YOa8MK3q4coGOqUBss0mme3u2jEzxoJ3SeqLS5Wx%2BlRLt1IPBSdAOtaroiVhscfwfa5u3mfE3%2B9x%2B1QWdEOmSC4xQtNKaJlykHtOHJTeFWnb%2BZ%2BTPjW23CZs1zKtbZMdg%2BeeQ2bnA9tXA05Z%2F2dgKG5bTn8tF%2Bn%2F9BFSzw5e4qiMfBUTXtmlwcmBs513vh7TaDlM6UJWq0uvTiNS9BYOEY2Fa4nnwQb7CnEgvf8MPxIO&X-Amz-Signature=3ee3da397281624607e0f22922f1a0e942156786b2d6d4c8c56770509a5220c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

