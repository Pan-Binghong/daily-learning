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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCB5EUMD%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhgbVVFq4UkLGKoZPmK6HCWwDy3yeq%2FUcUNWtx66q%2BYAIgEQlB47LXQaottVIN19BVy6EC1itjpSRV9gi1FcH701wq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDP%2FLoexVDR60ovNd9yrcA%2BVQ3L%2BP1Xi%2B0mHTZijGNMSVkpk04p4EJdbU1%2F%2FgK8j4M8gcr7FBG2rcvesmpGx0x7W8NIwOBUMOW%2BvCO7pbpEAKHEVH5wAJDfkc%2Bp1K3QCo6h65lHhlz%2BMbnxNe6jENwoNHgQQzeB6Var005Jx679VBzdetO0BDox%2B3DOoMqAiH%2Bmx%2BbA8HFp9v8d0CxGIj%2B9MNLywhttSQ42EnZ8IEL9xY2IZ6DrJqZcIELkDD7b006Apis3tIw57b68MHrSgFrPfvTjA5STWdALbxZ5ir22YFz6iQ7lXhcmGK3Eeo6vE05n87xEWyhRD6%2Fg2SArR1xaaHQBK40QQt3h9q%2F%2FKFsgSgT%2F9zJZv0htw554aGSM%2BAAWUxqTwSOU%2BI8BEwe5rMc9mYlgp%2F9QB%2FbOHcaEuV%2BRva8BZhvzN5%2BIGhYA4EaZXUimtth2gzsonWC82Oq%2Bt6ztsAGpnvBp1BB1Gv%2FSfdH%2FKI4s34YzBU34AXEopKh%2BdclrmlJSV5NOPPS0vANYnuKB5SA5PdwnryeXzqff94qqJoJxAhAF3a3hKZebic%2FRG5M6QLzGR5BLLkJO7v5h6uWxguyXCWWAO0EzbSrZE%2FF603OWpwvEvZLXh9KRtckqWFH%2Bu6cr4eCzxwNpWkMO%2Btvc4GOqUBYEuq3eQ0i9Jz38dDePzdtD3T3W3FmaT2bod%2BBrtUwulMKr6JNomD%2B6OVGSkGoN%2Bnf5KGl9LSN%2FoPZfvKOq%2BREvIIByJqAIZwkFCcCfDgomNSme%2Bgd7NtEUDj%2FgPtbFlNaxZivlkiETCzTMA2aQBbN795vij3bjA%2F2c0rlNtX7KypqlBhG%2FR20SX2MpUaw0g0Q2b9SW75USFcDbsSO3rmzWVXway6&X-Amz-Signature=9b025f8dbb2b7b2f37823313b107cf0baa519181af300f0ef991be4a1c708dff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

