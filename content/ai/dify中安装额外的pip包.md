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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HVHTT72%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvFcgbTX0t4MNF7FzhDGKDo7neqoRhmnZjkM6gCJ1xEAIhAJX0ZZumCVXreTxW%2FN7CS7DSjsCrtr3X7t%2FkL4PKmFxNKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGYxr3aZ9h1nnWxwwq3APxrY6zY90P%2BFKmQnB9yx7eoOxjTO8CB5lv8ur%2Bmr2R9AxpeCvEI4vqj1EUiQVL6geENfj0dgRCBoZBEeh4Dsbybz28v2BoNYQEccJhZlgz23X%2F3HBF1vMNpctb9S4kOkrvXpGT1IPBRBeW35Sb7d4lLhoAZ%2BYslJk0xCJG3CEy8dTeawV7UNJ9A0uGY8ZP%2BL38OpZh2n36rrSq%2FxFUVFKHV8NFs6jcIUYOeGO%2BIqDSKhIB8siB6syBOyGIRzWsi6xnTteql%2FfgK6Y5EgwIREWgp1%2Fo86eGeWgbWCoPLC2LB2QjyQ7kAmwWafFRtZyEhv%2FcXdqKXP1q6BsjnaUW%2F2ueK5g64GMZ%2Fy7NSsI5ZKiHpzDOSnL4goTqWj9JGR6Sgcqs8yq3XZqrerELUqnrI6AiW2T9t83pq%2BdztgOwXD7lXjXvo4RXqM4PECxkhvqqrhPUfJTFlkKK1mlyzKtLLclZSTt8qkFrQkPNzSJ93ys%2F9zO%2F1Foi%2Bdg96oqpKcCUUJAClKLN5Hkj4Z8%2BsB8ROIik2VnEZPGV9sE81BbNK9%2FbcQFroExINyY086%2FXXwF62mfatMrv42rDxAoYxOJacNlqGJ%2FNM3qfoG552UC4t1fgH0ZQlG4qKohkCeN34zDvncfKBjqkAeypAQHAexrYixOpey556Iw%2BgZ8%2FeT0dwIifCDw12KWLrSliuLKNxLOLyngfjog6rRnsPcIRHLUe0ntY8ooIEg5Eb92kehusro6vDXQMpCMxZWZHMln0F1K%2FFpdMIO%2BKJ62Nl0poFmS%2F22UnbWVKLF1ANvcY7w8h0goLDum2pBwX2R4CXLmbEIfPUYRwkQmPK7sswybCHSk%2FUz7rPdq8KotNmeT3&X-Amz-Signature=41d0a36cac7fc1b606f63914e370c17f1898e4c977c696b02db2bcce7c9b4658&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

