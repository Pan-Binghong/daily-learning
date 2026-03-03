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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6H7RPSV%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9sdJ5ZJgkvuc9tDnj%2Be8oZS4mjSE876YdM0tv7RHBOAiAOj%2BJIII9%2B1l86ef%2FyD7jNVgTUHrlcZhoyotw%2BNIo8mSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn8tlYyq%2B6%2BwQEAKuKtwD76zQTCKI34HCKDDB4m9HOrRdvnDZ46jIKOtO0vr6M1WzErTkAjujOEjoChSCjMggnyLry3rqqjZwAPh4XlcEst45I4yLJh77g9DV5d8p%2FEUIUfCe5E6nddTbxIKL23B%2FuIXS6WoBncTGdKwAnpVMbF32Gs1PNTHQSDclFOH3HPbaIXGpKnEK4dN2NuxjjqZ%2BBFtNk0wfuEU9X4VfDFaR8H90kUl5SumZJQC4wjPI5pqMBPDn%2F5STMWjga%2Fg7DnHB290jsuCivg9XmP8dlJYZZjQRkPMMzDVvlwuWZztvQKanCq4PSi%2FDJefMFcuRxEABgPoR%2BgmUOkOhgtt3MHIUB47Z1CmwuWBiOHllfy1zU9OShprdr6%2FPyz26prO6YHQSvlPrzFvafAaamensGm57Wsb%2Bm2ALgkvkMAGr1pYXQmAw0T8Znbm7zH1AnDEK22NnsjiovJxRdvujjuq6o4uhCFC%2F2sPPWTg6cYyK5lremh8Am3B5fR0klmwGbhb%2FOVHtTnkPbA9U2vY4BTsL6AvrVm8NC0a38981arJTI50v7yzYcJ9obLQ2o%2BEq3QboUOqwdnXVWuyN7vcv6z%2F7CkcGOSF7yUDILoLK%2BkH9NaeCwUkeiBYDStllItkGTJEwyrWYzQY6pgE7wuT8qFVu80bXrfuG7g8llIQrBa%2FUJxtk5qmAiap7GfmzmksjUozKz%2Fb7Jst2A3pQ0kwj0%2BozlWPsdZFuJPWZLhHDYYun8NC3C0Es%2BvqkBo5kE4dwlxLtJJWBu5SRmsSMLsof0wV9OvhQxzPIdE6I0BsHFPK7rNkH5QaSpz6owl9XGbRr6ZOd%2BIRx4VTIN%2BlzQrNeDsfePfcEQzGDfmK%2FB9cTSxRU&X-Amz-Signature=83d1e4f86b364dcfe93517ab206d650ef8ed511a12716391b4dc7f28909d35cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6H7RPSV%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9sdJ5ZJgkvuc9tDnj%2Be8oZS4mjSE876YdM0tv7RHBOAiAOj%2BJIII9%2B1l86ef%2FyD7jNVgTUHrlcZhoyotw%2BNIo8mSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn8tlYyq%2B6%2BwQEAKuKtwD76zQTCKI34HCKDDB4m9HOrRdvnDZ46jIKOtO0vr6M1WzErTkAjujOEjoChSCjMggnyLry3rqqjZwAPh4XlcEst45I4yLJh77g9DV5d8p%2FEUIUfCe5E6nddTbxIKL23B%2FuIXS6WoBncTGdKwAnpVMbF32Gs1PNTHQSDclFOH3HPbaIXGpKnEK4dN2NuxjjqZ%2BBFtNk0wfuEU9X4VfDFaR8H90kUl5SumZJQC4wjPI5pqMBPDn%2F5STMWjga%2Fg7DnHB290jsuCivg9XmP8dlJYZZjQRkPMMzDVvlwuWZztvQKanCq4PSi%2FDJefMFcuRxEABgPoR%2BgmUOkOhgtt3MHIUB47Z1CmwuWBiOHllfy1zU9OShprdr6%2FPyz26prO6YHQSvlPrzFvafAaamensGm57Wsb%2Bm2ALgkvkMAGr1pYXQmAw0T8Znbm7zH1AnDEK22NnsjiovJxRdvujjuq6o4uhCFC%2F2sPPWTg6cYyK5lremh8Am3B5fR0klmwGbhb%2FOVHtTnkPbA9U2vY4BTsL6AvrVm8NC0a38981arJTI50v7yzYcJ9obLQ2o%2BEq3QboUOqwdnXVWuyN7vcv6z%2F7CkcGOSF7yUDILoLK%2BkH9NaeCwUkeiBYDStllItkGTJEwyrWYzQY6pgE7wuT8qFVu80bXrfuG7g8llIQrBa%2FUJxtk5qmAiap7GfmzmksjUozKz%2Fb7Jst2A3pQ0kwj0%2BozlWPsdZFuJPWZLhHDYYun8NC3C0Es%2BvqkBo5kE4dwlxLtJJWBu5SRmsSMLsof0wV9OvhQxzPIdE6I0BsHFPK7rNkH5QaSpz6owl9XGbRr6ZOd%2BIRx4VTIN%2BlzQrNeDsfePfcEQzGDfmK%2FB9cTSxRU&X-Amz-Signature=f09f36bb00434c8e4c4dbd15f25b67d030ccb39fa67eec71882630cc974b14fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6H7RPSV%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9sdJ5ZJgkvuc9tDnj%2Be8oZS4mjSE876YdM0tv7RHBOAiAOj%2BJIII9%2B1l86ef%2FyD7jNVgTUHrlcZhoyotw%2BNIo8mSqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn8tlYyq%2B6%2BwQEAKuKtwD76zQTCKI34HCKDDB4m9HOrRdvnDZ46jIKOtO0vr6M1WzErTkAjujOEjoChSCjMggnyLry3rqqjZwAPh4XlcEst45I4yLJh77g9DV5d8p%2FEUIUfCe5E6nddTbxIKL23B%2FuIXS6WoBncTGdKwAnpVMbF32Gs1PNTHQSDclFOH3HPbaIXGpKnEK4dN2NuxjjqZ%2BBFtNk0wfuEU9X4VfDFaR8H90kUl5SumZJQC4wjPI5pqMBPDn%2F5STMWjga%2Fg7DnHB290jsuCivg9XmP8dlJYZZjQRkPMMzDVvlwuWZztvQKanCq4PSi%2FDJefMFcuRxEABgPoR%2BgmUOkOhgtt3MHIUB47Z1CmwuWBiOHllfy1zU9OShprdr6%2FPyz26prO6YHQSvlPrzFvafAaamensGm57Wsb%2Bm2ALgkvkMAGr1pYXQmAw0T8Znbm7zH1AnDEK22NnsjiovJxRdvujjuq6o4uhCFC%2F2sPPWTg6cYyK5lremh8Am3B5fR0klmwGbhb%2FOVHtTnkPbA9U2vY4BTsL6AvrVm8NC0a38981arJTI50v7yzYcJ9obLQ2o%2BEq3QboUOqwdnXVWuyN7vcv6z%2F7CkcGOSF7yUDILoLK%2BkH9NaeCwUkeiBYDStllItkGTJEwyrWYzQY6pgE7wuT8qFVu80bXrfuG7g8llIQrBa%2FUJxtk5qmAiap7GfmzmksjUozKz%2Fb7Jst2A3pQ0kwj0%2BozlWPsdZFuJPWZLhHDYYun8NC3C0Es%2BvqkBo5kE4dwlxLtJJWBu5SRmsSMLsof0wV9OvhQxzPIdE6I0BsHFPK7rNkH5QaSpz6owl9XGbRr6ZOd%2BIRx4VTIN%2BlzQrNeDsfePfcEQzGDfmK%2FB9cTSxRU&X-Amz-Signature=6f72b982ca2e85f1b7d0efad6322a348c7479069eb4040aedaa2b180884dc4b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

