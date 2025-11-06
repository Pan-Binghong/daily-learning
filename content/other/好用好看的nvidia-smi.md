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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWMZMXWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVj4YaT5yIxkYMk0hqWLx%2Bvhw%2BsSpnIYh1yhWoKJliAAiBTia3oVmChiOpSTuG0l5nt%2FVFxl1sLCtGCMEdP%2B%2FAR1CqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxTDwqdn3wvZwY23MKtwDjj%2FDXNQbJFzRT8s4o4x72lcLvHZcMH3gl777S9jJLy2IrgxSzxwwM4luCL7ix8XWVS9cLx2g1G%2FhX%2Fm6CvNrnQD64IOxa1hBFTJqQDxYMhNvnzOZ8pZH0idmhd2SaLycwkWh3jmL5VKLp7WPVTSuBHZOeW5mazqRPmGvVfVSzCJuLbyyxW0TRi%2B1MIM%2FK9alAFiwg85VyZGn0%2FOky6bwWn79Z6hAiwhBVy8yZbN4ehrozZlPDfi1curAhNCM%2FfMMEwvDq98Bw1lsr%2B3QDw55i8UtOLluVneC4zMdNdQtEnpZkXMyPwn9HgVNZ6iJis4v7MDvt5BgfWmJD516GC3DELABv5GRA3ugisOfwdHX23dth4kVNr2D9WQGJziPXIXPUYZoZ7dSyRtINWDus8IP8t2DbYu7g%2BNNpN2FeizqPJxjIDc9gdTx%2BAOD1pcR9MLRGOYc%2BBHJNrVhPI7KMjJculbkytIG8ukmQSZJSsXBP0QfwnVqZZVrPIWyCxcJfVBv5I3%2FWUGNXYpYrj%2FQXzpXV49HqUQfoFyGWhpOevZL%2FkZb9rjMjAJJzZQuV5tLmClywm8Agt%2Blycg%2FL2j7TrePNMD4PFPvXX9BZonyXvE5bV4BYH6n8C0nbPH5zM8w7vGvyAY6pgHLRe3YFBdj1ATHU7onjFlxtkO7fDxJpiKo8YZHSjk1%2FOv6u7g%2By28F8IhI3%2BruYuft12zNvxHTC0VPfFtt30AU1hdqQzVQiYMRV7ylahYvRYIQ%2FjBuZoBDu77sdUEuVaTXvIMfNrxLLXmhUvKDpwfp%2BCkKkoBNv4xIA5ApQ6EzuNMvtLuHKO%2BPMGUZ1pN6qFXxgy5HbOwkb6sZ3zfnPFTxQiBDde2J&X-Amz-Signature=3f3d78af60ab05894c6d158b11e8bb4790d8fc40c3392b6074f6b16b85a4818b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWMZMXWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVj4YaT5yIxkYMk0hqWLx%2Bvhw%2BsSpnIYh1yhWoKJliAAiBTia3oVmChiOpSTuG0l5nt%2FVFxl1sLCtGCMEdP%2B%2FAR1CqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxTDwqdn3wvZwY23MKtwDjj%2FDXNQbJFzRT8s4o4x72lcLvHZcMH3gl777S9jJLy2IrgxSzxwwM4luCL7ix8XWVS9cLx2g1G%2FhX%2Fm6CvNrnQD64IOxa1hBFTJqQDxYMhNvnzOZ8pZH0idmhd2SaLycwkWh3jmL5VKLp7WPVTSuBHZOeW5mazqRPmGvVfVSzCJuLbyyxW0TRi%2B1MIM%2FK9alAFiwg85VyZGn0%2FOky6bwWn79Z6hAiwhBVy8yZbN4ehrozZlPDfi1curAhNCM%2FfMMEwvDq98Bw1lsr%2B3QDw55i8UtOLluVneC4zMdNdQtEnpZkXMyPwn9HgVNZ6iJis4v7MDvt5BgfWmJD516GC3DELABv5GRA3ugisOfwdHX23dth4kVNr2D9WQGJziPXIXPUYZoZ7dSyRtINWDus8IP8t2DbYu7g%2BNNpN2FeizqPJxjIDc9gdTx%2BAOD1pcR9MLRGOYc%2BBHJNrVhPI7KMjJculbkytIG8ukmQSZJSsXBP0QfwnVqZZVrPIWyCxcJfVBv5I3%2FWUGNXYpYrj%2FQXzpXV49HqUQfoFyGWhpOevZL%2FkZb9rjMjAJJzZQuV5tLmClywm8Agt%2Blycg%2FL2j7TrePNMD4PFPvXX9BZonyXvE5bV4BYH6n8C0nbPH5zM8w7vGvyAY6pgHLRe3YFBdj1ATHU7onjFlxtkO7fDxJpiKo8YZHSjk1%2FOv6u7g%2By28F8IhI3%2BruYuft12zNvxHTC0VPfFtt30AU1hdqQzVQiYMRV7ylahYvRYIQ%2FjBuZoBDu77sdUEuVaTXvIMfNrxLLXmhUvKDpwfp%2BCkKkoBNv4xIA5ApQ6EzuNMvtLuHKO%2BPMGUZ1pN6qFXxgy5HbOwkb6sZ3zfnPFTxQiBDde2J&X-Amz-Signature=8cc4871633fc8a472bd707f797e157215f6dbbccf325bc2d8c7720a4935f317e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









