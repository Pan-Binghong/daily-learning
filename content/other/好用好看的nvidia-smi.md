---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2SQXO7%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIGdz%2F1mP0LBk%2F8mryXTzPkx62SMA3JSNJzUK43Qz784BAiEA%2BZGM%2F5sjQWqR0DnMkvIjTPJ1WUPOUYnn7pkwwRHS8TYq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPy0LqSwPkc7PidcyCrcA3mCtLsQP4w527BHPisO1mf1pZTnypwLK7eQo%2BdVhzuQfCSBKFokaIa5MQxjClR%2B%2Ba%2FnkG350sYlk84dxGjjux%2FGNK2cdg%2F3o%2FK0OqCjDz%2FYw43G2EQA8lHs9sbOYrrF3lA76ogzXTAPY57sy9%2BVjXzpbM4934F9pEVVJtGDgYtaCd5PeC6JJB%2FbjZLd4V8tdT8lwW57W6AC7Mo4kbvRKC9QN7IMVOny41cTvoSux3eQ%2FJYfqlQjzivszM5AUOPpHGoovzBYiM9%2BPKTI5g80owgpsaziObsfNKRVpBLVPG5%2BouMianEfQsMy%2F%2FinHHr8pSgJXwQmaTQjnV%2FShFwe1v6UhasdlwUC5TSrx6%2F4VArlhyFJEENyrzgmluxZ0%2BH3BM2PQGS6jceMD1KoTlGnRAgqEFpKBII5eczhwllIGwkds4PKPcXRpLFh152zgn7IaQ20a9J5soU9QWvJz1jfTwGwTfMtsw2XrjVJrd4L6VMpB9zoNDx9Urrd9LrUcmaf7fVF1ZdHJ7KnBF9uGjhhk77EB5qv0MD1ugQNN2BZX97V4NAaFxChTG1Y7nT090%2FSnj3wLLZFBgIqdhANN9ERyhsoJsHrjMOfX%2BjUzqet9hIJD6iC6xEEkW%2F4skgJMLGGhM0GOqUBLXeF8sJSmufMz%2FGxwRuwz7YUF59%2BmP3McxE7div0oywNAD%2F1M5xlV2WLNqZF%2BNZFhr3xT5QaMj9zQolId7wNpsMjJHRe90uRg9ha4AEyyto5bWWTd%2F9QV9cb43bEHYxJs42sP5NEGBcR76k3V1Ht9IKrRoFZIBiMK8q4PyMHi1vyOoqUZrPCm9lbyRHgAkAQ%2BpqetSxli5GlT9U3Mk%2BwyFVitfBN&X-Amz-Signature=6ad0bb616200d69a7fcd63fedd719cff57ab201be7411875d20599171daec56e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T2SQXO7%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIGdz%2F1mP0LBk%2F8mryXTzPkx62SMA3JSNJzUK43Qz784BAiEA%2BZGM%2F5sjQWqR0DnMkvIjTPJ1WUPOUYnn7pkwwRHS8TYq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPy0LqSwPkc7PidcyCrcA3mCtLsQP4w527BHPisO1mf1pZTnypwLK7eQo%2BdVhzuQfCSBKFokaIa5MQxjClR%2B%2Ba%2FnkG350sYlk84dxGjjux%2FGNK2cdg%2F3o%2FK0OqCjDz%2FYw43G2EQA8lHs9sbOYrrF3lA76ogzXTAPY57sy9%2BVjXzpbM4934F9pEVVJtGDgYtaCd5PeC6JJB%2FbjZLd4V8tdT8lwW57W6AC7Mo4kbvRKC9QN7IMVOny41cTvoSux3eQ%2FJYfqlQjzivszM5AUOPpHGoovzBYiM9%2BPKTI5g80owgpsaziObsfNKRVpBLVPG5%2BouMianEfQsMy%2F%2FinHHr8pSgJXwQmaTQjnV%2FShFwe1v6UhasdlwUC5TSrx6%2F4VArlhyFJEENyrzgmluxZ0%2BH3BM2PQGS6jceMD1KoTlGnRAgqEFpKBII5eczhwllIGwkds4PKPcXRpLFh152zgn7IaQ20a9J5soU9QWvJz1jfTwGwTfMtsw2XrjVJrd4L6VMpB9zoNDx9Urrd9LrUcmaf7fVF1ZdHJ7KnBF9uGjhhk77EB5qv0MD1ugQNN2BZX97V4NAaFxChTG1Y7nT090%2FSnj3wLLZFBgIqdhANN9ERyhsoJsHrjMOfX%2BjUzqet9hIJD6iC6xEEkW%2F4skgJMLGGhM0GOqUBLXeF8sJSmufMz%2FGxwRuwz7YUF59%2BmP3McxE7div0oywNAD%2F1M5xlV2WLNqZF%2BNZFhr3xT5QaMj9zQolId7wNpsMjJHRe90uRg9ha4AEyyto5bWWTd%2F9QV9cb43bEHYxJs42sP5NEGBcR76k3V1Ht9IKrRoFZIBiMK8q4PyMHi1vyOoqUZrPCm9lbyRHgAkAQ%2BpqetSxli5GlT9U3Mk%2BwyFVitfBN&X-Amz-Signature=2dd7056bd06b54f80b0052da1d024bbd047885f93425148684bc96d21f8a044e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









