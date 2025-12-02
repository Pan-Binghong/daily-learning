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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMJPXQ6H%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFkqqIkz%2FG%2BVjcjkOdXsEHHlzO%2B%2BZ2ycw5vfvMdIQfPUAiEAxVx5OLXghecc4tLKtpx%2FQZh%2BrtSFlSNcnXgMaT8ei%2Foq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDA0i0o6aO4i33z1nyCrcA1QkB2I7k3ow8FTSB4G7BL52OEu0P5dJwRRmVMLelCJHaomLpsptEv7LQAoJp00nPJC3M8FLm7zP36LUO28hoHGfSZkTFgpvO96K%2F7aTxSZJZw%2FniNb8DlrMEEXzIjLVb08NBcYyOu31pmSx8%2Fe7VHqPymBxhhLQTpwK4prVpMdTCxzbzXutV097OLNgzBXBdAy3Vb5%2BsRmMifG7VrfH%2FfBcXIiwcEr42QUvTccLOm7Gn1aHTKTJmlHcPHO5Q7bB56hNhY%2BK0wJ1OLdlXgHJaf565TRPjONM49BDrX8DoykAizrFgbw1eQyTziU3ZqqCkjvQbK0uWDQA2Ah%2B9PFvk5yi5trqmAFkbXqReHDfzbUDDzi0cqdcMgDD4B9R6UU6x5zTnkwl3WJoZI09F7jJAbziIjYXqAJIvQ5IESI1fYIcoT6xxaM6mR1pbKwPfhqrN8hFBjSpgDrxZHsdnPpu2HePd%2B6%2B43xOKUMidy6MWq2bSZaRaGsO80Jtd%2FxebQFpPY1F4S2LwXRlsSD6s68PiIyWUXDKSqD0SH%2BTRM9uTxIr7wU7MXbTU4on%2B%2BkxLlB0CpfOT1UprJqY4c0Vb8DbVK9X6uGwhypOwXvnxmdw68A2upQQKtxGvYkCl%2FLuMOPfuMkGOqUB0%2Fr9I8%2BEkpsihO4wPARmtKOs1IKUqdp7ef%2BFGwjj5Ds7khdgUd0LEwuM6lh0MeKLLjk88ILw4%2Fa532OhU%2BrDcD0IvojFVIr8mj3DhpbEURKhOTRnCQf3ElMwWQoAuhUezJw9bmAacUtZJtRubdfypzK%2BLGHarJjqT7bXsfGtwcu8G68uDE%2BhZRqoXK1cDVXy9UP4w6NK3w3ZUnpuNoL9kdx6ey2L&X-Amz-Signature=40c2af9366de44fc1eba4878aa981536cc1404be6960747438dfe8da3406b9f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMJPXQ6H%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIFkqqIkz%2FG%2BVjcjkOdXsEHHlzO%2B%2BZ2ycw5vfvMdIQfPUAiEAxVx5OLXghecc4tLKtpx%2FQZh%2BrtSFlSNcnXgMaT8ei%2Foq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDA0i0o6aO4i33z1nyCrcA1QkB2I7k3ow8FTSB4G7BL52OEu0P5dJwRRmVMLelCJHaomLpsptEv7LQAoJp00nPJC3M8FLm7zP36LUO28hoHGfSZkTFgpvO96K%2F7aTxSZJZw%2FniNb8DlrMEEXzIjLVb08NBcYyOu31pmSx8%2Fe7VHqPymBxhhLQTpwK4prVpMdTCxzbzXutV097OLNgzBXBdAy3Vb5%2BsRmMifG7VrfH%2FfBcXIiwcEr42QUvTccLOm7Gn1aHTKTJmlHcPHO5Q7bB56hNhY%2BK0wJ1OLdlXgHJaf565TRPjONM49BDrX8DoykAizrFgbw1eQyTziU3ZqqCkjvQbK0uWDQA2Ah%2B9PFvk5yi5trqmAFkbXqReHDfzbUDDzi0cqdcMgDD4B9R6UU6x5zTnkwl3WJoZI09F7jJAbziIjYXqAJIvQ5IESI1fYIcoT6xxaM6mR1pbKwPfhqrN8hFBjSpgDrxZHsdnPpu2HePd%2B6%2B43xOKUMidy6MWq2bSZaRaGsO80Jtd%2FxebQFpPY1F4S2LwXRlsSD6s68PiIyWUXDKSqD0SH%2BTRM9uTxIr7wU7MXbTU4on%2B%2BkxLlB0CpfOT1UprJqY4c0Vb8DbVK9X6uGwhypOwXvnxmdw68A2upQQKtxGvYkCl%2FLuMOPfuMkGOqUB0%2Fr9I8%2BEkpsihO4wPARmtKOs1IKUqdp7ef%2BFGwjj5Ds7khdgUd0LEwuM6lh0MeKLLjk88ILw4%2Fa532OhU%2BrDcD0IvojFVIr8mj3DhpbEURKhOTRnCQf3ElMwWQoAuhUezJw9bmAacUtZJtRubdfypzK%2BLGHarJjqT7bXsfGtwcu8G68uDE%2BhZRqoXK1cDVXy9UP4w6NK3w3ZUnpuNoL9kdx6ey2L&X-Amz-Signature=82ec4ee597952d81ddb6db02b6099be13dc18b6a1d3ba257f9004f696b8b8882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









