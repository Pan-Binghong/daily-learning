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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SPSD3CC%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCICn1Zjm9m7m3%2FCz7rliHAg6zYs9l%2BfMkGQsuoBH3kE93AiB2bhIVFKfWumqQwk4k4DZJtR%2FCojFGa17h3tWN4lhYvir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMn%2FLF5wKxjU3Cg3KMKtwDHXhMGtVTWmCW5OvL90yRa%2FesQnpzo7ly%2F2jRq3XUuos8AOMz2gXDtDmhBZzYw0d%2Bx9eJej%2FtWcjyti8bfdEABy8%2F9VGwUulmqcUlsqlAQ8htNDpfMSBPXIeeFjk%2Fsn58ENTnWegfLJIRQTleFB9ErQL4GNfqi%2BtFmFZv%2BZ1WAkXbtFpAXGzZLcQ2sxirrBSYSZWuwX%2BF6e1fvUwKdf7pb00SbEzNZzaJSADkU20OibxqAZHbeqWFwGqWBZbik9F8sp5d4AgyY0Gc8JHqBoNZFCEKgyHCqKuYXbthQqqRZy%2Ft0CTfe7qaY%2BP%2BEYriImYH0fINDY0elYhwjoYygDlChjAqgJlS3K8QFPNy3iPyrxeTGj9LFggARujjWLI1OxTzWg5DnCAAguidxBYsTB194YVt4LUQz5ClFAjkfQn7NS8GE03ajmlnXhCvCI1PzoOAYKBZPN2Rq0It5pdBjnCzwK8Ha0%2BLB9gj9cu2iA%2Fx5dl2BfsfpGesQ4EaC%2BQId9iW0IDvO4Z5dPvrxewhrvhakhTa8KUxRi1BbJ2jG7BV8z4MZWOZ8g3Dq0WcAmD5fCeaL%2FuNADlo9%2B0WZG2r7FcxrWzyIk2NJdxSjv%2F7ftzXLoSYg02ViVIW78vfpp4wlcKzzQY6pgF3EgS5m8Qrmatgr%2BDfDRw%2Bc4fzUaZDpd%2BxbEqqSg5xFWP7ww5NWqYnOm6my96pL0QNu%2B4Q9FXWe6k2OjF25JcQrj1i12Ue8Q0VkIG6%2FLWJ4mx1zWmwTl%2BKvfupINIKAWD7qochjPVG6uS2W1kcGWI06eQt73rzxL22%2FOSOUHaEIz6afsQMwB1TxcXY01Icdl3sXNE3chbJL0MgqN4ChN517GoVBzk5&X-Amz-Signature=61f14626e9369a8093405df53a241c3fb81c5ab711b0a0eea7aa3579c16aface&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

