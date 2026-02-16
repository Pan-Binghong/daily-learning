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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YS235ND%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIE5i1ZIGHHGYDVJDNwCRZSN4DzlGLJauTdETcfdst7nPAiEA0Obsn8jD6DMFmp1QQ3nKgKD0LWMtdH%2BA%2Bbaor13yyxwq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDG6QXeTO0Gy30wofpSrcA6XeDfRrweHYNXSmVKPBZifBWZRxhz82q9IfZpf0ThPz9upnPC8RsKNCTz9y079HK3rUwT9ly%2F14hR%2BBna6bi5NbNXEkplt%2BPFoKGGpVVYyqqb6l2ZComcZiPZvyPgCwRUaMWFq31rl22LzEcgjoDHVJgyfYjil68AvwkoGapsvtvryYuUqgO6GTJlJozS9WTEoonPMgssMnKV%2BjdNBF5JlgEFzqMPfFE88qmfljbtWHA%2BOVib89wuCpF0Zskf48JpPmOnYHPoJ8ULVCSf3e%2Fle99KS1ZaeqAETAzSZVoiATC1xcVrYCw8swcJNG0yrUJr0qW14gXQgrOZxCHyjkFBqCKozpMYXxSdzemYHwtIXAakBmrlXEBcHBHCVe8%2FtOX%2BokkRrKFP9wdh4%2BwxlQxVGRpkRDzQzn7dlzsao319QBEFKBCxMe6qwjJINfM37ReSY8jOjHZtMZ%2B%2BwU7urdAYJtoMveF8X3A0UpljmX9GiPb9TxSNLN7FtMl9ZUGFrxGSWE0vN5kbMI7cqowl637H5wIHwILZX30MPGju%2B5AVloZ5dpU4QaJHWCk4U2HkmP48D%2Flhh3T35HJZqZMxekw7QebSFkL%2FuR70DFXFhMTsADpruJp4rzBYGrx9ISMKOUyswGOqUB8occBqKB2gyj3SL3D%2FD84TJYVnPuFps7MRMfTQct7aHmcc0KRMRC9nB2qFzhy47OivVm5BtM6ed3E810OVSwHErcvJWNrhExVCg8lQ7L%2FcVeGkgH667e381fQGlY3uWh1fB%2FqdqB%2BPZMDyD%2FuZsNF%2FF%2B7W9ewR5kKvTxRw8P4QrZnFmGucfRWcotkMtKTH2pKsbxgj3T6CvHq23zPkJ39936vmG6&X-Amz-Signature=ebd01b2545d4f1f9d2a7d36b5c2f0b807e204bfb389176d88533b59792b488bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YS235ND%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIE5i1ZIGHHGYDVJDNwCRZSN4DzlGLJauTdETcfdst7nPAiEA0Obsn8jD6DMFmp1QQ3nKgKD0LWMtdH%2BA%2Bbaor13yyxwq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDG6QXeTO0Gy30wofpSrcA6XeDfRrweHYNXSmVKPBZifBWZRxhz82q9IfZpf0ThPz9upnPC8RsKNCTz9y079HK3rUwT9ly%2F14hR%2BBna6bi5NbNXEkplt%2BPFoKGGpVVYyqqb6l2ZComcZiPZvyPgCwRUaMWFq31rl22LzEcgjoDHVJgyfYjil68AvwkoGapsvtvryYuUqgO6GTJlJozS9WTEoonPMgssMnKV%2BjdNBF5JlgEFzqMPfFE88qmfljbtWHA%2BOVib89wuCpF0Zskf48JpPmOnYHPoJ8ULVCSf3e%2Fle99KS1ZaeqAETAzSZVoiATC1xcVrYCw8swcJNG0yrUJr0qW14gXQgrOZxCHyjkFBqCKozpMYXxSdzemYHwtIXAakBmrlXEBcHBHCVe8%2FtOX%2BokkRrKFP9wdh4%2BwxlQxVGRpkRDzQzn7dlzsao319QBEFKBCxMe6qwjJINfM37ReSY8jOjHZtMZ%2B%2BwU7urdAYJtoMveF8X3A0UpljmX9GiPb9TxSNLN7FtMl9ZUGFrxGSWE0vN5kbMI7cqowl637H5wIHwILZX30MPGju%2B5AVloZ5dpU4QaJHWCk4U2HkmP48D%2Flhh3T35HJZqZMxekw7QebSFkL%2FuR70DFXFhMTsADpruJp4rzBYGrx9ISMKOUyswGOqUB8occBqKB2gyj3SL3D%2FD84TJYVnPuFps7MRMfTQct7aHmcc0KRMRC9nB2qFzhy47OivVm5BtM6ed3E810OVSwHErcvJWNrhExVCg8lQ7L%2FcVeGkgH667e381fQGlY3uWh1fB%2FqdqB%2BPZMDyD%2FuZsNF%2FF%2B7W9ewR5kKvTxRw8P4QrZnFmGucfRWcotkMtKTH2pKsbxgj3T6CvHq23zPkJ39936vmG6&X-Amz-Signature=997ffc597714ec088b2039bf9d1c4b0bbcd5dfb8ea98b1dbb7f7bcf264c28544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









