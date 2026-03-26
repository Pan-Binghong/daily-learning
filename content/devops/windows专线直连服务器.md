---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IQYVEWG%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG6rKwJCNJiaDZIFO9KnUn1oN%2Fw0kBdxDT6r9mSGCjNuAiEAqoFmEnskojKGogFaPJG7mE5mdkgNzALT0p%2BuAJLp7E8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHN6Ll3%2FN%2BZiC3sOkyrcAzjI2F4SFbHdXpLICic3Sk11QEufkz6xijmIgtR7PS354ktL2UQ%2FBhjWgURGRjrZq0fsM0nLcnn%2Bi2cbPavOCfvbYJU%2F0cY1P079wtlljYrdZr%2FR19PdZQVTMYVpOw9j3KCA6X7nDOHkHAmqGylmae07WY9lijczUDb%2Bo00suy4%2BRUPQutEx%2FE5rSzd0TOxnBFX54ZEb2cj86Aeo6CT8YvVbAtke11A31TSsjh5pJ%2Fjv3rxhryx%2BDVjTEYoHLdIG5h9Qm1KTJnLk5GwViJwi%2FIZsktVtSkwUxCm4f1KH4xFsLc65AfCOXkPEvCw8dyDJEGGRodNcf1mCoM6j3FHpGeG1MygCZtbzlOt9BR6ALBvUjSD4%2FfMlbk6UA3bxADG9cBVmS4BkyLsQ7dspqXNwaVqaliVhLvhpMTNLAMHS0DRXoyR%2BLVmDL8PWaAA4YkJOA2fciZx779JT9VTYe8gnbZJgKuutlsZCy9usKW2gzhykm%2FvmyMCQ%2BaUKGgov5%2FfQKwIaOSCuxdPSZnbSEGligjdejVq5P5Yi18W6UY0gmZVLaGXbXUMkjuFeMzRG0w%2BaHhO5hqSgQ83S%2FvaUFZdxC236ScfZZ6r0ot%2BmG%2FAJ5C3PUjtJkJSk4NUcYkjwMJLJks4GOqUB4Dd7CVrZRmEzVx6Ser9XDRrFUzpBsWxvG6L%2BUkGPr4gmvA4A3BcW8Vp5wFeXSwRWTahLXeH2SgsB1bCY7s1wu2d6tQbz5tjROMcy3zgRdwNliXgv39unmuNaZj8H0SLhDR6OD%2B76s3N6t5sxuAfYm3jrr25L%2FE%2Fkl5G690yoe16spGnlVuL8h3ni1rGeWDsexZNk0Qec4bXdje8YsB3vehgzf3gx&X-Amz-Signature=46df9a60706d6cd93c15633ef75e848fc5377bf8546c414ccaf11a5441def720&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

