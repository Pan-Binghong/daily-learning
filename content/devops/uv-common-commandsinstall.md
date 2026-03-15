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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=ce3b853d89757034d36c56eea0d798adb7ca5b5b4c4cd5185c0a063c92755b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=2fed172d005b00d86ce839fb31a095bccbe5a5a222bbd51ce0304ffce6e718cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=15f4e7e6afeab0986e878d8ddf2ff3f03aa92329c99db5e94ef1928af136a672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

