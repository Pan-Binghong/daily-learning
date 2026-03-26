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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDLNH72D%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJuYvEI8sXygEMm4XvdSic2tvGueC9JTbi9NGWWwmVkQIhAL9Q5eX9ZRrjy2F6TQh%2Fc5NiLm1G3OQXeZIFlivWsR%2BaKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1A0UMBllnyo%2BAN5Iq3AMTeQD2jbeXVFAf8ub3hBn8iI1rxIWgC9eX1UyGB%2B0dRtK20BWoTs1vLHvmQHXOWUWhgb3c%2BbQyJtG1X%2BaZyPaEdby%2FDf7ImSFGWwqoOaoBRKLGEmRS2KQaqq7Ls5Q4SIxL6ic8GhGBdXtXplx8okwJtt5yVco8Sgsnb%2FWCaz3qaCxn9TMm1dbC6cA%2FVD9hEupju4BbspKfNPnHDuEQCRGdj0HqI8ouqsWp2BFgEjLMcJoKq672d%2BaOly2psoju8LgZ6wxYgPIgBev%2F1poryEMKYaPlqFhgCsftZzdrFWc3CTrBVBBQhjBcMcsoE7ocZD3AtH3Bn0lijdRx%2FNKM9nY3QcHYmgVfB2UL%2BDfy4DyrAoqA9FfzPWh26vNDLSnaa1i2KWql7t7jaRpjjsuf7I7aftgGjIuwXCpmEONjWiKObp4CsEyk6k3DvU%2FC4tSviAl6WpwYMqHhzH6q5PM9IDJ7tlR5IyRz1PSSu7XQ1rud2fZjSlF9leIwL%2BjJ5N3QboJ2Ux4jHzK0mtXwgirT%2Br8ur0TCJn9qiCY01LV4%2FLR54G1q8tYYjohIBD8bqsBF7LppXnVvhOUjVDjB2ragj5jxG0ubKLmmcayduberp6XLYI0j7y1%2BoCmy4gGBgDC0yZLOBjqkARnFdYJe3yqfKlrg7mqVdTOmEEs2R8mUGHZB%2BNK0drcuchvXY4aBR4XHPy6HvgciJtVlRKtl2DgxY9f0rZcdSf9suNeOAXxDnlt%2BsIEm2IUBhSVccpDALi4NEk8ynYHyaMg6iSeJx25vu36jQpZEj1%2FSU3kLNXAYYfXjm%2BXtuLXBqNr6c1rSPx5yS19iyFS40r2k0gAAATFuVOawI2wwUdvu%2BzOf&X-Amz-Signature=7576d5b5d7c69f76c515aa3b5236264b2ab7d1c90590bcbca892e4ac9e2fd35d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDLNH72D%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJuYvEI8sXygEMm4XvdSic2tvGueC9JTbi9NGWWwmVkQIhAL9Q5eX9ZRrjy2F6TQh%2Fc5NiLm1G3OQXeZIFlivWsR%2BaKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1A0UMBllnyo%2BAN5Iq3AMTeQD2jbeXVFAf8ub3hBn8iI1rxIWgC9eX1UyGB%2B0dRtK20BWoTs1vLHvmQHXOWUWhgb3c%2BbQyJtG1X%2BaZyPaEdby%2FDf7ImSFGWwqoOaoBRKLGEmRS2KQaqq7Ls5Q4SIxL6ic8GhGBdXtXplx8okwJtt5yVco8Sgsnb%2FWCaz3qaCxn9TMm1dbC6cA%2FVD9hEupju4BbspKfNPnHDuEQCRGdj0HqI8ouqsWp2BFgEjLMcJoKq672d%2BaOly2psoju8LgZ6wxYgPIgBev%2F1poryEMKYaPlqFhgCsftZzdrFWc3CTrBVBBQhjBcMcsoE7ocZD3AtH3Bn0lijdRx%2FNKM9nY3QcHYmgVfB2UL%2BDfy4DyrAoqA9FfzPWh26vNDLSnaa1i2KWql7t7jaRpjjsuf7I7aftgGjIuwXCpmEONjWiKObp4CsEyk6k3DvU%2FC4tSviAl6WpwYMqHhzH6q5PM9IDJ7tlR5IyRz1PSSu7XQ1rud2fZjSlF9leIwL%2BjJ5N3QboJ2Ux4jHzK0mtXwgirT%2Br8ur0TCJn9qiCY01LV4%2FLR54G1q8tYYjohIBD8bqsBF7LppXnVvhOUjVDjB2ragj5jxG0ubKLmmcayduberp6XLYI0j7y1%2BoCmy4gGBgDC0yZLOBjqkARnFdYJe3yqfKlrg7mqVdTOmEEs2R8mUGHZB%2BNK0drcuchvXY4aBR4XHPy6HvgciJtVlRKtl2DgxY9f0rZcdSf9suNeOAXxDnlt%2BsIEm2IUBhSVccpDALi4NEk8ynYHyaMg6iSeJx25vu36jQpZEj1%2FSU3kLNXAYYfXjm%2BXtuLXBqNr6c1rSPx5yS19iyFS40r2k0gAAATFuVOawI2wwUdvu%2BzOf&X-Amz-Signature=309adb91ea3c5f34068eb4ede2b2c512fa26f6f595069df77f5fc666434f89d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDLNH72D%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJuYvEI8sXygEMm4XvdSic2tvGueC9JTbi9NGWWwmVkQIhAL9Q5eX9ZRrjy2F6TQh%2Fc5NiLm1G3OQXeZIFlivWsR%2BaKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1A0UMBllnyo%2BAN5Iq3AMTeQD2jbeXVFAf8ub3hBn8iI1rxIWgC9eX1UyGB%2B0dRtK20BWoTs1vLHvmQHXOWUWhgb3c%2BbQyJtG1X%2BaZyPaEdby%2FDf7ImSFGWwqoOaoBRKLGEmRS2KQaqq7Ls5Q4SIxL6ic8GhGBdXtXplx8okwJtt5yVco8Sgsnb%2FWCaz3qaCxn9TMm1dbC6cA%2FVD9hEupju4BbspKfNPnHDuEQCRGdj0HqI8ouqsWp2BFgEjLMcJoKq672d%2BaOly2psoju8LgZ6wxYgPIgBev%2F1poryEMKYaPlqFhgCsftZzdrFWc3CTrBVBBQhjBcMcsoE7ocZD3AtH3Bn0lijdRx%2FNKM9nY3QcHYmgVfB2UL%2BDfy4DyrAoqA9FfzPWh26vNDLSnaa1i2KWql7t7jaRpjjsuf7I7aftgGjIuwXCpmEONjWiKObp4CsEyk6k3DvU%2FC4tSviAl6WpwYMqHhzH6q5PM9IDJ7tlR5IyRz1PSSu7XQ1rud2fZjSlF9leIwL%2BjJ5N3QboJ2Ux4jHzK0mtXwgirT%2Br8ur0TCJn9qiCY01LV4%2FLR54G1q8tYYjohIBD8bqsBF7LppXnVvhOUjVDjB2ragj5jxG0ubKLmmcayduberp6XLYI0j7y1%2BoCmy4gGBgDC0yZLOBjqkARnFdYJe3yqfKlrg7mqVdTOmEEs2R8mUGHZB%2BNK0drcuchvXY4aBR4XHPy6HvgciJtVlRKtl2DgxY9f0rZcdSf9suNeOAXxDnlt%2BsIEm2IUBhSVccpDALi4NEk8ynYHyaMg6iSeJx25vu36jQpZEj1%2FSU3kLNXAYYfXjm%2BXtuLXBqNr6c1rSPx5yS19iyFS40r2k0gAAATFuVOawI2wwUdvu%2BzOf&X-Amz-Signature=8d3683707c6f1d5754139a12357bc1a169bd3a8ef3b9c242a4a2d823a0d29c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

