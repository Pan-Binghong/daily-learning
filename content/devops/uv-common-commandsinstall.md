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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HQOBHYC%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDX8BUIS1eew5Ej74pg932FPipV3eaA6deGt2Ugno9SvgIhAIDHzVDs2UtPTDYuxR8DjrOZYmhKXmaTRAeUEyoog%2FKIKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3dOwjm3QnIf5p%2Fzoq3AN7r7L1BYAndjoklK75FqRa5NzaR89XqKHzb7D7Sd7G%2F2NIAjD6oVH7HGuLV3vhdWlGM%2BBEC5GcAbZP5pADf%2F0NVG1y%2BE3EM%2BM%2BLxe5ZgDOzg%2FQ2uuybckwRuaA5sBpLozfaDdqXSlwqAdCmbS5Ob0zIjRKX7r%2BKiucYNb%2Bg1%2Bl6QMuFHjGtS6wyC73f%2FNk2ZWoiSNp41mAh%2BeJEXaEq2HHJ18h1prXCR%2Bs3cHszwkb%2Bu%2BdNe0GLFqEyVi02S0py3UD6P0%2BTTMUl2LMxVIzsFre%2FOWtSmZx%2F%2BlM88zKB9FhBuvN5ti1x5DDrexEOUmUvNsb51jkv9Aw%2FJox8cCAU0X9%2BqMPsKgAkFXVwJdKa3ZmNxFdqlr1TLjuAhsrKjpPFrRsWJLDw%2BYgUogKjF9wV2ldMuN%2BOcQWdSvcO%2FKoeB608dS4%2Fpw90D%2FV3sQKdQtH%2FEkMAZmb0XnFBkeEBOF7A3BN1JBy7hW%2BQeCNVGW1EPvvx8lGT9aPDLiGDZDfl73BmTD6qJ784PlDM5dT4F14lyIlEWm%2FKPEOI3P2RO9cUXBpw9iHgqZAc3triracBoEndVe9EOP3rhpujXGdo2kAr4tw3t%2BsBcQEmFhnMzs9i3zFj397WR8hBHyUOH3sejDt5ZbLBjqkAbIXLWWKvFg9erIgU73pe0m3rI0ExOprcSdzhr8mP229atS%2FXW8Qgql%2BF74%2FXWOyMnGtdnCdi3wtCyKjREd25N1fgmqLBTJ3kDQ8HBR49%2Fku9oVCWB2gvi4M6fVuRpR3nFsPsA7hP7fUUPfkkzSXWdMFqBsaLE2VxJyxcxyi3Gqjy2%2Ff48URFWqyCHFDkOM7Ob6O1xEKbRM0aGTX8GwlOxVMwsv9&X-Amz-Signature=2a22702f13d4d1699a990908bf91548ec5b7ab7a64eff7b5900da1ef4cdcbd39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HQOBHYC%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDX8BUIS1eew5Ej74pg932FPipV3eaA6deGt2Ugno9SvgIhAIDHzVDs2UtPTDYuxR8DjrOZYmhKXmaTRAeUEyoog%2FKIKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3dOwjm3QnIf5p%2Fzoq3AN7r7L1BYAndjoklK75FqRa5NzaR89XqKHzb7D7Sd7G%2F2NIAjD6oVH7HGuLV3vhdWlGM%2BBEC5GcAbZP5pADf%2F0NVG1y%2BE3EM%2BM%2BLxe5ZgDOzg%2FQ2uuybckwRuaA5sBpLozfaDdqXSlwqAdCmbS5Ob0zIjRKX7r%2BKiucYNb%2Bg1%2Bl6QMuFHjGtS6wyC73f%2FNk2ZWoiSNp41mAh%2BeJEXaEq2HHJ18h1prXCR%2Bs3cHszwkb%2Bu%2BdNe0GLFqEyVi02S0py3UD6P0%2BTTMUl2LMxVIzsFre%2FOWtSmZx%2F%2BlM88zKB9FhBuvN5ti1x5DDrexEOUmUvNsb51jkv9Aw%2FJox8cCAU0X9%2BqMPsKgAkFXVwJdKa3ZmNxFdqlr1TLjuAhsrKjpPFrRsWJLDw%2BYgUogKjF9wV2ldMuN%2BOcQWdSvcO%2FKoeB608dS4%2Fpw90D%2FV3sQKdQtH%2FEkMAZmb0XnFBkeEBOF7A3BN1JBy7hW%2BQeCNVGW1EPvvx8lGT9aPDLiGDZDfl73BmTD6qJ784PlDM5dT4F14lyIlEWm%2FKPEOI3P2RO9cUXBpw9iHgqZAc3triracBoEndVe9EOP3rhpujXGdo2kAr4tw3t%2BsBcQEmFhnMzs9i3zFj397WR8hBHyUOH3sejDt5ZbLBjqkAbIXLWWKvFg9erIgU73pe0m3rI0ExOprcSdzhr8mP229atS%2FXW8Qgql%2BF74%2FXWOyMnGtdnCdi3wtCyKjREd25N1fgmqLBTJ3kDQ8HBR49%2Fku9oVCWB2gvi4M6fVuRpR3nFsPsA7hP7fUUPfkkzSXWdMFqBsaLE2VxJyxcxyi3Gqjy2%2Ff48URFWqyCHFDkOM7Ob6O1xEKbRM0aGTX8GwlOxVMwsv9&X-Amz-Signature=2be4dac5e6cce3047620ae3a874141103103eedde84bf1e9deade84156a596b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HQOBHYC%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDX8BUIS1eew5Ej74pg932FPipV3eaA6deGt2Ugno9SvgIhAIDHzVDs2UtPTDYuxR8DjrOZYmhKXmaTRAeUEyoog%2FKIKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3dOwjm3QnIf5p%2Fzoq3AN7r7L1BYAndjoklK75FqRa5NzaR89XqKHzb7D7Sd7G%2F2NIAjD6oVH7HGuLV3vhdWlGM%2BBEC5GcAbZP5pADf%2F0NVG1y%2BE3EM%2BM%2BLxe5ZgDOzg%2FQ2uuybckwRuaA5sBpLozfaDdqXSlwqAdCmbS5Ob0zIjRKX7r%2BKiucYNb%2Bg1%2Bl6QMuFHjGtS6wyC73f%2FNk2ZWoiSNp41mAh%2BeJEXaEq2HHJ18h1prXCR%2Bs3cHszwkb%2Bu%2BdNe0GLFqEyVi02S0py3UD6P0%2BTTMUl2LMxVIzsFre%2FOWtSmZx%2F%2BlM88zKB9FhBuvN5ti1x5DDrexEOUmUvNsb51jkv9Aw%2FJox8cCAU0X9%2BqMPsKgAkFXVwJdKa3ZmNxFdqlr1TLjuAhsrKjpPFrRsWJLDw%2BYgUogKjF9wV2ldMuN%2BOcQWdSvcO%2FKoeB608dS4%2Fpw90D%2FV3sQKdQtH%2FEkMAZmb0XnFBkeEBOF7A3BN1JBy7hW%2BQeCNVGW1EPvvx8lGT9aPDLiGDZDfl73BmTD6qJ784PlDM5dT4F14lyIlEWm%2FKPEOI3P2RO9cUXBpw9iHgqZAc3triracBoEndVe9EOP3rhpujXGdo2kAr4tw3t%2BsBcQEmFhnMzs9i3zFj397WR8hBHyUOH3sejDt5ZbLBjqkAbIXLWWKvFg9erIgU73pe0m3rI0ExOprcSdzhr8mP229atS%2FXW8Qgql%2BF74%2FXWOyMnGtdnCdi3wtCyKjREd25N1fgmqLBTJ3kDQ8HBR49%2Fku9oVCWB2gvi4M6fVuRpR3nFsPsA7hP7fUUPfkkzSXWdMFqBsaLE2VxJyxcxyi3Gqjy2%2Ff48URFWqyCHFDkOM7Ob6O1xEKbRM0aGTX8GwlOxVMwsv9&X-Amz-Signature=531f7045d888d9769f3f71b8009cba7623166fab03a3bb3c088ec3f6b0ea806f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

