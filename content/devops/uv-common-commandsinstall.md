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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKC7KVFH%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIBnJg9jnYu9uIcU0sEWnLB1cPIAkv2Sy2ipzFNduVBFEAiAMB%2FDny3GoOnlp%2BgY6FzrSvydMVe%2FfNLcEbqkRKXVF6yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMJ3ATdsgMngU4KxvJKtwDb9B57PwrgioLfnDHOg4pAe7oy8JS%2BHK%2BbI7yqOhK0bFdnllnII5%2BE82MPpWRXkaj59BxOG%2FKA5phVCjNAFuYxwuhOo4XPAhOxWxmT4PS8X%2FyyyHr9yfNrTemkf8I9yadAdtTWY%2Bb8IrwF331iBUOG8z3hSEOe2M%2FFRY6YN1KrwSv%2Fxvhn4tPkzEHjjs2IpaF89RomCZchs4SVSFx8hHQZ8At9tYku380TrO7wf0SriXS4VC%2FU6InlTiAL2sjeBJgyFMvSfesYwvfpdh6bKdv72OF9aC5ba1rRJjbpJCUD5O5NsaFyBdnFIhzUrAnOlH05qldJDkjXgqltvW%2FJ%2FZOholqhndi0D1MimA17U4QVlJT0Br%2FIsp6ypdo34ltZ%2F75k87S2a2rMTSaVl0aqTiprrcGljTVoJEIOYVMgB7O85KAa8RTg1k8Jcsy34Q1ZEvwL21i52JRVKR9S0n8pKORXsCv4BkGl6g8lz8pL9CVjkbeFQoO9M6E1a1ltfpO4dFDUdu%2BSnU1OqxOJ0LssSe83hLtmcWGCKM8tMRYN0TBnzLsnW%2FLxlTJo1bRqK9mCv%2FaxqKE8ccFpdWGj12LmDrXOqMO2nKof3CM5qlf1aVkbi2tayTOH2p1P%2F0PUKMwgdWbzwY6pgFcYm9KU1M2ooJcyU81r8T%2F%2BlKbunkHibBYe9%2FWY%2BKwVX4m5Ice4wtQ5qZfg3%2FxIK8YCY8RUNN00AMAA0C5OBtykOTkgzvzu%2F9SxYpUCw8yI2R3roAwzt%2FYmEfGDxm66fLqQJQGu2DhkYGOTI3izDG0HwNFQgNexhRG0fgS9MOesg0iU9GNDhjQmeIePYBToEhDtFE6D%2F0%2BqiYGiJHJ0ln%2BPrCYWdYC&X-Amz-Signature=1502989d878af70eb4e363d5adbc5c4d25524a8ae707ef370974f7b54283f669&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKC7KVFH%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIBnJg9jnYu9uIcU0sEWnLB1cPIAkv2Sy2ipzFNduVBFEAiAMB%2FDny3GoOnlp%2BgY6FzrSvydMVe%2FfNLcEbqkRKXVF6yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMJ3ATdsgMngU4KxvJKtwDb9B57PwrgioLfnDHOg4pAe7oy8JS%2BHK%2BbI7yqOhK0bFdnllnII5%2BE82MPpWRXkaj59BxOG%2FKA5phVCjNAFuYxwuhOo4XPAhOxWxmT4PS8X%2FyyyHr9yfNrTemkf8I9yadAdtTWY%2Bb8IrwF331iBUOG8z3hSEOe2M%2FFRY6YN1KrwSv%2Fxvhn4tPkzEHjjs2IpaF89RomCZchs4SVSFx8hHQZ8At9tYku380TrO7wf0SriXS4VC%2FU6InlTiAL2sjeBJgyFMvSfesYwvfpdh6bKdv72OF9aC5ba1rRJjbpJCUD5O5NsaFyBdnFIhzUrAnOlH05qldJDkjXgqltvW%2FJ%2FZOholqhndi0D1MimA17U4QVlJT0Br%2FIsp6ypdo34ltZ%2F75k87S2a2rMTSaVl0aqTiprrcGljTVoJEIOYVMgB7O85KAa8RTg1k8Jcsy34Q1ZEvwL21i52JRVKR9S0n8pKORXsCv4BkGl6g8lz8pL9CVjkbeFQoO9M6E1a1ltfpO4dFDUdu%2BSnU1OqxOJ0LssSe83hLtmcWGCKM8tMRYN0TBnzLsnW%2FLxlTJo1bRqK9mCv%2FaxqKE8ccFpdWGj12LmDrXOqMO2nKof3CM5qlf1aVkbi2tayTOH2p1P%2F0PUKMwgdWbzwY6pgFcYm9KU1M2ooJcyU81r8T%2F%2BlKbunkHibBYe9%2FWY%2BKwVX4m5Ice4wtQ5qZfg3%2FxIK8YCY8RUNN00AMAA0C5OBtykOTkgzvzu%2F9SxYpUCw8yI2R3roAwzt%2FYmEfGDxm66fLqQJQGu2DhkYGOTI3izDG0HwNFQgNexhRG0fgS9MOesg0iU9GNDhjQmeIePYBToEhDtFE6D%2F0%2BqiYGiJHJ0ln%2BPrCYWdYC&X-Amz-Signature=d139253ab67a415a864b4a53bda1f350da1047e6e72165bdfe4d278f6337086b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKC7KVFH%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIBnJg9jnYu9uIcU0sEWnLB1cPIAkv2Sy2ipzFNduVBFEAiAMB%2FDny3GoOnlp%2BgY6FzrSvydMVe%2FfNLcEbqkRKXVF6yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMJ3ATdsgMngU4KxvJKtwDb9B57PwrgioLfnDHOg4pAe7oy8JS%2BHK%2BbI7yqOhK0bFdnllnII5%2BE82MPpWRXkaj59BxOG%2FKA5phVCjNAFuYxwuhOo4XPAhOxWxmT4PS8X%2FyyyHr9yfNrTemkf8I9yadAdtTWY%2Bb8IrwF331iBUOG8z3hSEOe2M%2FFRY6YN1KrwSv%2Fxvhn4tPkzEHjjs2IpaF89RomCZchs4SVSFx8hHQZ8At9tYku380TrO7wf0SriXS4VC%2FU6InlTiAL2sjeBJgyFMvSfesYwvfpdh6bKdv72OF9aC5ba1rRJjbpJCUD5O5NsaFyBdnFIhzUrAnOlH05qldJDkjXgqltvW%2FJ%2FZOholqhndi0D1MimA17U4QVlJT0Br%2FIsp6ypdo34ltZ%2F75k87S2a2rMTSaVl0aqTiprrcGljTVoJEIOYVMgB7O85KAa8RTg1k8Jcsy34Q1ZEvwL21i52JRVKR9S0n8pKORXsCv4BkGl6g8lz8pL9CVjkbeFQoO9M6E1a1ltfpO4dFDUdu%2BSnU1OqxOJ0LssSe83hLtmcWGCKM8tMRYN0TBnzLsnW%2FLxlTJo1bRqK9mCv%2FaxqKE8ccFpdWGj12LmDrXOqMO2nKof3CM5qlf1aVkbi2tayTOH2p1P%2F0PUKMwgdWbzwY6pgFcYm9KU1M2ooJcyU81r8T%2F%2BlKbunkHibBYe9%2FWY%2BKwVX4m5Ice4wtQ5qZfg3%2FxIK8YCY8RUNN00AMAA0C5OBtykOTkgzvzu%2F9SxYpUCw8yI2R3roAwzt%2FYmEfGDxm66fLqQJQGu2DhkYGOTI3izDG0HwNFQgNexhRG0fgS9MOesg0iU9GNDhjQmeIePYBToEhDtFE6D%2F0%2BqiYGiJHJ0ln%2BPrCYWdYC&X-Amz-Signature=5ef4a7395843d18e725e1bed0db533c9cd4fcdc59baaa8c112fc05d3378576f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

