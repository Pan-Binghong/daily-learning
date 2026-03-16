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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A5E55P4%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQD5vpHHQbUwvo8cUijc%2F%2FqFup1ONA9%2BOG%2BaA1EaE0NpnwIgLgt2NnxPhGK32cmmuZABGm7QQzW6wVikT50foU%2B0cnwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvg7NTbBlZsEM2g2SrcA27FJZ1L%2FP5k6vztLIusIF25M0rSAG3zdjSwx1ixk9dAsQDCdDCmUcEl1c3TqQpqki52pUTkU%2F3gwzRASIL5AQlWfHAl%2Fjx%2Fg2JrTVlSJ6GQirC6jnHpp2oy1J32xtHpvWh4h0ejqCtiD%2FS8ye2ym4a7JEEza6ifJNzRGFNSMcGv7n4Ay5jlDwKUMhuS%2BvCf%2BmGBCiXJFmUuOknuNYortTSCtMoUS%2B1ym7M9%2FOa1z7HK0qK%2B8w50o6usbWBqXQ4qrXP1P3GjV5Bmnf8tS6Mg56N4XsS4r0sDWrRP8%2B2ZeF5kmp4cALLPUK1xDyvPPz4eFLQlrb3WFmzF4yC%2BNOJx0r33G7mADn5KYDMahdsMlrpbcJxs4qEEireJ%2BMxF5vJ419%2BhCTysATyP11a4N6gXplEIKO%2Byl20m3bDGKQ0TmIC5pf4doCjiNgeCCqFDOCgyaam87cC4KmFnjTribL2yuc8EPnWLLfktPKkAMmGdMRyIRftxuB01es%2FytYJ%2FQMHcC%2FxRdYXNiHy4ecB0U8UkEpuGFhRaU88PfEWplyGiBVHBULnHIaWkxWGcGNRkbiTH1Rx2h2Aw3qxV8CotJg9Az%2FB3mLp%2FyCm9eOwzt9X1T2uagU%2Bfipm1gqsjPOcsMMO93c0GOqUBF8HYkpXYAeV11hR%2FB11peu83HYM%2FpOJiSYvGVVLIbzfIdm4lrl7fBUQ2d80TSru6f%2BnjZJZ3nrZZFWKKsP0s%2Bb2vljHNx%2B%2F5JWOcXLxmofIkNyPNIZJfMyyWJdAo8p2PLlPxFotvpVOE4vDg5zxCHnvZjPnYnBnihNScvntoDo2%2BXq%2F7ItG8w4uo8fXokze6fEeU1SN8k7c4FexSW6b2q3y23GtK&X-Amz-Signature=0335dc85684a9162c608dc506d6ceca67d0018ffe64f411a0d80f47a30cfa94d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A5E55P4%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQD5vpHHQbUwvo8cUijc%2F%2FqFup1ONA9%2BOG%2BaA1EaE0NpnwIgLgt2NnxPhGK32cmmuZABGm7QQzW6wVikT50foU%2B0cnwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvg7NTbBlZsEM2g2SrcA27FJZ1L%2FP5k6vztLIusIF25M0rSAG3zdjSwx1ixk9dAsQDCdDCmUcEl1c3TqQpqki52pUTkU%2F3gwzRASIL5AQlWfHAl%2Fjx%2Fg2JrTVlSJ6GQirC6jnHpp2oy1J32xtHpvWh4h0ejqCtiD%2FS8ye2ym4a7JEEza6ifJNzRGFNSMcGv7n4Ay5jlDwKUMhuS%2BvCf%2BmGBCiXJFmUuOknuNYortTSCtMoUS%2B1ym7M9%2FOa1z7HK0qK%2B8w50o6usbWBqXQ4qrXP1P3GjV5Bmnf8tS6Mg56N4XsS4r0sDWrRP8%2B2ZeF5kmp4cALLPUK1xDyvPPz4eFLQlrb3WFmzF4yC%2BNOJx0r33G7mADn5KYDMahdsMlrpbcJxs4qEEireJ%2BMxF5vJ419%2BhCTysATyP11a4N6gXplEIKO%2Byl20m3bDGKQ0TmIC5pf4doCjiNgeCCqFDOCgyaam87cC4KmFnjTribL2yuc8EPnWLLfktPKkAMmGdMRyIRftxuB01es%2FytYJ%2FQMHcC%2FxRdYXNiHy4ecB0U8UkEpuGFhRaU88PfEWplyGiBVHBULnHIaWkxWGcGNRkbiTH1Rx2h2Aw3qxV8CotJg9Az%2FB3mLp%2FyCm9eOwzt9X1T2uagU%2Bfipm1gqsjPOcsMMO93c0GOqUBF8HYkpXYAeV11hR%2FB11peu83HYM%2FpOJiSYvGVVLIbzfIdm4lrl7fBUQ2d80TSru6f%2BnjZJZ3nrZZFWKKsP0s%2Bb2vljHNx%2B%2F5JWOcXLxmofIkNyPNIZJfMyyWJdAo8p2PLlPxFotvpVOE4vDg5zxCHnvZjPnYnBnihNScvntoDo2%2BXq%2F7ItG8w4uo8fXokze6fEeU1SN8k7c4FexSW6b2q3y23GtK&X-Amz-Signature=f85eb069177eba6dd61b5748c874157c745a40cd503267985dd2d8a2815e6b3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A5E55P4%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQD5vpHHQbUwvo8cUijc%2F%2FqFup1ONA9%2BOG%2BaA1EaE0NpnwIgLgt2NnxPhGK32cmmuZABGm7QQzW6wVikT50foU%2B0cnwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvg7NTbBlZsEM2g2SrcA27FJZ1L%2FP5k6vztLIusIF25M0rSAG3zdjSwx1ixk9dAsQDCdDCmUcEl1c3TqQpqki52pUTkU%2F3gwzRASIL5AQlWfHAl%2Fjx%2Fg2JrTVlSJ6GQirC6jnHpp2oy1J32xtHpvWh4h0ejqCtiD%2FS8ye2ym4a7JEEza6ifJNzRGFNSMcGv7n4Ay5jlDwKUMhuS%2BvCf%2BmGBCiXJFmUuOknuNYortTSCtMoUS%2B1ym7M9%2FOa1z7HK0qK%2B8w50o6usbWBqXQ4qrXP1P3GjV5Bmnf8tS6Mg56N4XsS4r0sDWrRP8%2B2ZeF5kmp4cALLPUK1xDyvPPz4eFLQlrb3WFmzF4yC%2BNOJx0r33G7mADn5KYDMahdsMlrpbcJxs4qEEireJ%2BMxF5vJ419%2BhCTysATyP11a4N6gXplEIKO%2Byl20m3bDGKQ0TmIC5pf4doCjiNgeCCqFDOCgyaam87cC4KmFnjTribL2yuc8EPnWLLfktPKkAMmGdMRyIRftxuB01es%2FytYJ%2FQMHcC%2FxRdYXNiHy4ecB0U8UkEpuGFhRaU88PfEWplyGiBVHBULnHIaWkxWGcGNRkbiTH1Rx2h2Aw3qxV8CotJg9Az%2FB3mLp%2FyCm9eOwzt9X1T2uagU%2Bfipm1gqsjPOcsMMO93c0GOqUBF8HYkpXYAeV11hR%2FB11peu83HYM%2FpOJiSYvGVVLIbzfIdm4lrl7fBUQ2d80TSru6f%2BnjZJZ3nrZZFWKKsP0s%2Bb2vljHNx%2B%2F5JWOcXLxmofIkNyPNIZJfMyyWJdAo8p2PLlPxFotvpVOE4vDg5zxCHnvZjPnYnBnihNScvntoDo2%2BXq%2F7ItG8w4uo8fXokze6fEeU1SN8k7c4FexSW6b2q3y23GtK&X-Amz-Signature=b59739658eeb07c5aef0b0efa89aa92c3c879a09f1fb5f216cc038a6351b9755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

