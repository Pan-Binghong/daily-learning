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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUSWSWJ%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDGuZ5zK2uTbk%2FdZ0QGTF5tdtidDEnp6q4TiJCaBN7DNAiAUdL2cMrPZJyLuSAuWFksuvdNXfGMixmOlKnFisgHu2Cr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMXY0icAtb3%2BjGmDzKKtwDd78UeNASvb1TiZfmtJGIx9QD%2BdBBEIxm4sdR25PhMwPsfthAl5u4p7Bn1R5srNbDj2Qm1XvC3JyXjiGL4t0v%2BVBqVaPgE4HBfRAHD4E7IOuqJDjJ2QW9lbjx3h20EvYJe2FBQvYBPsW%2BcQDKXlXIclyDgjRm7PE81p6ar%2Fj6MNarOUm5UFo3egT2oo7XnWMeUaKEvFlJzIL5Pq1GJCjNdHj9gmIwtZADiv8QoA5XQwllbcju%2B1SzNcfcyc2z%2FZUlEoHrElUbt37V%2FiuM5PFuUDyAR0uyINPDRhdXAc%2FAcltwpA%2FX6%2B6fRZtTGJMzoIoXQIoScECmNsXtTk8n1D%2F8evGMyFNKg11I%2Blqaj1WfnsT5ANBW81LISPm8Sgs5gVvALGWnk2iRyPONfPZ5se0LK9bXrF2O3C1H9HzsskxNa6xWcXDxoQgcOGqYVYT3k4PPyxa%2FkLHq3QwtX0t3F6Vwk4A809RKpahbIX8rxZ3W7hpvNNAO97Tfk4351odfooU%2BjPQvFRvNNzBrln3g7fqqmYXfuIORwcgwgjANlL8KwXbjjWFW7JDYXC3SBeZQjtk7sFsGEoMaGBwgm3EHTWejPyS20tX7hQy7rEffF%2FEfrtOEx81yxahaH8JmNs4woNPgywY6pgF63oNARYTrAstjPPa50VjQDjeOaNtdekF%2FBjwFPwpDzD4gtiMMoLbLUFSmx5hT5bPKXDQSNOrL77Vbqq1knUXGGQx14BOoXjfThjNZxMUVHoDh0Fh4LCC2vlfZsTR46LlYakLPQH9JGdPJiUUOvLhBqx3GejH29gh5OUBKsgciNJTuHm2ti7ftHwxPkXftUJjRh1fsrsnlzbnjwtaTHVcWuqWny1cz&X-Amz-Signature=9a9bdbfa3d071b4e0e5e5297375263eeed354fb33822015403877692058db460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUSWSWJ%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDGuZ5zK2uTbk%2FdZ0QGTF5tdtidDEnp6q4TiJCaBN7DNAiAUdL2cMrPZJyLuSAuWFksuvdNXfGMixmOlKnFisgHu2Cr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMXY0icAtb3%2BjGmDzKKtwDd78UeNASvb1TiZfmtJGIx9QD%2BdBBEIxm4sdR25PhMwPsfthAl5u4p7Bn1R5srNbDj2Qm1XvC3JyXjiGL4t0v%2BVBqVaPgE4HBfRAHD4E7IOuqJDjJ2QW9lbjx3h20EvYJe2FBQvYBPsW%2BcQDKXlXIclyDgjRm7PE81p6ar%2Fj6MNarOUm5UFo3egT2oo7XnWMeUaKEvFlJzIL5Pq1GJCjNdHj9gmIwtZADiv8QoA5XQwllbcju%2B1SzNcfcyc2z%2FZUlEoHrElUbt37V%2FiuM5PFuUDyAR0uyINPDRhdXAc%2FAcltwpA%2FX6%2B6fRZtTGJMzoIoXQIoScECmNsXtTk8n1D%2F8evGMyFNKg11I%2Blqaj1WfnsT5ANBW81LISPm8Sgs5gVvALGWnk2iRyPONfPZ5se0LK9bXrF2O3C1H9HzsskxNa6xWcXDxoQgcOGqYVYT3k4PPyxa%2FkLHq3QwtX0t3F6Vwk4A809RKpahbIX8rxZ3W7hpvNNAO97Tfk4351odfooU%2BjPQvFRvNNzBrln3g7fqqmYXfuIORwcgwgjANlL8KwXbjjWFW7JDYXC3SBeZQjtk7sFsGEoMaGBwgm3EHTWejPyS20tX7hQy7rEffF%2FEfrtOEx81yxahaH8JmNs4woNPgywY6pgF63oNARYTrAstjPPa50VjQDjeOaNtdekF%2FBjwFPwpDzD4gtiMMoLbLUFSmx5hT5bPKXDQSNOrL77Vbqq1knUXGGQx14BOoXjfThjNZxMUVHoDh0Fh4LCC2vlfZsTR46LlYakLPQH9JGdPJiUUOvLhBqx3GejH29gh5OUBKsgciNJTuHm2ti7ftHwxPkXftUJjRh1fsrsnlzbnjwtaTHVcWuqWny1cz&X-Amz-Signature=7f32cce132faf87a3702ed0f88bd52de841b0a70325f7f4fddddc49c3903c59e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUSWSWJ%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDGuZ5zK2uTbk%2FdZ0QGTF5tdtidDEnp6q4TiJCaBN7DNAiAUdL2cMrPZJyLuSAuWFksuvdNXfGMixmOlKnFisgHu2Cr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMXY0icAtb3%2BjGmDzKKtwDd78UeNASvb1TiZfmtJGIx9QD%2BdBBEIxm4sdR25PhMwPsfthAl5u4p7Bn1R5srNbDj2Qm1XvC3JyXjiGL4t0v%2BVBqVaPgE4HBfRAHD4E7IOuqJDjJ2QW9lbjx3h20EvYJe2FBQvYBPsW%2BcQDKXlXIclyDgjRm7PE81p6ar%2Fj6MNarOUm5UFo3egT2oo7XnWMeUaKEvFlJzIL5Pq1GJCjNdHj9gmIwtZADiv8QoA5XQwllbcju%2B1SzNcfcyc2z%2FZUlEoHrElUbt37V%2FiuM5PFuUDyAR0uyINPDRhdXAc%2FAcltwpA%2FX6%2B6fRZtTGJMzoIoXQIoScECmNsXtTk8n1D%2F8evGMyFNKg11I%2Blqaj1WfnsT5ANBW81LISPm8Sgs5gVvALGWnk2iRyPONfPZ5se0LK9bXrF2O3C1H9HzsskxNa6xWcXDxoQgcOGqYVYT3k4PPyxa%2FkLHq3QwtX0t3F6Vwk4A809RKpahbIX8rxZ3W7hpvNNAO97Tfk4351odfooU%2BjPQvFRvNNzBrln3g7fqqmYXfuIORwcgwgjANlL8KwXbjjWFW7JDYXC3SBeZQjtk7sFsGEoMaGBwgm3EHTWejPyS20tX7hQy7rEffF%2FEfrtOEx81yxahaH8JmNs4woNPgywY6pgF63oNARYTrAstjPPa50VjQDjeOaNtdekF%2FBjwFPwpDzD4gtiMMoLbLUFSmx5hT5bPKXDQSNOrL77Vbqq1knUXGGQx14BOoXjfThjNZxMUVHoDh0Fh4LCC2vlfZsTR46LlYakLPQH9JGdPJiUUOvLhBqx3GejH29gh5OUBKsgciNJTuHm2ti7ftHwxPkXftUJjRh1fsrsnlzbnjwtaTHVcWuqWny1cz&X-Amz-Signature=db0431c42813ee3d16765d21796a0c70ec4123ec7b123bd80b69a18dd55e8043&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

