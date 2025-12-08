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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIBCTMSR%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7eTSkvwFFLjk7578k%2Bt2iu%2BIgcP0m7U15vgyHRBdAQAiEAxEWQIRG%2FSpsjYo9vTUrSKy5z%2BAXx34viVWfEgZr8HdsqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEedfwRjBzxLxGKsqircA1bP5rjJ%2FkKZVV%2FEJfW9fGCldtfRcnrSsvL3iDSBKwHS4hdMlR3nlWhsb4LxnMbQY%2F%2FA2SRr%2BS7WU%2BQypHxiWWPxwTP00tW%2FHpICVKzV4iLmQT%2BhS3mZDGfZIdOq22%2FwSAtcqRDIQCOc3FwYjleOLkiLttngvfvbBzQW1CWGAVLP9WZEaCYKR7u2VYtp2GMIxO3sT%2BtMXJBjQbm3%2BBCqL21tpFyWPsjDBxjKC2amIO%2BkOenIREFtoJ4CoWLaXQAOGQiAKPWy30z60LaioAf439JijS28E4Dy6BT4fFYdQXcBxfPtkQ%2BeMn4QFTPpKLWSRDYUQYHKqg4dRf7JLVwzm%2FmrFm8h1EynXUk%2BnhiRSjs1%2BYXXaamb7D3qJizFTld2%2BNQa9BA19Ai446%2BbwPkwfapqKRjltqeaDbmV8bXQOcdZ%2FtIuSvtZoDynZi0nt6gLMcDAmUNwEW2Lg9WoxVTj7%2B7ONWBjq2PzGI%2Fq1OoMbYGF%2BlpxJVO7R5zo2FY7bcroo5cMjBPCdpyD0xsbv5thDpSlaZP9ImZBpmoJRAAeSLxHVlrnb%2FHr%2BufhCb8kMEh%2FYcUpUoJxNzCGFA7Zzd4Hud%2FFNVGm3OFcpKZ5V3GymqcEWXbH2qyzGsCPx9WfMKDu2MkGOqUBuxaiegWX2bpYhYUrUBqE6rcubbYsJjzi3jb5g9bQG19c2pzMGISyvxyge%2FzGkRdFJaWieyipBsNq8yUg4Xy4zhm2iMCNa6SscryPlgfkmwDdfqflIuzeCmqWd2F12y7QQFaRT0Rn6Quu6hSSs3qpIScF6pat6QmmpnEwoGQr2VhQ3BXOsa4W%2FLqb2gws0YDuRkngEk8iswEDO9d52XY7bGFaicjO&X-Amz-Signature=7c970f90800053a117886c43ad44bcb8785fdaa7b0545d5a97a457b8d8d3555f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIBCTMSR%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7eTSkvwFFLjk7578k%2Bt2iu%2BIgcP0m7U15vgyHRBdAQAiEAxEWQIRG%2FSpsjYo9vTUrSKy5z%2BAXx34viVWfEgZr8HdsqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEedfwRjBzxLxGKsqircA1bP5rjJ%2FkKZVV%2FEJfW9fGCldtfRcnrSsvL3iDSBKwHS4hdMlR3nlWhsb4LxnMbQY%2F%2FA2SRr%2BS7WU%2BQypHxiWWPxwTP00tW%2FHpICVKzV4iLmQT%2BhS3mZDGfZIdOq22%2FwSAtcqRDIQCOc3FwYjleOLkiLttngvfvbBzQW1CWGAVLP9WZEaCYKR7u2VYtp2GMIxO3sT%2BtMXJBjQbm3%2BBCqL21tpFyWPsjDBxjKC2amIO%2BkOenIREFtoJ4CoWLaXQAOGQiAKPWy30z60LaioAf439JijS28E4Dy6BT4fFYdQXcBxfPtkQ%2BeMn4QFTPpKLWSRDYUQYHKqg4dRf7JLVwzm%2FmrFm8h1EynXUk%2BnhiRSjs1%2BYXXaamb7D3qJizFTld2%2BNQa9BA19Ai446%2BbwPkwfapqKRjltqeaDbmV8bXQOcdZ%2FtIuSvtZoDynZi0nt6gLMcDAmUNwEW2Lg9WoxVTj7%2B7ONWBjq2PzGI%2Fq1OoMbYGF%2BlpxJVO7R5zo2FY7bcroo5cMjBPCdpyD0xsbv5thDpSlaZP9ImZBpmoJRAAeSLxHVlrnb%2FHr%2BufhCb8kMEh%2FYcUpUoJxNzCGFA7Zzd4Hud%2FFNVGm3OFcpKZ5V3GymqcEWXbH2qyzGsCPx9WfMKDu2MkGOqUBuxaiegWX2bpYhYUrUBqE6rcubbYsJjzi3jb5g9bQG19c2pzMGISyvxyge%2FzGkRdFJaWieyipBsNq8yUg4Xy4zhm2iMCNa6SscryPlgfkmwDdfqflIuzeCmqWd2F12y7QQFaRT0Rn6Quu6hSSs3qpIScF6pat6QmmpnEwoGQr2VhQ3BXOsa4W%2FLqb2gws0YDuRkngEk8iswEDO9d52XY7bGFaicjO&X-Amz-Signature=93dd91352f302a10731f4ad9bf4f112398c45e412e045876a8551d5b4c3d5229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









