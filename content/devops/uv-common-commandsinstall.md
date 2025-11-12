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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGBBZZEH%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEdc%2Bj9bTOuXFNkCaG%2Fki6PcwSojkgOzcw%2F4GG5e1OETAiAIQJQd2aubN8E0kCfu3j0pA6cTzr8P%2F6GFj%2FwWVlc2yyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMgcdSJYAZmMPpe0r%2BKtwDnPCMDn8ONYEAW4vk4TKp3RuL6MZHwFz1tj7rTk65khy7h%2FEutx%2FI6A%2FEsv6YHOJYd72hAtbJK9LFUrBQwFmukyNcGEtxm6xxzWwaMsMP3QqBuhLSHvc0U83u090u3u9nFxNfHa8MHsN2llw9b%2Be7B5l7fqWnSOEs3qYAxSyzanFyTOeTKqKbG%2BWl92JUHYYtbqVjCulIJFfl6rDGmQLvsUpdbhZ6YiGWQqWNYsH5FwfbKJ0RBTVgoXh5mDwdYBl6w5acRxgLcPTNoVFExNSr%2FlswiKRIJ5boGpZLfzjE%2Bca%2Fe%2BmGw1UjP6x0qEUB1mwlmub1vqUujS191OtF4WlN3B4LALKnNhU2Udq%2FiE0Q%2F2YLgDClIR0fBp9P5Q7%2BGH%2FNM0V1CJsAnhvM0V2g0SaO7TIe99Utqrn0Ql5%2B03Wz3ixhP%2Bw7WGotN2LbJGjpvdLmticrU1DuryrIqz8Q7kVl%2F350fI4y42OrUrfi6%2Ffdlah7dKctaLO%2BfPw1%2BBNiU%2FRTwFmLhJpFkIu2c2inr8f56tZWxtSK578XT7yNiKGvaRwEJqCBfaYRqPwSHwtM4uTNsW7WAgFZnhg%2FHPPuB4L4A20tsQir4t9VJKTGwsRMp7NjhoEI3eRtQVHZXjYwoOPPyAY6pgHA82ChTv%2BppanZuVJv1qcUj7xduh9pUWZqszYsaBkGtGVf8rhOmRFxiEyMcW%2BN8ZX%2BGf%2BuLIAxUeLhbgz%2BZLuhOZa5M9z8upv8a%2F0EV1LNBEkKI4rLHbqCBhZzxCb5cq5PJT9PHpE3f1padRH7E0vERVneCfhZG70xGCdlcsZIQKatLwvNDgQpCyUv6YPA2WA%2Fiy9Q6OmF%2BpJuEgArNjkprAp7zuEN&X-Amz-Signature=a9183f1ec81746cd88e0996188c345a386ee7e71600e41e991f74451426b0d60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGBBZZEH%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEdc%2Bj9bTOuXFNkCaG%2Fki6PcwSojkgOzcw%2F4GG5e1OETAiAIQJQd2aubN8E0kCfu3j0pA6cTzr8P%2F6GFj%2FwWVlc2yyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMgcdSJYAZmMPpe0r%2BKtwDnPCMDn8ONYEAW4vk4TKp3RuL6MZHwFz1tj7rTk65khy7h%2FEutx%2FI6A%2FEsv6YHOJYd72hAtbJK9LFUrBQwFmukyNcGEtxm6xxzWwaMsMP3QqBuhLSHvc0U83u090u3u9nFxNfHa8MHsN2llw9b%2Be7B5l7fqWnSOEs3qYAxSyzanFyTOeTKqKbG%2BWl92JUHYYtbqVjCulIJFfl6rDGmQLvsUpdbhZ6YiGWQqWNYsH5FwfbKJ0RBTVgoXh5mDwdYBl6w5acRxgLcPTNoVFExNSr%2FlswiKRIJ5boGpZLfzjE%2Bca%2Fe%2BmGw1UjP6x0qEUB1mwlmub1vqUujS191OtF4WlN3B4LALKnNhU2Udq%2FiE0Q%2F2YLgDClIR0fBp9P5Q7%2BGH%2FNM0V1CJsAnhvM0V2g0SaO7TIe99Utqrn0Ql5%2B03Wz3ixhP%2Bw7WGotN2LbJGjpvdLmticrU1DuryrIqz8Q7kVl%2F350fI4y42OrUrfi6%2Ffdlah7dKctaLO%2BfPw1%2BBNiU%2FRTwFmLhJpFkIu2c2inr8f56tZWxtSK578XT7yNiKGvaRwEJqCBfaYRqPwSHwtM4uTNsW7WAgFZnhg%2FHPPuB4L4A20tsQir4t9VJKTGwsRMp7NjhoEI3eRtQVHZXjYwoOPPyAY6pgHA82ChTv%2BppanZuVJv1qcUj7xduh9pUWZqszYsaBkGtGVf8rhOmRFxiEyMcW%2BN8ZX%2BGf%2BuLIAxUeLhbgz%2BZLuhOZa5M9z8upv8a%2F0EV1LNBEkKI4rLHbqCBhZzxCb5cq5PJT9PHpE3f1padRH7E0vERVneCfhZG70xGCdlcsZIQKatLwvNDgQpCyUv6YPA2WA%2Fiy9Q6OmF%2BpJuEgArNjkprAp7zuEN&X-Amz-Signature=417b063809bb9d24b6348faff2be39daf800654a00f8d96dc9f11d3dc3535672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGBBZZEH%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEdc%2Bj9bTOuXFNkCaG%2Fki6PcwSojkgOzcw%2F4GG5e1OETAiAIQJQd2aubN8E0kCfu3j0pA6cTzr8P%2F6GFj%2FwWVlc2yyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMgcdSJYAZmMPpe0r%2BKtwDnPCMDn8ONYEAW4vk4TKp3RuL6MZHwFz1tj7rTk65khy7h%2FEutx%2FI6A%2FEsv6YHOJYd72hAtbJK9LFUrBQwFmukyNcGEtxm6xxzWwaMsMP3QqBuhLSHvc0U83u090u3u9nFxNfHa8MHsN2llw9b%2Be7B5l7fqWnSOEs3qYAxSyzanFyTOeTKqKbG%2BWl92JUHYYtbqVjCulIJFfl6rDGmQLvsUpdbhZ6YiGWQqWNYsH5FwfbKJ0RBTVgoXh5mDwdYBl6w5acRxgLcPTNoVFExNSr%2FlswiKRIJ5boGpZLfzjE%2Bca%2Fe%2BmGw1UjP6x0qEUB1mwlmub1vqUujS191OtF4WlN3B4LALKnNhU2Udq%2FiE0Q%2F2YLgDClIR0fBp9P5Q7%2BGH%2FNM0V1CJsAnhvM0V2g0SaO7TIe99Utqrn0Ql5%2B03Wz3ixhP%2Bw7WGotN2LbJGjpvdLmticrU1DuryrIqz8Q7kVl%2F350fI4y42OrUrfi6%2Ffdlah7dKctaLO%2BfPw1%2BBNiU%2FRTwFmLhJpFkIu2c2inr8f56tZWxtSK578XT7yNiKGvaRwEJqCBfaYRqPwSHwtM4uTNsW7WAgFZnhg%2FHPPuB4L4A20tsQir4t9VJKTGwsRMp7NjhoEI3eRtQVHZXjYwoOPPyAY6pgHA82ChTv%2BppanZuVJv1qcUj7xduh9pUWZqszYsaBkGtGVf8rhOmRFxiEyMcW%2BN8ZX%2BGf%2BuLIAxUeLhbgz%2BZLuhOZa5M9z8upv8a%2F0EV1LNBEkKI4rLHbqCBhZzxCb5cq5PJT9PHpE3f1padRH7E0vERVneCfhZG70xGCdlcsZIQKatLwvNDgQpCyUv6YPA2WA%2Fiy9Q6OmF%2BpJuEgArNjkprAp7zuEN&X-Amz-Signature=3f0128d15a177f95b0b60e299277da92ed812982fb53a4eb5fa6bf8a035390ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

