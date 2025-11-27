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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFCX3IVW%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmhcg7JqZnlzJC%2BhW%2FUVjbKEJJ3tRXBWbeUIIyPEYmQwIgVq6I7vOfI3HL%2BSItLo9B96q5PLvSDzAVqVvr23rwrc8qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLO6zqOEzuEo22XpeCrcA%2B3iICTv9PS75q%2FWcoO3Bcvzv5bixwTmpEXPLwZDJg7LynAZc25NHNK%2FLrBZphnMAGisJrp11Z0gKGcjeGg%2FexraUdklahlC8H2dWovChWYEX7GSjN8amF4JBv04tgGI9uCjqiVhssb7gz0XSEI8gFKFXB79%2BxcUlxLbLLnYlQkp4ZoyP2rYJE%2F5mMNaKOhwH%2BfrLtvefwhl5rzvSUZp6dMCh1lh483dvfoI1u4KqbBqySBuSA29CJ%2B7xziHfRMWbmNbfUEYgLWAL8P4XxsT57giuuk9XYCcfA%2BdL3E2mdb7uTJtfhGLucdM3NKCU5y0KzYj4RlxcHk4SVqNc3KfUldJY8h1V6eQ06IkmGvDKO0ay3Ef%2FCqB8ttfrNgjNFXq4SnPHUQHFP140nQvMtCVy0tDLS9VjNx2w4ujh2KfFutpp90XzJv1%2BlBB2p3GB1U4btgtp4LN3YSpUZKv1E8nDYx9dA0PJrKM21lHos4dCbsiFrtN1nKzixHyk8p38xviYnDLtJm7knccL%2FuVnrf1uPJf8s0MFsnKTewDo1QK270%2FjkvqDvtTF2aDLgFQY%2FRFCkXjzVqRSB6aijJ193kpKpN15280uv%2Bn%2B6ehwp16y4YmFsc5qAW5D6v6lGOpMNLMnskGOqUBmTxT1rsx4ZqBikjv1IdEeRBYOpqUM1tQ2%2BA2wmJOhQGTk3gfJ5ou5RDGuM9tlBkdIOWBBYUAsWnsmxnEMWp%2B37YCuF7u7qiKQHMQnTRkNpepw%2FfDiXi59n8sPFg7eY2SrnvOIbSj6J7KS%2BZfl0MktIiUmZaY2wX0bbv9X1zH6%2FB4R34F2MMDncpOoVMJ2Btnq%2Bqlf1h8e87eGSYAgt8%2Beg%2BpW9E8&X-Amz-Signature=9969e938ef0d3eb2d129439013bacabf1fd850cadd6ff0907620523e12731433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFCX3IVW%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmhcg7JqZnlzJC%2BhW%2FUVjbKEJJ3tRXBWbeUIIyPEYmQwIgVq6I7vOfI3HL%2BSItLo9B96q5PLvSDzAVqVvr23rwrc8qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLO6zqOEzuEo22XpeCrcA%2B3iICTv9PS75q%2FWcoO3Bcvzv5bixwTmpEXPLwZDJg7LynAZc25NHNK%2FLrBZphnMAGisJrp11Z0gKGcjeGg%2FexraUdklahlC8H2dWovChWYEX7GSjN8amF4JBv04tgGI9uCjqiVhssb7gz0XSEI8gFKFXB79%2BxcUlxLbLLnYlQkp4ZoyP2rYJE%2F5mMNaKOhwH%2BfrLtvefwhl5rzvSUZp6dMCh1lh483dvfoI1u4KqbBqySBuSA29CJ%2B7xziHfRMWbmNbfUEYgLWAL8P4XxsT57giuuk9XYCcfA%2BdL3E2mdb7uTJtfhGLucdM3NKCU5y0KzYj4RlxcHk4SVqNc3KfUldJY8h1V6eQ06IkmGvDKO0ay3Ef%2FCqB8ttfrNgjNFXq4SnPHUQHFP140nQvMtCVy0tDLS9VjNx2w4ujh2KfFutpp90XzJv1%2BlBB2p3GB1U4btgtp4LN3YSpUZKv1E8nDYx9dA0PJrKM21lHos4dCbsiFrtN1nKzixHyk8p38xviYnDLtJm7knccL%2FuVnrf1uPJf8s0MFsnKTewDo1QK270%2FjkvqDvtTF2aDLgFQY%2FRFCkXjzVqRSB6aijJ193kpKpN15280uv%2Bn%2B6ehwp16y4YmFsc5qAW5D6v6lGOpMNLMnskGOqUBmTxT1rsx4ZqBikjv1IdEeRBYOpqUM1tQ2%2BA2wmJOhQGTk3gfJ5ou5RDGuM9tlBkdIOWBBYUAsWnsmxnEMWp%2B37YCuF7u7qiKQHMQnTRkNpepw%2FfDiXi59n8sPFg7eY2SrnvOIbSj6J7KS%2BZfl0MktIiUmZaY2wX0bbv9X1zH6%2FB4R34F2MMDncpOoVMJ2Btnq%2Bqlf1h8e87eGSYAgt8%2Beg%2BpW9E8&X-Amz-Signature=03fe9ca4d7a481f744c3d3e47c679a05b917abf7d98cd882f2092c925ef63ae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFCX3IVW%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmhcg7JqZnlzJC%2BhW%2FUVjbKEJJ3tRXBWbeUIIyPEYmQwIgVq6I7vOfI3HL%2BSItLo9B96q5PLvSDzAVqVvr23rwrc8qiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLO6zqOEzuEo22XpeCrcA%2B3iICTv9PS75q%2FWcoO3Bcvzv5bixwTmpEXPLwZDJg7LynAZc25NHNK%2FLrBZphnMAGisJrp11Z0gKGcjeGg%2FexraUdklahlC8H2dWovChWYEX7GSjN8amF4JBv04tgGI9uCjqiVhssb7gz0XSEI8gFKFXB79%2BxcUlxLbLLnYlQkp4ZoyP2rYJE%2F5mMNaKOhwH%2BfrLtvefwhl5rzvSUZp6dMCh1lh483dvfoI1u4KqbBqySBuSA29CJ%2B7xziHfRMWbmNbfUEYgLWAL8P4XxsT57giuuk9XYCcfA%2BdL3E2mdb7uTJtfhGLucdM3NKCU5y0KzYj4RlxcHk4SVqNc3KfUldJY8h1V6eQ06IkmGvDKO0ay3Ef%2FCqB8ttfrNgjNFXq4SnPHUQHFP140nQvMtCVy0tDLS9VjNx2w4ujh2KfFutpp90XzJv1%2BlBB2p3GB1U4btgtp4LN3YSpUZKv1E8nDYx9dA0PJrKM21lHos4dCbsiFrtN1nKzixHyk8p38xviYnDLtJm7knccL%2FuVnrf1uPJf8s0MFsnKTewDo1QK270%2FjkvqDvtTF2aDLgFQY%2FRFCkXjzVqRSB6aijJ193kpKpN15280uv%2Bn%2B6ehwp16y4YmFsc5qAW5D6v6lGOpMNLMnskGOqUBmTxT1rsx4ZqBikjv1IdEeRBYOpqUM1tQ2%2BA2wmJOhQGTk3gfJ5ou5RDGuM9tlBkdIOWBBYUAsWnsmxnEMWp%2B37YCuF7u7qiKQHMQnTRkNpepw%2FfDiXi59n8sPFg7eY2SrnvOIbSj6J7KS%2BZfl0MktIiUmZaY2wX0bbv9X1zH6%2FB4R34F2MMDncpOoVMJ2Btnq%2Bqlf1h8e87eGSYAgt8%2Beg%2BpW9E8&X-Amz-Signature=fa371f6d5fc1e1c8cd93a0a6480e13a4fa7938e477439b7bb5f55db58be07838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

