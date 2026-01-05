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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOBKZIVQ%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEpQYYdSndDv3ySQE3zQpek74bcK7yr9tQwa%2FMdVlTnBAiAMJxOGuStvX%2FJFegXWdDNbiTxGjmZhah0APrb2CW60RSr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIM7gEKV9IpVf5p%2B97GKtwDWd3p9%2F6wi3O9GbsxamFT5umQG2AJ7jWRUEjo0UiR2zncllI1J5Xa6Ub2heTgP1Zvds6lrps2YAsWFRpqlZWzvpomGfL8kK0k4Lq7%2BAQsUm4uPqtT4hHVIgoHgISBMeubanVeaM7ifpPMs5L5BUJw8okwt1rZX%2Be8CEBGn4zK8XN0vgjH5NBJbsh0SXWp%2FzniG3jCIDHCG7m4YV5HQyNv8RRz9Clc%2FhYdoOKUX26ZQAkjF%2FqzNicIaj06ZoaSb5cAW434OeTfZMBdpHVqb8rgbGUW6lx4FpPkdC%2F2SrhhImQsK1eX%2BI%2FgMuDNCW6LpM0aOa9kNvmAWRaKjWQo3PKWoeVmrzsQZanVIS%2FDcHUxPiD6upAx27bSP1L0soaD5rgf62YNCtrvM8Gnv4kpBSbdr7RMaiV3llQWIjCaoR%2Fv4DqvRuCas3dT6PYEkQxo4iiK7D5HEoJ%2F0zRZGbd2VgxhinosiM40SP4%2FytLr26vah00MdVi8DAMTbVP%2B9XU8jcQ8uTtykM9X7xIM9vxBGc03hawSOYPMcZ6B7PjT00N4CI05vyR7MLyedaF2HBPyc3gr8BmJ7JQfwXJx%2FrJo1Ca884JIVrSd8l4as9mBm5muWaTU4KCfZvJ6T8tf28Ywq%2BDrygY6pgGG3vTQqx9nDvjc71lCH9MSknEuz2xZkuwxfpcCvAiVH2%2Fg%2FA%2FO%2B7RCactTl4FnlBmUzWM5752xnzYFFdCj6NQAOedo10T5s19ITNPcmIVIZNV5oO7G5YlctM6Xevitp4kNSc7Mz9ZLS%2Bucdf%2FGOjGUv063cGzP9NYAQvjuO%2FxknasNBAcERgur84SoRg0FSjVO093Hp1kXBMtCGL%2BOL9s92qVG0IQ9&X-Amz-Signature=304999179f3265cd7d3ffb45c50a729f2a4c02f160849483cebb72325200904b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOBKZIVQ%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIEpQYYdSndDv3ySQE3zQpek74bcK7yr9tQwa%2FMdVlTnBAiAMJxOGuStvX%2FJFegXWdDNbiTxGjmZhah0APrb2CW60RSr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIM7gEKV9IpVf5p%2B97GKtwDWd3p9%2F6wi3O9GbsxamFT5umQG2AJ7jWRUEjo0UiR2zncllI1J5Xa6Ub2heTgP1Zvds6lrps2YAsWFRpqlZWzvpomGfL8kK0k4Lq7%2BAQsUm4uPqtT4hHVIgoHgISBMeubanVeaM7ifpPMs5L5BUJw8okwt1rZX%2Be8CEBGn4zK8XN0vgjH5NBJbsh0SXWp%2FzniG3jCIDHCG7m4YV5HQyNv8RRz9Clc%2FhYdoOKUX26ZQAkjF%2FqzNicIaj06ZoaSb5cAW434OeTfZMBdpHVqb8rgbGUW6lx4FpPkdC%2F2SrhhImQsK1eX%2BI%2FgMuDNCW6LpM0aOa9kNvmAWRaKjWQo3PKWoeVmrzsQZanVIS%2FDcHUxPiD6upAx27bSP1L0soaD5rgf62YNCtrvM8Gnv4kpBSbdr7RMaiV3llQWIjCaoR%2Fv4DqvRuCas3dT6PYEkQxo4iiK7D5HEoJ%2F0zRZGbd2VgxhinosiM40SP4%2FytLr26vah00MdVi8DAMTbVP%2B9XU8jcQ8uTtykM9X7xIM9vxBGc03hawSOYPMcZ6B7PjT00N4CI05vyR7MLyedaF2HBPyc3gr8BmJ7JQfwXJx%2FrJo1Ca884JIVrSd8l4as9mBm5muWaTU4KCfZvJ6T8tf28Ywq%2BDrygY6pgGG3vTQqx9nDvjc71lCH9MSknEuz2xZkuwxfpcCvAiVH2%2Fg%2FA%2FO%2B7RCactTl4FnlBmUzWM5752xnzYFFdCj6NQAOedo10T5s19ITNPcmIVIZNV5oO7G5YlctM6Xevitp4kNSc7Mz9ZLS%2Bucdf%2FGOjGUv063cGzP9NYAQvjuO%2FxknasNBAcERgur84SoRg0FSjVO093Hp1kXBMtCGL%2BOL9s92qVG0IQ9&X-Amz-Signature=bb2c135ba677c172af68aff723e60de41a7d7012da8506f8e802a317a3c9c499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









