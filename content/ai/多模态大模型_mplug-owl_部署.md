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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DSKB2Q4%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFGS13UclPMkgo90q%2B%2FQFHKAY3IlYjQgURxYIbBIpEs3AiAl6Hqth%2FZzB97TvrMmg9rdCvUdsQn4flgfSdljf9AA%2BCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYDOSyK6Q3q8i89KEKtwDAwX3SH8PU9nZJNZ5%2BeWXX7IRX86fQqiL9FE1nyMGyoziTR%2FEMDeSFKnUI8ERvVhiFLbGUsrw8xPAnsRAquDDIlUpN7354YHcMDbu9uKoSROiFVQoY1v6tQ4%2Fuz%2B%2BsEXwq%2B%2B6yMv80D1zF2qPm5R9trK03VBUu7IVLs9eBYaFZwy4AtIwkby4y6qaezndGx6wkQ9itxToW%2FXGTJHkS%2FFisP8AoZuthel0kjOyoFA7RvDNm1b5Ickae7t%2Fgty9pSda2GUYUCnwKY0TiPhoRFSC72kgQC9QO8X21EJH%2BrDhhKFj8F%2FPd9bXSG0%2BSHR9kDBgQ05j%2FufoGVTaaAWhKI2RUlCdARy3MgCro%2FrNnE8SXgANQvC%2Bj60%2BRvO2WntxbpUW%2BNJY06Qz5gQyHrP3QwfI51s5uK%2FifKKfGSyXqZfr84feG5Cf70r9EMf%2F4nOoWhM5et36eMgYl%2BpTDvJ0PHMyqKkb6Vs9XTQrtiuksuo7mWht7AMBd4QdIK4OPJp5J%2B4cb4qZX0s2sjqocAh2LpeveEQf7nHZXWBSTHBC6CPQ9NcjAEeZtPEfeFJ%2BJNaiGPCXp6xP1zw0YjXpFeFYJrwtgKn7YSASkzk5c0SywuEkJzXXT1RCqj3GEArCdYgw4ZnXygY6pgHAOFYLajRpSETSe8YssWmAvGQLHgF6t1SMAwmjGRYHjGMsomE16ApZLOTGlg75i5yNuYnp8Vqd8FL6rDfzP%2Fu1WW7kMbigKQ7Cs03UXREpvgUu9Yjw0FcjzW6TkvOM7E9AEilBd78WsRzX9wbMfbHxVuyb%2Bb46vR5GV9ZugVmsmfq6pIRWFsRK5mh798RtJYVtqVQjPmkn5xhbFq4y2SU5%2B7QY94TG&X-Amz-Signature=6aa4f205fa8bf599025c3b8982ee87878d93b681ac1efd790fae44c25fed37ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DSKB2Q4%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFGS13UclPMkgo90q%2B%2FQFHKAY3IlYjQgURxYIbBIpEs3AiAl6Hqth%2FZzB97TvrMmg9rdCvUdsQn4flgfSdljf9AA%2BCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYDOSyK6Q3q8i89KEKtwDAwX3SH8PU9nZJNZ5%2BeWXX7IRX86fQqiL9FE1nyMGyoziTR%2FEMDeSFKnUI8ERvVhiFLbGUsrw8xPAnsRAquDDIlUpN7354YHcMDbu9uKoSROiFVQoY1v6tQ4%2Fuz%2B%2BsEXwq%2B%2B6yMv80D1zF2qPm5R9trK03VBUu7IVLs9eBYaFZwy4AtIwkby4y6qaezndGx6wkQ9itxToW%2FXGTJHkS%2FFisP8AoZuthel0kjOyoFA7RvDNm1b5Ickae7t%2Fgty9pSda2GUYUCnwKY0TiPhoRFSC72kgQC9QO8X21EJH%2BrDhhKFj8F%2FPd9bXSG0%2BSHR9kDBgQ05j%2FufoGVTaaAWhKI2RUlCdARy3MgCro%2FrNnE8SXgANQvC%2Bj60%2BRvO2WntxbpUW%2BNJY06Qz5gQyHrP3QwfI51s5uK%2FifKKfGSyXqZfr84feG5Cf70r9EMf%2F4nOoWhM5et36eMgYl%2BpTDvJ0PHMyqKkb6Vs9XTQrtiuksuo7mWht7AMBd4QdIK4OPJp5J%2B4cb4qZX0s2sjqocAh2LpeveEQf7nHZXWBSTHBC6CPQ9NcjAEeZtPEfeFJ%2BJNaiGPCXp6xP1zw0YjXpFeFYJrwtgKn7YSASkzk5c0SywuEkJzXXT1RCqj3GEArCdYgw4ZnXygY6pgHAOFYLajRpSETSe8YssWmAvGQLHgF6t1SMAwmjGRYHjGMsomE16ApZLOTGlg75i5yNuYnp8Vqd8FL6rDfzP%2Fu1WW7kMbigKQ7Cs03UXREpvgUu9Yjw0FcjzW6TkvOM7E9AEilBd78WsRzX9wbMfbHxVuyb%2Bb46vR5GV9ZugVmsmfq6pIRWFsRK5mh798RtJYVtqVQjPmkn5xhbFq4y2SU5%2B7QY94TG&X-Amz-Signature=14982b3c7ee86d474889ae7e7548d3e589bcdb6cc7365566c213f53502746945&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

