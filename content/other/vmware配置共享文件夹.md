---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SYXZ6G4%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXl2uqPFeCezxSmZGkF8XvZAfaNdWjKJp8w5MzGSbM1AiEA1zD0DUv9DsNAIUUJs22ntvOdLTn5R9TSOEE%2BbQmTs5AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOwzBI09Ywta0%2BG7ircA%2BcChxSqhuADXUR04Gr0bJebO3kWLNHZWC4uWFfFPpOfuLWgUCbwABbCFgEShxs09EHCNO8aU1VqxDOnQKMXKlBl6Sa49PcSi08XFwVr0fzGhuME%2FNenmiKtPLqNQKCcokxFJ5v9royQ44ZuMpPOlkH583zRhogbL2XN%2BK0VTMVM34Z8vsU60nWKYWz8Z%2BFFY4%2FoHz5x9uRriZfRHfkF54R8H366Ugpby51S9RkVQomtFY94IdKEy8KjpzWMI%2B9GFG%2F7tVG3%2FzztS8uny10QvQpUOkvJ8sNGzKLw6PtagKqdrYi17d2QQCIir%2BPs23mHCRvvbfLS2zN%2F2jUJyuINlE1DizzoXnoDOCPBXvB8%2F8Vdg0vSA43TnUGsM32SyTtsGi%2BmQstErZWMDlRkU26o1g%2FyWYEsAa5ELlra3NEEK%2By3OcNBasYKfz%2BnKw%2FUdaIEoKLQRPH597HxExlWOZUGUaGl97tox%2FvZ11BiERwLqC%2FUv7kt6%2FasUKOTOI4IuZBdNrqb9Suvpo59FHP1IF18taKq1fQ8QAc%2F3tMLNTGdte41OXDl8ISHrc1Pjiu7L4T8phJN0sSkoS8V011dWF6nJYXldsIKLohHRgzvmxH%2BLdaRQST9G7EADDP32MdmMJ2xzM4GOqUBF2%2FIsOiFBF4c7w7XsG7jAn6Pl5RuN131E3vKFXbPMrhVl4621KB7Jda7ozBFv%2FlQhC4TDsATFh2u%2FjSSBOV%2BjzMNST6aUTXlvg%2FyEW62WN0JMOe5n1YKkkgTRLB2%2B%2B0Azz1UC0U7mTvm832p3YUj65CrcfDoMunH0X7iSbB75DKvz67oDKthDKq4nqhAojAP1ynWfbxQyBnpUK9PlO9PRmh0i8CC&X-Amz-Signature=40d3f09a0b8cbd097cb7babf15eceae7dfd102abac0533b7e6b4f490989ef29d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```



