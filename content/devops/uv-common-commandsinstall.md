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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF2J56FU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfXJz4yQh7lcAQoY3uog%2BhWjboL7qc56DVuCTJj0I5kQIhAKBNBBrzaAJFJT7ZgcrhJAHTFGiktLWFCZHJddIS1nOrKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOt%2BU5CQ8B9T24Xx0q3AOOM%2FMH7R1ozv%2F8DZ%2FKNOhY2DrMIPN4MK0wwzrDM07G5OCG5KiQJIJAzTgkAv1A5kSWVCzx%2Fx6C99YmOcG3dYWUd1pDYsf91JL4XQeBlpLhR%2B46z4TPiqV4ievlgl8CHz%2FELjAm%2Fcw2Hfg66nlmO5HGe7EfONOk0oXpQb8tqktDHfQBcHxfkszitLIl9LA12IxkDsUcaSi3LRedw2DxeilwxlMrAnhXuI2lovDhpHEYqK1nv4wIdv6Il%2FFpDlMc2Nez0AFwMGn1w0zZ4SqYfMUAHiugNAf8EMx4iS8agMmTE%2Fo6ZLicHVhsEQJ0dAQXW6iy0sLJIWu74LrBX9tC%2BzBsMTWak6qAlH8aC%2BlyfmXGlYM0zb5TTAw8UgqMrvZgprpgwTqCUJckvnw8FlZNxvcSYjX3DzCsR25iVbU3wjvUJyjPbOSXhyQO9wNtGl9FN42BgAeL0YZw%2BECe2keQ4Hw5XsEIbco%2BBtTc2Mny5pTnmxfzWpHht73pC8zyxOn7vuye8R%2FZWnu9QtZyK%2BbxmIoH%2FH5Td6fHlH%2B%2FPOdYq8xEXk7UFP3Gp1cYL7WlD%2BQ%2BX%2BDyA4Gnytp9bTBY6zx%2FRhmYZ4SwGpAVJiZV6NLF0ul1oRPVHB6RCDTPdl4VBTCj8q%2FIBjqkAa2V1Mx4LgdNVX537gN2Uzja9yUCo9cBKrkWKhjtYBZe%2F1Qt17GFcfTO9MaIyTkGYIz7WafJiJ%2BXIzfAGWfHNof8J8w%2BuddAcJ5Ct56stfhJaQs%2BUNRTNk5spafjFqQqdKSE2PamJp4Cbg9OFtWPFWpF1RWZpt3jwYeMDEu0FXD%2FdFLxhJw4uIZ55hUkJuMXMt9paCwjDqYJPO8ASR2Jqbh46KwC&X-Amz-Signature=8c9d678444feea45c0034d43af7bd9ec00bc66ffc9e4e3d6fea934843b3dbd54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF2J56FU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfXJz4yQh7lcAQoY3uog%2BhWjboL7qc56DVuCTJj0I5kQIhAKBNBBrzaAJFJT7ZgcrhJAHTFGiktLWFCZHJddIS1nOrKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOt%2BU5CQ8B9T24Xx0q3AOOM%2FMH7R1ozv%2F8DZ%2FKNOhY2DrMIPN4MK0wwzrDM07G5OCG5KiQJIJAzTgkAv1A5kSWVCzx%2Fx6C99YmOcG3dYWUd1pDYsf91JL4XQeBlpLhR%2B46z4TPiqV4ievlgl8CHz%2FELjAm%2Fcw2Hfg66nlmO5HGe7EfONOk0oXpQb8tqktDHfQBcHxfkszitLIl9LA12IxkDsUcaSi3LRedw2DxeilwxlMrAnhXuI2lovDhpHEYqK1nv4wIdv6Il%2FFpDlMc2Nez0AFwMGn1w0zZ4SqYfMUAHiugNAf8EMx4iS8agMmTE%2Fo6ZLicHVhsEQJ0dAQXW6iy0sLJIWu74LrBX9tC%2BzBsMTWak6qAlH8aC%2BlyfmXGlYM0zb5TTAw8UgqMrvZgprpgwTqCUJckvnw8FlZNxvcSYjX3DzCsR25iVbU3wjvUJyjPbOSXhyQO9wNtGl9FN42BgAeL0YZw%2BECe2keQ4Hw5XsEIbco%2BBtTc2Mny5pTnmxfzWpHht73pC8zyxOn7vuye8R%2FZWnu9QtZyK%2BbxmIoH%2FH5Td6fHlH%2B%2FPOdYq8xEXk7UFP3Gp1cYL7WlD%2BQ%2BX%2BDyA4Gnytp9bTBY6zx%2FRhmYZ4SwGpAVJiZV6NLF0ul1oRPVHB6RCDTPdl4VBTCj8q%2FIBjqkAa2V1Mx4LgdNVX537gN2Uzja9yUCo9cBKrkWKhjtYBZe%2F1Qt17GFcfTO9MaIyTkGYIz7WafJiJ%2BXIzfAGWfHNof8J8w%2BuddAcJ5Ct56stfhJaQs%2BUNRTNk5spafjFqQqdKSE2PamJp4Cbg9OFtWPFWpF1RWZpt3jwYeMDEu0FXD%2FdFLxhJw4uIZ55hUkJuMXMt9paCwjDqYJPO8ASR2Jqbh46KwC&X-Amz-Signature=04a8db11eb24e83d7a3b841f95b4373042378b9003f778494ceabfb79a60978f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF2J56FU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfXJz4yQh7lcAQoY3uog%2BhWjboL7qc56DVuCTJj0I5kQIhAKBNBBrzaAJFJT7ZgcrhJAHTFGiktLWFCZHJddIS1nOrKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOt%2BU5CQ8B9T24Xx0q3AOOM%2FMH7R1ozv%2F8DZ%2FKNOhY2DrMIPN4MK0wwzrDM07G5OCG5KiQJIJAzTgkAv1A5kSWVCzx%2Fx6C99YmOcG3dYWUd1pDYsf91JL4XQeBlpLhR%2B46z4TPiqV4ievlgl8CHz%2FELjAm%2Fcw2Hfg66nlmO5HGe7EfONOk0oXpQb8tqktDHfQBcHxfkszitLIl9LA12IxkDsUcaSi3LRedw2DxeilwxlMrAnhXuI2lovDhpHEYqK1nv4wIdv6Il%2FFpDlMc2Nez0AFwMGn1w0zZ4SqYfMUAHiugNAf8EMx4iS8agMmTE%2Fo6ZLicHVhsEQJ0dAQXW6iy0sLJIWu74LrBX9tC%2BzBsMTWak6qAlH8aC%2BlyfmXGlYM0zb5TTAw8UgqMrvZgprpgwTqCUJckvnw8FlZNxvcSYjX3DzCsR25iVbU3wjvUJyjPbOSXhyQO9wNtGl9FN42BgAeL0YZw%2BECe2keQ4Hw5XsEIbco%2BBtTc2Mny5pTnmxfzWpHht73pC8zyxOn7vuye8R%2FZWnu9QtZyK%2BbxmIoH%2FH5Td6fHlH%2B%2FPOdYq8xEXk7UFP3Gp1cYL7WlD%2BQ%2BX%2BDyA4Gnytp9bTBY6zx%2FRhmYZ4SwGpAVJiZV6NLF0ul1oRPVHB6RCDTPdl4VBTCj8q%2FIBjqkAa2V1Mx4LgdNVX537gN2Uzja9yUCo9cBKrkWKhjtYBZe%2F1Qt17GFcfTO9MaIyTkGYIz7WafJiJ%2BXIzfAGWfHNof8J8w%2BuddAcJ5Ct56stfhJaQs%2BUNRTNk5spafjFqQqdKSE2PamJp4Cbg9OFtWPFWpF1RWZpt3jwYeMDEu0FXD%2FdFLxhJw4uIZ55hUkJuMXMt9paCwjDqYJPO8ASR2Jqbh46KwC&X-Amz-Signature=81d2ea72c0b2dfb97073c564d7355738a3383f46961bf96b5dbbd1d3eb74ee75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

