---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFD5FY7M%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHENbuRCZ4QDTUTi%2F7F%2FqwV07guQzgjJRHQtj92XoXSEAiBXggIl2ErUw7IM9rfCvtxBioaUR0I6x%2F3hlJ94ALYJWCqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiZPJe6XAeh0VfIPZKtwDflzUUpael44J%2B9RJ8gAmKjJ%2BFM83W%2FxKeug4VsY2YcR04VWKoRoofLbhKhcvoIL%2FQZQcSSREUw3pL9JRlg4%2Fe4qdkErWczGwFAdioP4%2FRxNeSkHcao989Q9mPphIQUfrgAz23BekCXApLEGRC%2ByyPXXb9rtK3zguS6jwkS6NLNcqt4v%2FNdMoIoF%2BJ3VYYx1uL3bRHzX1PkKXl9uNAR1SFAUX5F4sXnI0Bm9O7NYnf6LB7nSTHm6e3uzIiux0mch3WoEk%2FKCte7OBvZsX4ihJs%2FWtTI91QCNun%2B5EXY6o%2FhgJuQMPcJTNjiu1ItsoWkcWvG2F6Lb5NzJVRpOD4lnMUCpKRMFk%2F%2Fl1F%2Bf%2BkOrGdZ5OvXninstdtv9WmqbilkYzRGatncFNx%2BN8RhEfaeb6Eq5X7YVOi%2FnTQIwQ%2F3X%2BRVAMAqjKZ7pMvS7KJQjVOmuQKM4YC0vckLEyPQau%2BgzG37FItqX%2FKuiltY%2Fk7d8tK%2BWyrEEVL4rZTONV171NFM%2Fi9SmP3nS4sp3pVfnfT7YTUpzmqljad9Z5zPic0bEnVBpQgiPS8XauupIz6gv%2Fm%2FP2EoXrnEnOOdzWdWnMD%2BunQIbQbdEvJ6jHkViRDQTQGCL%2FEt9KsfDfnk%2BXEVkwgLnNzQY6pgFyve6Qa6rbVjCrWEUlI%2Fob%2BlsXXurn7TaFTN2xrz%2FKMN3Q95ZLLiUQmqggAh1KJeFlYmjgbelcQVRKecOlefEZhaTJpK3pNn9ioAJTtuUt14EyC%2BL3Z%2FPybc5EWw%2FpwldOXQwupCzumk%2BUIa58LZCxpqJ6VnROALDNSCY86ht9cCARHfyHjuaFV1d862sfrXd5fbeBr25Tt1ySnb55RCLxKjF7pgWA&X-Amz-Signature=a83db98a06f4b42a4d2248b6a0f14c67905db3108f4ecd36be7e61eef32afd44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFD5FY7M%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHENbuRCZ4QDTUTi%2F7F%2FqwV07guQzgjJRHQtj92XoXSEAiBXggIl2ErUw7IM9rfCvtxBioaUR0I6x%2F3hlJ94ALYJWCqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiZPJe6XAeh0VfIPZKtwDflzUUpael44J%2B9RJ8gAmKjJ%2BFM83W%2FxKeug4VsY2YcR04VWKoRoofLbhKhcvoIL%2FQZQcSSREUw3pL9JRlg4%2Fe4qdkErWczGwFAdioP4%2FRxNeSkHcao989Q9mPphIQUfrgAz23BekCXApLEGRC%2ByyPXXb9rtK3zguS6jwkS6NLNcqt4v%2FNdMoIoF%2BJ3VYYx1uL3bRHzX1PkKXl9uNAR1SFAUX5F4sXnI0Bm9O7NYnf6LB7nSTHm6e3uzIiux0mch3WoEk%2FKCte7OBvZsX4ihJs%2FWtTI91QCNun%2B5EXY6o%2FhgJuQMPcJTNjiu1ItsoWkcWvG2F6Lb5NzJVRpOD4lnMUCpKRMFk%2F%2Fl1F%2Bf%2BkOrGdZ5OvXninstdtv9WmqbilkYzRGatncFNx%2BN8RhEfaeb6Eq5X7YVOi%2FnTQIwQ%2F3X%2BRVAMAqjKZ7pMvS7KJQjVOmuQKM4YC0vckLEyPQau%2BgzG37FItqX%2FKuiltY%2Fk7d8tK%2BWyrEEVL4rZTONV171NFM%2Fi9SmP3nS4sp3pVfnfT7YTUpzmqljad9Z5zPic0bEnVBpQgiPS8XauupIz6gv%2Fm%2FP2EoXrnEnOOdzWdWnMD%2BunQIbQbdEvJ6jHkViRDQTQGCL%2FEt9KsfDfnk%2BXEVkwgLnNzQY6pgFyve6Qa6rbVjCrWEUlI%2Fob%2BlsXXurn7TaFTN2xrz%2FKMN3Q95ZLLiUQmqggAh1KJeFlYmjgbelcQVRKecOlefEZhaTJpK3pNn9ioAJTtuUt14EyC%2BL3Z%2FPybc5EWw%2FpwldOXQwupCzumk%2BUIa58LZCxpqJ6VnROALDNSCY86ht9cCARHfyHjuaFV1d862sfrXd5fbeBr25Tt1ySnb55RCLxKjF7pgWA&X-Amz-Signature=5f139ba083d5eb36d0e98b035f1ea4defa8eafca2f731a1856332f07649ed563&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFD5FY7M%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHENbuRCZ4QDTUTi%2F7F%2FqwV07guQzgjJRHQtj92XoXSEAiBXggIl2ErUw7IM9rfCvtxBioaUR0I6x%2F3hlJ94ALYJWCqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiZPJe6XAeh0VfIPZKtwDflzUUpael44J%2B9RJ8gAmKjJ%2BFM83W%2FxKeug4VsY2YcR04VWKoRoofLbhKhcvoIL%2FQZQcSSREUw3pL9JRlg4%2Fe4qdkErWczGwFAdioP4%2FRxNeSkHcao989Q9mPphIQUfrgAz23BekCXApLEGRC%2ByyPXXb9rtK3zguS6jwkS6NLNcqt4v%2FNdMoIoF%2BJ3VYYx1uL3bRHzX1PkKXl9uNAR1SFAUX5F4sXnI0Bm9O7NYnf6LB7nSTHm6e3uzIiux0mch3WoEk%2FKCte7OBvZsX4ihJs%2FWtTI91QCNun%2B5EXY6o%2FhgJuQMPcJTNjiu1ItsoWkcWvG2F6Lb5NzJVRpOD4lnMUCpKRMFk%2F%2Fl1F%2Bf%2BkOrGdZ5OvXninstdtv9WmqbilkYzRGatncFNx%2BN8RhEfaeb6Eq5X7YVOi%2FnTQIwQ%2F3X%2BRVAMAqjKZ7pMvS7KJQjVOmuQKM4YC0vckLEyPQau%2BgzG37FItqX%2FKuiltY%2Fk7d8tK%2BWyrEEVL4rZTONV171NFM%2Fi9SmP3nS4sp3pVfnfT7YTUpzmqljad9Z5zPic0bEnVBpQgiPS8XauupIz6gv%2Fm%2FP2EoXrnEnOOdzWdWnMD%2BunQIbQbdEvJ6jHkViRDQTQGCL%2FEt9KsfDfnk%2BXEVkwgLnNzQY6pgFyve6Qa6rbVjCrWEUlI%2Fob%2BlsXXurn7TaFTN2xrz%2FKMN3Q95ZLLiUQmqggAh1KJeFlYmjgbelcQVRKecOlefEZhaTJpK3pNn9ioAJTtuUt14EyC%2BL3Z%2FPybc5EWw%2FpwldOXQwupCzumk%2BUIa58LZCxpqJ6VnROALDNSCY86ht9cCARHfyHjuaFV1d862sfrXd5fbeBr25Tt1ySnb55RCLxKjF7pgWA&X-Amz-Signature=847b224af74c6b2e3fdee6df168b7d62db357557efc2d3c225d93169f8eb87af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

