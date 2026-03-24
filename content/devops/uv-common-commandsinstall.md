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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672VEO5UT%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDzpoW8Mkfjy6zB3UkGlqMJX3Pl2jYHr%2FzmjL0%2FhpLgAiAOTQ%2FWB3qM8DU7teM3ECsyRjzDp70Ez1aGZ%2BjRESlEGyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPpABxJmbFvZ0kfgKtwD%2FfxVCcKmPTJ1CnSK2itR12AdPPQd8CyZru1HJDJ4esJpu2eWSDcdj4eDMyz387ZItw15lTtSpuKGcjplCu9qpqrSwOqRKn52hSBhIBtQDTWNq18iHF%2FzKqjInMHVuZYyzhMqSdWJWYwGStvRv9nTJVQVMsOTcd2dKDDv%2BSEbi%2BJg2tkaDzmi8QhVk4IX%2FGpCUkx5Dm1PX0L0ZzTsIrDmMrjjGYHXsuUBpZAo9aXeq0OdZ4cSU%2B2wyTNkI3qcoL%2B0YLwQdaz0x14yVZgFQC9oAN289%2B36s6%2Br6Avx4dqBZBgWWnrQQhyepwmcC9VxV%2BVn0tL7Ll%2BXoig8BDHU49GiD5iSZyZhMU5DKXPvqkoqxLyy8Ox5JgzpoBJ0bqvnAG%2Fwlp9LPhA%2BSTst5mpFrxsH1QHS4ThIoCdKH1I1r5tb8Ag7lalDXrqnpRwBodrFpJA1%2F%2B6Uk8qapbIzblRfvXK1zV43xt6Vw%2F0A4oarKSqglU%2FG%2Bz92990t4JuX1xxkiA3FvZzSrN%2BUyStRqKF0nR7F2G%2FMaOtj%2FmD31LanOA8GwzyEp8BYNHbtulcgvsEHiVo23ga%2BEw03zUa%2BzUewKIdCpVFLOgV86IClg91focOA2Cob6QLt9mVeTzItpEIw6%2FOHzgY6pgH%2Bp1Wq4R4RtHkcuOpJy2MVw6vOqZIqohurbmUOhZHgBWV4PO7iR%2Bd3MxRQH7JT9guCh5RTdvgNpILlzmVp%2BDr0Fsu73Be%2BjO6dm%2FIsJAj4zqzhLGVDQYzjCcT2lCO8I299CufwyrNueHni%2FC3JCQecB%2FXGqyc14A9B1pDYASjEUHRGMhTPnBLOwYirhAtfDk17%2F2KuGvfFVfhPGr%2BKf6d8SP%2F5Ewry&X-Amz-Signature=51bc28997e4e44105bd9e642c24e4bb635b816cf7fc44ab2383abefd60ac7215&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672VEO5UT%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDzpoW8Mkfjy6zB3UkGlqMJX3Pl2jYHr%2FzmjL0%2FhpLgAiAOTQ%2FWB3qM8DU7teM3ECsyRjzDp70Ez1aGZ%2BjRESlEGyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPpABxJmbFvZ0kfgKtwD%2FfxVCcKmPTJ1CnSK2itR12AdPPQd8CyZru1HJDJ4esJpu2eWSDcdj4eDMyz387ZItw15lTtSpuKGcjplCu9qpqrSwOqRKn52hSBhIBtQDTWNq18iHF%2FzKqjInMHVuZYyzhMqSdWJWYwGStvRv9nTJVQVMsOTcd2dKDDv%2BSEbi%2BJg2tkaDzmi8QhVk4IX%2FGpCUkx5Dm1PX0L0ZzTsIrDmMrjjGYHXsuUBpZAo9aXeq0OdZ4cSU%2B2wyTNkI3qcoL%2B0YLwQdaz0x14yVZgFQC9oAN289%2B36s6%2Br6Avx4dqBZBgWWnrQQhyepwmcC9VxV%2BVn0tL7Ll%2BXoig8BDHU49GiD5iSZyZhMU5DKXPvqkoqxLyy8Ox5JgzpoBJ0bqvnAG%2Fwlp9LPhA%2BSTst5mpFrxsH1QHS4ThIoCdKH1I1r5tb8Ag7lalDXrqnpRwBodrFpJA1%2F%2B6Uk8qapbIzblRfvXK1zV43xt6Vw%2F0A4oarKSqglU%2FG%2Bz92990t4JuX1xxkiA3FvZzSrN%2BUyStRqKF0nR7F2G%2FMaOtj%2FmD31LanOA8GwzyEp8BYNHbtulcgvsEHiVo23ga%2BEw03zUa%2BzUewKIdCpVFLOgV86IClg91focOA2Cob6QLt9mVeTzItpEIw6%2FOHzgY6pgH%2Bp1Wq4R4RtHkcuOpJy2MVw6vOqZIqohurbmUOhZHgBWV4PO7iR%2Bd3MxRQH7JT9guCh5RTdvgNpILlzmVp%2BDr0Fsu73Be%2BjO6dm%2FIsJAj4zqzhLGVDQYzjCcT2lCO8I299CufwyrNueHni%2FC3JCQecB%2FXGqyc14A9B1pDYASjEUHRGMhTPnBLOwYirhAtfDk17%2F2KuGvfFVfhPGr%2BKf6d8SP%2F5Ewry&X-Amz-Signature=8f05c46f00fc7900c04774e8085a12eff9fabb6c00133fe76e536d677d674566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672VEO5UT%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDDzpoW8Mkfjy6zB3UkGlqMJX3Pl2jYHr%2FzmjL0%2FhpLgAiAOTQ%2FWB3qM8DU7teM3ECsyRjzDp70Ez1aGZ%2BjRESlEGyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIPpABxJmbFvZ0kfgKtwD%2FfxVCcKmPTJ1CnSK2itR12AdPPQd8CyZru1HJDJ4esJpu2eWSDcdj4eDMyz387ZItw15lTtSpuKGcjplCu9qpqrSwOqRKn52hSBhIBtQDTWNq18iHF%2FzKqjInMHVuZYyzhMqSdWJWYwGStvRv9nTJVQVMsOTcd2dKDDv%2BSEbi%2BJg2tkaDzmi8QhVk4IX%2FGpCUkx5Dm1PX0L0ZzTsIrDmMrjjGYHXsuUBpZAo9aXeq0OdZ4cSU%2B2wyTNkI3qcoL%2B0YLwQdaz0x14yVZgFQC9oAN289%2B36s6%2Br6Avx4dqBZBgWWnrQQhyepwmcC9VxV%2BVn0tL7Ll%2BXoig8BDHU49GiD5iSZyZhMU5DKXPvqkoqxLyy8Ox5JgzpoBJ0bqvnAG%2Fwlp9LPhA%2BSTst5mpFrxsH1QHS4ThIoCdKH1I1r5tb8Ag7lalDXrqnpRwBodrFpJA1%2F%2B6Uk8qapbIzblRfvXK1zV43xt6Vw%2F0A4oarKSqglU%2FG%2Bz92990t4JuX1xxkiA3FvZzSrN%2BUyStRqKF0nR7F2G%2FMaOtj%2FmD31LanOA8GwzyEp8BYNHbtulcgvsEHiVo23ga%2BEw03zUa%2BzUewKIdCpVFLOgV86IClg91focOA2Cob6QLt9mVeTzItpEIw6%2FOHzgY6pgH%2Bp1Wq4R4RtHkcuOpJy2MVw6vOqZIqohurbmUOhZHgBWV4PO7iR%2Bd3MxRQH7JT9guCh5RTdvgNpILlzmVp%2BDr0Fsu73Be%2BjO6dm%2FIsJAj4zqzhLGVDQYzjCcT2lCO8I299CufwyrNueHni%2FC3JCQecB%2FXGqyc14A9B1pDYASjEUHRGMhTPnBLOwYirhAtfDk17%2F2KuGvfFVfhPGr%2BKf6d8SP%2F5Ewry&X-Amz-Signature=29e7b032abfd65a6ba2db6719fe7286013bdac8a6e77cc8ca30f6ff8f900422f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

