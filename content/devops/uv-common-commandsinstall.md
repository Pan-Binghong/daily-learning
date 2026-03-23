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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLFIQXU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn6XYh5Lyp1GWX8%2BIAMbDhV4rzzgnvaYsg4j6Ed702HAIgJ%2BYKWnb3W%2BkJaqLWSU%2F7wTAIpy7Cy8zjCFuVJsjCFtUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJfXN4I5oORIEBLvNircAyrSDScpWExPy2q1lYQiXEyS9mvcvwtFsQlOYwco5w4UN9vCL9Bh%2BbsVNnnT2NCVaqR6%2BBxzwYKr0Te40jbwSX2ptR3eC%2FqPIsCqtVuqEGT5lrh5PYZ7HjIY%2BhXmMOm9JyNbUAu4QOnrVbUH3syLyJRMDW510qVZjdSnc7OcBN6NAve0mbAZthxEz7mZX1%2BoHCOJiBIgrkFyIfrzLIO0L1QBiNMpy%2BDPyu6No4uOyTHmZ0Xw%2BlatndDsYhzF4C4T%2BWg6FsNaAI3NpYIEeh8HxLsRYfL44tLLhCFkRgyBPhN3FhNkZNEFadn5GsYP2ujb0oSUJOM6t%2B3i82uzmYlu45UgkwvLIwlPNS7bpuz%2FsKLm%2F0ATevZHQU3sApLSGs6zwH2Goq91ZLaLBUVLQKUd0H%2B3DvqKWaLKWQWbQ%2Ba7rUHqgTsyaUQpRIZ9sco7qhrEu5FUWBNyIHoWKzOtmNGvhI5h06zVs9SfEyTcNMEm%2BRkltbIA7u9dbAv8keE7IEyUlhU1U81muCnGEexBQ2SYFXsWc%2BVnYz4El9%2BMfSDVHBfHv9JpWfGCDif2LHqDrm5k2cHyfqoMDQ8R%2FxEF90W15x9OHxIPqCXNVKpyHUEkwyCGMIv%2FcsPyduCZzufcMPzjgs4GOqUBL60exCEqS04hb1E07G86gEuRjtLDk%2F9q8WtA10AJOt9I4Fov%2FPqkD6IY8dnguUu5%2BfMia6smvzA%2F3O24TRUZfjM0C5nLTkaK19U4FlIsSZ%2Fqins7n9PsWLl89UgcbjJUKQlTRDta%2B66kTJ2eGARBAHlhTEL4LuMdhEbB6Zs%2FE8Z90aAcaeT7E8Ykt98TdIZZDuJRT8nvKkWLxjQ6sKMrxmp8GQy3&X-Amz-Signature=f00c4e6cbbbfb4f476656af593fba9ffb682ae7b87d2ede200a86dfaed7aa651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLFIQXU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn6XYh5Lyp1GWX8%2BIAMbDhV4rzzgnvaYsg4j6Ed702HAIgJ%2BYKWnb3W%2BkJaqLWSU%2F7wTAIpy7Cy8zjCFuVJsjCFtUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJfXN4I5oORIEBLvNircAyrSDScpWExPy2q1lYQiXEyS9mvcvwtFsQlOYwco5w4UN9vCL9Bh%2BbsVNnnT2NCVaqR6%2BBxzwYKr0Te40jbwSX2ptR3eC%2FqPIsCqtVuqEGT5lrh5PYZ7HjIY%2BhXmMOm9JyNbUAu4QOnrVbUH3syLyJRMDW510qVZjdSnc7OcBN6NAve0mbAZthxEz7mZX1%2BoHCOJiBIgrkFyIfrzLIO0L1QBiNMpy%2BDPyu6No4uOyTHmZ0Xw%2BlatndDsYhzF4C4T%2BWg6FsNaAI3NpYIEeh8HxLsRYfL44tLLhCFkRgyBPhN3FhNkZNEFadn5GsYP2ujb0oSUJOM6t%2B3i82uzmYlu45UgkwvLIwlPNS7bpuz%2FsKLm%2F0ATevZHQU3sApLSGs6zwH2Goq91ZLaLBUVLQKUd0H%2B3DvqKWaLKWQWbQ%2Ba7rUHqgTsyaUQpRIZ9sco7qhrEu5FUWBNyIHoWKzOtmNGvhI5h06zVs9SfEyTcNMEm%2BRkltbIA7u9dbAv8keE7IEyUlhU1U81muCnGEexBQ2SYFXsWc%2BVnYz4El9%2BMfSDVHBfHv9JpWfGCDif2LHqDrm5k2cHyfqoMDQ8R%2FxEF90W15x9OHxIPqCXNVKpyHUEkwyCGMIv%2FcsPyduCZzufcMPzjgs4GOqUBL60exCEqS04hb1E07G86gEuRjtLDk%2F9q8WtA10AJOt9I4Fov%2FPqkD6IY8dnguUu5%2BfMia6smvzA%2F3O24TRUZfjM0C5nLTkaK19U4FlIsSZ%2Fqins7n9PsWLl89UgcbjJUKQlTRDta%2B66kTJ2eGARBAHlhTEL4LuMdhEbB6Zs%2FE8Z90aAcaeT7E8Ykt98TdIZZDuJRT8nvKkWLxjQ6sKMrxmp8GQy3&X-Amz-Signature=f92c2386e0b25e237deb593e5292eab0d8005fe3019dc4b7e5b5e3493dbebdf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLFIQXU%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn6XYh5Lyp1GWX8%2BIAMbDhV4rzzgnvaYsg4j6Ed702HAIgJ%2BYKWnb3W%2BkJaqLWSU%2F7wTAIpy7Cy8zjCFuVJsjCFtUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJfXN4I5oORIEBLvNircAyrSDScpWExPy2q1lYQiXEyS9mvcvwtFsQlOYwco5w4UN9vCL9Bh%2BbsVNnnT2NCVaqR6%2BBxzwYKr0Te40jbwSX2ptR3eC%2FqPIsCqtVuqEGT5lrh5PYZ7HjIY%2BhXmMOm9JyNbUAu4QOnrVbUH3syLyJRMDW510qVZjdSnc7OcBN6NAve0mbAZthxEz7mZX1%2BoHCOJiBIgrkFyIfrzLIO0L1QBiNMpy%2BDPyu6No4uOyTHmZ0Xw%2BlatndDsYhzF4C4T%2BWg6FsNaAI3NpYIEeh8HxLsRYfL44tLLhCFkRgyBPhN3FhNkZNEFadn5GsYP2ujb0oSUJOM6t%2B3i82uzmYlu45UgkwvLIwlPNS7bpuz%2FsKLm%2F0ATevZHQU3sApLSGs6zwH2Goq91ZLaLBUVLQKUd0H%2B3DvqKWaLKWQWbQ%2Ba7rUHqgTsyaUQpRIZ9sco7qhrEu5FUWBNyIHoWKzOtmNGvhI5h06zVs9SfEyTcNMEm%2BRkltbIA7u9dbAv8keE7IEyUlhU1U81muCnGEexBQ2SYFXsWc%2BVnYz4El9%2BMfSDVHBfHv9JpWfGCDif2LHqDrm5k2cHyfqoMDQ8R%2FxEF90W15x9OHxIPqCXNVKpyHUEkwyCGMIv%2FcsPyduCZzufcMPzjgs4GOqUBL60exCEqS04hb1E07G86gEuRjtLDk%2F9q8WtA10AJOt9I4Fov%2FPqkD6IY8dnguUu5%2BfMia6smvzA%2F3O24TRUZfjM0C5nLTkaK19U4FlIsSZ%2Fqins7n9PsWLl89UgcbjJUKQlTRDta%2B66kTJ2eGARBAHlhTEL4LuMdhEbB6Zs%2FE8Z90aAcaeT7E8Ykt98TdIZZDuJRT8nvKkWLxjQ6sKMrxmp8GQy3&X-Amz-Signature=ddf4966d822c114654384b517308523fd73604e42d27b9f16e357609281e40f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

