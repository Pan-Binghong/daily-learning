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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSJKJNBW%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjmacaSwuS6iFchH%2BJHbWVAMx9jBP%2FlsODZgGkWX%2BE2AiEAuVPXXZzvOdGyIVHt7hRBgZKhmW%2B4T3RORXAQd%2Ft4v0UqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNo6zJ7ZScwOikJolSrcAzvw6nI2rdCiar7oytkZVUsOjChe9lStraaKzUrHcyPJ5ge4baG%2BnJpbWeKc9eNXrv2yZ0fDOS50CIspE0stus5VepAwSk%2BP%2BTxiycsTot6HGyNOFutALTtgzBL%2B%2FXUHspP2KpQ7TNDMyKh6nhOCN1dXB0%2F%2BulTXn3zypSPAgCfClY7S1hK%2BnoM8xpJoUNNGq4fVQEEHddclMlZocXiQYxKyrcOFyIjetwmSX3GbH82ADz83%2F0pOln8jEM2PjjSRAOMmmlM5y3Wkp60B3QSOCxx2Rjjx5gSUpLAw1IowE1rAitjYTAnpenV93eCnk9oKUmRK1llrHE5XB01mj2%2F9DRZHCPzBORIbsL55%2B4%2FoRaWd%2BiZEAlSDUB2eYXpNMd%2BRR3fnQjAkToFuFaEmZkgPX6sDemS6dhhEo9%2F5Tw0Va6ABPelLy5m1nLAIJft5kh8FfcOTYPMoFCbU7fTp04iAUKQb4dnU7LLPuNc3cw%2B6HqGfzSMlZlbTw%2BEO07sSMAGawpS4Dh9hCQ4axy2%2Bs1GjCHokRK0cHGnHBMiE%2B8Yte8kUChKdWGrvZhFUZ1lJclrPj%2FEqSXA%2F0GCmNC9F6v5I40LnBeuLNYDnTmmqeqQRrGbG4fstGWZhdausrTjiMIK95MwGOqUB%2FvMCSjwRKOfOcKhpO6STx4mPuYZgXfJjAtchlXjA%2FFOPVjT6mJltkdirIFPtBS9e6v%2BvSXaBbEMynzikZiItCk1gXYLrVhmScv4Bu3U12WWAo17mhdd73yYem7hz0Rc2FQfuCZDE3%2FnhflvR2NDiAfNFgzl%2B4PSCAbUW51Fsl4hCdLa0nUOVQtwCj0asiMK4lKVZdA70kvdc5XP3BPQFhOOAlAI7&X-Amz-Signature=2c0724ac07cbfb63fd1b1d80547c58a9a91316f29cb9a5eb91850c9f8927e62a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSJKJNBW%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjmacaSwuS6iFchH%2BJHbWVAMx9jBP%2FlsODZgGkWX%2BE2AiEAuVPXXZzvOdGyIVHt7hRBgZKhmW%2B4T3RORXAQd%2Ft4v0UqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNo6zJ7ZScwOikJolSrcAzvw6nI2rdCiar7oytkZVUsOjChe9lStraaKzUrHcyPJ5ge4baG%2BnJpbWeKc9eNXrv2yZ0fDOS50CIspE0stus5VepAwSk%2BP%2BTxiycsTot6HGyNOFutALTtgzBL%2B%2FXUHspP2KpQ7TNDMyKh6nhOCN1dXB0%2F%2BulTXn3zypSPAgCfClY7S1hK%2BnoM8xpJoUNNGq4fVQEEHddclMlZocXiQYxKyrcOFyIjetwmSX3GbH82ADz83%2F0pOln8jEM2PjjSRAOMmmlM5y3Wkp60B3QSOCxx2Rjjx5gSUpLAw1IowE1rAitjYTAnpenV93eCnk9oKUmRK1llrHE5XB01mj2%2F9DRZHCPzBORIbsL55%2B4%2FoRaWd%2BiZEAlSDUB2eYXpNMd%2BRR3fnQjAkToFuFaEmZkgPX6sDemS6dhhEo9%2F5Tw0Va6ABPelLy5m1nLAIJft5kh8FfcOTYPMoFCbU7fTp04iAUKQb4dnU7LLPuNc3cw%2B6HqGfzSMlZlbTw%2BEO07sSMAGawpS4Dh9hCQ4axy2%2Bs1GjCHokRK0cHGnHBMiE%2B8Yte8kUChKdWGrvZhFUZ1lJclrPj%2FEqSXA%2F0GCmNC9F6v5I40LnBeuLNYDnTmmqeqQRrGbG4fstGWZhdausrTjiMIK95MwGOqUB%2FvMCSjwRKOfOcKhpO6STx4mPuYZgXfJjAtchlXjA%2FFOPVjT6mJltkdirIFPtBS9e6v%2BvSXaBbEMynzikZiItCk1gXYLrVhmScv4Bu3U12WWAo17mhdd73yYem7hz0Rc2FQfuCZDE3%2FnhflvR2NDiAfNFgzl%2B4PSCAbUW51Fsl4hCdLa0nUOVQtwCj0asiMK4lKVZdA70kvdc5XP3BPQFhOOAlAI7&X-Amz-Signature=0817c0a9037db06ce763b833034a6cf5b1c1934f2e682bb84caabc80c29fabda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









