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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7MIFH7P%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaoaCiN%2FJ85%2FqvldS7Qgvg%2Fy4m1S17FOLzV4oangZfcAiEAzv2qaTH8fnY%2FhK9wtHd%2BuEOgAjKYFLbECjKh%2Fo1x70Iq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDCnqBHNYB4LaHx%2FlGyrcA4OaraOHuUdF3MykBASLGqRLWTp1L1CNhdmImiYFcVOXyaSTJ%2BQB1GKazZlKWT%2FfpZ8f474EgzFpz7mx%2FTQ0UEFel90fMUujC524656FBpRlBaXViHs9%2BA2tdr3wdTHlfBhga5DWEqJyWmQ9haZl1tXYyjubqRbpoSRb8nb7a1bUd46YdLYVdTtXJzD3NXtyxRyAmRvwzI7APpKcVdu%2BzAZuTYjPSNRtk6Z4seFYlATEjurpy9kMoIJMFsVxG9FahOPnIm8wmxUAFiFg4VwLezga86eyCmHBRgsr7%2BNU3jFTkotkV4gy88392s9fJG%2FbX5KA8SBJBCbQkLFgOp8U8WiE3xM0PmXJr27YqT%2FBWJuXynv3oxcdtuJJAaSiVlJ8A1LfuViJcsaia4N1tFxt7UjqP8odY1fh30siWQbzuYUU2Lk9LC7RyflNdY5QfjB4Rtul7Keg9NPiF%2BPljBx7QAacRgC2te3ztHWYV5QMjGZ7kZD8OeNZPgqpL8%2B0RFgr4iUGutsW7g2eeqdgAXYeQouI3PO9pHr5ODM5Jwi5qQ20Fn6iZ0X5u%2FlFzvFBdqz%2BDtNOoNY9D2pNqQRc6ZrUqp%2F%2BCtztrRFjZiZnSRvTkhaAErKqVyB9fzhcq3GnMOnjwcoGOqUBVO62IYPjmIU559gEr1KffsxzQktIxBMNigEmMTRoGedNns8d2TBtZZxGIDVp%2FchL2zlk%2Bzx5MuQtrIrHyE470ecsbl3t3TADtmeAQYaHdZGfbSCYdoO7%2FffbhUuP0HCyoKnUslFBU8Tz%2FEKlETzyrtpH5SVNyRwERRb9gBhKmSmOXBe6z45Rq9n%2Bk8FvnNTSl1pS9LG1QTOiPn95%2Fc78U0KOaqjJ&X-Amz-Signature=c9fd7cb9f5821a2356893b92b5c0b2134207c6cca71fc5596cd8ba41fe30848a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7MIFH7P%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaoaCiN%2FJ85%2FqvldS7Qgvg%2Fy4m1S17FOLzV4oangZfcAiEAzv2qaTH8fnY%2FhK9wtHd%2BuEOgAjKYFLbECjKh%2Fo1x70Iq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDCnqBHNYB4LaHx%2FlGyrcA4OaraOHuUdF3MykBASLGqRLWTp1L1CNhdmImiYFcVOXyaSTJ%2BQB1GKazZlKWT%2FfpZ8f474EgzFpz7mx%2FTQ0UEFel90fMUujC524656FBpRlBaXViHs9%2BA2tdr3wdTHlfBhga5DWEqJyWmQ9haZl1tXYyjubqRbpoSRb8nb7a1bUd46YdLYVdTtXJzD3NXtyxRyAmRvwzI7APpKcVdu%2BzAZuTYjPSNRtk6Z4seFYlATEjurpy9kMoIJMFsVxG9FahOPnIm8wmxUAFiFg4VwLezga86eyCmHBRgsr7%2BNU3jFTkotkV4gy88392s9fJG%2FbX5KA8SBJBCbQkLFgOp8U8WiE3xM0PmXJr27YqT%2FBWJuXynv3oxcdtuJJAaSiVlJ8A1LfuViJcsaia4N1tFxt7UjqP8odY1fh30siWQbzuYUU2Lk9LC7RyflNdY5QfjB4Rtul7Keg9NPiF%2BPljBx7QAacRgC2te3ztHWYV5QMjGZ7kZD8OeNZPgqpL8%2B0RFgr4iUGutsW7g2eeqdgAXYeQouI3PO9pHr5ODM5Jwi5qQ20Fn6iZ0X5u%2FlFzvFBdqz%2BDtNOoNY9D2pNqQRc6ZrUqp%2F%2BCtztrRFjZiZnSRvTkhaAErKqVyB9fzhcq3GnMOnjwcoGOqUBVO62IYPjmIU559gEr1KffsxzQktIxBMNigEmMTRoGedNns8d2TBtZZxGIDVp%2FchL2zlk%2Bzx5MuQtrIrHyE470ecsbl3t3TADtmeAQYaHdZGfbSCYdoO7%2FffbhUuP0HCyoKnUslFBU8Tz%2FEKlETzyrtpH5SVNyRwERRb9gBhKmSmOXBe6z45Rq9n%2Bk8FvnNTSl1pS9LG1QTOiPn95%2Fc78U0KOaqjJ&X-Amz-Signature=ad9cb10cf55caa297799eac02731584f7ae5aac6a78a20517da8be3e64f23b56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









