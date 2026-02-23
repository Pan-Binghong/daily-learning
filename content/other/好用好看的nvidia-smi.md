---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROBBQSA5%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCICkuXa0P%2FQRs56kzWu99fS0DtyopgJkq4HXzv1QGClg8AiEA0kXHxzgdaxBflZxeXuSKDdPXZEDCIhG3zcYZzX8j7YUqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCWeHstvH5vFsSGQyrcA6UEFGR5aev796AVT4tA2HsO2UzPrWBaQ%2B30BkFZH%2FoIRNUCbpVIlNi2QM%2FlA2FhlTRGg9tBSYUG75MDmtFyDEKV490MnJ2Welcz4jI17dQgf%2FU8neQr%2F0%2BiYWaB4KWukjSH%2FxSriI4qe1GdvNuno%2B%2Ft7Nqrj6344DTucrSA%2B%2FNeDJXERfkZv%2BCZvUOpaIx04t4PYdbaf0KvGOMa5wGvt0llRhkYlSaBWwvSbp3tix5%2BQ%2BD7y7FPBT%2F3TtNPgf7Fhso4%2F5Gf1GgjFuAnQcDhVFQ8lE%2FMyICoSaZ0MvxatrMT1TRxcgl7s2lm3Jm5ytbdOovKc%2B%2F50ItJlK0rMvXw4SFhPwd4vwmcZJERW8FeH%2BitK6w8eJnvYu5mPDtXEfqui5dKYolfK7bLvGbXQRs9I4mBT4tr5V87Gr9549%2FLfvbpyKuWk4I7913smRiLrhm74XJRH2A7itrqFtmDitViJ0PKZ3pyomYCxYpTpFdfFvsk3Lxx2h9sPsmJit%2Fnx8H0N3BJxq85DpZOVop3PY1cp7YAZJm%2FM0Z2krD8WHHzebdeHXuLVidhHAuOk2Qy1ALXzdVA2%2FrOjiPoozvaDiz8dJWJp2ilf0oN7xqoCcRb4WaAT3Xpj3y%2Fjo28XSvvMIKU78wGOqUBYwJTTFv5vuSDPMcVdUrMPrAInPh9t5Fz9CATILcdDuxDU8fx921GUdfM6QT9p65J1SCG5TOZVAL58xL7a5SFRv0%2B7zu5xQTretd0RMT7BSiO5H4WfOpwjleoqyF6wbU1R2kGyKcl7z7Zz2ADT%2BWJ3OvyYojBmeR8ebkN0MFA60zkxO2xhdoQBZs4x29BCOJ81UGo7JaVj072gtCMk6spgXCG3auN&X-Amz-Signature=7f69c6daaab578f72c7577ccb61ac273524577f15fc15f7ff77cd88cbe462a12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROBBQSA5%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCICkuXa0P%2FQRs56kzWu99fS0DtyopgJkq4HXzv1QGClg8AiEA0kXHxzgdaxBflZxeXuSKDdPXZEDCIhG3zcYZzX8j7YUqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCWeHstvH5vFsSGQyrcA6UEFGR5aev796AVT4tA2HsO2UzPrWBaQ%2B30BkFZH%2FoIRNUCbpVIlNi2QM%2FlA2FhlTRGg9tBSYUG75MDmtFyDEKV490MnJ2Welcz4jI17dQgf%2FU8neQr%2F0%2BiYWaB4KWukjSH%2FxSriI4qe1GdvNuno%2B%2Ft7Nqrj6344DTucrSA%2B%2FNeDJXERfkZv%2BCZvUOpaIx04t4PYdbaf0KvGOMa5wGvt0llRhkYlSaBWwvSbp3tix5%2BQ%2BD7y7FPBT%2F3TtNPgf7Fhso4%2F5Gf1GgjFuAnQcDhVFQ8lE%2FMyICoSaZ0MvxatrMT1TRxcgl7s2lm3Jm5ytbdOovKc%2B%2F50ItJlK0rMvXw4SFhPwd4vwmcZJERW8FeH%2BitK6w8eJnvYu5mPDtXEfqui5dKYolfK7bLvGbXQRs9I4mBT4tr5V87Gr9549%2FLfvbpyKuWk4I7913smRiLrhm74XJRH2A7itrqFtmDitViJ0PKZ3pyomYCxYpTpFdfFvsk3Lxx2h9sPsmJit%2Fnx8H0N3BJxq85DpZOVop3PY1cp7YAZJm%2FM0Z2krD8WHHzebdeHXuLVidhHAuOk2Qy1ALXzdVA2%2FrOjiPoozvaDiz8dJWJp2ilf0oN7xqoCcRb4WaAT3Xpj3y%2Fjo28XSvvMIKU78wGOqUBYwJTTFv5vuSDPMcVdUrMPrAInPh9t5Fz9CATILcdDuxDU8fx921GUdfM6QT9p65J1SCG5TOZVAL58xL7a5SFRv0%2B7zu5xQTretd0RMT7BSiO5H4WfOpwjleoqyF6wbU1R2kGyKcl7z7Zz2ADT%2BWJ3OvyYojBmeR8ebkN0MFA60zkxO2xhdoQBZs4x29BCOJ81UGo7JaVj072gtCMk6spgXCG3auN&X-Amz-Signature=dfa682f1f141e6f5ed76e0fbb884ab62cf31ac19a52d47ed2ef5887f7de8145b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









