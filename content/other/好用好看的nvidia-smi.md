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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM4P4VPQ%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUkAMnP4YGHzdo0nKPVhW1Uyksk6EFbvBnMicjyr%2FfJAiAG15qQQC5uX8qbQU%2F3LuAwup5z45gkAEJB9R1YYRhnbSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjFhT0YMM8bjMLePCKtwDWMSVCjGyYT%2BqYk92CsNOu4KozZ4JkBAfTTPETXpX0nS9YTcGMwZqs25wnqeCxeTQUMADxbdl1x8pfmovu8gUihLf90F81WFU%2B2gBepa7bFDtOmy9%2BV0ny0IW5w1i33t27q%2Fhv9y7GNRCZa408KKm09KQhj94tgZY5DE5VWvOZAgvnEdyZKbnFS%2Fahqqau2aUR1nAwPvHw0yoHpQFal8HQ1LXQaPnmCA2p%2FvOwstE9Z1qI9FMej6tg7J2cVrSB4DSFOTs1H35YhWMdAN54W1360cZ1CV0HyqZdVxXcGQogxpMq%2F5AojuMv9IVmzoOnBdnCjPTIZaGzk7eFtcKzrn%2BkabQZyahV4%2FdeSIQs3NKwa3v1zSIChVlp1GM4yyvBBskkKkgoWtF5HCIBcSG51yzAB1%2BN748qzVcH0dUpxJzIEziNmk4eyPElgnNhJzRXWzwNKHsaRgdukUPqA6x8kjs%2BF0rLDLaACgvOrlaiOEeOICuEgNzTg%2BjoN0n2WwlP1HZ50%2FPCwKWGg2dvD%2BFJMYst2WM1u8dOlr%2Bzzn49Fc9xGN3ERjIl0c%2F3nrD5HlE401N1fRKGi1NqIuamzNl2DegST3TPCOhkk1fd2nKrlvCLp44De61kQmeylE5Ge0w%2F8vpzAY6pgGYsjT0nnViv3S8KxcAc4EnaMAaaR5KCRz4Fy6OeO%2BX0KPwWZO3KsCuSDrxnPduX6F%2BxkQURmFiN6YdUPRVRDn2bHpiEKMiywluISODQooOzDqsG7G8yKv4qLz4XqeVVbwgtuccfi2E92wKhk9DN8OSkfZvShgEDj255zfXIcgsofgZxl%2BXOZ0ezRlj%2BwTJR9XRIMNXRl%2BP5Bx2MotRUnSkq31xi4ME&X-Amz-Signature=fb2dd0145d225763096f465c5ab4a451b55008118c8034a0c371172e4b018866&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM4P4VPQ%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUkAMnP4YGHzdo0nKPVhW1Uyksk6EFbvBnMicjyr%2FfJAiAG15qQQC5uX8qbQU%2F3LuAwup5z45gkAEJB9R1YYRhnbSqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjFhT0YMM8bjMLePCKtwDWMSVCjGyYT%2BqYk92CsNOu4KozZ4JkBAfTTPETXpX0nS9YTcGMwZqs25wnqeCxeTQUMADxbdl1x8pfmovu8gUihLf90F81WFU%2B2gBepa7bFDtOmy9%2BV0ny0IW5w1i33t27q%2Fhv9y7GNRCZa408KKm09KQhj94tgZY5DE5VWvOZAgvnEdyZKbnFS%2Fahqqau2aUR1nAwPvHw0yoHpQFal8HQ1LXQaPnmCA2p%2FvOwstE9Z1qI9FMej6tg7J2cVrSB4DSFOTs1H35YhWMdAN54W1360cZ1CV0HyqZdVxXcGQogxpMq%2F5AojuMv9IVmzoOnBdnCjPTIZaGzk7eFtcKzrn%2BkabQZyahV4%2FdeSIQs3NKwa3v1zSIChVlp1GM4yyvBBskkKkgoWtF5HCIBcSG51yzAB1%2BN748qzVcH0dUpxJzIEziNmk4eyPElgnNhJzRXWzwNKHsaRgdukUPqA6x8kjs%2BF0rLDLaACgvOrlaiOEeOICuEgNzTg%2BjoN0n2WwlP1HZ50%2FPCwKWGg2dvD%2BFJMYst2WM1u8dOlr%2Bzzn49Fc9xGN3ERjIl0c%2F3nrD5HlE401N1fRKGi1NqIuamzNl2DegST3TPCOhkk1fd2nKrlvCLp44De61kQmeylE5Ge0w%2F8vpzAY6pgGYsjT0nnViv3S8KxcAc4EnaMAaaR5KCRz4Fy6OeO%2BX0KPwWZO3KsCuSDrxnPduX6F%2BxkQURmFiN6YdUPRVRDn2bHpiEKMiywluISODQooOzDqsG7G8yKv4qLz4XqeVVbwgtuccfi2E92wKhk9DN8OSkfZvShgEDj255zfXIcgsofgZxl%2BXOZ0ezRlj%2BwTJR9XRIMNXRl%2BP5Bx2MotRUnSkq31xi4ME&X-Amz-Signature=cadb540ebfc5d13ece79fc254608f9bb565422680232a6b92924b80a76d62bf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









