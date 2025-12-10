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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HJXOTLI%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIB1oEtgOJ49Mz7g5PfrQAOs7MCywVk7eby%2BSfQNC6M6oAiAxumPCTBWxpyJaOWCBpEZh8WjX7OmWp2JDT4UI1qdGmyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBoEwpP1Gb7Qg3AQoKtwDOSqir9whu3KT1E3CF8%2B8uokIbrIAkNtYrF03BEyatw01iyrUVNWgajsSj7%2FLjuC7cDAzfOh%2FF%2BF7E55JZzw5RA6%2BRUxZoD9W9UQ8RnEllsBf%2FPUcyc9yYM2wVhvXJoKFyCUo84QeF%2BiTCU4rd36OyIQGwsBp0X4D20wV%2BMaB7iBRKKigDwbHAQGoFjBGOYO1Eb4O%2FyP01bb8u9CSbDbg25tCwyH4mUMD3iyAdVXxI2B3H9k%2Btk4vPDOJHLBcaGTcrLalg6KpaValNRgnxoawoWhF4RpFoho0c2LyosPImJVFjYTctydwrQPXyQhxpPC0RIrstvgDZmjcRkYs40obbilZx4%2FJpU0td8Jb2%2FyZl2zWWMM2ES3L14kur9BlNIvGvQ%2FLqLs9%2Fyc2ZM214AUUbuTJk8XLy8GMhPlZmg4E4QXkWra0C5AGjq3NcZPHYWh6NimXi6tfKansApQxmmSgF%2FjOrDHIwa03VQ9at3EJIdl9zChjsNDyUD9k6O93T4gnaAzieSHorV2%2F74SlZ1OC7okGIa96dB2FeXy%2FUXOWjtSB9Zw%2BMDq%2Bk3kGrdef0KS2rrPeJjqoKXKK38ZyDyv%2FPjseYkosTY1WfN7pK64ZnlJgn2rDf9liOXT4rMUwx7%2FjyQY6pgHr0U2Exsl8cKbf5SGjQpM51GVoEJ9TvTZ8AZcy7azxf4M2OVEy%2BsOkUkUtL32ktbanglWkb5%2BA6L3yTXunJf8Y%2B%2Bmxm4w9wQbf4pcDD%2BnQB03wFE8zJHZ5HGslSkyBIrRfsvbqpiLE%2BJnSEMr2630YWLr%2FB8hx2GB7w0QyuN8wlOdKeEws1kLUnwb0Dh%2FpmcdMcoAz07mV4uBNQY5ZDTD2XH%2F5LGUD&X-Amz-Signature=5dbdd638c3c5b00c9a5114d0c40f9bc50bc7f100d27d7d81f82715b3476852f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HJXOTLI%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIB1oEtgOJ49Mz7g5PfrQAOs7MCywVk7eby%2BSfQNC6M6oAiAxumPCTBWxpyJaOWCBpEZh8WjX7OmWp2JDT4UI1qdGmyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBoEwpP1Gb7Qg3AQoKtwDOSqir9whu3KT1E3CF8%2B8uokIbrIAkNtYrF03BEyatw01iyrUVNWgajsSj7%2FLjuC7cDAzfOh%2FF%2BF7E55JZzw5RA6%2BRUxZoD9W9UQ8RnEllsBf%2FPUcyc9yYM2wVhvXJoKFyCUo84QeF%2BiTCU4rd36OyIQGwsBp0X4D20wV%2BMaB7iBRKKigDwbHAQGoFjBGOYO1Eb4O%2FyP01bb8u9CSbDbg25tCwyH4mUMD3iyAdVXxI2B3H9k%2Btk4vPDOJHLBcaGTcrLalg6KpaValNRgnxoawoWhF4RpFoho0c2LyosPImJVFjYTctydwrQPXyQhxpPC0RIrstvgDZmjcRkYs40obbilZx4%2FJpU0td8Jb2%2FyZl2zWWMM2ES3L14kur9BlNIvGvQ%2FLqLs9%2Fyc2ZM214AUUbuTJk8XLy8GMhPlZmg4E4QXkWra0C5AGjq3NcZPHYWh6NimXi6tfKansApQxmmSgF%2FjOrDHIwa03VQ9at3EJIdl9zChjsNDyUD9k6O93T4gnaAzieSHorV2%2F74SlZ1OC7okGIa96dB2FeXy%2FUXOWjtSB9Zw%2BMDq%2Bk3kGrdef0KS2rrPeJjqoKXKK38ZyDyv%2FPjseYkosTY1WfN7pK64ZnlJgn2rDf9liOXT4rMUwx7%2FjyQY6pgHr0U2Exsl8cKbf5SGjQpM51GVoEJ9TvTZ8AZcy7azxf4M2OVEy%2BsOkUkUtL32ktbanglWkb5%2BA6L3yTXunJf8Y%2B%2Bmxm4w9wQbf4pcDD%2BnQB03wFE8zJHZ5HGslSkyBIrRfsvbqpiLE%2BJnSEMr2630YWLr%2FB8hx2GB7w0QyuN8wlOdKeEws1kLUnwb0Dh%2FpmcdMcoAz07mV4uBNQY5ZDTD2XH%2F5LGUD&X-Amz-Signature=32a5d3b1f41cb1ca5590f08cc3fcd5e01c115087458147b6c006df4d7fbba2a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HJXOTLI%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIB1oEtgOJ49Mz7g5PfrQAOs7MCywVk7eby%2BSfQNC6M6oAiAxumPCTBWxpyJaOWCBpEZh8WjX7OmWp2JDT4UI1qdGmyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBoEwpP1Gb7Qg3AQoKtwDOSqir9whu3KT1E3CF8%2B8uokIbrIAkNtYrF03BEyatw01iyrUVNWgajsSj7%2FLjuC7cDAzfOh%2FF%2BF7E55JZzw5RA6%2BRUxZoD9W9UQ8RnEllsBf%2FPUcyc9yYM2wVhvXJoKFyCUo84QeF%2BiTCU4rd36OyIQGwsBp0X4D20wV%2BMaB7iBRKKigDwbHAQGoFjBGOYO1Eb4O%2FyP01bb8u9CSbDbg25tCwyH4mUMD3iyAdVXxI2B3H9k%2Btk4vPDOJHLBcaGTcrLalg6KpaValNRgnxoawoWhF4RpFoho0c2LyosPImJVFjYTctydwrQPXyQhxpPC0RIrstvgDZmjcRkYs40obbilZx4%2FJpU0td8Jb2%2FyZl2zWWMM2ES3L14kur9BlNIvGvQ%2FLqLs9%2Fyc2ZM214AUUbuTJk8XLy8GMhPlZmg4E4QXkWra0C5AGjq3NcZPHYWh6NimXi6tfKansApQxmmSgF%2FjOrDHIwa03VQ9at3EJIdl9zChjsNDyUD9k6O93T4gnaAzieSHorV2%2F74SlZ1OC7okGIa96dB2FeXy%2FUXOWjtSB9Zw%2BMDq%2Bk3kGrdef0KS2rrPeJjqoKXKK38ZyDyv%2FPjseYkosTY1WfN7pK64ZnlJgn2rDf9liOXT4rMUwx7%2FjyQY6pgHr0U2Exsl8cKbf5SGjQpM51GVoEJ9TvTZ8AZcy7azxf4M2OVEy%2BsOkUkUtL32ktbanglWkb5%2BA6L3yTXunJf8Y%2B%2Bmxm4w9wQbf4pcDD%2BnQB03wFE8zJHZ5HGslSkyBIrRfsvbqpiLE%2BJnSEMr2630YWLr%2FB8hx2GB7w0QyuN8wlOdKeEws1kLUnwb0Dh%2FpmcdMcoAz07mV4uBNQY5ZDTD2XH%2F5LGUD&X-Amz-Signature=0bc4e266130ef6855db787a54fc68e4388a168cd1f7408b608cdde29440138f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

