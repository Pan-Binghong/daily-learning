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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCOAJ65Y%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdp9YttxiMbTKkEO5XImN%2FG%2F5ICfb2l7rRc6cDe%2FHVggIhAJJLWoobM2dLNtqQawLn7jjl8b%2FE9VaTZyQ7PEfmRTELKv8DCEoQABoMNjM3NDIzMTgzODA1Igw8Veo2d1pqAV4xJ%2FIq3APGACwgrGvoggUOMGal2wo5cpZ6%2FWfeN6EijiIX7NdqHsL6mo2lgVH6CD%2BmTwRdGUp8T7fKf%2FzJ8hDyF%2Fj1Ic2w4LOhM3Z9CebW%2FiXW3QJvWIMMcHbZoHdTWmvZH%2BbdAj39uinklkjIAp9ZGxPHEuhHC3rPgbiFHAqnfQfH2XnDaKOvUomvBZKeeh0YTIP4IYaoKpaoJdPoIKVcymkvza8hNj2i1V31jcWI8DOdb%2BWFGv78BO5tTQl7qdfG39ppB7mIO8egMyGAZFe69BJyp237bLKkNdxmKnYh17mpftx%2BsNCcp1UvUBtQOVqr0%2BwoMi%2BOHlZZh1YbyYCf0GD5yBkajsq0fPdiCpTU0ysVU1B%2BxMuchDUrGqoJqHYEaz2rQxMA9PQ1TXF5syBP52Ea1cEbVBoT44LExswweP06Mr7I60YpQSZK9I6pmFukB6J7Q%2FCcjIzRXeMENAuHvlO1SMrfwfuhpp%2BYj741g7nY2BN1FCr5Vh%2BCnZe6oVOor%2BHYnAu7egATEjRIaBQNpHRiZftUgwDvLB6p154kHYfrO13sRb3%2BaaujdG6QJoviZVRqdL8AKkUi9XV7Ee3Xtq4%2BCn9lhWJaVVIJoFNvKgS1WchsiB%2BAomSALDu7Psb96jD5247JBjqkAbGAsw8ps1I4rR1szdpqQOl0pPox%2FgS0Ya%2BHfIx1VoY8c0ldW1nkpj3cZLLI6m6f3g7TdMN%2F79Q%2Bp0ejVT8VHLS9C201alk4h8773HB0R8quKPXqADgLHxIxENa28JAQ42bLXzkjimtek8zaD4qHk7r51%2B4OWACUMPSLSOEofHz1BwT%2BkuS9vj9NnuDGH7W8uD5aA%2BO55G0LULf65QR7kFZgdOae&X-Amz-Signature=76b39ec3bd4089fab608346460f3e04a551352515f5536e5a616e5681a4604dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCOAJ65Y%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdp9YttxiMbTKkEO5XImN%2FG%2F5ICfb2l7rRc6cDe%2FHVggIhAJJLWoobM2dLNtqQawLn7jjl8b%2FE9VaTZyQ7PEfmRTELKv8DCEoQABoMNjM3NDIzMTgzODA1Igw8Veo2d1pqAV4xJ%2FIq3APGACwgrGvoggUOMGal2wo5cpZ6%2FWfeN6EijiIX7NdqHsL6mo2lgVH6CD%2BmTwRdGUp8T7fKf%2FzJ8hDyF%2Fj1Ic2w4LOhM3Z9CebW%2FiXW3QJvWIMMcHbZoHdTWmvZH%2BbdAj39uinklkjIAp9ZGxPHEuhHC3rPgbiFHAqnfQfH2XnDaKOvUomvBZKeeh0YTIP4IYaoKpaoJdPoIKVcymkvza8hNj2i1V31jcWI8DOdb%2BWFGv78BO5tTQl7qdfG39ppB7mIO8egMyGAZFe69BJyp237bLKkNdxmKnYh17mpftx%2BsNCcp1UvUBtQOVqr0%2BwoMi%2BOHlZZh1YbyYCf0GD5yBkajsq0fPdiCpTU0ysVU1B%2BxMuchDUrGqoJqHYEaz2rQxMA9PQ1TXF5syBP52Ea1cEbVBoT44LExswweP06Mr7I60YpQSZK9I6pmFukB6J7Q%2FCcjIzRXeMENAuHvlO1SMrfwfuhpp%2BYj741g7nY2BN1FCr5Vh%2BCnZe6oVOor%2BHYnAu7egATEjRIaBQNpHRiZftUgwDvLB6p154kHYfrO13sRb3%2BaaujdG6QJoviZVRqdL8AKkUi9XV7Ee3Xtq4%2BCn9lhWJaVVIJoFNvKgS1WchsiB%2BAomSALDu7Psb96jD5247JBjqkAbGAsw8ps1I4rR1szdpqQOl0pPox%2FgS0Ya%2BHfIx1VoY8c0ldW1nkpj3cZLLI6m6f3g7TdMN%2F79Q%2Bp0ejVT8VHLS9C201alk4h8773HB0R8quKPXqADgLHxIxENa28JAQ42bLXzkjimtek8zaD4qHk7r51%2B4OWACUMPSLSOEofHz1BwT%2BkuS9vj9NnuDGH7W8uD5aA%2BO55G0LULf65QR7kFZgdOae&X-Amz-Signature=0a39a82014dbea1dbeca3c4f1e54307168d95330c80d3cd45b5612de5358a699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCOAJ65Y%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdp9YttxiMbTKkEO5XImN%2FG%2F5ICfb2l7rRc6cDe%2FHVggIhAJJLWoobM2dLNtqQawLn7jjl8b%2FE9VaTZyQ7PEfmRTELKv8DCEoQABoMNjM3NDIzMTgzODA1Igw8Veo2d1pqAV4xJ%2FIq3APGACwgrGvoggUOMGal2wo5cpZ6%2FWfeN6EijiIX7NdqHsL6mo2lgVH6CD%2BmTwRdGUp8T7fKf%2FzJ8hDyF%2Fj1Ic2w4LOhM3Z9CebW%2FiXW3QJvWIMMcHbZoHdTWmvZH%2BbdAj39uinklkjIAp9ZGxPHEuhHC3rPgbiFHAqnfQfH2XnDaKOvUomvBZKeeh0YTIP4IYaoKpaoJdPoIKVcymkvza8hNj2i1V31jcWI8DOdb%2BWFGv78BO5tTQl7qdfG39ppB7mIO8egMyGAZFe69BJyp237bLKkNdxmKnYh17mpftx%2BsNCcp1UvUBtQOVqr0%2BwoMi%2BOHlZZh1YbyYCf0GD5yBkajsq0fPdiCpTU0ysVU1B%2BxMuchDUrGqoJqHYEaz2rQxMA9PQ1TXF5syBP52Ea1cEbVBoT44LExswweP06Mr7I60YpQSZK9I6pmFukB6J7Q%2FCcjIzRXeMENAuHvlO1SMrfwfuhpp%2BYj741g7nY2BN1FCr5Vh%2BCnZe6oVOor%2BHYnAu7egATEjRIaBQNpHRiZftUgwDvLB6p154kHYfrO13sRb3%2BaaujdG6QJoviZVRqdL8AKkUi9XV7Ee3Xtq4%2BCn9lhWJaVVIJoFNvKgS1WchsiB%2BAomSALDu7Psb96jD5247JBjqkAbGAsw8ps1I4rR1szdpqQOl0pPox%2FgS0Ya%2BHfIx1VoY8c0ldW1nkpj3cZLLI6m6f3g7TdMN%2F79Q%2Bp0ejVT8VHLS9C201alk4h8773HB0R8quKPXqADgLHxIxENa28JAQ42bLXzkjimtek8zaD4qHk7r51%2B4OWACUMPSLSOEofHz1BwT%2BkuS9vj9NnuDGH7W8uD5aA%2BO55G0LULf65QR7kFZgdOae&X-Amz-Signature=302c003b2dcf05600fd6d8c31ae409aa088adf103bc2e68f01a3233a896cec1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

