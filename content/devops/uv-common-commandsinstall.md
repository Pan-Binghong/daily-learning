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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCS5G3JK%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxUesI2oZQgGr5yTkAxj1v60MLVhf4PXuS39ix2nkEwwIhAJ%2FTki2A%2BJ1LbxMbH6d1obHL4vSEdN91NCbok5Bkt0WnKv8DCEsQABoMNjM3NDIzMTgzODA1IgwDvaXWWhoxEkGrSi4q3ANU4TS77Hdq%2BpWxfr%2B9rct9zlXjlr%2BAncQJl1UUwjsUynUL5h5Uip2Q2HeVECWFGhOtzrdM93M%2BEsMfTI8u1thCz4v8Swz6eAkKTxUKhjd5VDroxFs%2BatCuoriwMpPr996If9Iz3lRt3WMtoUzer6X3H7uyDqcQjl52vlFzWCsLea9ba8xiN2uWRCJes5Ei4xSRWevlxwWZL9JZ0L6Co1GBlnO0QKnqvWNWXtC7VFsKILMc7UdpjEgggKoFzOw9bqKMON%2FI1BAXq9NuHe9YXCUwpxxoy%2BGtw8CtKQPWk8KokrbkVQji6430RvDXrNH5cUfBUO18CDtZ3S2bCg4CjLwlf57Mwt49qaF%2BiMMKds0Wv%2B%2Btsp6q2kzgSx%2BF9bB7s4VUy1wODy0lTXAFOo99Y2SoJKPRDuwQfcMJEdFF9uwufG68lLMMjr0Gnc23vkI2dBMIxPLg0c9Sjh0kO5zp21o5fw9iu%2FZTQlwXZDmAGMQy3Df0Q644spV8L9D81%2BFv%2B9BbKuPnUpJvzp9aYVmlLQmXtT7cV%2FUiCZh2Jfsf3D%2FykpOVUkZN4RfB%2BJ40YdpS3lwVshTBqwbDmE9UopE9Awct3m8GkGRzZ79ICFpLj6tV7%2Bx9YXw5KiDc5NhYmDD%2BlYnNBjqkARgwBgtDIaaHY8Q0OfIO43q7e51kgrm0rVMnGx6nOA9Lq6P2U5KX62n8r%2FVrqJUnb5rSJvwZ4Gyann%2BXR3XGidMZxG5C%2FxJ43hAYivAQ7LTHf3OaGmPxmFUSixiQjO%2BkjE70Fc6mgMlY%2FGqdCzt7yUjsZzg8cz341F6YmEnxwBNsNC6k78vAxaAKVH5JPP5agNRWBDThNOhXEYwcjSQtjP37cFS5&X-Amz-Signature=65be729505d16e18a143ec05ba18dedfca01ac1ad9b44a99cbb80549b455de25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCS5G3JK%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxUesI2oZQgGr5yTkAxj1v60MLVhf4PXuS39ix2nkEwwIhAJ%2FTki2A%2BJ1LbxMbH6d1obHL4vSEdN91NCbok5Bkt0WnKv8DCEsQABoMNjM3NDIzMTgzODA1IgwDvaXWWhoxEkGrSi4q3ANU4TS77Hdq%2BpWxfr%2B9rct9zlXjlr%2BAncQJl1UUwjsUynUL5h5Uip2Q2HeVECWFGhOtzrdM93M%2BEsMfTI8u1thCz4v8Swz6eAkKTxUKhjd5VDroxFs%2BatCuoriwMpPr996If9Iz3lRt3WMtoUzer6X3H7uyDqcQjl52vlFzWCsLea9ba8xiN2uWRCJes5Ei4xSRWevlxwWZL9JZ0L6Co1GBlnO0QKnqvWNWXtC7VFsKILMc7UdpjEgggKoFzOw9bqKMON%2FI1BAXq9NuHe9YXCUwpxxoy%2BGtw8CtKQPWk8KokrbkVQji6430RvDXrNH5cUfBUO18CDtZ3S2bCg4CjLwlf57Mwt49qaF%2BiMMKds0Wv%2B%2Btsp6q2kzgSx%2BF9bB7s4VUy1wODy0lTXAFOo99Y2SoJKPRDuwQfcMJEdFF9uwufG68lLMMjr0Gnc23vkI2dBMIxPLg0c9Sjh0kO5zp21o5fw9iu%2FZTQlwXZDmAGMQy3Df0Q644spV8L9D81%2BFv%2B9BbKuPnUpJvzp9aYVmlLQmXtT7cV%2FUiCZh2Jfsf3D%2FykpOVUkZN4RfB%2BJ40YdpS3lwVshTBqwbDmE9UopE9Awct3m8GkGRzZ79ICFpLj6tV7%2Bx9YXw5KiDc5NhYmDD%2BlYnNBjqkARgwBgtDIaaHY8Q0OfIO43q7e51kgrm0rVMnGx6nOA9Lq6P2U5KX62n8r%2FVrqJUnb5rSJvwZ4Gyann%2BXR3XGidMZxG5C%2FxJ43hAYivAQ7LTHf3OaGmPxmFUSixiQjO%2BkjE70Fc6mgMlY%2FGqdCzt7yUjsZzg8cz341F6YmEnxwBNsNC6k78vAxaAKVH5JPP5agNRWBDThNOhXEYwcjSQtjP37cFS5&X-Amz-Signature=fce09b0be7026cd346f69a34ee9bd068cdeafb29b741e89f22cca7ff1faac093&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCS5G3JK%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxUesI2oZQgGr5yTkAxj1v60MLVhf4PXuS39ix2nkEwwIhAJ%2FTki2A%2BJ1LbxMbH6d1obHL4vSEdN91NCbok5Bkt0WnKv8DCEsQABoMNjM3NDIzMTgzODA1IgwDvaXWWhoxEkGrSi4q3ANU4TS77Hdq%2BpWxfr%2B9rct9zlXjlr%2BAncQJl1UUwjsUynUL5h5Uip2Q2HeVECWFGhOtzrdM93M%2BEsMfTI8u1thCz4v8Swz6eAkKTxUKhjd5VDroxFs%2BatCuoriwMpPr996If9Iz3lRt3WMtoUzer6X3H7uyDqcQjl52vlFzWCsLea9ba8xiN2uWRCJes5Ei4xSRWevlxwWZL9JZ0L6Co1GBlnO0QKnqvWNWXtC7VFsKILMc7UdpjEgggKoFzOw9bqKMON%2FI1BAXq9NuHe9YXCUwpxxoy%2BGtw8CtKQPWk8KokrbkVQji6430RvDXrNH5cUfBUO18CDtZ3S2bCg4CjLwlf57Mwt49qaF%2BiMMKds0Wv%2B%2Btsp6q2kzgSx%2BF9bB7s4VUy1wODy0lTXAFOo99Y2SoJKPRDuwQfcMJEdFF9uwufG68lLMMjr0Gnc23vkI2dBMIxPLg0c9Sjh0kO5zp21o5fw9iu%2FZTQlwXZDmAGMQy3Df0Q644spV8L9D81%2BFv%2B9BbKuPnUpJvzp9aYVmlLQmXtT7cV%2FUiCZh2Jfsf3D%2FykpOVUkZN4RfB%2BJ40YdpS3lwVshTBqwbDmE9UopE9Awct3m8GkGRzZ79ICFpLj6tV7%2Bx9YXw5KiDc5NhYmDD%2BlYnNBjqkARgwBgtDIaaHY8Q0OfIO43q7e51kgrm0rVMnGx6nOA9Lq6P2U5KX62n8r%2FVrqJUnb5rSJvwZ4Gyann%2BXR3XGidMZxG5C%2FxJ43hAYivAQ7LTHf3OaGmPxmFUSixiQjO%2BkjE70Fc6mgMlY%2FGqdCzt7yUjsZzg8cz341F6YmEnxwBNsNC6k78vAxaAKVH5JPP5agNRWBDThNOhXEYwcjSQtjP37cFS5&X-Amz-Signature=22c02302b6d40e3242b47dd98ff272acf57cc9752e5dff4bfebaf0f901d537f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

