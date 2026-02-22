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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K6EAE4M%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgrVkVh0uIC8%2FTsh7o5Xa6OBjTJk02l88MMrQlK%2BNGoQIgbG%2BeGypjrNU9rhzhNSzFlxu8BOIi%2B%2Fu0Jjgov%2B0lNqsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3vOP4MiRUcgpI2aircAyBF5yCRNgXRne6ean9gx5okxp0diLfOtv58Tnjdm1icI4WGF5221ttgS3da2aDdlODzuDIf6M9eSmnP1ckQi6Q86gJHAUZQga9zkQvdgKLVObpO2lceUjDdJpIyOpLDsh138ZrkTZrV6tgW%2FbInXcXROQCmi1D%2BqsJf30yd9%2BZ9RGgV1d4QyFrFTauiHlB6WhH0s98crfoRDsTEWsqxFrxD0yDUb%2F8SGf7guvGqlo%2FcH6Os861IlUj2k52cI9jv00lYAKn3fjpER%2BRXffpW139P8voJJ2VMGm%2Bm%2Fgun0p7ifuiicsbqF8lhvbjcyNbBGTgog2aNy2xYL%2BPjBgAiq%2B981M8vfhks6LI53gNZftGpHtjlfgCqFh2iRZzfjGw7H48zNTJSm0AmBIrA1nj9qxHNKTV8BDh%2FroUKnE%2B0XCdwkqelbd7sJv5RNz6tR0oW1dx8xIdVas4OZN795mXCwbVP7Nn9U41%2FQlqb0P5J6ucpsywitBy9vPg6muR%2Fwb%2FRe%2F2WiB5o64oMpiBp9mMzgArmk7Ve0hiCer50ua24hZoIxurM%2Ftbzqy1LBS%2FFZbOtNhS%2F2b%2FcwE73oHe9x2GNj22yXs05uP4R8CISyAYioAbZyJlKTGoiZyVs0Y22MKX06cwGOqUBHH8FigF1TMfA6M3rNpDbC%2B6a%2FoeUZ6rarC2uN0hcEy60LCpXT64FJR%2BacDqz13Xk4VVKd7d%2FWA2MMCSr92KcEqsOUQw4CZEbetpaTPYKXnuz9mysqhNL5qBMakR7NF9PpR2uXJ2mVucO9ElOnz24ucYAzuNk9MWcXKyO0qSV%2B%2FjUXFvQBFo0iua8Fspp56UXtIHUGfQoK7048Qh6ZCq1CNzioWki&X-Amz-Signature=b2ab7224ba83869dedb21a5fab524df6a9531032ea41d2fcf98846b8b6270432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K6EAE4M%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgrVkVh0uIC8%2FTsh7o5Xa6OBjTJk02l88MMrQlK%2BNGoQIgbG%2BeGypjrNU9rhzhNSzFlxu8BOIi%2B%2Fu0Jjgov%2B0lNqsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3vOP4MiRUcgpI2aircAyBF5yCRNgXRne6ean9gx5okxp0diLfOtv58Tnjdm1icI4WGF5221ttgS3da2aDdlODzuDIf6M9eSmnP1ckQi6Q86gJHAUZQga9zkQvdgKLVObpO2lceUjDdJpIyOpLDsh138ZrkTZrV6tgW%2FbInXcXROQCmi1D%2BqsJf30yd9%2BZ9RGgV1d4QyFrFTauiHlB6WhH0s98crfoRDsTEWsqxFrxD0yDUb%2F8SGf7guvGqlo%2FcH6Os861IlUj2k52cI9jv00lYAKn3fjpER%2BRXffpW139P8voJJ2VMGm%2Bm%2Fgun0p7ifuiicsbqF8lhvbjcyNbBGTgog2aNy2xYL%2BPjBgAiq%2B981M8vfhks6LI53gNZftGpHtjlfgCqFh2iRZzfjGw7H48zNTJSm0AmBIrA1nj9qxHNKTV8BDh%2FroUKnE%2B0XCdwkqelbd7sJv5RNz6tR0oW1dx8xIdVas4OZN795mXCwbVP7Nn9U41%2FQlqb0P5J6ucpsywitBy9vPg6muR%2Fwb%2FRe%2F2WiB5o64oMpiBp9mMzgArmk7Ve0hiCer50ua24hZoIxurM%2Ftbzqy1LBS%2FFZbOtNhS%2F2b%2FcwE73oHe9x2GNj22yXs05uP4R8CISyAYioAbZyJlKTGoiZyVs0Y22MKX06cwGOqUBHH8FigF1TMfA6M3rNpDbC%2B6a%2FoeUZ6rarC2uN0hcEy60LCpXT64FJR%2BacDqz13Xk4VVKd7d%2FWA2MMCSr92KcEqsOUQw4CZEbetpaTPYKXnuz9mysqhNL5qBMakR7NF9PpR2uXJ2mVucO9ElOnz24ucYAzuNk9MWcXKyO0qSV%2B%2FjUXFvQBFo0iua8Fspp56UXtIHUGfQoK7048Qh6ZCq1CNzioWki&X-Amz-Signature=1744c4d5c5b58f7f224f78943e12abcd4f4df80140091d19ba507fdc30f19ec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K6EAE4M%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgrVkVh0uIC8%2FTsh7o5Xa6OBjTJk02l88MMrQlK%2BNGoQIgbG%2BeGypjrNU9rhzhNSzFlxu8BOIi%2B%2Fu0Jjgov%2B0lNqsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL3vOP4MiRUcgpI2aircAyBF5yCRNgXRne6ean9gx5okxp0diLfOtv58Tnjdm1icI4WGF5221ttgS3da2aDdlODzuDIf6M9eSmnP1ckQi6Q86gJHAUZQga9zkQvdgKLVObpO2lceUjDdJpIyOpLDsh138ZrkTZrV6tgW%2FbInXcXROQCmi1D%2BqsJf30yd9%2BZ9RGgV1d4QyFrFTauiHlB6WhH0s98crfoRDsTEWsqxFrxD0yDUb%2F8SGf7guvGqlo%2FcH6Os861IlUj2k52cI9jv00lYAKn3fjpER%2BRXffpW139P8voJJ2VMGm%2Bm%2Fgun0p7ifuiicsbqF8lhvbjcyNbBGTgog2aNy2xYL%2BPjBgAiq%2B981M8vfhks6LI53gNZftGpHtjlfgCqFh2iRZzfjGw7H48zNTJSm0AmBIrA1nj9qxHNKTV8BDh%2FroUKnE%2B0XCdwkqelbd7sJv5RNz6tR0oW1dx8xIdVas4OZN795mXCwbVP7Nn9U41%2FQlqb0P5J6ucpsywitBy9vPg6muR%2Fwb%2FRe%2F2WiB5o64oMpiBp9mMzgArmk7Ve0hiCer50ua24hZoIxurM%2Ftbzqy1LBS%2FFZbOtNhS%2F2b%2FcwE73oHe9x2GNj22yXs05uP4R8CISyAYioAbZyJlKTGoiZyVs0Y22MKX06cwGOqUBHH8FigF1TMfA6M3rNpDbC%2B6a%2FoeUZ6rarC2uN0hcEy60LCpXT64FJR%2BacDqz13Xk4VVKd7d%2FWA2MMCSr92KcEqsOUQw4CZEbetpaTPYKXnuz9mysqhNL5qBMakR7NF9PpR2uXJ2mVucO9ElOnz24ucYAzuNk9MWcXKyO0qSV%2B%2FjUXFvQBFo0iua8Fspp56UXtIHUGfQoK7048Qh6ZCq1CNzioWki&X-Amz-Signature=ee4ac1a820f417b2d5f6657006af23dd71d0e0d9f8009b9c1dafed98135bb836&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

