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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOUGWYN%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIG%2Bz2TM62lYOXsCWWxHHhABZyegpMOVjH%2BZHaCAET8MwAiA5Gg3Cak8NFEto5wRO3CemupRuzliYxpirfDHaqirSeSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMzS32s%2Bogt8BFsXS7KtwDebHTlkCsYR2WCDFSx9UALEhoYQML4l4vGExwmsqLxY8OWQg08XfQzBSGtiRqhmaaYPyOrqu2t8cuKGT%2FCTnBEVDzhGMdzgM6NFuksRUqfsdGovmwUaPqwPwnUb78BwQB1nD9gKqh8tujJfHh72WcqvgnlmyPDPLIar%2FvuMVL2J%2Fe7pJov%2FwwO2vgZF46KU4JPoM8AlHfD5aC6yr19WW6Wtv4KU9%2BnCEqIv2%2FSnLUnZ8rWIwfnkIpeXaIiEw%2Fv%2B8pHzPWaLJFMpxz4SvHpgKx0li6nxpDpVhGCG%2BKNWX5kR3tyeTX3O9gDplDHIkBPtOrW0jQdNJ9pIOZVJice1jHl7vtjh0eYjRjAdYE5nyyb3XRbuMaswBVq9nJhoyrx37iNBD6SB1KbHRTgd8xsCCxRgU%2FPCoPNcQx9d%2B%2BpSoomxog5XxsMuR0tgOdRnd9npd6UsjWMIse07EUlJQQb9jevqArA8UgctS5Kc4C6pD5PjeCJhg1hph531lG2MR4hdHs%2B0KPNuZ%2F9eudJMxWURc6SKBf7F4PiI%2F0vnXvqTI8I5%2FCHCRa5nIIdAEzKTOvnhyUZFxNAZwN%2BqRcf%2Bpv4MzbCh7F5jaoYm8M2s%2FcmDizYhzUZpsymS0DAn4fFK4w487QywY6pgGAFBOVGU9ppVLYlrJNeiAAx6VfCErTqK6jfYHzQRbVfAQI451c5eGOCenilOEYLz8f8qolJaTOa6jmC2jFicrLFdA3UuSXo8aMYzCaY5TWnip1aX0am%2B7YbZeiyUgkZdOVl4oCNCEA4PFkwXS0ggJYepKrLtDees%2FdpmpmON3gf%2FoOBINFCsU44Pa6oAfqn4yExyd8Hqwa9Ku4Y22vKqZ2iy%2BS2vKU&X-Amz-Signature=2c7bc0af9feaf2de343bcb9efb9524d1f5828301fd3a401fdef6c480005ecca6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOUGWYN%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIG%2Bz2TM62lYOXsCWWxHHhABZyegpMOVjH%2BZHaCAET8MwAiA5Gg3Cak8NFEto5wRO3CemupRuzliYxpirfDHaqirSeSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMzS32s%2Bogt8BFsXS7KtwDebHTlkCsYR2WCDFSx9UALEhoYQML4l4vGExwmsqLxY8OWQg08XfQzBSGtiRqhmaaYPyOrqu2t8cuKGT%2FCTnBEVDzhGMdzgM6NFuksRUqfsdGovmwUaPqwPwnUb78BwQB1nD9gKqh8tujJfHh72WcqvgnlmyPDPLIar%2FvuMVL2J%2Fe7pJov%2FwwO2vgZF46KU4JPoM8AlHfD5aC6yr19WW6Wtv4KU9%2BnCEqIv2%2FSnLUnZ8rWIwfnkIpeXaIiEw%2Fv%2B8pHzPWaLJFMpxz4SvHpgKx0li6nxpDpVhGCG%2BKNWX5kR3tyeTX3O9gDplDHIkBPtOrW0jQdNJ9pIOZVJice1jHl7vtjh0eYjRjAdYE5nyyb3XRbuMaswBVq9nJhoyrx37iNBD6SB1KbHRTgd8xsCCxRgU%2FPCoPNcQx9d%2B%2BpSoomxog5XxsMuR0tgOdRnd9npd6UsjWMIse07EUlJQQb9jevqArA8UgctS5Kc4C6pD5PjeCJhg1hph531lG2MR4hdHs%2B0KPNuZ%2F9eudJMxWURc6SKBf7F4PiI%2F0vnXvqTI8I5%2FCHCRa5nIIdAEzKTOvnhyUZFxNAZwN%2BqRcf%2Bpv4MzbCh7F5jaoYm8M2s%2FcmDizYhzUZpsymS0DAn4fFK4w487QywY6pgGAFBOVGU9ppVLYlrJNeiAAx6VfCErTqK6jfYHzQRbVfAQI451c5eGOCenilOEYLz8f8qolJaTOa6jmC2jFicrLFdA3UuSXo8aMYzCaY5TWnip1aX0am%2B7YbZeiyUgkZdOVl4oCNCEA4PFkwXS0ggJYepKrLtDees%2FdpmpmON3gf%2FoOBINFCsU44Pa6oAfqn4yExyd8Hqwa9Ku4Y22vKqZ2iy%2BS2vKU&X-Amz-Signature=e3f8f1e09428287d933057b16967b8ba319e90e8e300174d4ba0ee9996513d7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCOUGWYN%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIG%2Bz2TM62lYOXsCWWxHHhABZyegpMOVjH%2BZHaCAET8MwAiA5Gg3Cak8NFEto5wRO3CemupRuzliYxpirfDHaqirSeSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMzS32s%2Bogt8BFsXS7KtwDebHTlkCsYR2WCDFSx9UALEhoYQML4l4vGExwmsqLxY8OWQg08XfQzBSGtiRqhmaaYPyOrqu2t8cuKGT%2FCTnBEVDzhGMdzgM6NFuksRUqfsdGovmwUaPqwPwnUb78BwQB1nD9gKqh8tujJfHh72WcqvgnlmyPDPLIar%2FvuMVL2J%2Fe7pJov%2FwwO2vgZF46KU4JPoM8AlHfD5aC6yr19WW6Wtv4KU9%2BnCEqIv2%2FSnLUnZ8rWIwfnkIpeXaIiEw%2Fv%2B8pHzPWaLJFMpxz4SvHpgKx0li6nxpDpVhGCG%2BKNWX5kR3tyeTX3O9gDplDHIkBPtOrW0jQdNJ9pIOZVJice1jHl7vtjh0eYjRjAdYE5nyyb3XRbuMaswBVq9nJhoyrx37iNBD6SB1KbHRTgd8xsCCxRgU%2FPCoPNcQx9d%2B%2BpSoomxog5XxsMuR0tgOdRnd9npd6UsjWMIse07EUlJQQb9jevqArA8UgctS5Kc4C6pD5PjeCJhg1hph531lG2MR4hdHs%2B0KPNuZ%2F9eudJMxWURc6SKBf7F4PiI%2F0vnXvqTI8I5%2FCHCRa5nIIdAEzKTOvnhyUZFxNAZwN%2BqRcf%2Bpv4MzbCh7F5jaoYm8M2s%2FcmDizYhzUZpsymS0DAn4fFK4w487QywY6pgGAFBOVGU9ppVLYlrJNeiAAx6VfCErTqK6jfYHzQRbVfAQI451c5eGOCenilOEYLz8f8qolJaTOa6jmC2jFicrLFdA3UuSXo8aMYzCaY5TWnip1aX0am%2B7YbZeiyUgkZdOVl4oCNCEA4PFkwXS0ggJYepKrLtDees%2FdpmpmON3gf%2FoOBINFCsU44Pa6oAfqn4yExyd8Hqwa9Ku4Y22vKqZ2iy%2BS2vKU&X-Amz-Signature=127bcea654bb2799858b6221103d4b5a0fa8b6a37ea8f7521927518206cdc6cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

