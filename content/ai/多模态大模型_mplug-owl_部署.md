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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674VT2RSD%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCnJ0IbFzspwRcef%2BGQHE5O%2Bz4DicKu1e7MC87yWOz9sAIhAJzXqv2a3nYYDZEU7Pfnt1rvIgYwQKmUnzlCm5nQVyrDKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJOR3TCsi96Okn7Eoq3APJ3Bg0YLtj5qihYchnEXRTbA%2BLyPhMRNyS8QU3l7Hely9euXg2YmP%2BdsYVwIuy%2FAiIVkG5tOLIzJBnM7sX0e4SKvXympbaSQRoqjxWmAmGu9ZRWf89O0j2HrK%2F09n5FP6XUDaRwlCzPt5zPD1IioUfbR%2BPMsXopOosj02WKKTYnlpckQylvcjV7iGyNh%2Bjk6gT%2F63H9PG%2F7ordIaJiTLWOI6zGH02609AHa4GKCdK%2FRFqI%2B8nomxlERQziRKdP8dSHq0CGqzFLDPRLrwQf05%2BJaP92yc0%2FDHZ7JcQw9soz0RGoGHSPhPMLnm5iCBLLd5mG%2BvhPZSMNn6Hy7qwrjN3sPIcrUTxpV5aA5XOvA%2BBxlLqOd5%2FzYSX9dvsT0M0%2Bc%2FVJOu%2Bk1YNhkLOq5R%2FhsMdl3YSyVrgPVjZPZbyLbHNIvCic3eCkr80G32B2GqWsc3DxhoVTpjGfKixBvCOspQUUDIUAu2JX3JmCbSDiwplkNZp8Sz4hDe5OP4f3g%2FuZGgVsHg1SMBVlWyP60Zw0h43ML8gsDLOjTSCYsxeRviE%2Bd4M%2BTTmQh03QOyTfCe8joKhdSuuz2SdHiUGwIYvktHMCn%2Fu%2FR85bjDro8v51NduiXDRWJr5Z8UzqrgLFOTDz18XLBjqkAV628s3IuBt5z4myQTpz3lIhVD%2BJY8JHcUqoeJzLoVrQdIBxWgsjH25QIl6CTCo7SP%2FDgfoVVdk16YDlrSik7iKcnTTngloTzX9WcneqaNiFmex5HFnXjPIuAqUELt5VuUXiunlClrjAuaa%2B%2FJhxKmgr5NUuSt6qtXg%2FlBEjm2z4zlX%2BgCtmtbdE7H66fNc0xNduppO7R2pxZEeDfXrz8U4f8nmU&X-Amz-Signature=0a3e98aa42caa106a479f7a4de1166a2fa6b5d8f6599041a5e06e898f431e7d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674VT2RSD%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCnJ0IbFzspwRcef%2BGQHE5O%2Bz4DicKu1e7MC87yWOz9sAIhAJzXqv2a3nYYDZEU7Pfnt1rvIgYwQKmUnzlCm5nQVyrDKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJOR3TCsi96Okn7Eoq3APJ3Bg0YLtj5qihYchnEXRTbA%2BLyPhMRNyS8QU3l7Hely9euXg2YmP%2BdsYVwIuy%2FAiIVkG5tOLIzJBnM7sX0e4SKvXympbaSQRoqjxWmAmGu9ZRWf89O0j2HrK%2F09n5FP6XUDaRwlCzPt5zPD1IioUfbR%2BPMsXopOosj02WKKTYnlpckQylvcjV7iGyNh%2Bjk6gT%2F63H9PG%2F7ordIaJiTLWOI6zGH02609AHa4GKCdK%2FRFqI%2B8nomxlERQziRKdP8dSHq0CGqzFLDPRLrwQf05%2BJaP92yc0%2FDHZ7JcQw9soz0RGoGHSPhPMLnm5iCBLLd5mG%2BvhPZSMNn6Hy7qwrjN3sPIcrUTxpV5aA5XOvA%2BBxlLqOd5%2FzYSX9dvsT0M0%2Bc%2FVJOu%2Bk1YNhkLOq5R%2FhsMdl3YSyVrgPVjZPZbyLbHNIvCic3eCkr80G32B2GqWsc3DxhoVTpjGfKixBvCOspQUUDIUAu2JX3JmCbSDiwplkNZp8Sz4hDe5OP4f3g%2FuZGgVsHg1SMBVlWyP60Zw0h43ML8gsDLOjTSCYsxeRviE%2Bd4M%2BTTmQh03QOyTfCe8joKhdSuuz2SdHiUGwIYvktHMCn%2Fu%2FR85bjDro8v51NduiXDRWJr5Z8UzqrgLFOTDz18XLBjqkAV628s3IuBt5z4myQTpz3lIhVD%2BJY8JHcUqoeJzLoVrQdIBxWgsjH25QIl6CTCo7SP%2FDgfoVVdk16YDlrSik7iKcnTTngloTzX9WcneqaNiFmex5HFnXjPIuAqUELt5VuUXiunlClrjAuaa%2B%2FJhxKmgr5NUuSt6qtXg%2FlBEjm2z4zlX%2BgCtmtbdE7H66fNc0xNduppO7R2pxZEeDfXrz8U4f8nmU&X-Amz-Signature=88541f2bd419f74153d3b3216645cd981d7cf02df02be0474e1546d1ce752a38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

