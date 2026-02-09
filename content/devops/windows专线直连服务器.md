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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J5K6ZN5%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD07Y5W3BJ7AACryTttDMOIkeCgfK%2BkINM1dLsrB9H4RAIhAKr5CFdfo06MX92nkDRPtIz84wyN1kgA0buPgowaw6E%2BKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxDpb632613RkilVoq3AP55zvcTP0n0Ad2ECJ1RxBXAHqA7ITmJ%2Fy%2Bgvoho9x8OtQCAOhWmxSLMHYV1R40ce9FHKfjNpIf6%2FV20ijkLqQ%2FKporBdMF9yqP9EaaslbHuPVy%2FzINO%2FFpxmfm8SiFbvj8rnfxMLuVMWxPPIBmpBbTjaSrnJ3dlUMn3Il1vsnFFhuZvXw%2FO%2BQIg%2F3uarN75zQxD6b9zLVyL08L17j4%2B%2BeJ%2BAliGLNAy56ebFlK5oqjI%2F5aa5i4AnS1Ebgqbe6K4SpbaAV7U9%2BVx4TADoIM47wexxQYHJ4A1mQijz0gi%2BQkbp%2F1pzX6nfxK%2BFHvhlj3wqg5hncvXbOXDg3txyVcgdthlsRSbg89ZceYfZphbcwdtWGi1PHqOrAJ5W0JvYeJEyw8%2FfMizdshBf9kUOCTIPkHYcMEEwpxPnVqCnG%2FhpvBHe4qvyvDqzXYEOtLRDcaMW60NJJF6qZirAEygOjf5%2BeVtuaWspLy5WDZtJqo5SIyONn3d9ksewED142FQ7kKwIqyHbfQKAPjoEOul7wD2exuQiNE8O2PDnz5mBeqRdg8IaxmJ%2FOFS1T0KEiS4SOnDXfyTnZhw2yXdO%2FRcFvv9Plo2Y3CYXzFRCWHaBaXZN%2BF%2BTM5Hny2H4uAF4M40zDel6XMBjqkAfh9EDGolPQ84EyO4SMiQ0d5ywPq5xLaW84x6XwPVgKgDOTZ1cPFiBrwocqO5YD3eKI3B0GIdrpaxgWFCmDYjVoJNCtADjuHVqn9f7w89IYgfoQ0bRiWLKA4fZBw2JiQat1S29f5GIf2%2BWjIx8jgmv1S6x4guUpWRIex3O8QemNFZQ%2BpcUEVahPQiOjzw1uJL97qDefESTMWfHRBvjLLvVGA6gz6&X-Amz-Signature=8ca5976467f00a795308ad25d9bd695fa2d53706bba1046ee1acd5a630532cd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

