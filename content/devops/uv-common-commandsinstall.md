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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CV6WWOL%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIB%2BozOgSPHhzyMR1ajp7Z%2F4bItDeJXfkl4SBWlFe1wq5AiEAl%2Bt0sY1%2BGWv4wiW2TRtrMsxctVjm5zzNYivr1DODipgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsgR4Wjh7aoTdq8aCrcAzN5n65Qci51ElTGy6kBkDKDW%2Fp6GzLscmhjuiV546KNFszT3OMeI9vGH3jhZQG1HogMJPz98y1dWvhQAEOgXZ4gKSu6jMXgI5CNFhUUOu1LhKVXNZzBKUfAwjeUqRC8UVb0lgsmXVqJiGrvJk%2BzQj820i1A4pY03LXzeFuiyKNZ9%2FKTbeNtXEUx%2FA4aNCDxndaCsfAUxnfRPbIJV1Kx7zwYT7cSVHmcjM4c%2B%2BLfvZdH%2BE8%2FX7LCkQmvZ1REzevbv1bL9QVG1A%2B4a1Zg5mdXwfLA4WlgXrjI3w8PPzbaUMUCfU%2FkEqXP0tvwiUGoX2JlFEVoiBU1zISkmJaqlKDc8A3Za%2FAWdgUb6lkX%2F1HCwwibL49ltm0WpymM%2FUZTVudEKkvSKS3NhYG8MwziMmA19w5mbdsx9rHsF70c10h73duQRjSX2%2B4s7adYMumCOsoOsIRpraRBZ1GrLrvtqx0V41LkeVzD1w9MLqyLLp8kQCdI9c5PyiXN0iZ6nBy8jxBAZlwAgm%2FhBjrhTOX2AjoZCg0Udn81P2sbKxioEjW%2Bl0GyiZz%2BtGFJmfyuenN1tj0nfkLZBQLg1R22B3ED6S9OZ4bxoo9iSTo1DZLLQ7T4bDWRYhe7waMFZ1UihRxoMNnsnM4GOqUBmwjuCRly%2B8QaywSrHgKg9zTPv9nl%2B7U1oMBdJZx%2BfIGTfkrIuFHMRMJq0YFb5NdUyZtWmcUAWIhsQ2x8SLr6%2F2brcSU9vuHH4z%2FXzZLc0vN3vmufsAE3Dc4GgMsQuOIEvjRaYUJJZVE6rE1pCTWToM6ZTpOqg2J72Fsth8jKZDTslnYjd3E9c4fzFBbNAYm2CBKjBWcOTSRhbflhxr2jV%2BhfJ0ud&X-Amz-Signature=c11c5fd77b9d85562ddc070dff2ca9a98cc6fa9d6aeabd46c8ea6d3565778f61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CV6WWOL%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIB%2BozOgSPHhzyMR1ajp7Z%2F4bItDeJXfkl4SBWlFe1wq5AiEAl%2Bt0sY1%2BGWv4wiW2TRtrMsxctVjm5zzNYivr1DODipgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsgR4Wjh7aoTdq8aCrcAzN5n65Qci51ElTGy6kBkDKDW%2Fp6GzLscmhjuiV546KNFszT3OMeI9vGH3jhZQG1HogMJPz98y1dWvhQAEOgXZ4gKSu6jMXgI5CNFhUUOu1LhKVXNZzBKUfAwjeUqRC8UVb0lgsmXVqJiGrvJk%2BzQj820i1A4pY03LXzeFuiyKNZ9%2FKTbeNtXEUx%2FA4aNCDxndaCsfAUxnfRPbIJV1Kx7zwYT7cSVHmcjM4c%2B%2BLfvZdH%2BE8%2FX7LCkQmvZ1REzevbv1bL9QVG1A%2B4a1Zg5mdXwfLA4WlgXrjI3w8PPzbaUMUCfU%2FkEqXP0tvwiUGoX2JlFEVoiBU1zISkmJaqlKDc8A3Za%2FAWdgUb6lkX%2F1HCwwibL49ltm0WpymM%2FUZTVudEKkvSKS3NhYG8MwziMmA19w5mbdsx9rHsF70c10h73duQRjSX2%2B4s7adYMumCOsoOsIRpraRBZ1GrLrvtqx0V41LkeVzD1w9MLqyLLp8kQCdI9c5PyiXN0iZ6nBy8jxBAZlwAgm%2FhBjrhTOX2AjoZCg0Udn81P2sbKxioEjW%2Bl0GyiZz%2BtGFJmfyuenN1tj0nfkLZBQLg1R22B3ED6S9OZ4bxoo9iSTo1DZLLQ7T4bDWRYhe7waMFZ1UihRxoMNnsnM4GOqUBmwjuCRly%2B8QaywSrHgKg9zTPv9nl%2B7U1oMBdJZx%2BfIGTfkrIuFHMRMJq0YFb5NdUyZtWmcUAWIhsQ2x8SLr6%2F2brcSU9vuHH4z%2FXzZLc0vN3vmufsAE3Dc4GgMsQuOIEvjRaYUJJZVE6rE1pCTWToM6ZTpOqg2J72Fsth8jKZDTslnYjd3E9c4fzFBbNAYm2CBKjBWcOTSRhbflhxr2jV%2BhfJ0ud&X-Amz-Signature=ef58179435edd359cd4c0749b58bd5440b3da706f7762dc4e6c6c0dc13aa901a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CV6WWOL%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIB%2BozOgSPHhzyMR1ajp7Z%2F4bItDeJXfkl4SBWlFe1wq5AiEAl%2Bt0sY1%2BGWv4wiW2TRtrMsxctVjm5zzNYivr1DODipgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsgR4Wjh7aoTdq8aCrcAzN5n65Qci51ElTGy6kBkDKDW%2Fp6GzLscmhjuiV546KNFszT3OMeI9vGH3jhZQG1HogMJPz98y1dWvhQAEOgXZ4gKSu6jMXgI5CNFhUUOu1LhKVXNZzBKUfAwjeUqRC8UVb0lgsmXVqJiGrvJk%2BzQj820i1A4pY03LXzeFuiyKNZ9%2FKTbeNtXEUx%2FA4aNCDxndaCsfAUxnfRPbIJV1Kx7zwYT7cSVHmcjM4c%2B%2BLfvZdH%2BE8%2FX7LCkQmvZ1REzevbv1bL9QVG1A%2B4a1Zg5mdXwfLA4WlgXrjI3w8PPzbaUMUCfU%2FkEqXP0tvwiUGoX2JlFEVoiBU1zISkmJaqlKDc8A3Za%2FAWdgUb6lkX%2F1HCwwibL49ltm0WpymM%2FUZTVudEKkvSKS3NhYG8MwziMmA19w5mbdsx9rHsF70c10h73duQRjSX2%2B4s7adYMumCOsoOsIRpraRBZ1GrLrvtqx0V41LkeVzD1w9MLqyLLp8kQCdI9c5PyiXN0iZ6nBy8jxBAZlwAgm%2FhBjrhTOX2AjoZCg0Udn81P2sbKxioEjW%2Bl0GyiZz%2BtGFJmfyuenN1tj0nfkLZBQLg1R22B3ED6S9OZ4bxoo9iSTo1DZLLQ7T4bDWRYhe7waMFZ1UihRxoMNnsnM4GOqUBmwjuCRly%2B8QaywSrHgKg9zTPv9nl%2B7U1oMBdJZx%2BfIGTfkrIuFHMRMJq0YFb5NdUyZtWmcUAWIhsQ2x8SLr6%2F2brcSU9vuHH4z%2FXzZLc0vN3vmufsAE3Dc4GgMsQuOIEvjRaYUJJZVE6rE1pCTWToM6ZTpOqg2J72Fsth8jKZDTslnYjd3E9c4fzFBbNAYm2CBKjBWcOTSRhbflhxr2jV%2BhfJ0ud&X-Amz-Signature=c2bbee46438138ac50a290806eba93b9ad83a23cae28f178135794a515cdbb77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

