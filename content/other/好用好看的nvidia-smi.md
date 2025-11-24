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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C3DE7OG%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIQsWt84ymjUwSK%2BOn8JgY2yZMZnlHvs4qTWJxnSIwFAiEApg8wz2bNrMxnkFGNW8KIjrbc8tZXBRLwSDTFuU4uMWAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE%2FpgtcxmDzVACAtCCrcA05vBI6XIr5VKWOAwN3yRJrbnb2RZKdzfANdp1FT%2BPMcVUo2OgATaV9vdOHJMT8LZNFNBnmlOlOwyndswWWeieCFVmqrf0y7y2%2BFdTmagk6LE%2FHkCP6p7GndRtKyZTkqlHjgjzwe1M%2Bj9%2BsbgfYqa96Eq%2FXdi0rTMCbQNWY19NaYJ8vz7BPbOeqexLkfM6cdjlsSbt62gvhR25z0nPn03xdrlrndDFtr3ndoCVn97mr9qq3HdAU9wlqBpkgfZestgH903LRAS%2Ff2hF7UAPVbLaZfqhKsIt0ufRQ9RRQo%2FqT2OVMP5wMnqrU4i6fgu5zh3yoMHoz84aaJnyhwidXyo7im4vOgEY2yT33Jmt0vQehWVuI2rQ4Jfj8nM7rUvZTEDdfcFa7sULM%2Bo1nVcSL%2FirT2nOiUHzLwM3p6xxJp82V0O08cMMR%2Fij6P3Yw2aUVkgIGo4LCMuxSo1BTiIbWKJMsudmoaOtVP451PNqPIHX0LqPXO1alMQm4zY1FDYIxajgPz4OYV2FpkmEmJPvSfni05j6pvPl4KWGhMyfHa06ottxqDrlEm%2F1%2BdWu%2BmMyooR4s9Cjswg8nZHMrtMl8t01rUTaYxUyd%2B2PeFGVdwtZqlfdg08RqW2Vwa6twlMIDcjskGOqUBK%2BQ2jKHTXJZkDLglTjTE9LLNTL9mywUXdkloSH90%2BlCnRLASnNOxnYoO46wwbxCMMIxnLUnPdbGf5xaZP%2FZ89ER0MPYnLG6vOFXMdqqv9Cren9o3RwPcXeyQhln%2BUQpTpr46OAxO%2F5VdeKnXU472BrVIEcTkA9GcDMkoIegyjFWNO8QUF7chq0sxz8zd8HTc9C1O05N0IgG40KTLsyGtWqXPb%2Bac&X-Amz-Signature=71e45762b0e5ae5b97211dd9a327ad305c8657c8589cd4ccbede7a89a3a168b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C3DE7OG%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIQsWt84ymjUwSK%2BOn8JgY2yZMZnlHvs4qTWJxnSIwFAiEApg8wz2bNrMxnkFGNW8KIjrbc8tZXBRLwSDTFuU4uMWAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE%2FpgtcxmDzVACAtCCrcA05vBI6XIr5VKWOAwN3yRJrbnb2RZKdzfANdp1FT%2BPMcVUo2OgATaV9vdOHJMT8LZNFNBnmlOlOwyndswWWeieCFVmqrf0y7y2%2BFdTmagk6LE%2FHkCP6p7GndRtKyZTkqlHjgjzwe1M%2Bj9%2BsbgfYqa96Eq%2FXdi0rTMCbQNWY19NaYJ8vz7BPbOeqexLkfM6cdjlsSbt62gvhR25z0nPn03xdrlrndDFtr3ndoCVn97mr9qq3HdAU9wlqBpkgfZestgH903LRAS%2Ff2hF7UAPVbLaZfqhKsIt0ufRQ9RRQo%2FqT2OVMP5wMnqrU4i6fgu5zh3yoMHoz84aaJnyhwidXyo7im4vOgEY2yT33Jmt0vQehWVuI2rQ4Jfj8nM7rUvZTEDdfcFa7sULM%2Bo1nVcSL%2FirT2nOiUHzLwM3p6xxJp82V0O08cMMR%2Fij6P3Yw2aUVkgIGo4LCMuxSo1BTiIbWKJMsudmoaOtVP451PNqPIHX0LqPXO1alMQm4zY1FDYIxajgPz4OYV2FpkmEmJPvSfni05j6pvPl4KWGhMyfHa06ottxqDrlEm%2F1%2BdWu%2BmMyooR4s9Cjswg8nZHMrtMl8t01rUTaYxUyd%2B2PeFGVdwtZqlfdg08RqW2Vwa6twlMIDcjskGOqUBK%2BQ2jKHTXJZkDLglTjTE9LLNTL9mywUXdkloSH90%2BlCnRLASnNOxnYoO46wwbxCMMIxnLUnPdbGf5xaZP%2FZ89ER0MPYnLG6vOFXMdqqv9Cren9o3RwPcXeyQhln%2BUQpTpr46OAxO%2F5VdeKnXU472BrVIEcTkA9GcDMkoIegyjFWNO8QUF7chq0sxz8zd8HTc9C1O05N0IgG40KTLsyGtWqXPb%2Bac&X-Amz-Signature=d9aeff9a1ea7fae5d1230cbf75afc2df6b8dfc8e242efe403f87a8dd3a7cc7cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









