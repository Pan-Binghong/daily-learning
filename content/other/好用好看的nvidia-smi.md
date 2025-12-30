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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMKZFZET%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyn8y2Sx2gq%2B23BoFLZv3FdOlyrPxIANP7iKqpDWs8FAiEAjJpZZ%2BwKDGdDLSr1cww4EjTp7CBfvLQMa2gFug1rPW0qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9WDr%2B8lRV1MzUp9CrcA9Gn8iRVPqcfSGKHnhm5KhhqtXJgbm6rrHvkM6WRaIHBoVMDIMQ3Y0lwD8amYOWuDF1W2ek2NsSSFjGtz%2B%2F%2FNpzpwl2dQSViQSjCOAhu2eziFsTy41AQDv4GYV0Fy9iWq%2FPNxNRvIaDP%2BRWgILD26Bntfv7RTAavXvvfQo%2FBWUYaCy64UniUjORomdryGHi6kMfHgs%2B5buL9BjRyn2I%2BEo9U4IQpgpYxi6PsMUmy6uFj%2FZrSgm1pLHOK%2Fnu9hBBAx9IALJyrEc%2BA6RVzIo%2FPGxnYles30qcP%2BRRDDOITEHuF1F4ZQWj%2FMe0T6prUg%2FtDTxhEZg1QHqioNP5BVvJC3hS%2BfAI3u%2FHZm79%2FFqoqkmPmqDqHaAOeOWd5sTi6AhCG2%2FqO5Pauz4Ah0ste5Y9%2BfuzUK3u2LqoIhT6iRBWRPE2ng7hWIttLyNhCDtx3F36JwqTn4OZb6oFvKMc0U4x3%2Fya70732AFgtFKslJzzM14jQvtzopMkS%2Bm%2BFGvFCaqJJJ2EF55F77ty1ib3UZ9n02hd3%2FtnvcPYdHFc0h%2FeHEuAZ3hnnx5aYPwGtlYPOomMOWcZ0Cq7e7wAZ8WPOEahqW%2FckHg2m3PB5CSTTNGNzdbYD4T%2Fyn6lpmCcKt29MMJ7ZzMoGOqUB%2FtvkZPQ69IlY%2BSO1hfPaxcHh2DySKGyODHcQms1FTv5tfOvLnRj48AnvJ7JTtMngkANatGUc7Ie9YKfAbSVGXiRPoRlufCCvD3I5wl2m9oBVULaHXtx2DgUcFFK%2BkGvofOdhrv19%2FdW0xMR7F2vw64sMpbgRoQzutMnXKpX6YudOJFvcXGAf%2FyIXNkoaHZ7lk%2Bhy0aQ1%2FLWqu6CLEEq1t0pR%2BdFn&X-Amz-Signature=2205747f3214d22135b05b317b5c1339bebe441fc19d4e2892b142e8f0cc2704&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMKZFZET%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAyn8y2Sx2gq%2B23BoFLZv3FdOlyrPxIANP7iKqpDWs8FAiEAjJpZZ%2BwKDGdDLSr1cww4EjTp7CBfvLQMa2gFug1rPW0qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9WDr%2B8lRV1MzUp9CrcA9Gn8iRVPqcfSGKHnhm5KhhqtXJgbm6rrHvkM6WRaIHBoVMDIMQ3Y0lwD8amYOWuDF1W2ek2NsSSFjGtz%2B%2F%2FNpzpwl2dQSViQSjCOAhu2eziFsTy41AQDv4GYV0Fy9iWq%2FPNxNRvIaDP%2BRWgILD26Bntfv7RTAavXvvfQo%2FBWUYaCy64UniUjORomdryGHi6kMfHgs%2B5buL9BjRyn2I%2BEo9U4IQpgpYxi6PsMUmy6uFj%2FZrSgm1pLHOK%2Fnu9hBBAx9IALJyrEc%2BA6RVzIo%2FPGxnYles30qcP%2BRRDDOITEHuF1F4ZQWj%2FMe0T6prUg%2FtDTxhEZg1QHqioNP5BVvJC3hS%2BfAI3u%2FHZm79%2FFqoqkmPmqDqHaAOeOWd5sTi6AhCG2%2FqO5Pauz4Ah0ste5Y9%2BfuzUK3u2LqoIhT6iRBWRPE2ng7hWIttLyNhCDtx3F36JwqTn4OZb6oFvKMc0U4x3%2Fya70732AFgtFKslJzzM14jQvtzopMkS%2Bm%2BFGvFCaqJJJ2EF55F77ty1ib3UZ9n02hd3%2FtnvcPYdHFc0h%2FeHEuAZ3hnnx5aYPwGtlYPOomMOWcZ0Cq7e7wAZ8WPOEahqW%2FckHg2m3PB5CSTTNGNzdbYD4T%2Fyn6lpmCcKt29MMJ7ZzMoGOqUB%2FtvkZPQ69IlY%2BSO1hfPaxcHh2DySKGyODHcQms1FTv5tfOvLnRj48AnvJ7JTtMngkANatGUc7Ie9YKfAbSVGXiRPoRlufCCvD3I5wl2m9oBVULaHXtx2DgUcFFK%2BkGvofOdhrv19%2FdW0xMR7F2vw64sMpbgRoQzutMnXKpX6YudOJFvcXGAf%2FyIXNkoaHZ7lk%2Bhy0aQ1%2FLWqu6CLEEq1t0pR%2BdFn&X-Amz-Signature=346be8f8a789fc30ec7a563b822e60361e580116358918cd02c5762b32defc99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









