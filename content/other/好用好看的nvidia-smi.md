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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2LQZL6N%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9IeZ7Artr%2BMNfRGwciq90yjLmw8S3mGVZyHRzVxGajAiAhZglB0VegaHIrmO8og%2BpDBTMIFmCZDDru%2BPZIevGSSiqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPYn%2FIWeK%2FeglmWPoKtwDCMc%2F2TkHEvpR%2BUOdFtrIfbDx5upA%2FBPSJend4nXF2oJDNUyup%2BR9XXAPZgrRw1iJTJt2bWH2EVVygUbWzERfugCcAVFhBO0Ct%2BdCfvsi5dl8sur8GT08XoyA6VqhM%2FiScUMumOU9iP6jiLIfH0V1hzTi30tvPedSXvy0Umfvk5AoPIdHsQux%2BHhONDvqFwr2qiy8IZRsU%2FaLMF71oc5B9FeaF2HJ8SiQe85iWS%2BkANbUPZR77Lr%2F5K2HpY17jjN2YNaVoJ%2F6ntEI1y2AnIUwtdyf8lR%2Bx8Ji2qNL5Biuj17jaEXqefLJRz5C%2F242D6akv90FUjd22tOcfTyEc3LMCcoW7QsdDdlW4vxa7BL5SNi0kHiO67UPtqC6mfAUMKlrJhrdz%2BPPqQDVBNwFs6qNjPaRuwQTNgxJuQek%2FYgfJRMgKw6O1gyBmAcRXizlhpQFGqAn5snGloGM8L%2FpZ6fJfxrynvkCgSWBqfhpmbDf1Uby5Pu2dMnq6iXRwUpnJSC6D587PnZGg02754CtV5P%2BqEV1MJFgu7EpOJZgKrHeUZTh%2B4uwGRWd%2BXq6zOn7AYsOAl4IFDfaGza1SD%2FZbgLjPh1pcZ514ptlVZcnvcYuJTiugPxzpTcBzexMl8ww45WwyAY6pgGYnJauqMJbveoXg4kpjQjQHiIjqz%2FaTGKAhlVLi3oYqReVF4PDmfgrshPfn0vDJ8PQCqXjp5MusncO1V4XKihaDc6XR1JJxc83LbdsCxRP1bjrK5dJOwSx5gDOF3g13rx8cUjjb61jciQ1oJjsWR%2FRU2q4mPnOi69ILyrzmfAbejlgaMwJUIMuBxILbTF1Cn4S8U3a2E%2FcPThG%2FBCL0hgY0riONyxc&X-Amz-Signature=0949bc7b104fa5a5c78e05d85181da112ae4823f5fa1aab831886ae11addc09a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2LQZL6N%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG9IeZ7Artr%2BMNfRGwciq90yjLmw8S3mGVZyHRzVxGajAiAhZglB0VegaHIrmO8og%2BpDBTMIFmCZDDru%2BPZIevGSSiqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPYn%2FIWeK%2FeglmWPoKtwDCMc%2F2TkHEvpR%2BUOdFtrIfbDx5upA%2FBPSJend4nXF2oJDNUyup%2BR9XXAPZgrRw1iJTJt2bWH2EVVygUbWzERfugCcAVFhBO0Ct%2BdCfvsi5dl8sur8GT08XoyA6VqhM%2FiScUMumOU9iP6jiLIfH0V1hzTi30tvPedSXvy0Umfvk5AoPIdHsQux%2BHhONDvqFwr2qiy8IZRsU%2FaLMF71oc5B9FeaF2HJ8SiQe85iWS%2BkANbUPZR77Lr%2F5K2HpY17jjN2YNaVoJ%2F6ntEI1y2AnIUwtdyf8lR%2Bx8Ji2qNL5Biuj17jaEXqefLJRz5C%2F242D6akv90FUjd22tOcfTyEc3LMCcoW7QsdDdlW4vxa7BL5SNi0kHiO67UPtqC6mfAUMKlrJhrdz%2BPPqQDVBNwFs6qNjPaRuwQTNgxJuQek%2FYgfJRMgKw6O1gyBmAcRXizlhpQFGqAn5snGloGM8L%2FpZ6fJfxrynvkCgSWBqfhpmbDf1Uby5Pu2dMnq6iXRwUpnJSC6D587PnZGg02754CtV5P%2BqEV1MJFgu7EpOJZgKrHeUZTh%2B4uwGRWd%2BXq6zOn7AYsOAl4IFDfaGza1SD%2FZbgLjPh1pcZ514ptlVZcnvcYuJTiugPxzpTcBzexMl8ww45WwyAY6pgGYnJauqMJbveoXg4kpjQjQHiIjqz%2FaTGKAhlVLi3oYqReVF4PDmfgrshPfn0vDJ8PQCqXjp5MusncO1V4XKihaDc6XR1JJxc83LbdsCxRP1bjrK5dJOwSx5gDOF3g13rx8cUjjb61jciQ1oJjsWR%2FRU2q4mPnOi69ILyrzmfAbejlgaMwJUIMuBxILbTF1Cn4S8U3a2E%2FcPThG%2FBCL0hgY0riONyxc&X-Amz-Signature=fa635064e7d66ec548d2a8facc64bb5b815f061b0bb1b0c517f717f671db0499&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









