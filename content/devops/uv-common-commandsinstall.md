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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOMWR77%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCvRRzQIdBL%2BRnclP4yGOPOfSAI2ZmqgHsMuswspmfWUgIgeA12f3SGtgtGmlufMtEkxhWv5Zj4Faf4ePQ2VCM%2F2TEq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDM3m2pcDrMD%2FiLIoJSrcA7djYN%2Fm50Gf8q1vK5gHVoFHCGorwTSdWoEEEouGDUIs4ZmG8yN0lYdBEl23rgbexbg9NfOWN9Eplh1Fpo%2FjNxQ66We%2BS2iHHkb24V1nxBryQOnrdm1R25T3QG9LOLkqdK9%2FHG2JsSOj2PMiKRmD8HWzd1iPSOyRheaKqpzXAw%2F6xYcgZgcBTI9KvO%2Ft%2FPzCsmwI4DU3c0gaOFp8HNihir%2F8ZtF8hgFPrN9Iow9KxUade2qN1%2Bs2qNnXrk%2F%2Fvb7PjxqZRtVHK02yYKirGDYdV13h1wGelLZmn7uIe3rKr6aDRMYcabPAbT8sfy2huwvg3p7%2B52KdCvWtaRarfJxPm8pPuYziLTD9ukRxc91VnNiFUT5iY1YU1Z4rvGSXQr%2F33L56%2BST54j19kiGNB%2BuxfNU%2FQI%2FBNlooPhiioDAY2%2F8v9bI25UHvYj7wPK6RoZlAa6cf5mi%2FL49g4pFi5e3pDrUDY0lj8Qof6ZC3AromEAT%2BobI7qCBeuhwolRa3h6RWE4AZwcRxoUOGpOAA4jjZV%2FN7jm8BGXoWipEDTNJU%2Fj%2BiM%2FWwiSp5U1q476Q6REhP31jyLCPC2CvqWby4oh%2FCuMmZZ1IgI8n64rT1E6s5B%2BNx%2B5eR9%2F6038HgiXUaMNzniswGOqUBCO4k6itEv3JkkDI063owKt%2BCwa6eNS6P55RQ1f0r%2BMG17h5fqkrdCXtpVrs4UVPxWXGAeOeQ98INWtQ1MpyFzSEqM9NDOqIa687%2BJ7afH4vtY%2FuNbic9NR7vwyquqSuMsGynAb9sZBSF%2B%2FlNdDG8gUD%2B9DyMzf4sUUkRoj8FbY%2FENGQkqsG7w5AU09Ufc39lw7IivvSj%2BHgXdqy4g8t8EOmDGEbn&X-Amz-Signature=2012681dacbddbe3bbec495227c4a04abcfc42e6b4b80323677416098e35ab0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOMWR77%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCvRRzQIdBL%2BRnclP4yGOPOfSAI2ZmqgHsMuswspmfWUgIgeA12f3SGtgtGmlufMtEkxhWv5Zj4Faf4ePQ2VCM%2F2TEq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDM3m2pcDrMD%2FiLIoJSrcA7djYN%2Fm50Gf8q1vK5gHVoFHCGorwTSdWoEEEouGDUIs4ZmG8yN0lYdBEl23rgbexbg9NfOWN9Eplh1Fpo%2FjNxQ66We%2BS2iHHkb24V1nxBryQOnrdm1R25T3QG9LOLkqdK9%2FHG2JsSOj2PMiKRmD8HWzd1iPSOyRheaKqpzXAw%2F6xYcgZgcBTI9KvO%2Ft%2FPzCsmwI4DU3c0gaOFp8HNihir%2F8ZtF8hgFPrN9Iow9KxUade2qN1%2Bs2qNnXrk%2F%2Fvb7PjxqZRtVHK02yYKirGDYdV13h1wGelLZmn7uIe3rKr6aDRMYcabPAbT8sfy2huwvg3p7%2B52KdCvWtaRarfJxPm8pPuYziLTD9ukRxc91VnNiFUT5iY1YU1Z4rvGSXQr%2F33L56%2BST54j19kiGNB%2BuxfNU%2FQI%2FBNlooPhiioDAY2%2F8v9bI25UHvYj7wPK6RoZlAa6cf5mi%2FL49g4pFi5e3pDrUDY0lj8Qof6ZC3AromEAT%2BobI7qCBeuhwolRa3h6RWE4AZwcRxoUOGpOAA4jjZV%2FN7jm8BGXoWipEDTNJU%2Fj%2BiM%2FWwiSp5U1q476Q6REhP31jyLCPC2CvqWby4oh%2FCuMmZZ1IgI8n64rT1E6s5B%2BNx%2B5eR9%2F6038HgiXUaMNzniswGOqUBCO4k6itEv3JkkDI063owKt%2BCwa6eNS6P55RQ1f0r%2BMG17h5fqkrdCXtpVrs4UVPxWXGAeOeQ98INWtQ1MpyFzSEqM9NDOqIa687%2BJ7afH4vtY%2FuNbic9NR7vwyquqSuMsGynAb9sZBSF%2B%2FlNdDG8gUD%2B9DyMzf4sUUkRoj8FbY%2FENGQkqsG7w5AU09Ufc39lw7IivvSj%2BHgXdqy4g8t8EOmDGEbn&X-Amz-Signature=4732e4ec19cbb5de4fd874f3d92ef28473cfac440cfaf7ed81292108b88de71f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOMWR77%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCvRRzQIdBL%2BRnclP4yGOPOfSAI2ZmqgHsMuswspmfWUgIgeA12f3SGtgtGmlufMtEkxhWv5Zj4Faf4ePQ2VCM%2F2TEq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDM3m2pcDrMD%2FiLIoJSrcA7djYN%2Fm50Gf8q1vK5gHVoFHCGorwTSdWoEEEouGDUIs4ZmG8yN0lYdBEl23rgbexbg9NfOWN9Eplh1Fpo%2FjNxQ66We%2BS2iHHkb24V1nxBryQOnrdm1R25T3QG9LOLkqdK9%2FHG2JsSOj2PMiKRmD8HWzd1iPSOyRheaKqpzXAw%2F6xYcgZgcBTI9KvO%2Ft%2FPzCsmwI4DU3c0gaOFp8HNihir%2F8ZtF8hgFPrN9Iow9KxUade2qN1%2Bs2qNnXrk%2F%2Fvb7PjxqZRtVHK02yYKirGDYdV13h1wGelLZmn7uIe3rKr6aDRMYcabPAbT8sfy2huwvg3p7%2B52KdCvWtaRarfJxPm8pPuYziLTD9ukRxc91VnNiFUT5iY1YU1Z4rvGSXQr%2F33L56%2BST54j19kiGNB%2BuxfNU%2FQI%2FBNlooPhiioDAY2%2F8v9bI25UHvYj7wPK6RoZlAa6cf5mi%2FL49g4pFi5e3pDrUDY0lj8Qof6ZC3AromEAT%2BobI7qCBeuhwolRa3h6RWE4AZwcRxoUOGpOAA4jjZV%2FN7jm8BGXoWipEDTNJU%2Fj%2BiM%2FWwiSp5U1q476Q6REhP31jyLCPC2CvqWby4oh%2FCuMmZZ1IgI8n64rT1E6s5B%2BNx%2B5eR9%2F6038HgiXUaMNzniswGOqUBCO4k6itEv3JkkDI063owKt%2BCwa6eNS6P55RQ1f0r%2BMG17h5fqkrdCXtpVrs4UVPxWXGAeOeQ98INWtQ1MpyFzSEqM9NDOqIa687%2BJ7afH4vtY%2FuNbic9NR7vwyquqSuMsGynAb9sZBSF%2B%2FlNdDG8gUD%2B9DyMzf4sUUkRoj8FbY%2FENGQkqsG7w5AU09Ufc39lw7IivvSj%2BHgXdqy4g8t8EOmDGEbn&X-Amz-Signature=017fc041a7f67d644d30b6678d4c08cf33dd4ee90c861a9d1e49c26822b6ac52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

