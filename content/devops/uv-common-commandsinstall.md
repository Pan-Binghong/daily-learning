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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DN4EQEF%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIAUjUkWILIFKriqhYLiXjfAW8cFh1MFYzRGMOXDianGPAiAOegYepZ%2Bx6a1cXdTbflAMKnHYGl%2F3FkchDijxjGSTVir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMV1VbQ4KyWswgjF2YKtwDNrEzZ5NgsogytSpJY4oNoDaiy0%2Fy%2FEMysrp8OFsJviaASTyBDIDZphaL%2FS0c5ksI3PDYtxr1xYol51rLZxsrH%2BqslBe3djtBx7cm7jO26kzGf6S%2FP%2BYR5HImUwqYgQoEKH57%2Bhw34SRU5k2RTJKeydprGCGSCGo3GX0kEXTF3Q4O9wZCiD62OaN4pgZdijUjlxjnr%2FNo0QXjHwcTLJq%2FYy5IfDsJl7UzyhdVzoyZ6ZB%2BiK%2FRjEkN5IjlKG9b8C6RmeTmbPsq0UnVvT5lJ2N2m%2FttQm2rZd4OARxZPoFBuXDU8nF3AFlXA7gF7OAJx4Dmow240bg2YGuP8qAKFblzgluS3POMqHjLPplZCkWFcb63higPwW8YzEvWZ8wh95HyohLbVQ4uYf3cSoA36%2FZb1DglwfdxIWxnd692N99Dz4GMWwvO6A6dNQ0FdeybtFgoYZK7uleWiZCSDR0cbedEY9M21t%2B8XnIIPNMc7%2BDpSOGCpndEX4plHygBsiKQdj35RtVCzL4uuxwjhHEN9j59N4%2BqFcyaEKhrYLkeyn%2FYoPdqzrUXxUy9b%2FPZ3tpj7znRUVWcDEDOm%2BodHVp%2BeyL4mjmd5z1CLmRsX1R6izlfelpLFcaP7J21plinJaUw8I%2B%2BzQY6pgGkn83tqaHbt33R2J7dZYzlmhfgKV3VEdU9jT5e46m9PwN4GN4VNEF1Pzah%2F2Mu%2BPFhTaBBsSlRorlno5g7M2T%2BqkVKzFFh23bODch4pFBc400BNagWSZB4KmTtSdynzTCiStR%2BwodF6LRMB%2BCQadi6BGjnl%2FjjxXzNpsBE1CDKJukRnjLw1MP3cTebcekMUJzCMi0BPWkHextCy1bXeCoQNwssbX9u&X-Amz-Signature=8206ea960a1e44b0b875c64b8f7d52369e3e57fe43b1cfdc05e5fae78f6c573d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DN4EQEF%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIAUjUkWILIFKriqhYLiXjfAW8cFh1MFYzRGMOXDianGPAiAOegYepZ%2Bx6a1cXdTbflAMKnHYGl%2F3FkchDijxjGSTVir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMV1VbQ4KyWswgjF2YKtwDNrEzZ5NgsogytSpJY4oNoDaiy0%2Fy%2FEMysrp8OFsJviaASTyBDIDZphaL%2FS0c5ksI3PDYtxr1xYol51rLZxsrH%2BqslBe3djtBx7cm7jO26kzGf6S%2FP%2BYR5HImUwqYgQoEKH57%2Bhw34SRU5k2RTJKeydprGCGSCGo3GX0kEXTF3Q4O9wZCiD62OaN4pgZdijUjlxjnr%2FNo0QXjHwcTLJq%2FYy5IfDsJl7UzyhdVzoyZ6ZB%2BiK%2FRjEkN5IjlKG9b8C6RmeTmbPsq0UnVvT5lJ2N2m%2FttQm2rZd4OARxZPoFBuXDU8nF3AFlXA7gF7OAJx4Dmow240bg2YGuP8qAKFblzgluS3POMqHjLPplZCkWFcb63higPwW8YzEvWZ8wh95HyohLbVQ4uYf3cSoA36%2FZb1DglwfdxIWxnd692N99Dz4GMWwvO6A6dNQ0FdeybtFgoYZK7uleWiZCSDR0cbedEY9M21t%2B8XnIIPNMc7%2BDpSOGCpndEX4plHygBsiKQdj35RtVCzL4uuxwjhHEN9j59N4%2BqFcyaEKhrYLkeyn%2FYoPdqzrUXxUy9b%2FPZ3tpj7znRUVWcDEDOm%2BodHVp%2BeyL4mjmd5z1CLmRsX1R6izlfelpLFcaP7J21plinJaUw8I%2B%2BzQY6pgGkn83tqaHbt33R2J7dZYzlmhfgKV3VEdU9jT5e46m9PwN4GN4VNEF1Pzah%2F2Mu%2BPFhTaBBsSlRorlno5g7M2T%2BqkVKzFFh23bODch4pFBc400BNagWSZB4KmTtSdynzTCiStR%2BwodF6LRMB%2BCQadi6BGjnl%2FjjxXzNpsBE1CDKJukRnjLw1MP3cTebcekMUJzCMi0BPWkHextCy1bXeCoQNwssbX9u&X-Amz-Signature=22a55175d035974ca964d0e845c9b3484e328990be0c1d1cdd30db73ee479bdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DN4EQEF%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIAUjUkWILIFKriqhYLiXjfAW8cFh1MFYzRGMOXDianGPAiAOegYepZ%2Bx6a1cXdTbflAMKnHYGl%2F3FkchDijxjGSTVir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMV1VbQ4KyWswgjF2YKtwDNrEzZ5NgsogytSpJY4oNoDaiy0%2Fy%2FEMysrp8OFsJviaASTyBDIDZphaL%2FS0c5ksI3PDYtxr1xYol51rLZxsrH%2BqslBe3djtBx7cm7jO26kzGf6S%2FP%2BYR5HImUwqYgQoEKH57%2Bhw34SRU5k2RTJKeydprGCGSCGo3GX0kEXTF3Q4O9wZCiD62OaN4pgZdijUjlxjnr%2FNo0QXjHwcTLJq%2FYy5IfDsJl7UzyhdVzoyZ6ZB%2BiK%2FRjEkN5IjlKG9b8C6RmeTmbPsq0UnVvT5lJ2N2m%2FttQm2rZd4OARxZPoFBuXDU8nF3AFlXA7gF7OAJx4Dmow240bg2YGuP8qAKFblzgluS3POMqHjLPplZCkWFcb63higPwW8YzEvWZ8wh95HyohLbVQ4uYf3cSoA36%2FZb1DglwfdxIWxnd692N99Dz4GMWwvO6A6dNQ0FdeybtFgoYZK7uleWiZCSDR0cbedEY9M21t%2B8XnIIPNMc7%2BDpSOGCpndEX4plHygBsiKQdj35RtVCzL4uuxwjhHEN9j59N4%2BqFcyaEKhrYLkeyn%2FYoPdqzrUXxUy9b%2FPZ3tpj7znRUVWcDEDOm%2BodHVp%2BeyL4mjmd5z1CLmRsX1R6izlfelpLFcaP7J21plinJaUw8I%2B%2BzQY6pgGkn83tqaHbt33R2J7dZYzlmhfgKV3VEdU9jT5e46m9PwN4GN4VNEF1Pzah%2F2Mu%2BPFhTaBBsSlRorlno5g7M2T%2BqkVKzFFh23bODch4pFBc400BNagWSZB4KmTtSdynzTCiStR%2BwodF6LRMB%2BCQadi6BGjnl%2FjjxXzNpsBE1CDKJukRnjLw1MP3cTebcekMUJzCMi0BPWkHextCy1bXeCoQNwssbX9u&X-Amz-Signature=c7d77d0786cbf737dad7e4b9881aefc43810bd77ccd8b217fd999af326b8ccc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

