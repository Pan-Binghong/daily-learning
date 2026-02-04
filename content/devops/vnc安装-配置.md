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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3WHRZN6%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDqovztAqe%2BcrU0ddx5UV1knXKFtVPqgtIWIOkTxtsZeQIgJ67Ohl7OiAxdoWo9OAKdLzPygU8uYrz1japSEgs2DA0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPMyFEVvtU3QDv0VaircA5zxz5BCtRuaMaZREHOv5ha58NtUXN3XazTXj1FMJi1ksQX7ESMRPz9EOZNTEFug%2BIEa78n%2Fu8mEgVKtRMb9S3I%2FTPnuCu4u%2Bn9p1l83KihN%2BJcHTozyPFoEyJBeZlZhutaBihz%2BguXYjVhLOBUVVcnDkIIVsaF6Dsq0x8UX9xDXYW2VS5TifeN2qorDe1HTtxpRUrO5A8pz3Ka4xS8MZQjNgwRm8HS5yVIcvq6Y4WDygSgIu84o%2Bcu2bLLMGa2ap1OBKPTQu9409CbFsXyrei2Mx88O47hRWwQ517sxoGQM0Wd5cZl09Bpb00N4ihgb8kK8bl2Ks2dfOxms6TRX5kIPpdrvIdvZLihbBHQYOfrBdal6QlnGtvjH6QZ%2BYPnkDZqjgNj7CPS92EC2P3TOUJ31tRmsKLOO5tCDN%2BlFANBgUCPlLQtAQIYo2R1UBhHhftD487hDXhQ0rETa5qdx8AcHr12ZzXYoBnICaND1VYEtKRjvIQHwxAehzEuIjhXgib8jb%2BI5AknPKOFp3RpAfyy4zvriK2lf%2FC96p3nDKpyejrQSImoI%2B8NFnrGZT5pEYw72IomHVA%2Br2biIknLgmk8RhD71pkOcgKDlklU9AFMD2IDvXAa6sFH0aL2vMN7oiswGOqUB87g8ukg8mH8MNyBqhRiNp%2B4WlxxgGIwFN9jEO4lDw5nLhDF6FhZ2cZv5lP31d3MUJA%2FEgXY2QddUVeHYslx7w1QXocvm7DvBqDfXkIfqJS2cOhcz2SRTFAnLVq%2Fsxt4X0kXcOwxvxWHUB%2ByEHP4CJ95415PxXOAaV5x4SLUu53Zc3KihGttooofpxCgnXE%2Bnlh%2F3oNltFotJXZVc4AznQMTDgUss&X-Amz-Signature=ca42484fab186e841387a24e9ffdcb3581a6028cbe1c2c0e3c4c99ee93d6017c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3WHRZN6%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDqovztAqe%2BcrU0ddx5UV1knXKFtVPqgtIWIOkTxtsZeQIgJ67Ohl7OiAxdoWo9OAKdLzPygU8uYrz1japSEgs2DA0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPMyFEVvtU3QDv0VaircA5zxz5BCtRuaMaZREHOv5ha58NtUXN3XazTXj1FMJi1ksQX7ESMRPz9EOZNTEFug%2BIEa78n%2Fu8mEgVKtRMb9S3I%2FTPnuCu4u%2Bn9p1l83KihN%2BJcHTozyPFoEyJBeZlZhutaBihz%2BguXYjVhLOBUVVcnDkIIVsaF6Dsq0x8UX9xDXYW2VS5TifeN2qorDe1HTtxpRUrO5A8pz3Ka4xS8MZQjNgwRm8HS5yVIcvq6Y4WDygSgIu84o%2Bcu2bLLMGa2ap1OBKPTQu9409CbFsXyrei2Mx88O47hRWwQ517sxoGQM0Wd5cZl09Bpb00N4ihgb8kK8bl2Ks2dfOxms6TRX5kIPpdrvIdvZLihbBHQYOfrBdal6QlnGtvjH6QZ%2BYPnkDZqjgNj7CPS92EC2P3TOUJ31tRmsKLOO5tCDN%2BlFANBgUCPlLQtAQIYo2R1UBhHhftD487hDXhQ0rETa5qdx8AcHr12ZzXYoBnICaND1VYEtKRjvIQHwxAehzEuIjhXgib8jb%2BI5AknPKOFp3RpAfyy4zvriK2lf%2FC96p3nDKpyejrQSImoI%2B8NFnrGZT5pEYw72IomHVA%2Br2biIknLgmk8RhD71pkOcgKDlklU9AFMD2IDvXAa6sFH0aL2vMN7oiswGOqUB87g8ukg8mH8MNyBqhRiNp%2B4WlxxgGIwFN9jEO4lDw5nLhDF6FhZ2cZv5lP31d3MUJA%2FEgXY2QddUVeHYslx7w1QXocvm7DvBqDfXkIfqJS2cOhcz2SRTFAnLVq%2Fsxt4X0kXcOwxvxWHUB%2ByEHP4CJ95415PxXOAaV5x4SLUu53Zc3KihGttooofpxCgnXE%2Bnlh%2F3oNltFotJXZVc4AznQMTDgUss&X-Amz-Signature=516b6c9a42eb71e00c9963178649749c7921965ba6a2480d28c14392bed5625c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

