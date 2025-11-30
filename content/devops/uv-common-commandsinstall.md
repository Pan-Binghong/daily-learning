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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIKT2SF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIENq8Dv3ZPzO2hq2sQ4%2FNr3B4WmWSfPcXWsWUiXqozT3AiEA05iTO%2FL%2BEzsY4XdK08x%2BTX9bmChl7uLvGeSadSSEwcAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtlDc%2BFMF5V0rUNqCrcA0L2KxyPNaqmnn1gPk6RHYBLsLiw04Fk7rroNwHStnE422HAoaJ8UZUVYAPWzFBDsGQpgPNy2AhSFTQ7qv8cLVxHfuWE3eCpY4iLya4Su17mNJRFmjT2BzUe%2B0tfCGCDTiefl%2BLLvI6fTe1mNIhCsyKu9jgHkP7b2%2BahS9klWtJKqPwG3efITLrsuRLIuwbo64hYom%2FHSRAi%2F6100RfBLE4aj6tLZNsFSOZD4%2FuDXNbl1BqKVi0sKWjkv3m3FNZ8I55dDsYKdCUOzOyfYHB6QYXbXi9t5yzV2fMP7bL5FXvIQxyBRGygTvgcUajkZA9ToMif14fLFEajBCgXNgLC0X3GT56IVAGY%2BYovDf1KM1Dof4RqWRlDXv7rVtY3Zw%2FXv6AFd5gUkO10LN8DrFS74co8KDBZMCNu9HFMcqMPOvjroA5XzpdXPLJeTMaUnUi8KqTCsQPWFpHtashXexWeCmaBQwRT%2F1sH7kH499QxBIbSWnqpZcDrtOgoA%2BJYw0rhIxnDAlqJ%2FOT9MAD5iYvIPEweJYrTk0DT3aKWUTcErfdFqt3u9msdjpieA1V5aQkpuzjyD84MzB2XtF6YGS51UAv8TgE%2BHR3bvfDve8wcFVtbg56zkTlMl5NwplaRMKbSrckGOqUBbkoQfNR%2BcXarmOWZ1Jimg2O%2FR1odxouRh8lcsqK0sIX382tgQ0q3EAQPKJ0tYZn5OXmTgTX4AvH7sWb%2BbzvzGIjlsDDQ8JdYwO%2FuxAXshGzr2t3nCyDnvN7dm6pz6slEfqAtVMoluQSoqNAGiDerCXkq9qJr1rFm87OSAEgG6VWYOpLO%2FOKA9ktycStgfwjjhmu71VuMVZKlf5koWOdUuhQQBA0s&X-Amz-Signature=3a7cb11f28ed40cb2d7a032e9dda7f21a31a58d53ae04894de76af794331cabe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIKT2SF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIENq8Dv3ZPzO2hq2sQ4%2FNr3B4WmWSfPcXWsWUiXqozT3AiEA05iTO%2FL%2BEzsY4XdK08x%2BTX9bmChl7uLvGeSadSSEwcAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtlDc%2BFMF5V0rUNqCrcA0L2KxyPNaqmnn1gPk6RHYBLsLiw04Fk7rroNwHStnE422HAoaJ8UZUVYAPWzFBDsGQpgPNy2AhSFTQ7qv8cLVxHfuWE3eCpY4iLya4Su17mNJRFmjT2BzUe%2B0tfCGCDTiefl%2BLLvI6fTe1mNIhCsyKu9jgHkP7b2%2BahS9klWtJKqPwG3efITLrsuRLIuwbo64hYom%2FHSRAi%2F6100RfBLE4aj6tLZNsFSOZD4%2FuDXNbl1BqKVi0sKWjkv3m3FNZ8I55dDsYKdCUOzOyfYHB6QYXbXi9t5yzV2fMP7bL5FXvIQxyBRGygTvgcUajkZA9ToMif14fLFEajBCgXNgLC0X3GT56IVAGY%2BYovDf1KM1Dof4RqWRlDXv7rVtY3Zw%2FXv6AFd5gUkO10LN8DrFS74co8KDBZMCNu9HFMcqMPOvjroA5XzpdXPLJeTMaUnUi8KqTCsQPWFpHtashXexWeCmaBQwRT%2F1sH7kH499QxBIbSWnqpZcDrtOgoA%2BJYw0rhIxnDAlqJ%2FOT9MAD5iYvIPEweJYrTk0DT3aKWUTcErfdFqt3u9msdjpieA1V5aQkpuzjyD84MzB2XtF6YGS51UAv8TgE%2BHR3bvfDve8wcFVtbg56zkTlMl5NwplaRMKbSrckGOqUBbkoQfNR%2BcXarmOWZ1Jimg2O%2FR1odxouRh8lcsqK0sIX382tgQ0q3EAQPKJ0tYZn5OXmTgTX4AvH7sWb%2BbzvzGIjlsDDQ8JdYwO%2FuxAXshGzr2t3nCyDnvN7dm6pz6slEfqAtVMoluQSoqNAGiDerCXkq9qJr1rFm87OSAEgG6VWYOpLO%2FOKA9ktycStgfwjjhmu71VuMVZKlf5koWOdUuhQQBA0s&X-Amz-Signature=c059ffb5983cec78aebe5051e1b6b323d2de03e1348a6450f7b48d336376618c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXIKT2SF%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIENq8Dv3ZPzO2hq2sQ4%2FNr3B4WmWSfPcXWsWUiXqozT3AiEA05iTO%2FL%2BEzsY4XdK08x%2BTX9bmChl7uLvGeSadSSEwcAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtlDc%2BFMF5V0rUNqCrcA0L2KxyPNaqmnn1gPk6RHYBLsLiw04Fk7rroNwHStnE422HAoaJ8UZUVYAPWzFBDsGQpgPNy2AhSFTQ7qv8cLVxHfuWE3eCpY4iLya4Su17mNJRFmjT2BzUe%2B0tfCGCDTiefl%2BLLvI6fTe1mNIhCsyKu9jgHkP7b2%2BahS9klWtJKqPwG3efITLrsuRLIuwbo64hYom%2FHSRAi%2F6100RfBLE4aj6tLZNsFSOZD4%2FuDXNbl1BqKVi0sKWjkv3m3FNZ8I55dDsYKdCUOzOyfYHB6QYXbXi9t5yzV2fMP7bL5FXvIQxyBRGygTvgcUajkZA9ToMif14fLFEajBCgXNgLC0X3GT56IVAGY%2BYovDf1KM1Dof4RqWRlDXv7rVtY3Zw%2FXv6AFd5gUkO10LN8DrFS74co8KDBZMCNu9HFMcqMPOvjroA5XzpdXPLJeTMaUnUi8KqTCsQPWFpHtashXexWeCmaBQwRT%2F1sH7kH499QxBIbSWnqpZcDrtOgoA%2BJYw0rhIxnDAlqJ%2FOT9MAD5iYvIPEweJYrTk0DT3aKWUTcErfdFqt3u9msdjpieA1V5aQkpuzjyD84MzB2XtF6YGS51UAv8TgE%2BHR3bvfDve8wcFVtbg56zkTlMl5NwplaRMKbSrckGOqUBbkoQfNR%2BcXarmOWZ1Jimg2O%2FR1odxouRh8lcsqK0sIX382tgQ0q3EAQPKJ0tYZn5OXmTgTX4AvH7sWb%2BbzvzGIjlsDDQ8JdYwO%2FuxAXshGzr2t3nCyDnvN7dm6pz6slEfqAtVMoluQSoqNAGiDerCXkq9qJr1rFm87OSAEgG6VWYOpLO%2FOKA9ktycStgfwjjhmu71VuMVZKlf5koWOdUuhQQBA0s&X-Amz-Signature=22bb38cd7d5d79c685b3e8f64571b6256ed829ab4027ab7ee279610595716024&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

