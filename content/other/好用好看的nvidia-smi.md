---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLBBCGBZ%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDD1B1wtIHnXl%2BG9aHMxHM4Fs47yX2O86Fd6sfs2AoPyAIgYtY5MkIL5yUgQ0%2Bwr0Xx%2BjpLYGmqR3d8KMTUsUvwjBcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEtWstP6SIDJ%2B0o4qSrcA7r5OcDCZmhYp%2F%2BA1MIyEvAHqKC3AjgmCCb6ghl%2BTE2CRuLXXmwi80WI3jTuwxgMkntAxQ2Y4gpbXvNE5svbmMzggDARMDVukLMaV2jA8TdwIYvuD2AVO49vCViJy9jcB7G1PvB6S3V3I2%2F%2BAP9k2Ol%2BsmHw%2FhwSPFr25wWIbjF8RDBkrz0OoS2Jov9catXEpnDSAnqZp3p3%2FtacgOMkeKQbNFJPPi09lzH3e15s4JHkMC1yTCN6nzrqfRed3z4T8%2Bqdne5IAJEq2QQhGEvtq3tODTPzj9Wtyv5erjkSmK%2B82H3b58M%2Bh4IXW1HSUx%2FTaRpbJJOOVlFOWwMIT%2BFj4K8%2FXqdwTiY39sZE5vkqbaxYXyLoJBJgSCsiu%2B4bowC%2BJbr%2B3aLUvfuJZrIIje1xbu%2Fcvm5jpfXxmSxlu2EZmDLIYunIlGArhTTn1JwHnYOtXoWsCNTArvyNwuZwLN6lysBrNIZjKkFPQu5xu8CIxcNxQO%2Fws%2FTEbZ74zZ2npuD%2FaplYPG8Ek4HO15loe4Bhw8VgF9lOhXSRp%2Fh4IIP3OiayiMyn2FapCSBONbH%2BizeEkE360wUTaRPU7dwdovxkJ%2BaEqfv75h5jEkzXUIOpPaqN3j3Fv%2Fth%2F%2BaOv7AsMNDI9MgGOqUBk373M%2Fg9DFP7DOcylB0YFPu0lPmxAwcbV%2FBV9IzkG1ctRPV7QrL%2BTDhUrxr64Ey3NAX8MkqXZHSVC4mS0Ye8CKLkagfFIsXfdS4%2BMv0htm7NZ8sRjYwt9Z7ZiN%2FIjmt2l%2BSKQ9s%2BlBBgYFUmuTv2tmPpOYLuszUEWxaHthJ1H3TuuwmgMNkaILVn30fU4s0XSo0p7O7X4hIZkIBqul7eDquGKSAS&X-Amz-Signature=fd79b26c65a384b0b53ab0450904cd94e0ebad86780c188e1578724558012de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLBBCGBZ%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDD1B1wtIHnXl%2BG9aHMxHM4Fs47yX2O86Fd6sfs2AoPyAIgYtY5MkIL5yUgQ0%2Bwr0Xx%2BjpLYGmqR3d8KMTUsUvwjBcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEtWstP6SIDJ%2B0o4qSrcA7r5OcDCZmhYp%2F%2BA1MIyEvAHqKC3AjgmCCb6ghl%2BTE2CRuLXXmwi80WI3jTuwxgMkntAxQ2Y4gpbXvNE5svbmMzggDARMDVukLMaV2jA8TdwIYvuD2AVO49vCViJy9jcB7G1PvB6S3V3I2%2F%2BAP9k2Ol%2BsmHw%2FhwSPFr25wWIbjF8RDBkrz0OoS2Jov9catXEpnDSAnqZp3p3%2FtacgOMkeKQbNFJPPi09lzH3e15s4JHkMC1yTCN6nzrqfRed3z4T8%2Bqdne5IAJEq2QQhGEvtq3tODTPzj9Wtyv5erjkSmK%2B82H3b58M%2Bh4IXW1HSUx%2FTaRpbJJOOVlFOWwMIT%2BFj4K8%2FXqdwTiY39sZE5vkqbaxYXyLoJBJgSCsiu%2B4bowC%2BJbr%2B3aLUvfuJZrIIje1xbu%2Fcvm5jpfXxmSxlu2EZmDLIYunIlGArhTTn1JwHnYOtXoWsCNTArvyNwuZwLN6lysBrNIZjKkFPQu5xu8CIxcNxQO%2Fws%2FTEbZ74zZ2npuD%2FaplYPG8Ek4HO15loe4Bhw8VgF9lOhXSRp%2Fh4IIP3OiayiMyn2FapCSBONbH%2BizeEkE360wUTaRPU7dwdovxkJ%2BaEqfv75h5jEkzXUIOpPaqN3j3Fv%2Fth%2F%2BaOv7AsMNDI9MgGOqUBk373M%2Fg9DFP7DOcylB0YFPu0lPmxAwcbV%2FBV9IzkG1ctRPV7QrL%2BTDhUrxr64Ey3NAX8MkqXZHSVC4mS0Ye8CKLkagfFIsXfdS4%2BMv0htm7NZ8sRjYwt9Z7ZiN%2FIjmt2l%2BSKQ9s%2BlBBgYFUmuTv2tmPpOYLuszUEWxaHthJ1H3TuuwmgMNkaILVn30fU4s0XSo0p7O7X4hIZkIBqul7eDquGKSAS&X-Amz-Signature=4f6bad3fa70573d0cf9463dfa2b5f36bda5757d8f366cd46edd3c45d61b666ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









