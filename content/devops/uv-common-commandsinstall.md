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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WRJPJ7E%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW8G3UqUhIeFIa%2B6AGi2YyssvwrHOkz24cCf5rs01L8QIhAOn%2BfP8VccTG27nWQD2KiTuLxZIbvUD6HB5vkJG4KrYlKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqrZ%2BEnRGMxHkjOH8q3AN%2Bhu0hwdrfqL2eJ1zoSzwlSWiMj%2BbpTkZnn%2FP7SyV4KXbaajuB%2BQbHKAU3vIjT9cs%2BAO6Dks9gW6HNou4j03NaAbQbnqnKdDIvSG22xaezw%2F%2FLN5AnXs2UGf43PLoqpVUr66ErSJ15jtxTdDDZhW6ki0qzQkJIGTMciLChWtcH1lZo2f9cglAWOUn5%2Fp7Fg0j79Ejvs7hUZMh6pThENiIuGl3xW86ZWC5SIz%2BO1GPWDDp1BRptLytmlc4CR%2FLEv3pTGrCT5Q9uxmdIqC078O8Fv3I2hydI5JX1ADTj2tBzm1LLGLfupxLusjOYgCOnN7B8Z22Z8jkYlfuroBunYWRJ%2BwxgYbCnNZbFIMRofVUw0YSMOLFx%2Bw9y7GEA6ud%2FFCary9txHadToHnBLMyyWJammcKRkkUt8Pm07%2BJfy%2BDKtL7Xp85lto527Ubg%2Fz6h8YcwiS8cUt69r512o%2FXoDuhG9f7e2lNP6UTzzMDlIrrdWpB4%2BzLO4tNKOqttWSIKsSB4jzXiSFrIAyxyGwmyYdEMoMupTrLyuf9ujnu1nm9%2BCHj98pzxfxJysT%2FkFg%2FVajUAGWAgcYqObfg%2BvQtdJnfgEnEN1MGLlh5nSQqicAf1mJoTDoUHMDU%2BT0dacTClnMfKBjqkAeLWXxIN9EIo2hnD4CMAMGyMRvHddf%2BxesOv92QQvl8wDMkMgEZm4wo9SUkbN1pqov9DrRfM%2FH%2BynfvtjsQAEZ5Fg1tUHpeTHQeSh1DxXImqNxmpbpuQr5ioqdz4%2B2hFW%2B5LDU8%2FZzvzWsx%2FX36tvwfMX0hSej2Q%2FifGebLwRj9hB%2FJ7vEZ6KbJjZWLrM6M8cT08klWvSAAR5iohnomflZ08xbiW&X-Amz-Signature=9272ac583c13c715a21d640856dbf78873019f461d1221429ee4121afe46b94e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WRJPJ7E%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW8G3UqUhIeFIa%2B6AGi2YyssvwrHOkz24cCf5rs01L8QIhAOn%2BfP8VccTG27nWQD2KiTuLxZIbvUD6HB5vkJG4KrYlKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqrZ%2BEnRGMxHkjOH8q3AN%2Bhu0hwdrfqL2eJ1zoSzwlSWiMj%2BbpTkZnn%2FP7SyV4KXbaajuB%2BQbHKAU3vIjT9cs%2BAO6Dks9gW6HNou4j03NaAbQbnqnKdDIvSG22xaezw%2F%2FLN5AnXs2UGf43PLoqpVUr66ErSJ15jtxTdDDZhW6ki0qzQkJIGTMciLChWtcH1lZo2f9cglAWOUn5%2Fp7Fg0j79Ejvs7hUZMh6pThENiIuGl3xW86ZWC5SIz%2BO1GPWDDp1BRptLytmlc4CR%2FLEv3pTGrCT5Q9uxmdIqC078O8Fv3I2hydI5JX1ADTj2tBzm1LLGLfupxLusjOYgCOnN7B8Z22Z8jkYlfuroBunYWRJ%2BwxgYbCnNZbFIMRofVUw0YSMOLFx%2Bw9y7GEA6ud%2FFCary9txHadToHnBLMyyWJammcKRkkUt8Pm07%2BJfy%2BDKtL7Xp85lto527Ubg%2Fz6h8YcwiS8cUt69r512o%2FXoDuhG9f7e2lNP6UTzzMDlIrrdWpB4%2BzLO4tNKOqttWSIKsSB4jzXiSFrIAyxyGwmyYdEMoMupTrLyuf9ujnu1nm9%2BCHj98pzxfxJysT%2FkFg%2FVajUAGWAgcYqObfg%2BvQtdJnfgEnEN1MGLlh5nSQqicAf1mJoTDoUHMDU%2BT0dacTClnMfKBjqkAeLWXxIN9EIo2hnD4CMAMGyMRvHddf%2BxesOv92QQvl8wDMkMgEZm4wo9SUkbN1pqov9DrRfM%2FH%2BynfvtjsQAEZ5Fg1tUHpeTHQeSh1DxXImqNxmpbpuQr5ioqdz4%2B2hFW%2B5LDU8%2FZzvzWsx%2FX36tvwfMX0hSej2Q%2FifGebLwRj9hB%2FJ7vEZ6KbJjZWLrM6M8cT08klWvSAAR5iohnomflZ08xbiW&X-Amz-Signature=4640b1299710a7b4401223d065bdb182c0cfae83ea4296c5d833923b83394894&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WRJPJ7E%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW8G3UqUhIeFIa%2B6AGi2YyssvwrHOkz24cCf5rs01L8QIhAOn%2BfP8VccTG27nWQD2KiTuLxZIbvUD6HB5vkJG4KrYlKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwqrZ%2BEnRGMxHkjOH8q3AN%2Bhu0hwdrfqL2eJ1zoSzwlSWiMj%2BbpTkZnn%2FP7SyV4KXbaajuB%2BQbHKAU3vIjT9cs%2BAO6Dks9gW6HNou4j03NaAbQbnqnKdDIvSG22xaezw%2F%2FLN5AnXs2UGf43PLoqpVUr66ErSJ15jtxTdDDZhW6ki0qzQkJIGTMciLChWtcH1lZo2f9cglAWOUn5%2Fp7Fg0j79Ejvs7hUZMh6pThENiIuGl3xW86ZWC5SIz%2BO1GPWDDp1BRptLytmlc4CR%2FLEv3pTGrCT5Q9uxmdIqC078O8Fv3I2hydI5JX1ADTj2tBzm1LLGLfupxLusjOYgCOnN7B8Z22Z8jkYlfuroBunYWRJ%2BwxgYbCnNZbFIMRofVUw0YSMOLFx%2Bw9y7GEA6ud%2FFCary9txHadToHnBLMyyWJammcKRkkUt8Pm07%2BJfy%2BDKtL7Xp85lto527Ubg%2Fz6h8YcwiS8cUt69r512o%2FXoDuhG9f7e2lNP6UTzzMDlIrrdWpB4%2BzLO4tNKOqttWSIKsSB4jzXiSFrIAyxyGwmyYdEMoMupTrLyuf9ujnu1nm9%2BCHj98pzxfxJysT%2FkFg%2FVajUAGWAgcYqObfg%2BvQtdJnfgEnEN1MGLlh5nSQqicAf1mJoTDoUHMDU%2BT0dacTClnMfKBjqkAeLWXxIN9EIo2hnD4CMAMGyMRvHddf%2BxesOv92QQvl8wDMkMgEZm4wo9SUkbN1pqov9DrRfM%2FH%2BynfvtjsQAEZ5Fg1tUHpeTHQeSh1DxXImqNxmpbpuQr5ioqdz4%2B2hFW%2B5LDU8%2FZzvzWsx%2FX36tvwfMX0hSej2Q%2FifGebLwRj9hB%2FJ7vEZ6KbJjZWLrM6M8cT08klWvSAAR5iohnomflZ08xbiW&X-Amz-Signature=261325bfe37140824272a9497be524eff9d4c57cf83db6e71f941c2074cb9e4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

