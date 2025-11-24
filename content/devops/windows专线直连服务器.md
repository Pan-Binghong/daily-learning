---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBIB2AEJ%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHF5HmFl7uVJTEB9a1bKLKk3nxGQGpAgCSlRJY3NF04gIgXZqRCP2%2BarZTGdX5PgpakxzFlIvV2HHddBf%2FQ1GEwbQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGJC7%2F7aOD%2F0UEFiVCrcA0LZ2CsvLPgDMyqHNIF%2FRjzAs4PEhvD%2FR82ltpK0D7PY8jajP0IyQuvWetLxSEpP%2FF5rQdCe1W26ANtDbBEoXVgDoWR9%2FFM4xR0hesK%2BQ0V1uuZwhZ3UiNzWo4NEK1uI9M0hWFTpgm953%2FNAfM2q0gCtEzdLp9fFYHkSXA2EyVRSq0mj8zYjh9v9avZ1uSVoHSH5oWa%2BvvebyFB7BxdcBoj1fGnFiLbk5ygdp2ZS%2FHsSaJF280mO1cEC%2BJgE5f%2F6vk%2FiDSQtS%2FjumUf2PkUfGdOjSQpqoAK%2BVkTEX%2BlO2ZILviioEIdn2IDDU78%2BkNjqDtPrLV3vZJcyYC25wQUdidROdJPKWX9ub0Vg9VvktA4VdIjvofHIW2k7sILut7aWq%2BgcJOoyI0RK0KhRrbqT9YLwkRoBnxetAo5XIvX6BimK%2BqJRmx6x3DTdrAVaaEDjPy%2FaDPx0U4VY64o5FCNrWspmbtP%2BWrhXh1TmMLyRw8%2F6Z87sFXd%2BEDLTENela8hvTCvkU4WJw0omUihNuUhhsXNWeXYXXuQ3UxFg4iXZ467YHxXAzpjzqPyvnFgVF9Y598eDjYvQ1dPw1akGLZvohp11uLdVNcmTzfvZ8M6tjPu0oOy57xKP3xILPB0cMJndjskGOqUBuyU7SMxOz4cwaS0%2FIVmg6jsZrhQ2rNo2SwXf3v1NtYyveBXWkOfUTyuNFdxb%2BMl%2B%2Bp%2BR27IjCdd8OSeql%2BOVr9FDHoB1KNtYXqkpgE2UfcPzU61WMgGfUtJ12lXhqWVM%2BADKnTNWoATTxLd2Ni3A20Gc%2BTN7rCtNvsp1VusDtJvDw5XaOKGriZQzh6B2q1FEsmYDpmg41QASzOcp2MnHHqX3zO8b&X-Amz-Signature=8d6dd4d1a6b95cab225ca9aa71039f97d9059e347ca07f294645ce44e5360ec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

