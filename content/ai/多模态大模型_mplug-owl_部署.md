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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZPSW7XK%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDqW0f2%2F04P6%2Bmd8Uwa8THgj%2FQxQ3KBITzubrNr43KGZQIhAM4L8J%2BIN%2Bcgs5bBjgk30fPesrDlHoPXTxM5n1b5ir1JKv8DCAkQABoMNjM3NDIzMTgzODA1Igz1YjUXc%2FPHHYswCjoq3APKic7Jx7VRs5%2BkCzKr6f6xHIoojEIoTMCaW0n9%2FGCikvT33IqDqsSq2oED3GfDhAV9RBC3aZCOqjIMwiJcGdiaTmVrIEzJu3DxDuZXu14zBKsyecWaKTjLd0vH6PnGTGUrjpU76yXJLKk8vMUx73jjfGQcb5RJAalLDFqzRQIysV%2F15B4YU9XzEAKIXU4USvipyqA3RfxWhqhRrhOYKEp9cemlJqSNBo74LVcisa5CTbV4Z0fo7iWjXobGfYmUi%2BKcXvnBgy6VCxtIP3pr7IbnYfzWZS%2Bd%2FP6LFfb4XKcqM99ofqxGn22O3p%2ForTznNR8lnuAVYj3%2Br7TrJ8yPfH02%2Flwt60WguLokgqwUYODf6yyxyxMpZA564mRrnX2Co8rnaGpW6BaLeGJuVnVKoEPZoT25ueeFr8dTKW9n4tlqX5fwycMs8U1yIcbB7wYXayBr91O1fv6gCtBLw4UcwhQZWV5JkqwGHyzoX7VSmzDN432ao6m9Z4HclEnsOBSPkEwRWRZbUZKEI69cbxErOw7Z5Dpvpab8%2BUsLvKZoh4iwTYGW4LrQqx4voseCOQ2AcI2R3%2FwrgE8fkYbxeA2hbBvsm%2F2YnQXcRWPS9G9pFDJdDWbTfe5JBF7SMzt%2BSDD03bjJBjqkAVTdq2BgTxrwSpqDEhNiSJL2fFSGmIKPtVUCYZOTpnki7My0LVSHcS9iD2z3K18MrS00HKXWgPg8gKrAEiAM4AXtoVaOEbaR4ROQZX14Z%2BlabET8GObtlYefD9z3M%2FqNFb9btrGdXZH22heECRnogfxXuBtT6p5Op%2FFM%2FXroDbminaWajcGtFostQQAZmD7vh9lf9AsMhVGl0Xyix%2FAyyZFXU7Wb&X-Amz-Signature=05671b212d895c6fcfbcec4ac60bc03a4fdf8d558fb696974a46a1c433baca99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZPSW7XK%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDqW0f2%2F04P6%2Bmd8Uwa8THgj%2FQxQ3KBITzubrNr43KGZQIhAM4L8J%2BIN%2Bcgs5bBjgk30fPesrDlHoPXTxM5n1b5ir1JKv8DCAkQABoMNjM3NDIzMTgzODA1Igz1YjUXc%2FPHHYswCjoq3APKic7Jx7VRs5%2BkCzKr6f6xHIoojEIoTMCaW0n9%2FGCikvT33IqDqsSq2oED3GfDhAV9RBC3aZCOqjIMwiJcGdiaTmVrIEzJu3DxDuZXu14zBKsyecWaKTjLd0vH6PnGTGUrjpU76yXJLKk8vMUx73jjfGQcb5RJAalLDFqzRQIysV%2F15B4YU9XzEAKIXU4USvipyqA3RfxWhqhRrhOYKEp9cemlJqSNBo74LVcisa5CTbV4Z0fo7iWjXobGfYmUi%2BKcXvnBgy6VCxtIP3pr7IbnYfzWZS%2Bd%2FP6LFfb4XKcqM99ofqxGn22O3p%2ForTznNR8lnuAVYj3%2Br7TrJ8yPfH02%2Flwt60WguLokgqwUYODf6yyxyxMpZA564mRrnX2Co8rnaGpW6BaLeGJuVnVKoEPZoT25ueeFr8dTKW9n4tlqX5fwycMs8U1yIcbB7wYXayBr91O1fv6gCtBLw4UcwhQZWV5JkqwGHyzoX7VSmzDN432ao6m9Z4HclEnsOBSPkEwRWRZbUZKEI69cbxErOw7Z5Dpvpab8%2BUsLvKZoh4iwTYGW4LrQqx4voseCOQ2AcI2R3%2FwrgE8fkYbxeA2hbBvsm%2F2YnQXcRWPS9G9pFDJdDWbTfe5JBF7SMzt%2BSDD03bjJBjqkAVTdq2BgTxrwSpqDEhNiSJL2fFSGmIKPtVUCYZOTpnki7My0LVSHcS9iD2z3K18MrS00HKXWgPg8gKrAEiAM4AXtoVaOEbaR4ROQZX14Z%2BlabET8GObtlYefD9z3M%2FqNFb9btrGdXZH22heECRnogfxXuBtT6p5Op%2FFM%2FXroDbminaWajcGtFostQQAZmD7vh9lf9AsMhVGl0Xyix%2FAyyZFXU7Wb&X-Amz-Signature=f8d0fc75ce585bfd0303e66ef7d951a3d88abf3d4c0d1f05dafa1d41d6f7ca3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

