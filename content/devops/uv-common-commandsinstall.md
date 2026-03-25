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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4RB3UB%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCbKJhwZTA6Kz6Y8bqJXt0SbnDxeBPGYM5JHA1%2BtzKbgIhAMTm2GfPl7Mw3Lb1BdE%2FihDC%2BKM8Gtw0YhtP3eC1pzNzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZgz4Z3FQjDkLt3bMq3AOBscDx2uTqH13aEIlFnpE%2FKGZ1tM%2B93Dy%2F4OMN1B5TRB0tSkUk9v6L2XOjSBnkqzLaYca9wcJoilokGm6gvRfRTeJvsHjL%2BTXnvpVutiNIRb1kuyCWEe%2BGnLszCP%2BDoLvJtTB8vgrJyVhv6sqQlgTDUsPN9NP%2BDTfHHsq2XLaUIoLT4bhkDhx0QE5Hvdr5b%2FocKdbhkBNDVXnu%2B7ysJp%2F2KeovkFMi0fxLzk5inXssgbQGCSbhS4SDpScsLv5R3pFh42egWsoAGO%2BpQdfNGB9gJj2brUJTvldBY8mWt4x%2FdZI7U1sVDIGnYziqaKJaSTNqjgQiit%2FgGd8cRsTiNN0Ux4nqpWfY2%2BELOfX8OH94YuZhyQv3z8%2BiE%2F6vEMeC5mk2IefV37iGP8FylMMP9kfNhcZsmtmYqN0Y9glhFU6GhrEVJhXGwZ7z127gehSlYW0Yw95xp5UF04I9YGlfptpQHWCl%2BTn3%2BH6hp0MDXEcgH7S15Yh2tbp8LLeBEGoUSpe9c%2FLfPGiStEyxhBj5%2FlzpPO%2FP3jIG5bUvhJXBB8mdSfnO1qfGVVw%2FdAacaSNXy29f%2FK53mwXAMo1lJYodkIugEKjWgiR8nB6EuY2K95M%2FzEitZSWFHaLFYHbZ%2FjCA1o7OBjqkATw0RBIQ0kUQ%2Ba4StD%2Ffe9Pe9pvDyRcMdFUdh7zB3CphOdk4U93cY1PuaO5Fq%2BB7LK2ixmEmiwf1NZzcqwaPDu1SL3FbyZ8ITmO4to6%2BDgmEvJYUMYVSZBo76OVOBZ4U1nv%2BIg6tqwdnNPSAiLw2%2FtWX4BlzxsT2cyZe%2Fbyo%2Byv8TnIRTv6SwzhHdnhsF7PgxmBsKKPVi1UrDw%2F0SEX3L%2Fng7RzA&X-Amz-Signature=55aa6dbb7b7a64cb26d995a7f408dec1dfd6dfcddef7afb7e3d45466a2a5e8a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4RB3UB%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCbKJhwZTA6Kz6Y8bqJXt0SbnDxeBPGYM5JHA1%2BtzKbgIhAMTm2GfPl7Mw3Lb1BdE%2FihDC%2BKM8Gtw0YhtP3eC1pzNzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZgz4Z3FQjDkLt3bMq3AOBscDx2uTqH13aEIlFnpE%2FKGZ1tM%2B93Dy%2F4OMN1B5TRB0tSkUk9v6L2XOjSBnkqzLaYca9wcJoilokGm6gvRfRTeJvsHjL%2BTXnvpVutiNIRb1kuyCWEe%2BGnLszCP%2BDoLvJtTB8vgrJyVhv6sqQlgTDUsPN9NP%2BDTfHHsq2XLaUIoLT4bhkDhx0QE5Hvdr5b%2FocKdbhkBNDVXnu%2B7ysJp%2F2KeovkFMi0fxLzk5inXssgbQGCSbhS4SDpScsLv5R3pFh42egWsoAGO%2BpQdfNGB9gJj2brUJTvldBY8mWt4x%2FdZI7U1sVDIGnYziqaKJaSTNqjgQiit%2FgGd8cRsTiNN0Ux4nqpWfY2%2BELOfX8OH94YuZhyQv3z8%2BiE%2F6vEMeC5mk2IefV37iGP8FylMMP9kfNhcZsmtmYqN0Y9glhFU6GhrEVJhXGwZ7z127gehSlYW0Yw95xp5UF04I9YGlfptpQHWCl%2BTn3%2BH6hp0MDXEcgH7S15Yh2tbp8LLeBEGoUSpe9c%2FLfPGiStEyxhBj5%2FlzpPO%2FP3jIG5bUvhJXBB8mdSfnO1qfGVVw%2FdAacaSNXy29f%2FK53mwXAMo1lJYodkIugEKjWgiR8nB6EuY2K95M%2FzEitZSWFHaLFYHbZ%2FjCA1o7OBjqkATw0RBIQ0kUQ%2Ba4StD%2Ffe9Pe9pvDyRcMdFUdh7zB3CphOdk4U93cY1PuaO5Fq%2BB7LK2ixmEmiwf1NZzcqwaPDu1SL3FbyZ8ITmO4to6%2BDgmEvJYUMYVSZBo76OVOBZ4U1nv%2BIg6tqwdnNPSAiLw2%2FtWX4BlzxsT2cyZe%2Fbyo%2Byv8TnIRTv6SwzhHdnhsF7PgxmBsKKPVi1UrDw%2F0SEX3L%2Fng7RzA&X-Amz-Signature=cc9ca32fcd23333cf4efa6a2753838404840488e6a45a6eb565e88052e5cb5df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4RB3UB%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCbKJhwZTA6Kz6Y8bqJXt0SbnDxeBPGYM5JHA1%2BtzKbgIhAMTm2GfPl7Mw3Lb1BdE%2FihDC%2BKM8Gtw0YhtP3eC1pzNzKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZgz4Z3FQjDkLt3bMq3AOBscDx2uTqH13aEIlFnpE%2FKGZ1tM%2B93Dy%2F4OMN1B5TRB0tSkUk9v6L2XOjSBnkqzLaYca9wcJoilokGm6gvRfRTeJvsHjL%2BTXnvpVutiNIRb1kuyCWEe%2BGnLszCP%2BDoLvJtTB8vgrJyVhv6sqQlgTDUsPN9NP%2BDTfHHsq2XLaUIoLT4bhkDhx0QE5Hvdr5b%2FocKdbhkBNDVXnu%2B7ysJp%2F2KeovkFMi0fxLzk5inXssgbQGCSbhS4SDpScsLv5R3pFh42egWsoAGO%2BpQdfNGB9gJj2brUJTvldBY8mWt4x%2FdZI7U1sVDIGnYziqaKJaSTNqjgQiit%2FgGd8cRsTiNN0Ux4nqpWfY2%2BELOfX8OH94YuZhyQv3z8%2BiE%2F6vEMeC5mk2IefV37iGP8FylMMP9kfNhcZsmtmYqN0Y9glhFU6GhrEVJhXGwZ7z127gehSlYW0Yw95xp5UF04I9YGlfptpQHWCl%2BTn3%2BH6hp0MDXEcgH7S15Yh2tbp8LLeBEGoUSpe9c%2FLfPGiStEyxhBj5%2FlzpPO%2FP3jIG5bUvhJXBB8mdSfnO1qfGVVw%2FdAacaSNXy29f%2FK53mwXAMo1lJYodkIugEKjWgiR8nB6EuY2K95M%2FzEitZSWFHaLFYHbZ%2FjCA1o7OBjqkATw0RBIQ0kUQ%2Ba4StD%2Ffe9Pe9pvDyRcMdFUdh7zB3CphOdk4U93cY1PuaO5Fq%2BB7LK2ixmEmiwf1NZzcqwaPDu1SL3FbyZ8ITmO4to6%2BDgmEvJYUMYVSZBo76OVOBZ4U1nv%2BIg6tqwdnNPSAiLw2%2FtWX4BlzxsT2cyZe%2Fbyo%2Byv8TnIRTv6SwzhHdnhsF7PgxmBsKKPVi1UrDw%2F0SEX3L%2Fng7RzA&X-Amz-Signature=9f169c851f11b862141de49b14eb22dd266fc2aa62e3b72893dcb5fd352b8b42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

