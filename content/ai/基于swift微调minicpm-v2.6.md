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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCCZQ2MA%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC82cy7ZAdv8DrciPM20L7gXhSrS%2Fqtpld5773kV8U2AwIhAOEMElmMWRYslwvdJCGntGKABeKAWThjkLm3n1uGfmGkKv8DCFsQABoMNjM3NDIzMTgzODA1IgyKeuk71wh9L8x4%2FdUq3AM%2FkPBcT7B6koDRlZm%2Fjf%2FGXfbOxKdEvx50qLc9TTLvwrPBtIJukWmuPtAp1i7pXMLHh5wiOC7Qm7vpYDjPw55nQmNRtXSS5lwskkKTZNmPWxpnUeotIeWeo4XsMSBlwJ9TEOSjeS0izlT6xgisAjLGvFlZIRGhH%2B%2F27EyeRanoWPyk0tGSu4gapfK5o5ZP%2B2yTkewmZip0IXyyf%2FBhpAum2W7pHQ08Cmw3E6%2F%2FEUwVhhEcZrKpsKp3U1WhNS0MWzACuOSE0yZ7v4JzZwM3Q1llWrm049pAm0b5vD4vOiBhUosHS5N%2Bj6Z5bnGK4I9eH48G4lCjzXFpi7DH%2BBNUCcN%2BA0%2FYaJHlxBUGiBJp7f2lqRrbzV9m5nnwmoFQPfM9W9sHO6%2FH%2BIyu4ziLLVxy2wcW7Sef8w0S8pzKSUp%2F54GZZ98AC7m%2FqUo42WDo82%2FPcX6NoGFxekocm5H0zIlXolQdUZ7EK6L0LnSY3TIHI4LW1lKXZ6g0R01dWJesfQrwtArm%2Fcytc%2BdNVuJGVu4nWv7%2BSMD9cDDCC6gsNOqU7x%2Fpa9knZxDkMgcG7ccZ%2BA5zgC%2FgJ7dt1yMysWdIDCot8HWrG4zXuOkDlnPWfrcX7bWy%2F9M9gDELgHpOhVA0QTCd0qvLBjqkAb5u0ZvC9Q48gB68uuWc98g5%2BT%2FWBdefkvD8zCJYp%2FE4xXzsrs2gZI72AJjAS%2BIOmudwGfLShvZTFnMSOfNnNh74DAgO5p5hz6U71GOCW1fHaz%2FlHRRyQmVdprAba6o4CY%2FoJxBoTiTh6TFDllwquv7iDRJT5YFgDiFbtxGREbCATFFIma6I1kTYAOehurkUhw%2FVRYEUl5b4%2BGVyavCQW8umzZwo&X-Amz-Signature=cf5094a9c1baa49675a0a3d6e0505185e5b63cbe5e38dcd9cc386adf2c9072e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCCZQ2MA%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC82cy7ZAdv8DrciPM20L7gXhSrS%2Fqtpld5773kV8U2AwIhAOEMElmMWRYslwvdJCGntGKABeKAWThjkLm3n1uGfmGkKv8DCFsQABoMNjM3NDIzMTgzODA1IgyKeuk71wh9L8x4%2FdUq3AM%2FkPBcT7B6koDRlZm%2Fjf%2FGXfbOxKdEvx50qLc9TTLvwrPBtIJukWmuPtAp1i7pXMLHh5wiOC7Qm7vpYDjPw55nQmNRtXSS5lwskkKTZNmPWxpnUeotIeWeo4XsMSBlwJ9TEOSjeS0izlT6xgisAjLGvFlZIRGhH%2B%2F27EyeRanoWPyk0tGSu4gapfK5o5ZP%2B2yTkewmZip0IXyyf%2FBhpAum2W7pHQ08Cmw3E6%2F%2FEUwVhhEcZrKpsKp3U1WhNS0MWzACuOSE0yZ7v4JzZwM3Q1llWrm049pAm0b5vD4vOiBhUosHS5N%2Bj6Z5bnGK4I9eH48G4lCjzXFpi7DH%2BBNUCcN%2BA0%2FYaJHlxBUGiBJp7f2lqRrbzV9m5nnwmoFQPfM9W9sHO6%2FH%2BIyu4ziLLVxy2wcW7Sef8w0S8pzKSUp%2F54GZZ98AC7m%2FqUo42WDo82%2FPcX6NoGFxekocm5H0zIlXolQdUZ7EK6L0LnSY3TIHI4LW1lKXZ6g0R01dWJesfQrwtArm%2Fcytc%2BdNVuJGVu4nWv7%2BSMD9cDDCC6gsNOqU7x%2Fpa9knZxDkMgcG7ccZ%2BA5zgC%2FgJ7dt1yMysWdIDCot8HWrG4zXuOkDlnPWfrcX7bWy%2F9M9gDELgHpOhVA0QTCd0qvLBjqkAb5u0ZvC9Q48gB68uuWc98g5%2BT%2FWBdefkvD8zCJYp%2FE4xXzsrs2gZI72AJjAS%2BIOmudwGfLShvZTFnMSOfNnNh74DAgO5p5hz6U71GOCW1fHaz%2FlHRRyQmVdprAba6o4CY%2FoJxBoTiTh6TFDllwquv7iDRJT5YFgDiFbtxGREbCATFFIma6I1kTYAOehurkUhw%2FVRYEUl5b4%2BGVyavCQW8umzZwo&X-Amz-Signature=2792ebb556c5aae310bf3d64c1ddccc165b3931e470fd7f2339229885836ff89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCCZQ2MA%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC82cy7ZAdv8DrciPM20L7gXhSrS%2Fqtpld5773kV8U2AwIhAOEMElmMWRYslwvdJCGntGKABeKAWThjkLm3n1uGfmGkKv8DCFsQABoMNjM3NDIzMTgzODA1IgyKeuk71wh9L8x4%2FdUq3AM%2FkPBcT7B6koDRlZm%2Fjf%2FGXfbOxKdEvx50qLc9TTLvwrPBtIJukWmuPtAp1i7pXMLHh5wiOC7Qm7vpYDjPw55nQmNRtXSS5lwskkKTZNmPWxpnUeotIeWeo4XsMSBlwJ9TEOSjeS0izlT6xgisAjLGvFlZIRGhH%2B%2F27EyeRanoWPyk0tGSu4gapfK5o5ZP%2B2yTkewmZip0IXyyf%2FBhpAum2W7pHQ08Cmw3E6%2F%2FEUwVhhEcZrKpsKp3U1WhNS0MWzACuOSE0yZ7v4JzZwM3Q1llWrm049pAm0b5vD4vOiBhUosHS5N%2Bj6Z5bnGK4I9eH48G4lCjzXFpi7DH%2BBNUCcN%2BA0%2FYaJHlxBUGiBJp7f2lqRrbzV9m5nnwmoFQPfM9W9sHO6%2FH%2BIyu4ziLLVxy2wcW7Sef8w0S8pzKSUp%2F54GZZ98AC7m%2FqUo42WDo82%2FPcX6NoGFxekocm5H0zIlXolQdUZ7EK6L0LnSY3TIHI4LW1lKXZ6g0R01dWJesfQrwtArm%2Fcytc%2BdNVuJGVu4nWv7%2BSMD9cDDCC6gsNOqU7x%2Fpa9knZxDkMgcG7ccZ%2BA5zgC%2FgJ7dt1yMysWdIDCot8HWrG4zXuOkDlnPWfrcX7bWy%2F9M9gDELgHpOhVA0QTCd0qvLBjqkAb5u0ZvC9Q48gB68uuWc98g5%2BT%2FWBdefkvD8zCJYp%2FE4xXzsrs2gZI72AJjAS%2BIOmudwGfLShvZTFnMSOfNnNh74DAgO5p5hz6U71GOCW1fHaz%2FlHRRyQmVdprAba6o4CY%2FoJxBoTiTh6TFDllwquv7iDRJT5YFgDiFbtxGREbCATFFIma6I1kTYAOehurkUhw%2FVRYEUl5b4%2BGVyavCQW8umzZwo&X-Amz-Signature=4f41cedf67c248615e9dae3d00780dacf220c81f186fda8a170760c4a27c050a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

