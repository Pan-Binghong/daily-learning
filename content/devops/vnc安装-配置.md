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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHHP2UCV%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIHMqNE221hpUMShYhd5OgcP8jgPfvjWgZzs87vPfySndAiBya5WUP8OeVIxu%2BBw5IQvSs6cViBzt71rQqsgK8deNSyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsTIDnlANI%2B240ayYKtwDtmfeuDqqHGRC9Fd3zjcSbIcWNeciF12SbSs%2BIdUeVcHZzfluI4aUIGf2AIaLhmqvFPO1AC5w3DrPS9XnOuPJ2VhaefWlC8vNw2LyjF3zyCej6WZMJOtSuKoJmifFhPGcjBVgh9HQFmo5Tu8AQive8gexinaTO%2FGckAGejXtuMb3sX1ND6FHpSg6rK6DpRhoNNoimV0zgrGk7Zjq0f%2FqQdGuvTMZgSrzOiDaFS8CfvdWUcTiv0VScPJwGh4h1rvKbiyQyro%2FywRqfEJ%2Bx9ugtXDwFN6ACPOOBv2XtdNPJmqRj2YgLBJiU7g5maqFZq5YtywDuCZvgeaDJYVQxtLPA98eJ3%2FTNeKRPqSl078GIDKqRl0ElRKUw5mNTMfBVFdTyJDACL6Kk5dtIpthExVZ9%2FRJir1Z1yVC1NhKNXkn0YMiJ3uxrJ2HvDPYzXfUIYTglJDcUJct3N%2Bl4K%2FiN4YGyMGWtncVWtiKEzj1qpnHVnClmd%2F7Bw4Jwv3ZF32KrRfiNjJTBCFhuU2t%2B5H9vx04BiFULSdpPSgSPBuGcdsSCK5SDryn0XVb7%2FvD%2BsIGJwD%2FQONSJ%2BQ443YsNAoW6qkiB9ZmotM7XItnre9lK8nlIRtof7exijlz3AhsoF1Aw7qbozQY6pgGcCbxyzWa%2B3AtS66gEV22Ur9yIKFywRZ93JXntUHfE4QATjksXWbKB4IoPIi1jnwZAh4AZNRt6epob3V%2FrWU4oas8SXw60MM8NmudMrpEjqOqJAsd6jRa3BpIsjacjySg264tjwnypj2rdSP71G8ffF%2BhIu1P1wEqLV89DWSTIML1SJjawbIKMrt5NB1AKPBj0xhxGRcdhSGRcAPsup86jGNQgPLNJ&X-Amz-Signature=aed2778408b8e9e5c8b74d422ddf71271e3cf92517cedd493cc65435d6e51b2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHHP2UCV%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIHMqNE221hpUMShYhd5OgcP8jgPfvjWgZzs87vPfySndAiBya5WUP8OeVIxu%2BBw5IQvSs6cViBzt71rQqsgK8deNSyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsTIDnlANI%2B240ayYKtwDtmfeuDqqHGRC9Fd3zjcSbIcWNeciF12SbSs%2BIdUeVcHZzfluI4aUIGf2AIaLhmqvFPO1AC5w3DrPS9XnOuPJ2VhaefWlC8vNw2LyjF3zyCej6WZMJOtSuKoJmifFhPGcjBVgh9HQFmo5Tu8AQive8gexinaTO%2FGckAGejXtuMb3sX1ND6FHpSg6rK6DpRhoNNoimV0zgrGk7Zjq0f%2FqQdGuvTMZgSrzOiDaFS8CfvdWUcTiv0VScPJwGh4h1rvKbiyQyro%2FywRqfEJ%2Bx9ugtXDwFN6ACPOOBv2XtdNPJmqRj2YgLBJiU7g5maqFZq5YtywDuCZvgeaDJYVQxtLPA98eJ3%2FTNeKRPqSl078GIDKqRl0ElRKUw5mNTMfBVFdTyJDACL6Kk5dtIpthExVZ9%2FRJir1Z1yVC1NhKNXkn0YMiJ3uxrJ2HvDPYzXfUIYTglJDcUJct3N%2Bl4K%2FiN4YGyMGWtncVWtiKEzj1qpnHVnClmd%2F7Bw4Jwv3ZF32KrRfiNjJTBCFhuU2t%2B5H9vx04BiFULSdpPSgSPBuGcdsSCK5SDryn0XVb7%2FvD%2BsIGJwD%2FQONSJ%2BQ443YsNAoW6qkiB9ZmotM7XItnre9lK8nlIRtof7exijlz3AhsoF1Aw7qbozQY6pgGcCbxyzWa%2B3AtS66gEV22Ur9yIKFywRZ93JXntUHfE4QATjksXWbKB4IoPIi1jnwZAh4AZNRt6epob3V%2FrWU4oas8SXw60MM8NmudMrpEjqOqJAsd6jRa3BpIsjacjySg264tjwnypj2rdSP71G8ffF%2BhIu1P1wEqLV89DWSTIML1SJjawbIKMrt5NB1AKPBj0xhxGRcdhSGRcAPsup86jGNQgPLNJ&X-Amz-Signature=5d10dba6c47f0ab508c52651b6a2a8657e94e35b41e54a9ff81a818e0ae59169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

