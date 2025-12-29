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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OQRZMU%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDeJ%2F05aRHjKv%2Be7x2rJZBce2DdrsVC%2FygyEY1ct7FsoAiAR8kBYw9vl2%2FPNMKIzs%2FXZ%2BFf3RFLBZvyfjPm6X%2B18pCqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbBKhAo9cnsaVDmD7KtwDq0ie3t8q5Vyl9j2AOYHvuqdxzHFEi2pzPTCQR7hzJ2zTCve3XendCkPZlaVRUh%2FZfAsyK9wm72ntXiS8bRjUFkZPNkmUTXDjhQhWEOwQDfb2XZ0Sbe8S3LvI7T%2FSjwEF17MrPApDT6Rzr8bescsLrKDFWJDKOl%2FEYRGZH38TWTNK9F6Qq3qmy1nkZUQCXi3Tqb%2FQq0uQ5ckXH%2FrRv3TUdOIxm7nxY8C6wkCVxgKL%2Fx%2BhMEik8chWkRDlC6ctg0PR4BNqpvQmvM5%2FwqRcDbe3%2BqekOrplXq3oME3%2FOP5rEkXSoKHNdHvl9en%2BoBzzcz0yz6Ty4RSjFDKsnSbu9Q3sodPr4J6Oxc3kGTDeC4b%2FKkkma1RdZLKKbRsn89p1BJzVWw3X3KoUaQAUu5xGd0LYW3a9Az1e7qEWVTFtZKEgvfz%2BXfXfQln6Qwh0MmCEBRECJGg%2F6%2BQf8IOBe6T5w3Ra05iN9qVw0XRRCJD%2FsYBlYh4eAr897mKYfKwSGRxYlKUpP33XbntYchJFlIQ4cHtuyb8gP2aoZixgRXQ8IpbZIp0jbj%2By8WB01dNcHd7Wse%2FhJn9tb3%2BG%2B9IVi2hqqXhSVkYno%2FNimHZt40QhoSyFaP5ZPvMN6W2qKjA9BncwtqHHygY6pgEWZ2XXOdE20OonJSPhGOoe5kfiR1JKO3myXSAdypywb4yTEyOhyKcYtMFaYqlfMdgWUsZo9Q9xF5Mp9dvBZmov%2FbS%2F11p72g98SCTwzu6ux2A9PiFr0yJf2EZhNkT%2B6onrR%2FKeGHA0P2f%2B%2FSbrnaVh6ClgUMzrIGi9JjFA0MnMqNdoVsg3yCaq%2FzPf%2BfhZ9ONDkJdHlfS1b4YJbtjyQ5RJbk08swcb&X-Amz-Signature=5b386ee99f0c8567c945f7023753af6399985bacd36a29d0b54cf7d8ece879dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656OQRZMU%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDeJ%2F05aRHjKv%2Be7x2rJZBce2DdrsVC%2FygyEY1ct7FsoAiAR8kBYw9vl2%2FPNMKIzs%2FXZ%2BFf3RFLBZvyfjPm6X%2B18pCqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbBKhAo9cnsaVDmD7KtwDq0ie3t8q5Vyl9j2AOYHvuqdxzHFEi2pzPTCQR7hzJ2zTCve3XendCkPZlaVRUh%2FZfAsyK9wm72ntXiS8bRjUFkZPNkmUTXDjhQhWEOwQDfb2XZ0Sbe8S3LvI7T%2FSjwEF17MrPApDT6Rzr8bescsLrKDFWJDKOl%2FEYRGZH38TWTNK9F6Qq3qmy1nkZUQCXi3Tqb%2FQq0uQ5ckXH%2FrRv3TUdOIxm7nxY8C6wkCVxgKL%2Fx%2BhMEik8chWkRDlC6ctg0PR4BNqpvQmvM5%2FwqRcDbe3%2BqekOrplXq3oME3%2FOP5rEkXSoKHNdHvl9en%2BoBzzcz0yz6Ty4RSjFDKsnSbu9Q3sodPr4J6Oxc3kGTDeC4b%2FKkkma1RdZLKKbRsn89p1BJzVWw3X3KoUaQAUu5xGd0LYW3a9Az1e7qEWVTFtZKEgvfz%2BXfXfQln6Qwh0MmCEBRECJGg%2F6%2BQf8IOBe6T5w3Ra05iN9qVw0XRRCJD%2FsYBlYh4eAr897mKYfKwSGRxYlKUpP33XbntYchJFlIQ4cHtuyb8gP2aoZixgRXQ8IpbZIp0jbj%2By8WB01dNcHd7Wse%2FhJn9tb3%2BG%2B9IVi2hqqXhSVkYno%2FNimHZt40QhoSyFaP5ZPvMN6W2qKjA9BncwtqHHygY6pgEWZ2XXOdE20OonJSPhGOoe5kfiR1JKO3myXSAdypywb4yTEyOhyKcYtMFaYqlfMdgWUsZo9Q9xF5Mp9dvBZmov%2FbS%2F11p72g98SCTwzu6ux2A9PiFr0yJf2EZhNkT%2B6onrR%2FKeGHA0P2f%2B%2FSbrnaVh6ClgUMzrIGi9JjFA0MnMqNdoVsg3yCaq%2FzPf%2BfhZ9ONDkJdHlfS1b4YJbtjyQ5RJbk08swcb&X-Amz-Signature=df03dc7c887e821a3dde2bfed1d6e98334fa30a08e718fa41ec2ed85d6a1f592&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

