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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOOSRLFJ%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDsQ9WRZpRIJlExZ19ygYnqBKlq9i1QU5sV%2BrSmQkjN5gIhAO9qyP2fEjmzZhNp%2BP3LGMMOyC3WaCp8CwhTylG1fGIVKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeD9DX7lBUw0MQbxoq3AOPb4mDGjCUDXNix6foi7goHGkxIdTZZd%2Bmmtvjaf0CVrH5A813botGJw145%2Fisedg%2FIV78krIkv%2BJ2kuip%2Fjvej%2B%2BOyvIsMd4zP%2F%2BVpYe4JKacOXqN5qRgLVEVroro5aifKPiMoqw%2BBGvHdy4XFR6m9GRtHth4QlNfpDA9sEtu86VzhnkD9kROY5EWIt5LrTTzjGRiAIgib%2BZpSkQnfUppwtI1tzeJ6Jip3%2BZPwA3jh1ty5fsiEa1t89pdAtVSdmMUHBrbKxKYOeXZgnfn4Uzd2PsKZek8%2FjU3HcT1mPKMgXeLiNuuFDuxkervLKVIYKuMjxNJmRcSd8BLebyRagLI5ITe0pzjk7EWv899cZF0taz4x0HEqqf6maIfGPvs7gio4LR4RpoxlvROfu1vpI6ATD1A63qjL9rvO%2BWHb%2Fa9gtyqmxi%2FztVFg2xMl4zaAZWui5S9qCOKtkHx1Wda5AK79KTonUM1WRv3A%2BUrgb0nZFa2bWyKiobQ%2BTtPk6QJF9mlf2kQYiEDHTsnNyUxFlK0MMI%2BwW3WBEmOc99A6Wp5js8SY1QEpjCgcZY%2F5c4HOdGhLy5O9oy9D5Ng9WfxPRmS4fi5eQYMVgEmDLeQTgLqTFwbFJEnkga8n4G0xjDQt9zKBjqkAZidltqDA25jtHws27SyZTPkRdi4oAzFQxf62NJQuAtuG9M66nAsWniU594L0zDR%2FDiuzpeqCYHOa4TosDmVP%2BaPRokhi66lXviVhaDMxxWFhpiW%2BbQ2u5HdtvJkJMhdULsuSBT8%2FpnMrXB2B4w761yrpDOMJkoSkQTbYq47z8s5mLnKjF0VTcoj3246tiHZ3Is%2FBlfuo4bUZlQL4C0awt5fyhzH&X-Amz-Signature=3aebfc3a5f62ea585af94adfefb8eaf87c7fdbbee8171d9cd7f979a1e05576bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOOSRLFJ%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDsQ9WRZpRIJlExZ19ygYnqBKlq9i1QU5sV%2BrSmQkjN5gIhAO9qyP2fEjmzZhNp%2BP3LGMMOyC3WaCp8CwhTylG1fGIVKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzeD9DX7lBUw0MQbxoq3AOPb4mDGjCUDXNix6foi7goHGkxIdTZZd%2Bmmtvjaf0CVrH5A813botGJw145%2Fisedg%2FIV78krIkv%2BJ2kuip%2Fjvej%2B%2BOyvIsMd4zP%2F%2BVpYe4JKacOXqN5qRgLVEVroro5aifKPiMoqw%2BBGvHdy4XFR6m9GRtHth4QlNfpDA9sEtu86VzhnkD9kROY5EWIt5LrTTzjGRiAIgib%2BZpSkQnfUppwtI1tzeJ6Jip3%2BZPwA3jh1ty5fsiEa1t89pdAtVSdmMUHBrbKxKYOeXZgnfn4Uzd2PsKZek8%2FjU3HcT1mPKMgXeLiNuuFDuxkervLKVIYKuMjxNJmRcSd8BLebyRagLI5ITe0pzjk7EWv899cZF0taz4x0HEqqf6maIfGPvs7gio4LR4RpoxlvROfu1vpI6ATD1A63qjL9rvO%2BWHb%2Fa9gtyqmxi%2FztVFg2xMl4zaAZWui5S9qCOKtkHx1Wda5AK79KTonUM1WRv3A%2BUrgb0nZFa2bWyKiobQ%2BTtPk6QJF9mlf2kQYiEDHTsnNyUxFlK0MMI%2BwW3WBEmOc99A6Wp5js8SY1QEpjCgcZY%2F5c4HOdGhLy5O9oy9D5Ng9WfxPRmS4fi5eQYMVgEmDLeQTgLqTFwbFJEnkga8n4G0xjDQt9zKBjqkAZidltqDA25jtHws27SyZTPkRdi4oAzFQxf62NJQuAtuG9M66nAsWniU594L0zDR%2FDiuzpeqCYHOa4TosDmVP%2BaPRokhi66lXviVhaDMxxWFhpiW%2BbQ2u5HdtvJkJMhdULsuSBT8%2FpnMrXB2B4w761yrpDOMJkoSkQTbYq47z8s5mLnKjF0VTcoj3246tiHZ3Is%2FBlfuo4bUZlQL4C0awt5fyhzH&X-Amz-Signature=49b816f998b23480f80aabb6d433ee7d05f1f33c0c923290dd3c76a402ee7ceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









