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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR237IO6%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU1YhMvEe1ED4aUE9xrthDLcrbMGPcgQ8odC7iFdpd0QIgB4CJGw6W%2BXal8jx7lBeM4BSB5K16w83V6zNoZi%2FTwKUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMMRUjT5VSjIj%2FGU3SrcA6UAi6KVZe0zva8K3YKAr5egSSAzMy7YKLr061OSbtHwC9S2qwmzzO7rJUx4sm39ekeatXFKN%2FmIb%2FiXEI%2Fl0%2BPj70M6Lp2ifku0SU7K89B8ftymTuAsbkXiHm0H0CJGMzBbX1OjIB3ijYDurast8b3CUmilIf2hMVj3tSV6AsISxgOAKAHGhK7L150ZV8pNuwhQxBfLa97vTwtlRU2rfuTL%2B5M6cjuQLwf4DzMkZwMApyRdGsqFWlh7bbsVoHZoqXadP1lVr8qHrdo%2FSwBby0PGBKgOXP0j%2BVr1M6aybVLDRXOz5GGy9cCTKW1a%2FaFjiu4DLjjqsiqk5sQtsWaFQPOD6Dve3tudub20lam5KjXwcXbnYJIB65q0SU7lUk1g3SqY%2BIWc%2F2YkRBmkXBQLmKZENtuS5zYvJKL7yACUuPYYapTsb5rox%2B4Y0RnAsnoI9gN%2FjsxINgnguVPi6C0hk%2BC8rh%2Bn1VmHKDRCzLfyOzCBuO1rO1V1%2BBWpnpuDKC2WDbVegLcs%2FuJz25AUmTKNUt2nTipsTngULRQ3m5zhzyCOGET3oiTwOCzZUV1TPpa6VO5WjpukQZc24JuPuLNjKX1M45IeCNn643SSPwWC39eTeHW9HhzZ30CiThoOMKjk8coGOqUB9Myudlx%2FBK7L24dE%2BIddO%2B8aAbt2hi4%2FeSL1DlT5Q63DS8ra3aXIeYy%2BjbLOjZY4WFBJ7vnaMoRgpxfIj5nPbHtucej0RU3DzsGnp1RO1%2BLsh5eaPJcZ%2FGaeI5x2GzHu0G%2BlfZbifnBe77Cgsz%2FfVPlymbk%2BAUvUn03%2BISPBDuDGTfT2S4MZmKneYVMiBlDSxchnTyxpxxogZqcHEJ9gduvlgfHT&X-Amz-Signature=5765ba85c4cfff65a53dc7fd3b17e6fd7cbf920796bd9bba4bb1ba07d816e566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR237IO6%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU1YhMvEe1ED4aUE9xrthDLcrbMGPcgQ8odC7iFdpd0QIgB4CJGw6W%2BXal8jx7lBeM4BSB5K16w83V6zNoZi%2FTwKUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMMRUjT5VSjIj%2FGU3SrcA6UAi6KVZe0zva8K3YKAr5egSSAzMy7YKLr061OSbtHwC9S2qwmzzO7rJUx4sm39ekeatXFKN%2FmIb%2FiXEI%2Fl0%2BPj70M6Lp2ifku0SU7K89B8ftymTuAsbkXiHm0H0CJGMzBbX1OjIB3ijYDurast8b3CUmilIf2hMVj3tSV6AsISxgOAKAHGhK7L150ZV8pNuwhQxBfLa97vTwtlRU2rfuTL%2B5M6cjuQLwf4DzMkZwMApyRdGsqFWlh7bbsVoHZoqXadP1lVr8qHrdo%2FSwBby0PGBKgOXP0j%2BVr1M6aybVLDRXOz5GGy9cCTKW1a%2FaFjiu4DLjjqsiqk5sQtsWaFQPOD6Dve3tudub20lam5KjXwcXbnYJIB65q0SU7lUk1g3SqY%2BIWc%2F2YkRBmkXBQLmKZENtuS5zYvJKL7yACUuPYYapTsb5rox%2B4Y0RnAsnoI9gN%2FjsxINgnguVPi6C0hk%2BC8rh%2Bn1VmHKDRCzLfyOzCBuO1rO1V1%2BBWpnpuDKC2WDbVegLcs%2FuJz25AUmTKNUt2nTipsTngULRQ3m5zhzyCOGET3oiTwOCzZUV1TPpa6VO5WjpukQZc24JuPuLNjKX1M45IeCNn643SSPwWC39eTeHW9HhzZ30CiThoOMKjk8coGOqUB9Myudlx%2FBK7L24dE%2BIddO%2B8aAbt2hi4%2FeSL1DlT5Q63DS8ra3aXIeYy%2BjbLOjZY4WFBJ7vnaMoRgpxfIj5nPbHtucej0RU3DzsGnp1RO1%2BLsh5eaPJcZ%2FGaeI5x2GzHu0G%2BlfZbifnBe77Cgsz%2FfVPlymbk%2BAUvUn03%2BISPBDuDGTfT2S4MZmKneYVMiBlDSxchnTyxpxxogZqcHEJ9gduvlgfHT&X-Amz-Signature=ddea9c35a1df6a145067d6cbe5def3513a445227e860f66ad02ceaf8ce3e93b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR237IO6%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU1YhMvEe1ED4aUE9xrthDLcrbMGPcgQ8odC7iFdpd0QIgB4CJGw6W%2BXal8jx7lBeM4BSB5K16w83V6zNoZi%2FTwKUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMMRUjT5VSjIj%2FGU3SrcA6UAi6KVZe0zva8K3YKAr5egSSAzMy7YKLr061OSbtHwC9S2qwmzzO7rJUx4sm39ekeatXFKN%2FmIb%2FiXEI%2Fl0%2BPj70M6Lp2ifku0SU7K89B8ftymTuAsbkXiHm0H0CJGMzBbX1OjIB3ijYDurast8b3CUmilIf2hMVj3tSV6AsISxgOAKAHGhK7L150ZV8pNuwhQxBfLa97vTwtlRU2rfuTL%2B5M6cjuQLwf4DzMkZwMApyRdGsqFWlh7bbsVoHZoqXadP1lVr8qHrdo%2FSwBby0PGBKgOXP0j%2BVr1M6aybVLDRXOz5GGy9cCTKW1a%2FaFjiu4DLjjqsiqk5sQtsWaFQPOD6Dve3tudub20lam5KjXwcXbnYJIB65q0SU7lUk1g3SqY%2BIWc%2F2YkRBmkXBQLmKZENtuS5zYvJKL7yACUuPYYapTsb5rox%2B4Y0RnAsnoI9gN%2FjsxINgnguVPi6C0hk%2BC8rh%2Bn1VmHKDRCzLfyOzCBuO1rO1V1%2BBWpnpuDKC2WDbVegLcs%2FuJz25AUmTKNUt2nTipsTngULRQ3m5zhzyCOGET3oiTwOCzZUV1TPpa6VO5WjpukQZc24JuPuLNjKX1M45IeCNn643SSPwWC39eTeHW9HhzZ30CiThoOMKjk8coGOqUB9Myudlx%2FBK7L24dE%2BIddO%2B8aAbt2hi4%2FeSL1DlT5Q63DS8ra3aXIeYy%2BjbLOjZY4WFBJ7vnaMoRgpxfIj5nPbHtucej0RU3DzsGnp1RO1%2BLsh5eaPJcZ%2FGaeI5x2GzHu0G%2BlfZbifnBe77Cgsz%2FfVPlymbk%2BAUvUn03%2BISPBDuDGTfT2S4MZmKneYVMiBlDSxchnTyxpxxogZqcHEJ9gduvlgfHT&X-Amz-Signature=f490ce138315dfcb679909095c38a3541f475272f840d2f089865fad42a9ed69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

