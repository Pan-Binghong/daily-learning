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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WC2ZWGI%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIELLTGYYD1aB%2F4q457%2F0DcCDXxVss3FEE76Sl5HZ8Mr0AiEAuhxCP3LEr1le0s7s8EzOHrrBJKekMB2VyDZm%2FZRRtucq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDA2p06RDcRrz0kC8gCrcA%2F68WGR0byQE7AH5Wx8GfGVFgbI3mpYwHTBXT1MJedEdFe1hxCuSbsaCyzNZC9oiaWHMB1VQGS4w2Ihn8X9aDXZHrCHagbEIiy9yiT55djK%2BCzxUjwovE5lTQm17qQCko6%2FcIwgTlbsdhN1VguUNO6SaceCPobfuTVN1%2BMVzPftn%2FIA5UCSu44gTMOfkSI%2FEFZTIoOtntEKVrssmB8vzkbcLst%2BJpNpkr7zkyNxGAyTvRZIvtvNesgoNvHkGeSBT0w%2F5fdEFyRAbVC4kbpy4%2FFvPGB%2F6gR5xFvn%2Bd5mUOI5GYo7PD5nanG8EEna61w%2F%2BF2Ku07XoTCAW7kxdjibJRW1r7Cv7C5AnTjuQfDBrPivcX%2BCQgYF7OzcMLb6FZIJJPVlvg70VSjq55stkDTfdx9h7lzgm0NceYiamDOFv0CwdhdhMtGrmalw0gCqwaUECPu24b6pMETh%2FalQ3ZJOW3CxBMKZg3WS1mejYyadIWlyd%2FzYv0ZkGX9MRdtYOnMeAWSINDQMujhNve%2B0SkNvS%2FSt2fT5M0pRFEg%2B3ULILbq61ajcq7yuxo9GPYD%2FGx3AErq4pWJ%2FSlL9%2Ffq7QYavEZxmafUSic4rfKHSnf5lP31ZLEM%2FLqQwPkS0hTxKnMKGMyMkGOqUBupVC0RM9EKdCxAzcThowMGhsqM0n3qZ1R10LZel9gkOjxI3YRWevsoYrc%2FiWhGiTSYdLQue7xIthPmUEkRY%2BDnZiSZHJ2W0S%2BLEZ6QPXnD1l2Xb4NlZRGED%2Bf8WWpngYbtk0EG4UX4tZe%2Bwp5J7i7vQoP8oKFG1iF8SE%2BopO8vGlRgzotR3F7R125x67tryyfBCqI0ynVAZEOZOVzMrJwXVrd1md&X-Amz-Signature=04ec0c757d26f01f4ddeaf8c9bc0f5afdd86c3ae5579b36b3f03905c874c4fd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WC2ZWGI%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIELLTGYYD1aB%2F4q457%2F0DcCDXxVss3FEE76Sl5HZ8Mr0AiEAuhxCP3LEr1le0s7s8EzOHrrBJKekMB2VyDZm%2FZRRtucq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDA2p06RDcRrz0kC8gCrcA%2F68WGR0byQE7AH5Wx8GfGVFgbI3mpYwHTBXT1MJedEdFe1hxCuSbsaCyzNZC9oiaWHMB1VQGS4w2Ihn8X9aDXZHrCHagbEIiy9yiT55djK%2BCzxUjwovE5lTQm17qQCko6%2FcIwgTlbsdhN1VguUNO6SaceCPobfuTVN1%2BMVzPftn%2FIA5UCSu44gTMOfkSI%2FEFZTIoOtntEKVrssmB8vzkbcLst%2BJpNpkr7zkyNxGAyTvRZIvtvNesgoNvHkGeSBT0w%2F5fdEFyRAbVC4kbpy4%2FFvPGB%2F6gR5xFvn%2Bd5mUOI5GYo7PD5nanG8EEna61w%2F%2BF2Ku07XoTCAW7kxdjibJRW1r7Cv7C5AnTjuQfDBrPivcX%2BCQgYF7OzcMLb6FZIJJPVlvg70VSjq55stkDTfdx9h7lzgm0NceYiamDOFv0CwdhdhMtGrmalw0gCqwaUECPu24b6pMETh%2FalQ3ZJOW3CxBMKZg3WS1mejYyadIWlyd%2FzYv0ZkGX9MRdtYOnMeAWSINDQMujhNve%2B0SkNvS%2FSt2fT5M0pRFEg%2B3ULILbq61ajcq7yuxo9GPYD%2FGx3AErq4pWJ%2FSlL9%2Ffq7QYavEZxmafUSic4rfKHSnf5lP31ZLEM%2FLqQwPkS0hTxKnMKGMyMkGOqUBupVC0RM9EKdCxAzcThowMGhsqM0n3qZ1R10LZel9gkOjxI3YRWevsoYrc%2FiWhGiTSYdLQue7xIthPmUEkRY%2BDnZiSZHJ2W0S%2BLEZ6QPXnD1l2Xb4NlZRGED%2Bf8WWpngYbtk0EG4UX4tZe%2Bwp5J7i7vQoP8oKFG1iF8SE%2BopO8vGlRgzotR3F7R125x67tryyfBCqI0ynVAZEOZOVzMrJwXVrd1md&X-Amz-Signature=b60c79c5d606e5d2d2992724eca75a40aa48262901e4f0f65894101124899527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









