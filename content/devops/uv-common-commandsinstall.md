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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVO2C3SS%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCHWs7K%2FTFplOP%2FF53T0qeat1GgpRvADO6UCuZUlXnPDwIhANiXjmpzS9CWeK9hth7lyrk81Y%2FnyGQAx4aNtnrYFbuqKv8DCAUQABoMNjM3NDIzMTgzODA1Igw6G7%2FEjDg3nDaw5X4q3APRVRKLtkKtRc0TkTv%2BiMNdc6ujG1AtPh87H6P79S5jSB6TitJPUikbzDuCjCaJio63SF02zWYzBB0T6%2BoQ7xQx74HX3%2F%2FDaRxUwv32j%2F6TEUimbOTatXzi8kIUsWb8JsyE%2BpsR0jhVo8PZ3%2FDFQ54L4YgTk8YqouQnTpWecmaDV1PoZU4xS6H%2FYUcsz%2FwwqIto4lIog%2BJilUpuuwIPPptiqq131Merou27%2BLCvZrwEoKMlzIM1Jef3NHGIvhIxYdT%2BxKAeu6v%2FjoxX1JQ9KcEr52Fwf9CwC1ollsBXh4M4vWaF5qttQfp7j0ZCRvnGFNA7TfMX90bAtJ7x2OPdZ6JhVkTYNBQ316BR2YpRh4NeGsrr%2BWVMn%2FMeqJqG8EslxcarJev3Y1rmoWO4KoZIffltVL1%2FoEtc6yS7aWDgyDUsZ4bKU2ZMy94Zw28IlEeyqqfCNyF1CxgjcIXhaX6jEVPJ96NYVyH8j8pZAfrAM1Tnp6%2BY23jbyEwpImcqc%2BQ1NeKlMTtzHY4ENor7RjCoEAUXF7n%2FZKb6yaSP15DF50d7Ez89kBjW4%2FhDFnMAoNcqfp9bNqN5koSuAZ41NrwACghxZcyGH8SRXfV6kj9NRKrZz9vbYKwILY92Tcx2oDD2vaLOBjqkAffXH1mWEVYxnqlZWJMZLr8KJTzZTQUDbnRslQx%2FrW15yRiXygsV%2Bt3MBl%2BaUAgpH1kj8ogqX5HljvWqWvWwZzUaQBV1b5lOUPUsGHzcxhD4vNn%2BKcNrwMGOG7oJd8YjNraGfZAKVz1rOZUcEtkjtfzW%2Bktdyc8eXmvx56ua%2BrfgmmGqNLnxFZLjWTSaV4gkzfei91snEBWIvk4q59TEdC9%2Fh5GB&X-Amz-Signature=d6430069608a863fa02e9ee610a6bd483e1c9e7c2fe5779bd63a01f21ce5d21c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVO2C3SS%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCHWs7K%2FTFplOP%2FF53T0qeat1GgpRvADO6UCuZUlXnPDwIhANiXjmpzS9CWeK9hth7lyrk81Y%2FnyGQAx4aNtnrYFbuqKv8DCAUQABoMNjM3NDIzMTgzODA1Igw6G7%2FEjDg3nDaw5X4q3APRVRKLtkKtRc0TkTv%2BiMNdc6ujG1AtPh87H6P79S5jSB6TitJPUikbzDuCjCaJio63SF02zWYzBB0T6%2BoQ7xQx74HX3%2F%2FDaRxUwv32j%2F6TEUimbOTatXzi8kIUsWb8JsyE%2BpsR0jhVo8PZ3%2FDFQ54L4YgTk8YqouQnTpWecmaDV1PoZU4xS6H%2FYUcsz%2FwwqIto4lIog%2BJilUpuuwIPPptiqq131Merou27%2BLCvZrwEoKMlzIM1Jef3NHGIvhIxYdT%2BxKAeu6v%2FjoxX1JQ9KcEr52Fwf9CwC1ollsBXh4M4vWaF5qttQfp7j0ZCRvnGFNA7TfMX90bAtJ7x2OPdZ6JhVkTYNBQ316BR2YpRh4NeGsrr%2BWVMn%2FMeqJqG8EslxcarJev3Y1rmoWO4KoZIffltVL1%2FoEtc6yS7aWDgyDUsZ4bKU2ZMy94Zw28IlEeyqqfCNyF1CxgjcIXhaX6jEVPJ96NYVyH8j8pZAfrAM1Tnp6%2BY23jbyEwpImcqc%2BQ1NeKlMTtzHY4ENor7RjCoEAUXF7n%2FZKb6yaSP15DF50d7Ez89kBjW4%2FhDFnMAoNcqfp9bNqN5koSuAZ41NrwACghxZcyGH8SRXfV6kj9NRKrZz9vbYKwILY92Tcx2oDD2vaLOBjqkAffXH1mWEVYxnqlZWJMZLr8KJTzZTQUDbnRslQx%2FrW15yRiXygsV%2Bt3MBl%2BaUAgpH1kj8ogqX5HljvWqWvWwZzUaQBV1b5lOUPUsGHzcxhD4vNn%2BKcNrwMGOG7oJd8YjNraGfZAKVz1rOZUcEtkjtfzW%2Bktdyc8eXmvx56ua%2BrfgmmGqNLnxFZLjWTSaV4gkzfei91snEBWIvk4q59TEdC9%2Fh5GB&X-Amz-Signature=c45258abbeb4950b6823d00e55492f17f33d54d4578130961d40e25f785c8513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVO2C3SS%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCHWs7K%2FTFplOP%2FF53T0qeat1GgpRvADO6UCuZUlXnPDwIhANiXjmpzS9CWeK9hth7lyrk81Y%2FnyGQAx4aNtnrYFbuqKv8DCAUQABoMNjM3NDIzMTgzODA1Igw6G7%2FEjDg3nDaw5X4q3APRVRKLtkKtRc0TkTv%2BiMNdc6ujG1AtPh87H6P79S5jSB6TitJPUikbzDuCjCaJio63SF02zWYzBB0T6%2BoQ7xQx74HX3%2F%2FDaRxUwv32j%2F6TEUimbOTatXzi8kIUsWb8JsyE%2BpsR0jhVo8PZ3%2FDFQ54L4YgTk8YqouQnTpWecmaDV1PoZU4xS6H%2FYUcsz%2FwwqIto4lIog%2BJilUpuuwIPPptiqq131Merou27%2BLCvZrwEoKMlzIM1Jef3NHGIvhIxYdT%2BxKAeu6v%2FjoxX1JQ9KcEr52Fwf9CwC1ollsBXh4M4vWaF5qttQfp7j0ZCRvnGFNA7TfMX90bAtJ7x2OPdZ6JhVkTYNBQ316BR2YpRh4NeGsrr%2BWVMn%2FMeqJqG8EslxcarJev3Y1rmoWO4KoZIffltVL1%2FoEtc6yS7aWDgyDUsZ4bKU2ZMy94Zw28IlEeyqqfCNyF1CxgjcIXhaX6jEVPJ96NYVyH8j8pZAfrAM1Tnp6%2BY23jbyEwpImcqc%2BQ1NeKlMTtzHY4ENor7RjCoEAUXF7n%2FZKb6yaSP15DF50d7Ez89kBjW4%2FhDFnMAoNcqfp9bNqN5koSuAZ41NrwACghxZcyGH8SRXfV6kj9NRKrZz9vbYKwILY92Tcx2oDD2vaLOBjqkAffXH1mWEVYxnqlZWJMZLr8KJTzZTQUDbnRslQx%2FrW15yRiXygsV%2Bt3MBl%2BaUAgpH1kj8ogqX5HljvWqWvWwZzUaQBV1b5lOUPUsGHzcxhD4vNn%2BKcNrwMGOG7oJd8YjNraGfZAKVz1rOZUcEtkjtfzW%2Bktdyc8eXmvx56ua%2BrfgmmGqNLnxFZLjWTSaV4gkzfei91snEBWIvk4q59TEdC9%2Fh5GB&X-Amz-Signature=fb48351913ab9a333d25987accc5ded7155130c53e2848b97411062e2f3d8be2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

