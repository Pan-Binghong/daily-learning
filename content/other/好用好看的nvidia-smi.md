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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIH7TXIC%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEnLtSuM%2FHL4LafHgo7uM8Dd2vye4YUo%2F01iXmrO4lw2AiBJwX5%2FTlBYi0FH9yw93elCofuFys%2FOe3ULy3Sf6gjUKSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGbjYG6qUVc7N9POZKtwD99docDLxJsjdXAxr8GoLIKnUfHlrgf0yWl%2FKY4IibQsVeD7%2BwIicTf9SkesKFZIS%2F7oP9qSxxMV5bFyvZQAOHomedi9OLAe35F9C9WLWs%2FQuaKgostq6lR0Lo8rej4ID%2B%2BQFFJ9HizQ7EjNMPOSudTYWrxWhHVfnAJsZ%2FfuttaT99FW3FBGhhx1hyzzUt1UeuYqi1CtvEmcaVEN2pSZz9rxWc73vA9xCzdZsqTAcfOoMhwumrJJ8EY8rrDl3KFOTOlu%2ByQtnOHhdEdmwl6gSxQzU6Vll40pYq%2BoZyR7wG67Y0UuyWIpuY%2Btf5QC0sN%2Fuidr92uACBJppybAPGJcxtXxCgQ6iGGEVmaG3hLFC2ej858ED8BOPqGM64%2B7dUITyZTwutCN2syZBevaxv%2B9hvU%2BK82nkNubu2aixAZ09CqX0FzAwtjkxnBbpyx%2Fy0tgod7m0A4ndm4w%2F7HCX6wJvIZYrTVT1InZef5SxZKuxEzyFvTB2S86mHZQmIHp5VJDqIpItFq9rtORWGVcx7UfydXgGqiuA1aEB%2BL%2FwU%2FkFQ8MtBLt4r6k8aMYpyKBKO%2Bp3f406qixdwpS2XsJ%2F8plvFHidfaWcxmL3bUTw6jHsFq26ehKGJ4ni1p%2BYtZYwrbe%2FyAY6pgFyfFFK4PLPbQP9kIoWja0%2Fjmzk2AjZhHceyUadCyrE%2FNjw3V5ujgpZWn4gfcrN%2F0BkoXxAmXMHmNQoTWHFK9IjCdS%2BlFx%2BQWXa%2BcSGwASzvD3cw7HRR3sdGFvhMFsSEphkq3DOjtKO%2FLBUZ0jmUyXlXq1z47%2BqVgt1p0%2BUzta8bkAt4qZAUT4U9gZFKDsW%2BWvMhxD6F6iUBkbZK36AA3X8dE01iozs&X-Amz-Signature=c85d544cac8370fe3051532bda7e8e0cc804c827cf6f680251945c1c20949355&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIH7TXIC%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEnLtSuM%2FHL4LafHgo7uM8Dd2vye4YUo%2F01iXmrO4lw2AiBJwX5%2FTlBYi0FH9yw93elCofuFys%2FOe3ULy3Sf6gjUKSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGbjYG6qUVc7N9POZKtwD99docDLxJsjdXAxr8GoLIKnUfHlrgf0yWl%2FKY4IibQsVeD7%2BwIicTf9SkesKFZIS%2F7oP9qSxxMV5bFyvZQAOHomedi9OLAe35F9C9WLWs%2FQuaKgostq6lR0Lo8rej4ID%2B%2BQFFJ9HizQ7EjNMPOSudTYWrxWhHVfnAJsZ%2FfuttaT99FW3FBGhhx1hyzzUt1UeuYqi1CtvEmcaVEN2pSZz9rxWc73vA9xCzdZsqTAcfOoMhwumrJJ8EY8rrDl3KFOTOlu%2ByQtnOHhdEdmwl6gSxQzU6Vll40pYq%2BoZyR7wG67Y0UuyWIpuY%2Btf5QC0sN%2Fuidr92uACBJppybAPGJcxtXxCgQ6iGGEVmaG3hLFC2ej858ED8BOPqGM64%2B7dUITyZTwutCN2syZBevaxv%2B9hvU%2BK82nkNubu2aixAZ09CqX0FzAwtjkxnBbpyx%2Fy0tgod7m0A4ndm4w%2F7HCX6wJvIZYrTVT1InZef5SxZKuxEzyFvTB2S86mHZQmIHp5VJDqIpItFq9rtORWGVcx7UfydXgGqiuA1aEB%2BL%2FwU%2FkFQ8MtBLt4r6k8aMYpyKBKO%2Bp3f406qixdwpS2XsJ%2F8plvFHidfaWcxmL3bUTw6jHsFq26ehKGJ4ni1p%2BYtZYwrbe%2FyAY6pgFyfFFK4PLPbQP9kIoWja0%2Fjmzk2AjZhHceyUadCyrE%2FNjw3V5ujgpZWn4gfcrN%2F0BkoXxAmXMHmNQoTWHFK9IjCdS%2BlFx%2BQWXa%2BcSGwASzvD3cw7HRR3sdGFvhMFsSEphkq3DOjtKO%2FLBUZ0jmUyXlXq1z47%2BqVgt1p0%2BUzta8bkAt4qZAUT4U9gZFKDsW%2BWvMhxD6F6iUBkbZK36AA3X8dE01iozs&X-Amz-Signature=9eed026e9f820e2a35a44be4dd168f9300c06651525ebdf1d42defd6234010b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









