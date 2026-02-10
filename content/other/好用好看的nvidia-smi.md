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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XR3RKIB%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhawATLcYxLjcjHTFH5febBMGXXDu2AYiP%2B8Kfn%2FbcrAiEAhqPjhCvWYO%2BM37Z8%2FhJTY8xhTbGTSV8unAb58BQbaKcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMu%2FkrI%2BExeRUqGCDCrcA9XLpAX%2Ff%2FZs0Fe1Flr1ot7DMc%2F8%2FNyXJheTvzjY6Cs2HixFiWD8UI0CqbPsAlyepJEssPQ4L5cZs20WB%2BVA7vsab%2Bbn6qHsJJvw1SgnG1O1VEfACfQ8%2FRAOOJFscFIi6NfEjN8gMuyTL2HFhkdP8IxvceypxU01Myn65W6lkSh7xsHsCgdk2euiWkq5phg5fn6Wa%2BT6K211yWhUhF%2BfD%2BFNBnWF03eOrWuy3bRLGfAikcP%2FiK1k1K8RrHRIbqR5pojkH64pbxlnKqu7j86uOuBLmmNf7D4bqLw%2BTePSzRvY08MovW1HT6XKRoMl6qpuAt0wrKd2V45yxVN7ERvPnbmkJhRzYQD2tB5oNiBdq44hGrs9Q%2BNaFPfwhhz%2BOXGQowfjOfkL6mMAmvJTxuvcBU3xwAl74%2BaCeUlCbnP7dY729fw9j3RI65bPT1E2k0MQuz0e1S4JVEwws8Kf6GVXaJMZmranLWAQ%2FCPadTtWXy%2FjCFqqqGuNccUxlJKenfpI0UdvuAFLISMwJdkexsvfnAYC2Qn8ippc4%2BUR9B%2BsHKHQEms%2FverjMhm0ps29KJ8sAeo4xwg8OGTSW1p6VlWJ7yyWyd%2Ftoqf9otIgyD28wt%2FH3adDKJtbTCdNouliMLTEqswGOqUBvdqgERitlDLGZii3zRbAJRSrrjyjAtUtUEngMpOudFn9liPImm4dTAHdWsNdIg3W0G1w6jTlcRwGiGi%2FNFio1KYGTywv1p4qdJWRPmAT6Qfl3FgASaAux%2FtrcS6xAiR%2BUwhES1DUG8MwGG7YBLWBI%2BJ37Tyg3K%2FDTpqVkU8LwwAhdkv5DlT2Of6YsUpDo8ADEyd87wLdPMk%2BooO%2F5Ci9TfkPcU%2BE&X-Amz-Signature=c19a8afcb30c45604d4318c3baaea61ed0de8e0f541505828e399a16bfb5d03b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XR3RKIB%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhawATLcYxLjcjHTFH5febBMGXXDu2AYiP%2B8Kfn%2FbcrAiEAhqPjhCvWYO%2BM37Z8%2FhJTY8xhTbGTSV8unAb58BQbaKcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMu%2FkrI%2BExeRUqGCDCrcA9XLpAX%2Ff%2FZs0Fe1Flr1ot7DMc%2F8%2FNyXJheTvzjY6Cs2HixFiWD8UI0CqbPsAlyepJEssPQ4L5cZs20WB%2BVA7vsab%2Bbn6qHsJJvw1SgnG1O1VEfACfQ8%2FRAOOJFscFIi6NfEjN8gMuyTL2HFhkdP8IxvceypxU01Myn65W6lkSh7xsHsCgdk2euiWkq5phg5fn6Wa%2BT6K211yWhUhF%2BfD%2BFNBnWF03eOrWuy3bRLGfAikcP%2FiK1k1K8RrHRIbqR5pojkH64pbxlnKqu7j86uOuBLmmNf7D4bqLw%2BTePSzRvY08MovW1HT6XKRoMl6qpuAt0wrKd2V45yxVN7ERvPnbmkJhRzYQD2tB5oNiBdq44hGrs9Q%2BNaFPfwhhz%2BOXGQowfjOfkL6mMAmvJTxuvcBU3xwAl74%2BaCeUlCbnP7dY729fw9j3RI65bPT1E2k0MQuz0e1S4JVEwws8Kf6GVXaJMZmranLWAQ%2FCPadTtWXy%2FjCFqqqGuNccUxlJKenfpI0UdvuAFLISMwJdkexsvfnAYC2Qn8ippc4%2BUR9B%2BsHKHQEms%2FverjMhm0ps29KJ8sAeo4xwg8OGTSW1p6VlWJ7yyWyd%2Ftoqf9otIgyD28wt%2FH3adDKJtbTCdNouliMLTEqswGOqUBvdqgERitlDLGZii3zRbAJRSrrjyjAtUtUEngMpOudFn9liPImm4dTAHdWsNdIg3W0G1w6jTlcRwGiGi%2FNFio1KYGTywv1p4qdJWRPmAT6Qfl3FgASaAux%2FtrcS6xAiR%2BUwhES1DUG8MwGG7YBLWBI%2BJ37Tyg3K%2FDTpqVkU8LwwAhdkv5DlT2Of6YsUpDo8ADEyd87wLdPMk%2BooO%2F5Ci9TfkPcU%2BE&X-Amz-Signature=abd6908665097b9dff95a61fdd18788ed9a0ec152ac4e197a68bfd0d3ce822fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









