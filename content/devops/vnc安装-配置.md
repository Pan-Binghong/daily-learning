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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662RWAAOB%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl3GS3CGhP3fZ3jFEBv1otLGRSfXOvgzdK067Cv10%2BHwIgUUviYN44QwkOlTVJS8roAfsC4jOJm14npCiBLpr310YqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJNs28zOrTpiFJdebSrcAxgcqPtYdORoo1ksANhkU%2F16zqY22ZN7q1eBn96huOnaXD5mqDLwBC6zU44%2B%2FYEddpN4Q25k8XrDFlTAGmRkyy1AA5RGLx4p2I0A%2BhBhoKhLtFwSSuaiBOPu7RPXJU4oraJ%2B8JBn71Hcy1IjRbE3tJVTV%2F0te2mZKCI1bMDC78Xo9Nhv7EARWgSVPgIU1rO2naVt3%2BC8ex6G3Or7AVRk1ZIMqms3dByIiGXunOmJvesjzqHOkKNgSUVzXrSEw8xnEfKtHa%2BPAgFtR%2F%2FDW%2FQ3Xzsgp8l6dk4vsWlGXV0K4YlEDuD9qslMP7V9oPHOWognqDDfFgr5Bf2a7G1YJ4Wp4s%2FhuS3RDh1VDiSPNvo4uwcz%2BZPDD659ZU9%2FHUP6HxvFB5xVlt9rxaO9BJaEYM3pzcsco2IOk0X6k1fU4KCwjdp5zs1CMPu1r6JowKDrQNCLDO1G0kv7C%2BseVR%2FNv365%2Bah8DIfMoyKl7G9D%2Bo%2BTe2VcuBBxpT5LwGYjC3rxopWDWF3Ybx38Ob%2FDjIL3yEhxVYR16p9xzwUnHH01HQzAd8b9H7W2eQkDxwvnB5UU0%2F3vGAdEf0UBvNBxYFAN43kK7nxVjWXhLnTMEsEx7ArY%2FCPFgrHgPGgjMvi9rnpnMMjz6cwGOqUB%2Fvz9WuV8EFCAAI4JO4vp5B4jdn%2BqUSzxWFdLY2h2WTp8qGcmwbGlmYPcvs4vwehX87YXjydogRqoF%2BOqknymCVyvIqenW5XN1Rxex1B4WLLcUZfbK2fyjwIV7xO5SSqaqn1xcwz4M5fXnHQJO6NBUub0zLocnFrrMddl%2FTMqSV%2B1DJ4QvmPqRgR2Ru%2B3JR3V2br5vDKnpa0LaqyQ%2FNzLaPwgucwV&X-Amz-Signature=511a939d7c3b2551db582d1528413892f9f3b3803559f4c0da5e868757436e70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662RWAAOB%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCl3GS3CGhP3fZ3jFEBv1otLGRSfXOvgzdK067Cv10%2BHwIgUUviYN44QwkOlTVJS8roAfsC4jOJm14npCiBLpr310YqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJNs28zOrTpiFJdebSrcAxgcqPtYdORoo1ksANhkU%2F16zqY22ZN7q1eBn96huOnaXD5mqDLwBC6zU44%2B%2FYEddpN4Q25k8XrDFlTAGmRkyy1AA5RGLx4p2I0A%2BhBhoKhLtFwSSuaiBOPu7RPXJU4oraJ%2B8JBn71Hcy1IjRbE3tJVTV%2F0te2mZKCI1bMDC78Xo9Nhv7EARWgSVPgIU1rO2naVt3%2BC8ex6G3Or7AVRk1ZIMqms3dByIiGXunOmJvesjzqHOkKNgSUVzXrSEw8xnEfKtHa%2BPAgFtR%2F%2FDW%2FQ3Xzsgp8l6dk4vsWlGXV0K4YlEDuD9qslMP7V9oPHOWognqDDfFgr5Bf2a7G1YJ4Wp4s%2FhuS3RDh1VDiSPNvo4uwcz%2BZPDD659ZU9%2FHUP6HxvFB5xVlt9rxaO9BJaEYM3pzcsco2IOk0X6k1fU4KCwjdp5zs1CMPu1r6JowKDrQNCLDO1G0kv7C%2BseVR%2FNv365%2Bah8DIfMoyKl7G9D%2Bo%2BTe2VcuBBxpT5LwGYjC3rxopWDWF3Ybx38Ob%2FDjIL3yEhxVYR16p9xzwUnHH01HQzAd8b9H7W2eQkDxwvnB5UU0%2F3vGAdEf0UBvNBxYFAN43kK7nxVjWXhLnTMEsEx7ArY%2FCPFgrHgPGgjMvi9rnpnMMjz6cwGOqUB%2Fvz9WuV8EFCAAI4JO4vp5B4jdn%2BqUSzxWFdLY2h2WTp8qGcmwbGlmYPcvs4vwehX87YXjydogRqoF%2BOqknymCVyvIqenW5XN1Rxex1B4WLLcUZfbK2fyjwIV7xO5SSqaqn1xcwz4M5fXnHQJO6NBUub0zLocnFrrMddl%2FTMqSV%2B1DJ4QvmPqRgR2Ru%2B3JR3V2br5vDKnpa0LaqyQ%2FNzLaPwgucwV&X-Amz-Signature=96cb0b06346acc8a2aac3ed48f9657f0268e1d6f5187ab34ef07ed5deb3b438a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

