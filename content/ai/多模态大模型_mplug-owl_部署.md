---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AQKLVXB%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHHz6r5E4q3fI4bTmAzRzPT3gTGeekZ5fc33MPyovOqFAiEAjH9qgN9DbQKsWtFu1uGKojiNHFZcyh7Yx7CJKqjeTKUqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKlgvAaV%2BuifYSFpyrcAyf0xdtKp4IAIV2IK31e1M%2FvYKs02W8nP6tXOg23y9v5cc%2FltgtiETQa4nEUFt8eruGMPPU5%2Bk4Ehmmo9xABQ%2BOyl0Aw6ifIX8PPKz%2BXem%2FspxKIQL%2FC3zGXzFbj%2BJmrLcyRcVbQZYup7ihrwkiLSVGBd5CtQ1RMaO%2Fwd4CjT5trItoJweM0O0rAYq3I8ia7LB7FTmkF0w5gZ%2B7mVzmHvq%2Bcg4mAkx1p52rT1ry%2FH5m5Ac%2BdSyTELeursWjjT3sd3xsvGQTe%2BKMxYtq1WSar15mMtBtGJmMLNWTdTpI7qe%2FoRNIAeQOjaEtrixSNpj45jcQ8phSr%2B5gbDl0yVOTaM1TUpFTgv6L57n53CG5H1IiEHPWLuPG3OLUI45wv3xlJx42fynj0gv90GACNdVvQ%2BeJP%2BMw%2F2OouxRuwZsiXYwB95LkwlclVAfj6BS6iRUXweJXCQpvtIz67aQsdMdDiBgAlb%2Fbau2m8I7W7daR5piUQ%2BmP5%2FwK1ER20Vec%2FDKoOeJMoS3rldW5cHPuFSZ8sDTeANFpgu%2BR9sy8QebZtNluCIfjaLlMisAvDHt313ashcl245v1Ket3J0iRR6D2UWVZ8Nz%2BSGnxckP4yqExJHy%2F0l48Il6PDWeamqsqBMKHV7ckGOqUB03OI181lWqqWEeDc9ExdAfsvJKT6gO4ni35SmmyIwfMn8b6R55DpEdrO7e40r1MZ9H%2BXtVOJLxB4SVmVYbmrs90r5yMuc%2FQjPi3%2BlgwCX4wgeJB76G3KT6vse04nA8bEfPglpqdUWvZJexs%2FvPQGKaXqLshR%2B3a02oJxvvA7E3ZEIt9YEWUiNq%2FQwbP64UZkJxxTVezOWsrQ0Qe7IiexKcFAOWyE&X-Amz-Signature=e6486d32d7a85be005773329d4d32060888dc558e1ef039b3d3db270e18a2bff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AQKLVXB%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIHHz6r5E4q3fI4bTmAzRzPT3gTGeekZ5fc33MPyovOqFAiEAjH9qgN9DbQKsWtFu1uGKojiNHFZcyh7Yx7CJKqjeTKUqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNKlgvAaV%2BuifYSFpyrcAyf0xdtKp4IAIV2IK31e1M%2FvYKs02W8nP6tXOg23y9v5cc%2FltgtiETQa4nEUFt8eruGMPPU5%2Bk4Ehmmo9xABQ%2BOyl0Aw6ifIX8PPKz%2BXem%2FspxKIQL%2FC3zGXzFbj%2BJmrLcyRcVbQZYup7ihrwkiLSVGBd5CtQ1RMaO%2Fwd4CjT5trItoJweM0O0rAYq3I8ia7LB7FTmkF0w5gZ%2B7mVzmHvq%2Bcg4mAkx1p52rT1ry%2FH5m5Ac%2BdSyTELeursWjjT3sd3xsvGQTe%2BKMxYtq1WSar15mMtBtGJmMLNWTdTpI7qe%2FoRNIAeQOjaEtrixSNpj45jcQ8phSr%2B5gbDl0yVOTaM1TUpFTgv6L57n53CG5H1IiEHPWLuPG3OLUI45wv3xlJx42fynj0gv90GACNdVvQ%2BeJP%2BMw%2F2OouxRuwZsiXYwB95LkwlclVAfj6BS6iRUXweJXCQpvtIz67aQsdMdDiBgAlb%2Fbau2m8I7W7daR5piUQ%2BmP5%2FwK1ER20Vec%2FDKoOeJMoS3rldW5cHPuFSZ8sDTeANFpgu%2BR9sy8QebZtNluCIfjaLlMisAvDHt313ashcl245v1Ket3J0iRR6D2UWVZ8Nz%2BSGnxckP4yqExJHy%2F0l48Il6PDWeamqsqBMKHV7ckGOqUB03OI181lWqqWEeDc9ExdAfsvJKT6gO4ni35SmmyIwfMn8b6R55DpEdrO7e40r1MZ9H%2BXtVOJLxB4SVmVYbmrs90r5yMuc%2FQjPi3%2BlgwCX4wgeJB76G3KT6vse04nA8bEfPglpqdUWvZJexs%2FvPQGKaXqLshR%2B3a02oJxvvA7E3ZEIt9YEWUiNq%2FQwbP64UZkJxxTVezOWsrQ0Qe7IiexKcFAOWyE&X-Amz-Signature=7a6f38359e8a1ae6cc925f8ff95d5118b24f2cd691be0cfeccdf0b7bc287bb55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

