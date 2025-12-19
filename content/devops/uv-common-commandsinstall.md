---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSKUSC4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqloiTAhC%2FExdCBMCqgCH8aPANQrE8HQETUOJXzzuCWwIgEXkZDFg7LQKcezos9G6TX43y2d8Xt5lkEzD83YmHgvAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTsYsWqbOqMgOdRyircA4JS1MjB1Br34LHw9sjdAJFvNxkjrBFVYJFDTlx2SGzvXCJtWp3%2ByczWruk%2BHwgEW%2BTGeicI0rLqCcJdFHbeu%2BMi31XIX%2B%2F59UYrfR%2B9bkI%2F3OmGw7BTatOYZaQAMj3QaQ1uNpdTFXDH7qC6lvJ8tuSmnVhvBjdgYHnSWO1ipDN2Jrrqfdw6%2FEQYWDTqnWLlHuyWb8VH8KmFp8x8uD5SCkbZ1isKcR82GhfdapwIadiRgyAN24XW9o2bpA28tFIdwsHnE6Obi84edKcFTbsjY%2BFVEeivcna6n1gBGpyrnF9HczNoQo6%2FmNcIaIiO7yg%2BFHeQHyd7asxdX9DR1rhehVy763Dm6NAWTatsc5tI4Qu6p3VWKuTlRFCcqMlMMzxA67FLCFwOBl4U%2B6ephVvA4IfAUlvcu8LdRhg65rXG0iA7AbYOhu5TcV1LB5eYFREWDUzUtX%2F0XM0%2Bjb8L0jrBqwHRWgz1hbPWvol9v7WL87u%2BptQSc%2Ffwh9qhpdGwQl80VqiIbYbZriVzP7mbUwzvU7iRA0DLg62XWFq0GPI9X8HBiGWZ%2FzxZ%2FfAH8hy1ziWxzXrAyBYG9xKJLiaYl2fB26XmfSUKT%2Fc04GDf%2Bwfe8XWbVtbixFcLLl2OR0xhMLnhksoGOqUBMBzwcgVltGWsQ8vaInECcG4Qlp2nty54zphrCSTLEdrEBRxPeRo3tcvv85GBa6pPaq6OmZGpZ57R9dZKqjSMsV0%2BuMvtvdT0nqWuEoaUk2sfeBb7YxW7J4rnBE%2FQfabiNXptWQgzlNsAuQy%2BXg5Fz2nAdPoJrqpuY0vFno4Ugb3btNVGsK3rvsAWCyJ4RIs9C0laYio8VwCJzHY8ncCebJ8f6dMb&X-Amz-Signature=c8ee07eeae43d8e0186ec4d6b7595f8f98df0539e692e5d9327c0568e6d12a4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSKUSC4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqloiTAhC%2FExdCBMCqgCH8aPANQrE8HQETUOJXzzuCWwIgEXkZDFg7LQKcezos9G6TX43y2d8Xt5lkEzD83YmHgvAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTsYsWqbOqMgOdRyircA4JS1MjB1Br34LHw9sjdAJFvNxkjrBFVYJFDTlx2SGzvXCJtWp3%2ByczWruk%2BHwgEW%2BTGeicI0rLqCcJdFHbeu%2BMi31XIX%2B%2F59UYrfR%2B9bkI%2F3OmGw7BTatOYZaQAMj3QaQ1uNpdTFXDH7qC6lvJ8tuSmnVhvBjdgYHnSWO1ipDN2Jrrqfdw6%2FEQYWDTqnWLlHuyWb8VH8KmFp8x8uD5SCkbZ1isKcR82GhfdapwIadiRgyAN24XW9o2bpA28tFIdwsHnE6Obi84edKcFTbsjY%2BFVEeivcna6n1gBGpyrnF9HczNoQo6%2FmNcIaIiO7yg%2BFHeQHyd7asxdX9DR1rhehVy763Dm6NAWTatsc5tI4Qu6p3VWKuTlRFCcqMlMMzxA67FLCFwOBl4U%2B6ephVvA4IfAUlvcu8LdRhg65rXG0iA7AbYOhu5TcV1LB5eYFREWDUzUtX%2F0XM0%2Bjb8L0jrBqwHRWgz1hbPWvol9v7WL87u%2BptQSc%2Ffwh9qhpdGwQl80VqiIbYbZriVzP7mbUwzvU7iRA0DLg62XWFq0GPI9X8HBiGWZ%2FzxZ%2FfAH8hy1ziWxzXrAyBYG9xKJLiaYl2fB26XmfSUKT%2Fc04GDf%2Bwfe8XWbVtbixFcLLl2OR0xhMLnhksoGOqUBMBzwcgVltGWsQ8vaInECcG4Qlp2nty54zphrCSTLEdrEBRxPeRo3tcvv85GBa6pPaq6OmZGpZ57R9dZKqjSMsV0%2BuMvtvdT0nqWuEoaUk2sfeBb7YxW7J4rnBE%2FQfabiNXptWQgzlNsAuQy%2BXg5Fz2nAdPoJrqpuY0vFno4Ugb3btNVGsK3rvsAWCyJ4RIs9C0laYio8VwCJzHY8ncCebJ8f6dMb&X-Amz-Signature=08dbebef2cb5dcda3e89bfd1af459fcc926964eddb5eae188d5bf6cc8ab9cce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDSKUSC4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqloiTAhC%2FExdCBMCqgCH8aPANQrE8HQETUOJXzzuCWwIgEXkZDFg7LQKcezos9G6TX43y2d8Xt5lkEzD83YmHgvAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTsYsWqbOqMgOdRyircA4JS1MjB1Br34LHw9sjdAJFvNxkjrBFVYJFDTlx2SGzvXCJtWp3%2ByczWruk%2BHwgEW%2BTGeicI0rLqCcJdFHbeu%2BMi31XIX%2B%2F59UYrfR%2B9bkI%2F3OmGw7BTatOYZaQAMj3QaQ1uNpdTFXDH7qC6lvJ8tuSmnVhvBjdgYHnSWO1ipDN2Jrrqfdw6%2FEQYWDTqnWLlHuyWb8VH8KmFp8x8uD5SCkbZ1isKcR82GhfdapwIadiRgyAN24XW9o2bpA28tFIdwsHnE6Obi84edKcFTbsjY%2BFVEeivcna6n1gBGpyrnF9HczNoQo6%2FmNcIaIiO7yg%2BFHeQHyd7asxdX9DR1rhehVy763Dm6NAWTatsc5tI4Qu6p3VWKuTlRFCcqMlMMzxA67FLCFwOBl4U%2B6ephVvA4IfAUlvcu8LdRhg65rXG0iA7AbYOhu5TcV1LB5eYFREWDUzUtX%2F0XM0%2Bjb8L0jrBqwHRWgz1hbPWvol9v7WL87u%2BptQSc%2Ffwh9qhpdGwQl80VqiIbYbZriVzP7mbUwzvU7iRA0DLg62XWFq0GPI9X8HBiGWZ%2FzxZ%2FfAH8hy1ziWxzXrAyBYG9xKJLiaYl2fB26XmfSUKT%2Fc04GDf%2Bwfe8XWbVtbixFcLLl2OR0xhMLnhksoGOqUBMBzwcgVltGWsQ8vaInECcG4Qlp2nty54zphrCSTLEdrEBRxPeRo3tcvv85GBa6pPaq6OmZGpZ57R9dZKqjSMsV0%2BuMvtvdT0nqWuEoaUk2sfeBb7YxW7J4rnBE%2FQfabiNXptWQgzlNsAuQy%2BXg5Fz2nAdPoJrqpuY0vFno4Ugb3btNVGsK3rvsAWCyJ4RIs9C0laYio8VwCJzHY8ncCebJ8f6dMb&X-Amz-Signature=6a2a3211511d6761bb2257c5656bffda44d1e1e6fc1ed3a6f9dff1dd88b44da5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

