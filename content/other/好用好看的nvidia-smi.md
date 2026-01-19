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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FRF5SF%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmCp5zz4bBf4NL8o1kX7XhcBLXCf%2BLknT6Xb%2F7%2F7n2CQIgFffxY67Fc0gcNP3mioQYCAHPQdpRclGVOE3co6OVs8EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFn09ecYiNNQhB%2BdACrcA3MIULfFweg5ud5tYXUtfD6nrdUuR4M1B4d2X%2Bz3d1ZktR%2FtrG1ZxCpnzapVY0pRBOz9KCCOsOcsIAqaFiqX12QsGuZCxTVNblFlwonjMJhlHsxazuXWY5dU%2B%2BMuYs%2Fk2eRtmaLuxiPCF32luISxkyxCDLcz%2BzQpBd5AHcXFyhuaXmTEQQEXRTLYtr%2BwDtYLXaGRWgbF0cOn9LfMEKUzS%2BeeKymsrMAF%2Fjjha0eL2EtiCu88PLXZbnK%2FESl5Hb%2FjaStm9IMqVwmgs5bsLqN%2Br7Fl2TwQglFcS8itzfxqZzxVY8Y1oETn4tRyRfmtA6KfA8bdPfWGN3YZ7AXoiolDbKFq6BgPIzUwcQcPlvS%2B5C9eAozrV0%2BKQFyFxRED7nsmBVzSnP3dBpkLBPSwYzRoR6fhewSDx5Cr0l9C9D11PQkBa7E0%2FMmeEMJKed6WH3AeJ%2FMWsv5MFCoO%2Bu3n5VJ09uQ%2F2w5NtfkIN7nw4ZfxVguRLodRVlNw43pRnNet27zbk4GirGDN5tMe5R2bb4yeusDhxmx5o%2FWVu5pQIOroS5yt0ny5J%2FU7mU1FvLNHUl39mWLjLK0I8P0UPlwHCvZTazzjoyPVk%2BaMqRDq135zzfnTbn4a8PSvqIJCtPc%2FMIrdtcsGOqUBMFpc3MAZ334XwOT2tIJatU8t5TU1ewft%2Bfjme%2BqbPLj3hzmIZom9fsUxvuA9Z2LbZetVziHftGu1y77%2FgjivhKFHOqfkG6mq8QrQyX%2F9k3EbgR36R1j6caGzqdiP%2BFEYPVo1cRDJy8VpO%2BxkUoeUicRiuuBNX1A68aD46dmkk8fe7uIV0TUo4Br5OeFB5uLAQOHcSiTJ0HV6CKhAZOsBPpdVkzL%2B&X-Amz-Signature=47bd46b518f268f0e59a6ec7bedadc98ad99b01327a28bdfeed21ee2963d7aef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FRF5SF%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmCp5zz4bBf4NL8o1kX7XhcBLXCf%2BLknT6Xb%2F7%2F7n2CQIgFffxY67Fc0gcNP3mioQYCAHPQdpRclGVOE3co6OVs8EqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFn09ecYiNNQhB%2BdACrcA3MIULfFweg5ud5tYXUtfD6nrdUuR4M1B4d2X%2Bz3d1ZktR%2FtrG1ZxCpnzapVY0pRBOz9KCCOsOcsIAqaFiqX12QsGuZCxTVNblFlwonjMJhlHsxazuXWY5dU%2B%2BMuYs%2Fk2eRtmaLuxiPCF32luISxkyxCDLcz%2BzQpBd5AHcXFyhuaXmTEQQEXRTLYtr%2BwDtYLXaGRWgbF0cOn9LfMEKUzS%2BeeKymsrMAF%2Fjjha0eL2EtiCu88PLXZbnK%2FESl5Hb%2FjaStm9IMqVwmgs5bsLqN%2Br7Fl2TwQglFcS8itzfxqZzxVY8Y1oETn4tRyRfmtA6KfA8bdPfWGN3YZ7AXoiolDbKFq6BgPIzUwcQcPlvS%2B5C9eAozrV0%2BKQFyFxRED7nsmBVzSnP3dBpkLBPSwYzRoR6fhewSDx5Cr0l9C9D11PQkBa7E0%2FMmeEMJKed6WH3AeJ%2FMWsv5MFCoO%2Bu3n5VJ09uQ%2F2w5NtfkIN7nw4ZfxVguRLodRVlNw43pRnNet27zbk4GirGDN5tMe5R2bb4yeusDhxmx5o%2FWVu5pQIOroS5yt0ny5J%2FU7mU1FvLNHUl39mWLjLK0I8P0UPlwHCvZTazzjoyPVk%2BaMqRDq135zzfnTbn4a8PSvqIJCtPc%2FMIrdtcsGOqUBMFpc3MAZ334XwOT2tIJatU8t5TU1ewft%2Bfjme%2BqbPLj3hzmIZom9fsUxvuA9Z2LbZetVziHftGu1y77%2FgjivhKFHOqfkG6mq8QrQyX%2F9k3EbgR36R1j6caGzqdiP%2BFEYPVo1cRDJy8VpO%2BxkUoeUicRiuuBNX1A68aD46dmkk8fe7uIV0TUo4Br5OeFB5uLAQOHcSiTJ0HV6CKhAZOsBPpdVkzL%2B&X-Amz-Signature=264f655c3f4db4a7bccc270dfd0abc5b486bf3029f8fc45f758a608f537da768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









