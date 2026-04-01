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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEIXEWS%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIL8l11Yar3VEVUD2T0xYc67XqynI3RAfiyNID70hyrgIgQWH3BWUc8m3%2FyBxYXRhd7xbfJYwPimkCNURTGBInrvYq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDBfkNHBA5c3rXSQ3DyrcAz7RfksuXjukNPLQkWR75TvVGkw6Ci0y89Cvt266%2BfeESCFdM7CRpXSGTp9Gn7%2BJTCN56lMRzyjHfJr6X2zFAGY2SnEF8eV%2BPzSGTuN4t9lV3JvMGzx9UKRZmpMWFNfenX0lASqdACvOUxEuil04vUmwKqrsbRHoWDwOEb2QQCeV1JgPfb%2FyLjsbpKvOVdhFpnq%2B%2Fm6tylyp6FpL9qCuBFaknX3QmMd%2BZJQS4JAynCjOIwlexf3Ih9p4If2Jf76pDhslkVgO3gFG0k%2Fu6vnR4g42g2CHRw4H1lVXqguPnwmSQdszWnIbAKium7GqNWX1DIkUIe%2BrpIi9JOOJ0Ftnu4lqt5ofWujOr53D0WwvSsPvhz2fY%2FmpJ%2B5Cft74kpmn9vXvca2wJdOM94%2BhdPAxKcTmBiivn6lcXc%2BkmFF8CTBXq%2F9muA5e0kPzM2U3l%2FxPnxnXAQpuhuOOiCBhwml9fLk17QzF8t73JIBYaNpCNZWD9Iol2adXhP%2FE1nERj4bXDAJaGJEgJp5hbCt8ZhUJO8jO9Oyk4P5lc2M6MJf1uTvaG2DyQc11Ysydpfm%2BZJV7%2F72ZYV2l1D5VD5Y%2FX6jJchseHHTSFqWMd3hMYiJOUiKENoBvHVHebserFdVlMISgss4GOqUBVcpHVYQ5KDLupV8TjdA91y0yNAfWdDQLRBg5%2BTTo8CWZoIuH%2BurcJxub18V9BrznhMdhoKtFR%2BgJB7VVQaPou09GpvnAegsDBzuGvDmiIMkkpSxNbHN6s5tOnVOo8ZPiroKiudlpHMoCLY%2FI9VI1UvPQqYhtfUmONG%2BiywDKiV%2FMrf46%2F%2FT9qo4CySBiZAlidHgjCgF8zaY3yG5uvVpRTxSnhldH&X-Amz-Signature=07b04d037728a0c493321e1892393916c6875bac77054abb722afbac4e66bfca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEIXEWS%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIL8l11Yar3VEVUD2T0xYc67XqynI3RAfiyNID70hyrgIgQWH3BWUc8m3%2FyBxYXRhd7xbfJYwPimkCNURTGBInrvYq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDBfkNHBA5c3rXSQ3DyrcAz7RfksuXjukNPLQkWR75TvVGkw6Ci0y89Cvt266%2BfeESCFdM7CRpXSGTp9Gn7%2BJTCN56lMRzyjHfJr6X2zFAGY2SnEF8eV%2BPzSGTuN4t9lV3JvMGzx9UKRZmpMWFNfenX0lASqdACvOUxEuil04vUmwKqrsbRHoWDwOEb2QQCeV1JgPfb%2FyLjsbpKvOVdhFpnq%2B%2Fm6tylyp6FpL9qCuBFaknX3QmMd%2BZJQS4JAynCjOIwlexf3Ih9p4If2Jf76pDhslkVgO3gFG0k%2Fu6vnR4g42g2CHRw4H1lVXqguPnwmSQdszWnIbAKium7GqNWX1DIkUIe%2BrpIi9JOOJ0Ftnu4lqt5ofWujOr53D0WwvSsPvhz2fY%2FmpJ%2B5Cft74kpmn9vXvca2wJdOM94%2BhdPAxKcTmBiivn6lcXc%2BkmFF8CTBXq%2F9muA5e0kPzM2U3l%2FxPnxnXAQpuhuOOiCBhwml9fLk17QzF8t73JIBYaNpCNZWD9Iol2adXhP%2FE1nERj4bXDAJaGJEgJp5hbCt8ZhUJO8jO9Oyk4P5lc2M6MJf1uTvaG2DyQc11Ysydpfm%2BZJV7%2F72ZYV2l1D5VD5Y%2FX6jJchseHHTSFqWMd3hMYiJOUiKENoBvHVHebserFdVlMISgss4GOqUBVcpHVYQ5KDLupV8TjdA91y0yNAfWdDQLRBg5%2BTTo8CWZoIuH%2BurcJxub18V9BrznhMdhoKtFR%2BgJB7VVQaPou09GpvnAegsDBzuGvDmiIMkkpSxNbHN6s5tOnVOo8ZPiroKiudlpHMoCLY%2FI9VI1UvPQqYhtfUmONG%2BiywDKiV%2FMrf46%2F%2FT9qo4CySBiZAlidHgjCgF8zaY3yG5uvVpRTxSnhldH&X-Amz-Signature=9603261cf73d9246974cfffbf3ef5a63eb13355f05d0d7ce2fc4e29bcbd6dceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMEIXEWS%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIL8l11Yar3VEVUD2T0xYc67XqynI3RAfiyNID70hyrgIgQWH3BWUc8m3%2FyBxYXRhd7xbfJYwPimkCNURTGBInrvYq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDBfkNHBA5c3rXSQ3DyrcAz7RfksuXjukNPLQkWR75TvVGkw6Ci0y89Cvt266%2BfeESCFdM7CRpXSGTp9Gn7%2BJTCN56lMRzyjHfJr6X2zFAGY2SnEF8eV%2BPzSGTuN4t9lV3JvMGzx9UKRZmpMWFNfenX0lASqdACvOUxEuil04vUmwKqrsbRHoWDwOEb2QQCeV1JgPfb%2FyLjsbpKvOVdhFpnq%2B%2Fm6tylyp6FpL9qCuBFaknX3QmMd%2BZJQS4JAynCjOIwlexf3Ih9p4If2Jf76pDhslkVgO3gFG0k%2Fu6vnR4g42g2CHRw4H1lVXqguPnwmSQdszWnIbAKium7GqNWX1DIkUIe%2BrpIi9JOOJ0Ftnu4lqt5ofWujOr53D0WwvSsPvhz2fY%2FmpJ%2B5Cft74kpmn9vXvca2wJdOM94%2BhdPAxKcTmBiivn6lcXc%2BkmFF8CTBXq%2F9muA5e0kPzM2U3l%2FxPnxnXAQpuhuOOiCBhwml9fLk17QzF8t73JIBYaNpCNZWD9Iol2adXhP%2FE1nERj4bXDAJaGJEgJp5hbCt8ZhUJO8jO9Oyk4P5lc2M6MJf1uTvaG2DyQc11Ysydpfm%2BZJV7%2F72ZYV2l1D5VD5Y%2FX6jJchseHHTSFqWMd3hMYiJOUiKENoBvHVHebserFdVlMISgss4GOqUBVcpHVYQ5KDLupV8TjdA91y0yNAfWdDQLRBg5%2BTTo8CWZoIuH%2BurcJxub18V9BrznhMdhoKtFR%2BgJB7VVQaPou09GpvnAegsDBzuGvDmiIMkkpSxNbHN6s5tOnVOo8ZPiroKiudlpHMoCLY%2FI9VI1UvPQqYhtfUmONG%2BiywDKiV%2FMrf46%2F%2FT9qo4CySBiZAlidHgjCgF8zaY3yG5uvVpRTxSnhldH&X-Amz-Signature=5fd128a78724ac63b1266c56cce09d522af7de9893bdf36d2515c8b60ad33feb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

