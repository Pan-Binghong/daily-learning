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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRV5GZ7V%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T033011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFRVsbTwlcCRUJEX41mCCV8Rl45T%2FNRGsREeFpuHiwtPAiEAnqy69JBTpyv9h%2F20AaE%2Ftxs%2BzcllAKK8bIWyxujcxvAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDMzKdtFDL3wrQEwlMyrcA50cpG9w9CPQQ7NIRDZcEWBbcjVMYICzQt%2BJGZ2pyWKLIe5jd74D%2FkUXDNk16MB5JDekedsmRqz9TTQoP2aH6ESEpYqUCyYytmtUpvg%2FBYoyxbUJM2s3a7IwaCW7%2FMR1ED1ghfBVVv3JN%2FtRs%2BxdKX58oxvydsk8zhow96ozdJl2pTUjwE9ea8tWjhXYQKT6VYApJNiq09cCyDZJeBD1TRCLkzAEbNOORWv0lsixAhecxqZS%2FnbjZigQhZUzTWTuAwrjlRi4xzfn3kaQPj2A8cZbPQw57kcgWBf41MuLwkl9xig57XUP81Yip04AHosaMb0b0oCREnSixy131x8J5NUTlGU5kRejsZI0PY9gHDh1swn6t%2FdlNDRL72JGAlYULJrzPO3P0a9cQ6SwYPdTODjjVwtSoWuyXIl8i9VR6FO0bW4Lc6%2FCutC6whNt4DkTTg0JqGDMQbyRNlAOZWZquWUSWPpZM5mD2jpsCDspW%2FNPHPLOfxPY%2FWtL%2BYjXHRCLNVM3SicOI%2BekkY%2F%2FLVNrh1VH3uqxcX9CGP5%2Fc9KgS%2BhrmRgiSqjiLTz%2Fyv4v5zkhx3272G68jga%2BjGX1zoUfvPPjVvbKwTPb1ugSXYj0G%2FUJo388X1eG8xSCYxd5MP2h68sGOqUBaWHKKAslZcwBuEOZ%2BcO1LEv%2FwZx%2BetxQpFbPfg8ZdbjxTbnvAADDDIzV9pIbE%2FfoMwyPFOuOfaBIskz36ubWn0w8Uc9VdJQrtJNH%2F%2BQ04k%2BpC%2FySDXH50%2BknCCBNHvSWvpptueMzcr6jzWAmZ8NwO4pKoYxLEX2pba1hbKmZnc2drTS2HCs3LwWGKeqilSYHkREZZzX30mgofTqnvKfqaYmrmyVn&X-Amz-Signature=48bd59fcf76e9dfdeffa2e7bfc813b48365e4df66e4372eb81bb12e556a082fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRV5GZ7V%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T033011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFRVsbTwlcCRUJEX41mCCV8Rl45T%2FNRGsREeFpuHiwtPAiEAnqy69JBTpyv9h%2F20AaE%2Ftxs%2BzcllAKK8bIWyxujcxvAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDMzKdtFDL3wrQEwlMyrcA50cpG9w9CPQQ7NIRDZcEWBbcjVMYICzQt%2BJGZ2pyWKLIe5jd74D%2FkUXDNk16MB5JDekedsmRqz9TTQoP2aH6ESEpYqUCyYytmtUpvg%2FBYoyxbUJM2s3a7IwaCW7%2FMR1ED1ghfBVVv3JN%2FtRs%2BxdKX58oxvydsk8zhow96ozdJl2pTUjwE9ea8tWjhXYQKT6VYApJNiq09cCyDZJeBD1TRCLkzAEbNOORWv0lsixAhecxqZS%2FnbjZigQhZUzTWTuAwrjlRi4xzfn3kaQPj2A8cZbPQw57kcgWBf41MuLwkl9xig57XUP81Yip04AHosaMb0b0oCREnSixy131x8J5NUTlGU5kRejsZI0PY9gHDh1swn6t%2FdlNDRL72JGAlYULJrzPO3P0a9cQ6SwYPdTODjjVwtSoWuyXIl8i9VR6FO0bW4Lc6%2FCutC6whNt4DkTTg0JqGDMQbyRNlAOZWZquWUSWPpZM5mD2jpsCDspW%2FNPHPLOfxPY%2FWtL%2BYjXHRCLNVM3SicOI%2BekkY%2F%2FLVNrh1VH3uqxcX9CGP5%2Fc9KgS%2BhrmRgiSqjiLTz%2Fyv4v5zkhx3272G68jga%2BjGX1zoUfvPPjVvbKwTPb1ugSXYj0G%2FUJo388X1eG8xSCYxd5MP2h68sGOqUBaWHKKAslZcwBuEOZ%2BcO1LEv%2FwZx%2BetxQpFbPfg8ZdbjxTbnvAADDDIzV9pIbE%2FfoMwyPFOuOfaBIskz36ubWn0w8Uc9VdJQrtJNH%2F%2BQ04k%2BpC%2FySDXH50%2BknCCBNHvSWvpptueMzcr6jzWAmZ8NwO4pKoYxLEX2pba1hbKmZnc2drTS2HCs3LwWGKeqilSYHkREZZzX30mgofTqnvKfqaYmrmyVn&X-Amz-Signature=5b905480da715223549150989b4db444fc60b6a99d4643eac88b5b2711e40a65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









