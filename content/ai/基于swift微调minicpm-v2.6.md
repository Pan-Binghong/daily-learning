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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6IZVU7W%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8SY2P1pG%2BdwLTXOQwJ9qtFgreorLU0%2FtKil2JTb3ZXQIhAO9Yr54b4XiXPqCZOosjjFmEH0k93xtrUeFaOIa81HpEKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxljDnDybZ6QfX%2FpCUq3ANYZb6i4Gsbt2eIVe82OCdH0nySq%2FQdHeBcFB4wTEOOIxTT4HoqbJp%2B3vU1N4wpOwC2bTmGYPDkWddksHuq3A%2BJac2oNM2hcqXFX51XHYssIJ0SJnhK8UANMCMyOiVPjc8KgKLsS8LPSgQdfVDnRksiaCe8xG8qEaT40W2WDITWkJdS8N5I6gJL4bs9%2BneMZVH7bHmO4um%2FirIvKMbk1Qeqrb19CBa2mML8%2BQmSBMlTuBQ6f%2B0kdIBhWYTGQwzMf%2F%2B%2F%2Bd5XVvXCyHFzvLiaY4KqcJ8xpfZrpe2UAdmAgW4PG6jPbyQDvMd9t298kWVWk9PL6V%2F9MGQMaOj5Ha8sZTdXkSlGDctF%2FMaPaMFXpZK3PDAuc%2BbKW3AJesmIivKITxLvJ5qS6%2FKgOsQPT30lxSTbobJF081ewXDZ1fPgGFgGBX8C%2FixYU7FoTFh89nix3lmhEBRRecVbijwTaovtHHuMxTWk1QP9NTO5GKWjiXPwR%2B4ZlSyPXvSVQ0V5YR%2BtYTiVfT%2BEq2FmBuvaxMmvgXrTgKbcHekaVRWZxsqb7a%2FzrB5fbDqcvMTlAFiuRkaaGyoqDwGFIAu%2B2g3oh0DeH6Nx3sY0d3cqm9IsZpScNFZS2%2Bj931NgEUVrcJBW9DD1sMzOBjqkAXrASihI2vbGxdOH2Wf5k6atX%2BJe22ZH8cjEd%2FOIm408BedWHksSM0mUGktSeveMuFMDd%2BNqcbLEACa6%2FwlRIzajohPFRli8hdLsx3dN%2BVC76yTR8uQA8BiZ856EArW0OWhOak8X%2Bx%2FIdZILvHux1aEbC8yscFqpcLrWljoVk2KSImk9pnK1q3cuBdNlAnp%2Flnn0c25MxyrJO2pooX2IlV4EJI80&X-Amz-Signature=1cfd08a5dbe582bcdceb2b6ba0a8397c6cad3bc573745635f143ddc9f589be0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6IZVU7W%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8SY2P1pG%2BdwLTXOQwJ9qtFgreorLU0%2FtKil2JTb3ZXQIhAO9Yr54b4XiXPqCZOosjjFmEH0k93xtrUeFaOIa81HpEKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxljDnDybZ6QfX%2FpCUq3ANYZb6i4Gsbt2eIVe82OCdH0nySq%2FQdHeBcFB4wTEOOIxTT4HoqbJp%2B3vU1N4wpOwC2bTmGYPDkWddksHuq3A%2BJac2oNM2hcqXFX51XHYssIJ0SJnhK8UANMCMyOiVPjc8KgKLsS8LPSgQdfVDnRksiaCe8xG8qEaT40W2WDITWkJdS8N5I6gJL4bs9%2BneMZVH7bHmO4um%2FirIvKMbk1Qeqrb19CBa2mML8%2BQmSBMlTuBQ6f%2B0kdIBhWYTGQwzMf%2F%2B%2F%2Bd5XVvXCyHFzvLiaY4KqcJ8xpfZrpe2UAdmAgW4PG6jPbyQDvMd9t298kWVWk9PL6V%2F9MGQMaOj5Ha8sZTdXkSlGDctF%2FMaPaMFXpZK3PDAuc%2BbKW3AJesmIivKITxLvJ5qS6%2FKgOsQPT30lxSTbobJF081ewXDZ1fPgGFgGBX8C%2FixYU7FoTFh89nix3lmhEBRRecVbijwTaovtHHuMxTWk1QP9NTO5GKWjiXPwR%2B4ZlSyPXvSVQ0V5YR%2BtYTiVfT%2BEq2FmBuvaxMmvgXrTgKbcHekaVRWZxsqb7a%2FzrB5fbDqcvMTlAFiuRkaaGyoqDwGFIAu%2B2g3oh0DeH6Nx3sY0d3cqm9IsZpScNFZS2%2Bj931NgEUVrcJBW9DD1sMzOBjqkAXrASihI2vbGxdOH2Wf5k6atX%2BJe22ZH8cjEd%2FOIm408BedWHksSM0mUGktSeveMuFMDd%2BNqcbLEACa6%2FwlRIzajohPFRli8hdLsx3dN%2BVC76yTR8uQA8BiZ856EArW0OWhOak8X%2Bx%2FIdZILvHux1aEbC8yscFqpcLrWljoVk2KSImk9pnK1q3cuBdNlAnp%2Flnn0c25MxyrJO2pooX2IlV4EJI80&X-Amz-Signature=b0e3091a87b1c35a2227fb8701392130ab3299575bdbfbe52f9a2878ed1d6162&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6IZVU7W%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8SY2P1pG%2BdwLTXOQwJ9qtFgreorLU0%2FtKil2JTb3ZXQIhAO9Yr54b4XiXPqCZOosjjFmEH0k93xtrUeFaOIa81HpEKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxljDnDybZ6QfX%2FpCUq3ANYZb6i4Gsbt2eIVe82OCdH0nySq%2FQdHeBcFB4wTEOOIxTT4HoqbJp%2B3vU1N4wpOwC2bTmGYPDkWddksHuq3A%2BJac2oNM2hcqXFX51XHYssIJ0SJnhK8UANMCMyOiVPjc8KgKLsS8LPSgQdfVDnRksiaCe8xG8qEaT40W2WDITWkJdS8N5I6gJL4bs9%2BneMZVH7bHmO4um%2FirIvKMbk1Qeqrb19CBa2mML8%2BQmSBMlTuBQ6f%2B0kdIBhWYTGQwzMf%2F%2B%2F%2Bd5XVvXCyHFzvLiaY4KqcJ8xpfZrpe2UAdmAgW4PG6jPbyQDvMd9t298kWVWk9PL6V%2F9MGQMaOj5Ha8sZTdXkSlGDctF%2FMaPaMFXpZK3PDAuc%2BbKW3AJesmIivKITxLvJ5qS6%2FKgOsQPT30lxSTbobJF081ewXDZ1fPgGFgGBX8C%2FixYU7FoTFh89nix3lmhEBRRecVbijwTaovtHHuMxTWk1QP9NTO5GKWjiXPwR%2B4ZlSyPXvSVQ0V5YR%2BtYTiVfT%2BEq2FmBuvaxMmvgXrTgKbcHekaVRWZxsqb7a%2FzrB5fbDqcvMTlAFiuRkaaGyoqDwGFIAu%2B2g3oh0DeH6Nx3sY0d3cqm9IsZpScNFZS2%2Bj931NgEUVrcJBW9DD1sMzOBjqkAXrASihI2vbGxdOH2Wf5k6atX%2BJe22ZH8cjEd%2FOIm408BedWHksSM0mUGktSeveMuFMDd%2BNqcbLEACa6%2FwlRIzajohPFRli8hdLsx3dN%2BVC76yTR8uQA8BiZ856EArW0OWhOak8X%2Bx%2FIdZILvHux1aEbC8yscFqpcLrWljoVk2KSImk9pnK1q3cuBdNlAnp%2Flnn0c25MxyrJO2pooX2IlV4EJI80&X-Amz-Signature=5f536a7d645bcc48fd8e0551055efbb77d1389788ea66bfe2842bbb6090f2bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

