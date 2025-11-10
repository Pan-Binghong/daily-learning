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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JG3WVQ5%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCjHCTohUL3c695v%2FezU5A%2FwfiH0MtRKKTh5OrFlfseygIgHE3EnJiVRi3ic5GsGsb1rcwN%2FvbIF2HuWyoLiCFxKSkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPYoMfZQHBpUEu94ircAwqpsWS6tN63ikJJm49GNoQh%2FSrYGI5SJmH0Bx1855KypU8PbZ6R6wny59ObxlVjqLtPYoLXmBATfzfFx%2F9Mv2fWmv2KiPpJeaGVW1Qb1rlqeiRmy45Ew7T%2FBM6T5KoGmNqKzV3yYuXaLKK1zVITpK0O7XFBD1xg38jJIVu99aOT90s%2BIfkQNdsK%2BLHI53cXzoyvPccclZSSEs9y0QIbbRsdmuM4zxXJRKLPwLD095A5JYX%2ByPOFeOJeGGDJA7sxNjH5cZ3PE80l7zbdK1T1xLhXm%2F%2BHRDC%2BcsXjrTp3dVFnjHE9AMFom6%2F%2FmxGPyZMgJAKybfv32vrugkveoPUbMgzlT56pi3Hrnufk6dFCDmHZInzrz4TUXvFZ6xKI3CuvYKyAHecciZ96D7FYc4ZR2O6goDyhuwLYl2G%2F7ZwtonwrYe71XMtSQLGuepjlMBdsNAgt7uOi0HM2l64%2BUZm3nvVI%2Blv4JzKIs17EGL0al6EDiNPPrvmh50BfN7tp4V%2FQmOUvU6zW4MZY21wZFZ1fIufczwEj2r7CcrIome31abGh2JYV3HBACv5%2FlgKj2IWANawJUlfoBS4f6ZpEphp4c%2Fntp4wtxM7YlgCNxI9dQEBhkQHaG2zqlaziBbtyMMW3xMgGOqUBbMXxFYuTmBag9xImmWPURnTB7%2BHrgfShD%2Fg%2BWIrc%2FkqCDklF8ueqTXBVO8YxfB1ffuNpnEqudWJl9QvycQroAR%2BpQiANQVMbuGu%2F6l2sj2trlXJZl1OpydY4TfDPeweNit1gnUEDDezwJlRRO%2FX%2FeKpEr%2BawX77kAvv%2Fs0BCtwInioh2fM3vqYKhJ34KyMFJV7eM7471Wg0x1QAOtoMoo4V6219G&X-Amz-Signature=f219c247a756e61d2934e4b986005691b49956ddc89647b5142756b2799abbbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JG3WVQ5%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCjHCTohUL3c695v%2FezU5A%2FwfiH0MtRKKTh5OrFlfseygIgHE3EnJiVRi3ic5GsGsb1rcwN%2FvbIF2HuWyoLiCFxKSkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPYoMfZQHBpUEu94ircAwqpsWS6tN63ikJJm49GNoQh%2FSrYGI5SJmH0Bx1855KypU8PbZ6R6wny59ObxlVjqLtPYoLXmBATfzfFx%2F9Mv2fWmv2KiPpJeaGVW1Qb1rlqeiRmy45Ew7T%2FBM6T5KoGmNqKzV3yYuXaLKK1zVITpK0O7XFBD1xg38jJIVu99aOT90s%2BIfkQNdsK%2BLHI53cXzoyvPccclZSSEs9y0QIbbRsdmuM4zxXJRKLPwLD095A5JYX%2ByPOFeOJeGGDJA7sxNjH5cZ3PE80l7zbdK1T1xLhXm%2F%2BHRDC%2BcsXjrTp3dVFnjHE9AMFom6%2F%2FmxGPyZMgJAKybfv32vrugkveoPUbMgzlT56pi3Hrnufk6dFCDmHZInzrz4TUXvFZ6xKI3CuvYKyAHecciZ96D7FYc4ZR2O6goDyhuwLYl2G%2F7ZwtonwrYe71XMtSQLGuepjlMBdsNAgt7uOi0HM2l64%2BUZm3nvVI%2Blv4JzKIs17EGL0al6EDiNPPrvmh50BfN7tp4V%2FQmOUvU6zW4MZY21wZFZ1fIufczwEj2r7CcrIome31abGh2JYV3HBACv5%2FlgKj2IWANawJUlfoBS4f6ZpEphp4c%2Fntp4wtxM7YlgCNxI9dQEBhkQHaG2zqlaziBbtyMMW3xMgGOqUBbMXxFYuTmBag9xImmWPURnTB7%2BHrgfShD%2Fg%2BWIrc%2FkqCDklF8ueqTXBVO8YxfB1ffuNpnEqudWJl9QvycQroAR%2BpQiANQVMbuGu%2F6l2sj2trlXJZl1OpydY4TfDPeweNit1gnUEDDezwJlRRO%2FX%2FeKpEr%2BawX77kAvv%2Fs0BCtwInioh2fM3vqYKhJ34KyMFJV7eM7471Wg0x1QAOtoMoo4V6219G&X-Amz-Signature=575adf8bb982d3d8ae2a92313d96458353122bdfa971c1f82c4ca8e04b2f8bbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









