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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHIQCQ5A%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDcxiecKe66A5xcK%2BHlOqhXoWffwB1JGOQ%2B40LvGdZGAQIgGJRRkVxS%2BCQYTgfG9doEHHu%2Fd3L4PIE%2BsgbA47eJQoMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoPMpUmUsTx96oeTircA%2BqOlTao8iEIE04AhIHDB0JWDse6zwdfaBBIOCtTvi8ZdkL9rrutvs%2B5unJ9qLDqkCmxssf4vG5oInyUQLh91gnyTo58KVg00%2FveQxtilFjn7dOlVYhq6R5S%2F2A2e3sgebEWsVmd98vzTKtdKpoLnFK7KQtCwDE74DLfGGk9B6EYsO3Ui2eev1l1ALAJdu1EggDPiQycuY5utMuClmLFX1ifUH5ZbrYoLkYl2cS848MF%2BK9xH3SMqwcB7LrA546jUTQlFiVR2sflfWUOQA1h%2FMBuH6wbC9YGL3ONJQz0G9HRJutyTWMwRoxWn%2FzkTX6nuVvRzq2ovMrSmm45ofm4ubpZbPuMEjHB4JwaulWfUfSz6vczMhrD%2BAt5Xd0c3FZIltb1osqmX74bBT8GTk%2FjEyK5a6%2B6RtZaoVDVAFVvViFHOaHckJ5MUYJMv%2FKlr1S0JXf54IJQBX%2FhV3B2OR8bZRxAtrIBKaK%2F1NKYfDi%2FptgXdDm0Hom5WUaPi2qhTiTUGFpzPnCXaIq4ciQqSgyzXtfjrU2rjCCZ6oSN5dQfx4xhdbgLbFoQ5bnY0oH%2BNH5IxaVsLkZvoMqLViHRo3JUt1m21yRthaU%2FKqskyrsodL0dCQPycYvlpTwSs3UXMP%2FQusgGOqUB%2Fx4VCMi%2FlkCtLxwN4bF3JekfioBzXgaAKxhWabb0rKJpNHs0mtHv4Ibpt5dm0pt3f44XbIRlncPdgSIKFkWLwkLsJElm%2FCIMGC3Tdb9S7bplvyxQNMYjxoMP0sg%2BL8ku54bpgYfiJx4njlY9CXJuQzdXqyBqy7Zv%2FwMVRO4dHHhNeyfVjBBgzxQO59IuGyJeyAXM2aFKTnznOI3VwHEwMr6%2FOaWV&X-Amz-Signature=de8e9742754198036f05e8340d61d0f1e57e78b5ebf8837029a39ce1c32c4f3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHIQCQ5A%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDcxiecKe66A5xcK%2BHlOqhXoWffwB1JGOQ%2B40LvGdZGAQIgGJRRkVxS%2BCQYTgfG9doEHHu%2Fd3L4PIE%2BsgbA47eJQoMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoPMpUmUsTx96oeTircA%2BqOlTao8iEIE04AhIHDB0JWDse6zwdfaBBIOCtTvi8ZdkL9rrutvs%2B5unJ9qLDqkCmxssf4vG5oInyUQLh91gnyTo58KVg00%2FveQxtilFjn7dOlVYhq6R5S%2F2A2e3sgebEWsVmd98vzTKtdKpoLnFK7KQtCwDE74DLfGGk9B6EYsO3Ui2eev1l1ALAJdu1EggDPiQycuY5utMuClmLFX1ifUH5ZbrYoLkYl2cS848MF%2BK9xH3SMqwcB7LrA546jUTQlFiVR2sflfWUOQA1h%2FMBuH6wbC9YGL3ONJQz0G9HRJutyTWMwRoxWn%2FzkTX6nuVvRzq2ovMrSmm45ofm4ubpZbPuMEjHB4JwaulWfUfSz6vczMhrD%2BAt5Xd0c3FZIltb1osqmX74bBT8GTk%2FjEyK5a6%2B6RtZaoVDVAFVvViFHOaHckJ5MUYJMv%2FKlr1S0JXf54IJQBX%2FhV3B2OR8bZRxAtrIBKaK%2F1NKYfDi%2FptgXdDm0Hom5WUaPi2qhTiTUGFpzPnCXaIq4ciQqSgyzXtfjrU2rjCCZ6oSN5dQfx4xhdbgLbFoQ5bnY0oH%2BNH5IxaVsLkZvoMqLViHRo3JUt1m21yRthaU%2FKqskyrsodL0dCQPycYvlpTwSs3UXMP%2FQusgGOqUB%2Fx4VCMi%2FlkCtLxwN4bF3JekfioBzXgaAKxhWabb0rKJpNHs0mtHv4Ibpt5dm0pt3f44XbIRlncPdgSIKFkWLwkLsJElm%2FCIMGC3Tdb9S7bplvyxQNMYjxoMP0sg%2BL8ku54bpgYfiJx4njlY9CXJuQzdXqyBqy7Zv%2FwMVRO4dHHhNeyfVjBBgzxQO59IuGyJeyAXM2aFKTnznOI3VwHEwMr6%2FOaWV&X-Amz-Signature=565afe3fa5785be60e307061b9ec554b5df994887732e4f8ccaf1ee0fc374512&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHIQCQ5A%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDcxiecKe66A5xcK%2BHlOqhXoWffwB1JGOQ%2B40LvGdZGAQIgGJRRkVxS%2BCQYTgfG9doEHHu%2Fd3L4PIE%2BsgbA47eJQoMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoPMpUmUsTx96oeTircA%2BqOlTao8iEIE04AhIHDB0JWDse6zwdfaBBIOCtTvi8ZdkL9rrutvs%2B5unJ9qLDqkCmxssf4vG5oInyUQLh91gnyTo58KVg00%2FveQxtilFjn7dOlVYhq6R5S%2F2A2e3sgebEWsVmd98vzTKtdKpoLnFK7KQtCwDE74DLfGGk9B6EYsO3Ui2eev1l1ALAJdu1EggDPiQycuY5utMuClmLFX1ifUH5ZbrYoLkYl2cS848MF%2BK9xH3SMqwcB7LrA546jUTQlFiVR2sflfWUOQA1h%2FMBuH6wbC9YGL3ONJQz0G9HRJutyTWMwRoxWn%2FzkTX6nuVvRzq2ovMrSmm45ofm4ubpZbPuMEjHB4JwaulWfUfSz6vczMhrD%2BAt5Xd0c3FZIltb1osqmX74bBT8GTk%2FjEyK5a6%2B6RtZaoVDVAFVvViFHOaHckJ5MUYJMv%2FKlr1S0JXf54IJQBX%2FhV3B2OR8bZRxAtrIBKaK%2F1NKYfDi%2FptgXdDm0Hom5WUaPi2qhTiTUGFpzPnCXaIq4ciQqSgyzXtfjrU2rjCCZ6oSN5dQfx4xhdbgLbFoQ5bnY0oH%2BNH5IxaVsLkZvoMqLViHRo3JUt1m21yRthaU%2FKqskyrsodL0dCQPycYvlpTwSs3UXMP%2FQusgGOqUB%2Fx4VCMi%2FlkCtLxwN4bF3JekfioBzXgaAKxhWabb0rKJpNHs0mtHv4Ibpt5dm0pt3f44XbIRlncPdgSIKFkWLwkLsJElm%2FCIMGC3Tdb9S7bplvyxQNMYjxoMP0sg%2BL8ku54bpgYfiJx4njlY9CXJuQzdXqyBqy7Zv%2FwMVRO4dHHhNeyfVjBBgzxQO59IuGyJeyAXM2aFKTnznOI3VwHEwMr6%2FOaWV&X-Amz-Signature=023e75be1180ed8022e3d59fd8aa78aad05e8803ebbceec68ee40b126d8344f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

