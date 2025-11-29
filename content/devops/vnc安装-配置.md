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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UCC4ONJ%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF7SGDQCMk7Kbg7iArReBslZRo9kj%2FB0pHWPLb%2ByZbG2AiBiLGfvfrSKQw4bmw5uTCh%2Fgphw9KQM%2Bsm9q%2FhjRy%2B3cSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM24D4frM%2F1HrCThuGKtwDalEVaLtBzy5sKp3yOonjjk5F%2Bz5gWd%2F%2BFw%2BRbnHFSMcIPC%2FEBGl4KH1rpUi%2BECACYXDGbt8HH9ZRANJOLZtHpKfa%2FnfeXZnv%2BN%2Fx09klq%2B0Dw3yn68DEF8pOVeA8WB2md46gO5y5sl%2BKePo2bV4s6Bk6M9iDWykaNAe544XKC6OFYppYTwBCLVLT6MuHVrmBS8h1BC%2Be7DgCTSuwH6P3O7N5UBQpbgwJqvnxBN2xTxC4uHXJoOMd0oZwNoz4PV%2FUU8MBjA%2FuWVfHuuGc6Vz50XG5bcoc6vlC7qpQ9ArUtRpOdKV5RPVHx4l6hD8IsRN%2BQ6kb7xcUapV6JX2%2BntxGBCxl3WbKNUWg6HNLvL09xm0RVIVSvRbhvAkUzuAW%2F01Cq%2F7b%2F9vHxKR%2BAm5SrmGA%2F6ldmLLLxDLnkWiBFtXrny7jTonFa%2B8OOt9CGeMgsqMJOfXiSENtQnM0xhNRgtbF9r7X6EeK%2F31A1%2FHC57AKxIY2VtsidP7qyNGDah%2FNbXBwh2hSZBUopM3qlgomci%2F1ozah3fuXY7ao%2BSEDOw5cpDXZ14TH%2F7rrPP%2FSeTTCu67f5gJnnj%2B6fmxCZGi61cSXGiLBBLQuUo9P9N7LZi1dhMjQds%2F4nAFe4zCr6C0wiJ2pyQY6pgEirANtFYy3cgh4i1PciUnNlINbJAsn%2FxaxqFdzvQvYkk3tbJCiaPcywvB16XqKjVQkZbr8NN2VyF%2BzXhxoPZlTdrZEfOTBewWZUyQVmBfmWDfy25fD5AfXsFUhOuRBhbt%2BZDZDE7W%2BhKl2%2F7u0KxPlcyzw1oiPLtFR2G4HNsR2h0sO%2FLrwGC0jgwjOUsfcJR5m%2BzXk0jkn%2FlTtvkmwu7ARTusbOpqa&X-Amz-Signature=561abba4d65414a7051ff0a85529f2524c104609d1c450b497a5a4a9d97846c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UCC4ONJ%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF7SGDQCMk7Kbg7iArReBslZRo9kj%2FB0pHWPLb%2ByZbG2AiBiLGfvfrSKQw4bmw5uTCh%2Fgphw9KQM%2Bsm9q%2FhjRy%2B3cSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM24D4frM%2F1HrCThuGKtwDalEVaLtBzy5sKp3yOonjjk5F%2Bz5gWd%2F%2BFw%2BRbnHFSMcIPC%2FEBGl4KH1rpUi%2BECACYXDGbt8HH9ZRANJOLZtHpKfa%2FnfeXZnv%2BN%2Fx09klq%2B0Dw3yn68DEF8pOVeA8WB2md46gO5y5sl%2BKePo2bV4s6Bk6M9iDWykaNAe544XKC6OFYppYTwBCLVLT6MuHVrmBS8h1BC%2Be7DgCTSuwH6P3O7N5UBQpbgwJqvnxBN2xTxC4uHXJoOMd0oZwNoz4PV%2FUU8MBjA%2FuWVfHuuGc6Vz50XG5bcoc6vlC7qpQ9ArUtRpOdKV5RPVHx4l6hD8IsRN%2BQ6kb7xcUapV6JX2%2BntxGBCxl3WbKNUWg6HNLvL09xm0RVIVSvRbhvAkUzuAW%2F01Cq%2F7b%2F9vHxKR%2BAm5SrmGA%2F6ldmLLLxDLnkWiBFtXrny7jTonFa%2B8OOt9CGeMgsqMJOfXiSENtQnM0xhNRgtbF9r7X6EeK%2F31A1%2FHC57AKxIY2VtsidP7qyNGDah%2FNbXBwh2hSZBUopM3qlgomci%2F1ozah3fuXY7ao%2BSEDOw5cpDXZ14TH%2F7rrPP%2FSeTTCu67f5gJnnj%2B6fmxCZGi61cSXGiLBBLQuUo9P9N7LZi1dhMjQds%2F4nAFe4zCr6C0wiJ2pyQY6pgEirANtFYy3cgh4i1PciUnNlINbJAsn%2FxaxqFdzvQvYkk3tbJCiaPcywvB16XqKjVQkZbr8NN2VyF%2BzXhxoPZlTdrZEfOTBewWZUyQVmBfmWDfy25fD5AfXsFUhOuRBhbt%2BZDZDE7W%2BhKl2%2F7u0KxPlcyzw1oiPLtFR2G4HNsR2h0sO%2FLrwGC0jgwjOUsfcJR5m%2BzXk0jkn%2FlTtvkmwu7ARTusbOpqa&X-Amz-Signature=52977659262e494fa2933c69eb594d0d0460afd453c37aa416727cd00df9ef02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

