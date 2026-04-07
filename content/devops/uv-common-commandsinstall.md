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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX2B5BNR%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHJU9UU7XB%2BxbZ95AvMDgYhQpGbYrVLNJ2LRA%2B9gm7CaAiEA3jg6M4HR%2FBIamWN%2BObII4qJ5D98ze%2FLiv%2B8hP8xhj6gqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcNX25mejehbJLjuyrcA5thiKUNF3h%2F4GpwFDHNfjUQfA0rNiL97ADDBFc2cn4mSmeFIwda%2FLs1Zjqos3TqnhBJloi%2FIUNaSIDeSEolSJv8DdyWPEa6ou62V42sf%2Fxiae%2B39gHK%2BwnV1g3%2F5pSXVTkgSj7ZTfl9i3VgcD7VaNWvXVCc%2Bu0UB1MBBjR%2BBSmc%2FKpUZZtEnGbgrnV052xPMhbF1vRz%2BLJTN9uCBfSoQzUOeqID5fxjz9ist8pnfVHhyPYwMYloGmH%2Fj%2BtEkdbK%2Bq6nO2THWMCqhLypY8IhOiV2X1cPo9brzTV6GUrbgJi5yOIl01Q7HYBmC9aDZbtNhkAUmJOOKFlV7CUl3EXxaI07W56inBxM5Qq6Be9Ixq0rCA1VIEmEgYYjcaLtq8uwrVRUoPtDZetmOSIANm3Y1x13VLRHcfY33JHjt3isybGfTvYS4RgdQlsgWBPv3EPW5V4Rt0P6DJhmZhLhIQ3qbU5i0beyCJoGQgtE1sbaWqEvI%2ByPfVJ8S3fNp3j3iYHS6zNcZda3HEoPXP%2BUR%2BDXbrLIuX9biAOL436iPT%2B2n6SAgI%2BXCIMJYUtXZYwsmZOPkFVG8IIild9qpZLCJJbstbedFmtah5GmNQMSvPg3VmKRS6akMLegs%2Fn9itqPMPP10c4GOqUBNYHJKkaH4gBDAmiWWOyHjtg7m1xjHeMRAD7WT0wz%2FglCjFgsY6A2XP0jmZGEWuOwZw1h3e0SQkWPTEJYg4dAULxAr4BuINehMcaUoHS83mtQxzuuEwIniRsH9qfXpg4Jkag5e6VeWaBNAZJ%2FCjTf13qH%2FoCMWervz5cPdIk5kaBDtx%2FrhdQbSiM9R4RTtVRjr6uF0keT0NDdIvrWV3tGzvGkrV9f&X-Amz-Signature=ad205415a2ee844b3c3178aa73b4f50a3f125e8ae80ac47b8e4aad31987c92fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX2B5BNR%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHJU9UU7XB%2BxbZ95AvMDgYhQpGbYrVLNJ2LRA%2B9gm7CaAiEA3jg6M4HR%2FBIamWN%2BObII4qJ5D98ze%2FLiv%2B8hP8xhj6gqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcNX25mejehbJLjuyrcA5thiKUNF3h%2F4GpwFDHNfjUQfA0rNiL97ADDBFc2cn4mSmeFIwda%2FLs1Zjqos3TqnhBJloi%2FIUNaSIDeSEolSJv8DdyWPEa6ou62V42sf%2Fxiae%2B39gHK%2BwnV1g3%2F5pSXVTkgSj7ZTfl9i3VgcD7VaNWvXVCc%2Bu0UB1MBBjR%2BBSmc%2FKpUZZtEnGbgrnV052xPMhbF1vRz%2BLJTN9uCBfSoQzUOeqID5fxjz9ist8pnfVHhyPYwMYloGmH%2Fj%2BtEkdbK%2Bq6nO2THWMCqhLypY8IhOiV2X1cPo9brzTV6GUrbgJi5yOIl01Q7HYBmC9aDZbtNhkAUmJOOKFlV7CUl3EXxaI07W56inBxM5Qq6Be9Ixq0rCA1VIEmEgYYjcaLtq8uwrVRUoPtDZetmOSIANm3Y1x13VLRHcfY33JHjt3isybGfTvYS4RgdQlsgWBPv3EPW5V4Rt0P6DJhmZhLhIQ3qbU5i0beyCJoGQgtE1sbaWqEvI%2ByPfVJ8S3fNp3j3iYHS6zNcZda3HEoPXP%2BUR%2BDXbrLIuX9biAOL436iPT%2B2n6SAgI%2BXCIMJYUtXZYwsmZOPkFVG8IIild9qpZLCJJbstbedFmtah5GmNQMSvPg3VmKRS6akMLegs%2Fn9itqPMPP10c4GOqUBNYHJKkaH4gBDAmiWWOyHjtg7m1xjHeMRAD7WT0wz%2FglCjFgsY6A2XP0jmZGEWuOwZw1h3e0SQkWPTEJYg4dAULxAr4BuINehMcaUoHS83mtQxzuuEwIniRsH9qfXpg4Jkag5e6VeWaBNAZJ%2FCjTf13qH%2FoCMWervz5cPdIk5kaBDtx%2FrhdQbSiM9R4RTtVRjr6uF0keT0NDdIvrWV3tGzvGkrV9f&X-Amz-Signature=a208e8ef9bb19ba7c36f66d62acd600b69780e942c0c92a52e5a74516c14a591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX2B5BNR%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIHJU9UU7XB%2BxbZ95AvMDgYhQpGbYrVLNJ2LRA%2B9gm7CaAiEA3jg6M4HR%2FBIamWN%2BObII4qJ5D98ze%2FLiv%2B8hP8xhj6gqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcNX25mejehbJLjuyrcA5thiKUNF3h%2F4GpwFDHNfjUQfA0rNiL97ADDBFc2cn4mSmeFIwda%2FLs1Zjqos3TqnhBJloi%2FIUNaSIDeSEolSJv8DdyWPEa6ou62V42sf%2Fxiae%2B39gHK%2BwnV1g3%2F5pSXVTkgSj7ZTfl9i3VgcD7VaNWvXVCc%2Bu0UB1MBBjR%2BBSmc%2FKpUZZtEnGbgrnV052xPMhbF1vRz%2BLJTN9uCBfSoQzUOeqID5fxjz9ist8pnfVHhyPYwMYloGmH%2Fj%2BtEkdbK%2Bq6nO2THWMCqhLypY8IhOiV2X1cPo9brzTV6GUrbgJi5yOIl01Q7HYBmC9aDZbtNhkAUmJOOKFlV7CUl3EXxaI07W56inBxM5Qq6Be9Ixq0rCA1VIEmEgYYjcaLtq8uwrVRUoPtDZetmOSIANm3Y1x13VLRHcfY33JHjt3isybGfTvYS4RgdQlsgWBPv3EPW5V4Rt0P6DJhmZhLhIQ3qbU5i0beyCJoGQgtE1sbaWqEvI%2ByPfVJ8S3fNp3j3iYHS6zNcZda3HEoPXP%2BUR%2BDXbrLIuX9biAOL436iPT%2B2n6SAgI%2BXCIMJYUtXZYwsmZOPkFVG8IIild9qpZLCJJbstbedFmtah5GmNQMSvPg3VmKRS6akMLegs%2Fn9itqPMPP10c4GOqUBNYHJKkaH4gBDAmiWWOyHjtg7m1xjHeMRAD7WT0wz%2FglCjFgsY6A2XP0jmZGEWuOwZw1h3e0SQkWPTEJYg4dAULxAr4BuINehMcaUoHS83mtQxzuuEwIniRsH9qfXpg4Jkag5e6VeWaBNAZJ%2FCjTf13qH%2FoCMWervz5cPdIk5kaBDtx%2FrhdQbSiM9R4RTtVRjr6uF0keT0NDdIvrWV3tGzvGkrV9f&X-Amz-Signature=7a7e170a8d3b3f3acf9838de702d5fb9b6931fb6abd4e61272da39abd857f47e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

