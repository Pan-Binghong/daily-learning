---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REXQQLUC%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTCRAusW3ZDiLzGj4oLeuZ1cpyFtFZKdYkpnPIELWEBwIhANnxTIsOC2vIDFvuMAgC%2Fvrzs7wlviqpva2Fk%2F%2Fj%2B8IfKv8DCEsQABoMNjM3NDIzMTgzODA1IgxjZTNBsDUs9fMBFfsq3AMWiwTNK1skGOf9fUTfhSADEJ5tm%2FCL8r5wbu6kSfe%2Ba9r7TNAHDCTVW673zyAl5DvrPfTxoVjr%2BRTWN%2FLu8ALVtFP%2BM1GhzESlb%2BcFg2Nx9eQdI%2FEjtCl1teXhqLnaW79l2SPiQhluPyvApQ4YQ36GukUwVCZ1PBdbqd3zCnUC3XQasGhzwzWKrmbaBc%2FlxyMYvyhHU9yMKL058th7fP8XqpcFIzOZWCRIE3vivizxXctIz084Q7BD9LMf1AqAQesq4upVMIIcBTqqVsLiKFYFsEHoza6gd3JZf2bB3voBTCgXEHwfYF61YNb9a0v7gA0RdsfHR0vRdHGjiA5pl0bS1BKMEDYsBtzBnxIkCl46yx4TtymVg9ZzfL7Pwb%2BsuD8qKjGA%2FGIr7%2Ftg42T%2F8fV2xTt7xZaTqOBL0CK55av4E4rU%2B%2FlG4SUTwmESIqtl1w%2BitExJmF0fpQCeS%2BPKhVkZdT%2BV6bcp3lIWSLBOxFEPTr9yG1XlwcH49LK6hrmkA44H3wuo3zuOyD%2BdT7XQlQBawLpBvO3u9ED4vIGXbVXdhSS%2B4imfGBoodsjx2uL966OFClewtETuTJVX0cRRPESEvyQaO%2F7GgnvsA1OdBE51RkPY1%2B2%2Fwv2%2BjuFD1TDz1LfKBjqkAfOPDfCktApX1SrOCq9tGmPX%2FC4jyRlyOc3YHVJS3LH2RshD5buFcuosmTx1gbTRaGvQ7ykgZPSNfygbjdvZ81FrA6xkFJh9%2Fp66dfTVIDpG5x3QZ5%2FYCa7G6myhfGz1pfowUOp1TtF7tjJbGtI1HOkCaYtQumNymnk%2Fv2ufQIFIMTxxPG3cKZohpEMUaMGhZur%2BudxtP2on3T7GjIEMX0rx00nQ&X-Amz-Signature=a8a5a5eaf37196497cf2a998bef4498b595783983fc01d2f2231deaf0866b736&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

