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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYENWFC7%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIDZ8YOOprOZFeRzYKXFvhuTDUlp9kXAdZH9bQBJGgmhbAiEAwbRvpr5%2F%2B0Yu6Az2Bvq6tdD1taNEdjAnRZl5Qly9tnAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJ1VtzKAXNaxqRRruircA27lVDhfugbITqHDRWlsmz5TB0zaC4bQqE2QygZsWc2FEkGy%2FA0u8BO8QUPiTnSIA8H0OTtdIl3UNrv6TlL5aykiWdBObjkcgL6%2B52oUY2kj9SrUJs2amcL6HbdEl0Ukyyt8LDzCS4BPipQk4p5UrSL%2FFZ6LuajldaoKTzMzXqszOFNokrn4KzFLNKYM7h5WaPS%2B3ra%2BHQ%2Ff2AqBZRkaWVIMK9CPUJGM1orGBIktges9m1Lbakp1ttH%2BoEKsEUCNKSI55pX3bYRvi1T14msDLDwR1Xdr%2BW0%2FzUj3APUKcgdMofq0LbNMlLP%2FPzMYBZvAdHddYndzLvxtG94O8putXdU%2BfhckTIluIraLL0t97uetF3%2B2ARXDXYkN%2BFHBFgcJ0bry54l%2BlJ7dT8pccQd3KTTCWhESOJwYALFeBt8q7qWG1SNlTulq%2FNzgYA8WMc6X2W3EOYR891siXiDSPKrSMcZsJirUSXqlNhn1KMu%2BTofL5eWhhYOqrD549RJoUPf0rpkBbayN9aqFPjCmaagvCmfjEWEolBBYMRUBnF3XwRXdx06icD0QLRt1LEVf0ouzbV2tL%2BPy%2Bw2kHvGo1MOlCo%2BXR6Ae3IUOc7f6ubXSQ3BAyrsyfRH%2BlqPffWOWMLGkssoGOqUBsmQ7co1rC2qLzd0r6gtJr3YMJSdGbEseGeHjTQ5HOdhcG0lkACxcDP3hKYUPR3KCNtNvnX1lkNEx2%2F%2FVcyRi7eAxHmjlIHUIGHGlvLHYfY6kdRhKeyQGBo7Rn8c3KpY776D%2F5GEfcNjiHw%2FkY5eGtgwgGthi9pLhsCKnj8Bll2rZsZAJcSUFIkvcHfsXjIZe9Gu5O3aunSBtGLifKZU4r65GIXOV&X-Amz-Signature=0bfad2e9cdbe3d2895f0a1253adc6b8d53d7828ef3f0b19dbe1e9c598ee8e45a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYENWFC7%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIDZ8YOOprOZFeRzYKXFvhuTDUlp9kXAdZH9bQBJGgmhbAiEAwbRvpr5%2F%2B0Yu6Az2Bvq6tdD1taNEdjAnRZl5Qly9tnAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJ1VtzKAXNaxqRRruircA27lVDhfugbITqHDRWlsmz5TB0zaC4bQqE2QygZsWc2FEkGy%2FA0u8BO8QUPiTnSIA8H0OTtdIl3UNrv6TlL5aykiWdBObjkcgL6%2B52oUY2kj9SrUJs2amcL6HbdEl0Ukyyt8LDzCS4BPipQk4p5UrSL%2FFZ6LuajldaoKTzMzXqszOFNokrn4KzFLNKYM7h5WaPS%2B3ra%2BHQ%2Ff2AqBZRkaWVIMK9CPUJGM1orGBIktges9m1Lbakp1ttH%2BoEKsEUCNKSI55pX3bYRvi1T14msDLDwR1Xdr%2BW0%2FzUj3APUKcgdMofq0LbNMlLP%2FPzMYBZvAdHddYndzLvxtG94O8putXdU%2BfhckTIluIraLL0t97uetF3%2B2ARXDXYkN%2BFHBFgcJ0bry54l%2BlJ7dT8pccQd3KTTCWhESOJwYALFeBt8q7qWG1SNlTulq%2FNzgYA8WMc6X2W3EOYR891siXiDSPKrSMcZsJirUSXqlNhn1KMu%2BTofL5eWhhYOqrD549RJoUPf0rpkBbayN9aqFPjCmaagvCmfjEWEolBBYMRUBnF3XwRXdx06icD0QLRt1LEVf0ouzbV2tL%2BPy%2Bw2kHvGo1MOlCo%2BXR6Ae3IUOc7f6ubXSQ3BAyrsyfRH%2BlqPffWOWMLGkssoGOqUBsmQ7co1rC2qLzd0r6gtJr3YMJSdGbEseGeHjTQ5HOdhcG0lkACxcDP3hKYUPR3KCNtNvnX1lkNEx2%2F%2FVcyRi7eAxHmjlIHUIGHGlvLHYfY6kdRhKeyQGBo7Rn8c3KpY776D%2F5GEfcNjiHw%2FkY5eGtgwgGthi9pLhsCKnj8Bll2rZsZAJcSUFIkvcHfsXjIZe9Gu5O3aunSBtGLifKZU4r65GIXOV&X-Amz-Signature=1e1042f77e2d989e631afeb46ad43519ee263ed91ed14b1c0da8e5c27d4cc635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYENWFC7%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIDZ8YOOprOZFeRzYKXFvhuTDUlp9kXAdZH9bQBJGgmhbAiEAwbRvpr5%2F%2B0Yu6Az2Bvq6tdD1taNEdjAnRZl5Qly9tnAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJ1VtzKAXNaxqRRruircA27lVDhfugbITqHDRWlsmz5TB0zaC4bQqE2QygZsWc2FEkGy%2FA0u8BO8QUPiTnSIA8H0OTtdIl3UNrv6TlL5aykiWdBObjkcgL6%2B52oUY2kj9SrUJs2amcL6HbdEl0Ukyyt8LDzCS4BPipQk4p5UrSL%2FFZ6LuajldaoKTzMzXqszOFNokrn4KzFLNKYM7h5WaPS%2B3ra%2BHQ%2Ff2AqBZRkaWVIMK9CPUJGM1orGBIktges9m1Lbakp1ttH%2BoEKsEUCNKSI55pX3bYRvi1T14msDLDwR1Xdr%2BW0%2FzUj3APUKcgdMofq0LbNMlLP%2FPzMYBZvAdHddYndzLvxtG94O8putXdU%2BfhckTIluIraLL0t97uetF3%2B2ARXDXYkN%2BFHBFgcJ0bry54l%2BlJ7dT8pccQd3KTTCWhESOJwYALFeBt8q7qWG1SNlTulq%2FNzgYA8WMc6X2W3EOYR891siXiDSPKrSMcZsJirUSXqlNhn1KMu%2BTofL5eWhhYOqrD549RJoUPf0rpkBbayN9aqFPjCmaagvCmfjEWEolBBYMRUBnF3XwRXdx06icD0QLRt1LEVf0ouzbV2tL%2BPy%2Bw2kHvGo1MOlCo%2BXR6Ae3IUOc7f6ubXSQ3BAyrsyfRH%2BlqPffWOWMLGkssoGOqUBsmQ7co1rC2qLzd0r6gtJr3YMJSdGbEseGeHjTQ5HOdhcG0lkACxcDP3hKYUPR3KCNtNvnX1lkNEx2%2F%2FVcyRi7eAxHmjlIHUIGHGlvLHYfY6kdRhKeyQGBo7Rn8c3KpY776D%2F5GEfcNjiHw%2FkY5eGtgwgGthi9pLhsCKnj8Bll2rZsZAJcSUFIkvcHfsXjIZe9Gu5O3aunSBtGLifKZU4r65GIXOV&X-Amz-Signature=8c0881067f69f05cd4e0dafabc23348d936336807f66685c2acb7cbadff4b0d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

