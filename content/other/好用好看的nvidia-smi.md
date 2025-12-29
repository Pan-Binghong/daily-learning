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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKOMAECM%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5dZK05ZZ0FuP%2BJtJGbLQx7Aq4eYE1YNHCmaAty5OneAIhAPqP769Vid1p10GlyFwAP16EVQbbl3YI%2B84uYlAzNUiYKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwID4j2V2zy2e%2BoBcgq3AMQP%2BnOX56miLcbUipLyqhttRpnmeLhUTrIbrtBv0jzgL%2Bdu%2FWE3pawEt0h5o0V9%2BuiW7awT2I8LVejWFG3M%2BPImXYQ0ubyv28TvJWqg9vR1HP6kEPF9i0sEuop3Xi8P7GB1VPto9ix0Qqe9AKFTT20js3y721G58tv7CVYIOLEJNLswD5f2nZp0tf1g1hL33azpqqlv0a4onsmvJ6A84oeqFC8LLA8axYnSFnA3rJ9y5L65B70fWhT36oc8%2BTmnJIzITKgdL5%2BGhmbWWQ8QUVNBBI%2BwjncemHWj5M%2B4B12Y1oYRiC5OkXEdSlcPsiaxXhXMQWplQ3Q4hcpdMQblbzbJU0pW%2BR%2BSrsyf1S4thus0Jqb6zhXhxDjkixLJHXxu1Qq1QvQGO0TFbcCYPTmO38XDWf%2Bvx2Nn4AyuWUGb5xNQHtFzVU7Qsd8Ndio%2FddubXvlbCGCNSgPpV5KQRzZzItVRYUXX6o%2FTxLOY2jjzxup0iuaridqRYu975SvpKEhw7qXEMb3YGwEcVDZBrbNJlM%2FgsIfs3YJY8%2FwUxRIumecn87LQlj%2BM1Cth8JDxSkW%2BfDs%2Bwl4fIjzYuIgzVtHFUmH1bLOQfgnLBymlkrlygzo5vaLTYWEqop%2Bm9zh3TDCn8fKBjqkAQSIAld3dhSMsiMrC5HGSzTXinYpU5FNcMqfm%2B0BR%2BumgdnoOc0DBM%2FimmoMQUU0%2F5tESaeb9oEddh3eC4gcaSgei%2FUxSWXSVf1SSffmcww8ACLlEA8T%2FERtNO%2Bwf0WW61TmZYHEcTpX4jSCLZhghUv2ycMlQGWZwLWQtSfLFC5QHRf5ZPqw3smUTskVZp1vCgiXMEx8%2BWU6makz19fnb%2FF%2FbCWC&X-Amz-Signature=454b780cefbdefd3921f77f34533d47055cf19994d2c892a3d45fd667eceaab3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKOMAECM%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5dZK05ZZ0FuP%2BJtJGbLQx7Aq4eYE1YNHCmaAty5OneAIhAPqP769Vid1p10GlyFwAP16EVQbbl3YI%2B84uYlAzNUiYKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwID4j2V2zy2e%2BoBcgq3AMQP%2BnOX56miLcbUipLyqhttRpnmeLhUTrIbrtBv0jzgL%2Bdu%2FWE3pawEt0h5o0V9%2BuiW7awT2I8LVejWFG3M%2BPImXYQ0ubyv28TvJWqg9vR1HP6kEPF9i0sEuop3Xi8P7GB1VPto9ix0Qqe9AKFTT20js3y721G58tv7CVYIOLEJNLswD5f2nZp0tf1g1hL33azpqqlv0a4onsmvJ6A84oeqFC8LLA8axYnSFnA3rJ9y5L65B70fWhT36oc8%2BTmnJIzITKgdL5%2BGhmbWWQ8QUVNBBI%2BwjncemHWj5M%2B4B12Y1oYRiC5OkXEdSlcPsiaxXhXMQWplQ3Q4hcpdMQblbzbJU0pW%2BR%2BSrsyf1S4thus0Jqb6zhXhxDjkixLJHXxu1Qq1QvQGO0TFbcCYPTmO38XDWf%2Bvx2Nn4AyuWUGb5xNQHtFzVU7Qsd8Ndio%2FddubXvlbCGCNSgPpV5KQRzZzItVRYUXX6o%2FTxLOY2jjzxup0iuaridqRYu975SvpKEhw7qXEMb3YGwEcVDZBrbNJlM%2FgsIfs3YJY8%2FwUxRIumecn87LQlj%2BM1Cth8JDxSkW%2BfDs%2Bwl4fIjzYuIgzVtHFUmH1bLOQfgnLBymlkrlygzo5vaLTYWEqop%2Bm9zh3TDCn8fKBjqkAQSIAld3dhSMsiMrC5HGSzTXinYpU5FNcMqfm%2B0BR%2BumgdnoOc0DBM%2FimmoMQUU0%2F5tESaeb9oEddh3eC4gcaSgei%2FUxSWXSVf1SSffmcww8ACLlEA8T%2FERtNO%2Bwf0WW61TmZYHEcTpX4jSCLZhghUv2ycMlQGWZwLWQtSfLFC5QHRf5ZPqw3smUTskVZp1vCgiXMEx8%2BWU6makz19fnb%2FF%2FbCWC&X-Amz-Signature=979b2a6e090559bfabf75bad2d6f89884b00e5c77f037df71672f4fec414d222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









