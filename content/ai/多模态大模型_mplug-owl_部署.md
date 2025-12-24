---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWVDV3F4%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFsPOsNuroNWt9PGDHb1Nt1KmXF1WNOUK5ejK6AU5aF4AiEA3Z3MmkkwS95ENv0FhUZEEV9%2FKlABhj9pn2FEGgcagKoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDKKY5bA8QDSn4RIs1yrcA86ET0G%2BuEfia%2BF55nFKbzEyLYJQxhx5eN2i8wdAYGKWxFXL%2FeNL%2Fk1RuvcT2bKMoR%2BELSrACbcJvUkxwMT1RAeAou%2BwVrBdKMiGhJU3J1YJh3OJ6U12EjE%2B291VddYS48QCzJbZVSHlIlmNcPIW45vekUNV946MaJFSjCA7Cb%2BGY%2BskmcCYCf5lmaasnw9L%2Bdt5zdP4e9CtZ0tcLkINmz2ZulYullE3IGrWXtPHGDbSv3mMC1XxsO4lVDCFjNvF14vzDDlyrlcVl6EhlVNpHtOmmflN9tReVAfHic%2BUEjDT0s%2B0euq%2FJ8UiwkspgLNakGFI5j%2Fsu%2B3EO0e45OofJpYYoHeVz5cu9oEpusRs38ZMI8t26ROYCZNUKv%2FFv0nh9bhf316N9vbwZF87AyT8En2AV6jJPa82bw4z2EUwLrnMMCxsoZ8WyjQ%2FFWKUE4pZTDaD6gJulDt5axbHC%2Fb39TeHSbs0htv%2BHALqEv4hh52PHpzSGtJUMiceXp1%2Fsr2ubS0akg33e%2Bnn0a%2FjzwQnxNYaxl6IIPemygcV%2F%2F%2BAS73QSL0V0k3CSkbeCTmzXPNjVcuC9DE%2B6KcYRSUin0M2ZKxCrc9tGMEDOiZRXsSx8%2FCtI7ij8godFFjCKGVQMNDgrMoGOqUBkNdT4HP6XD0u5JVnUsQVg0a5FFkVt5ka9YTFHyvM1I1ePLnKk1sYpuu1ww6SXhHvpZcUZ%2F%2BGZI3M2uG7%2B54aQuyCnpq5N3%2FkJQLHRhsZbu%2FHpRszOmDGoDUlE74BylC5ceoDJf7v1mqsxiFRKsBL3%2Bq3fi1%2BQuVIW5D7Fraq5Ul6mOR45Ytf2WT8C8kfkQJZBJbTeQ9sRbNVPC2UqDWgilBkvL1i&X-Amz-Signature=7f60ccc0a5050ea849dc6f065806e18878de86c74ae22091b97056e8b7f9ac14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWVDV3F4%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIFsPOsNuroNWt9PGDHb1Nt1KmXF1WNOUK5ejK6AU5aF4AiEA3Z3MmkkwS95ENv0FhUZEEV9%2FKlABhj9pn2FEGgcagKoq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDKKY5bA8QDSn4RIs1yrcA86ET0G%2BuEfia%2BF55nFKbzEyLYJQxhx5eN2i8wdAYGKWxFXL%2FeNL%2Fk1RuvcT2bKMoR%2BELSrACbcJvUkxwMT1RAeAou%2BwVrBdKMiGhJU3J1YJh3OJ6U12EjE%2B291VddYS48QCzJbZVSHlIlmNcPIW45vekUNV946MaJFSjCA7Cb%2BGY%2BskmcCYCf5lmaasnw9L%2Bdt5zdP4e9CtZ0tcLkINmz2ZulYullE3IGrWXtPHGDbSv3mMC1XxsO4lVDCFjNvF14vzDDlyrlcVl6EhlVNpHtOmmflN9tReVAfHic%2BUEjDT0s%2B0euq%2FJ8UiwkspgLNakGFI5j%2Fsu%2B3EO0e45OofJpYYoHeVz5cu9oEpusRs38ZMI8t26ROYCZNUKv%2FFv0nh9bhf316N9vbwZF87AyT8En2AV6jJPa82bw4z2EUwLrnMMCxsoZ8WyjQ%2FFWKUE4pZTDaD6gJulDt5axbHC%2Fb39TeHSbs0htv%2BHALqEv4hh52PHpzSGtJUMiceXp1%2Fsr2ubS0akg33e%2Bnn0a%2FjzwQnxNYaxl6IIPemygcV%2F%2F%2BAS73QSL0V0k3CSkbeCTmzXPNjVcuC9DE%2B6KcYRSUin0M2ZKxCrc9tGMEDOiZRXsSx8%2FCtI7ij8godFFjCKGVQMNDgrMoGOqUBkNdT4HP6XD0u5JVnUsQVg0a5FFkVt5ka9YTFHyvM1I1ePLnKk1sYpuu1ww6SXhHvpZcUZ%2F%2BGZI3M2uG7%2B54aQuyCnpq5N3%2FkJQLHRhsZbu%2FHpRszOmDGoDUlE74BylC5ceoDJf7v1mqsxiFRKsBL3%2Bq3fi1%2BQuVIW5D7Fraq5Ul6mOR45Ytf2WT8C8kfkQJZBJbTeQ9sRbNVPC2UqDWgilBkvL1i&X-Amz-Signature=75eed59c5f324072b88da5e2d0138b28467d1b0e71254dc3f835be6e09a85597&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

