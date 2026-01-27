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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AHUJMLI%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5BIdanbmabAokd7QYpokYM%2BCnln0JbavrcXuuqku95gIgZyzO8maR1kSFEiybQT9jnK7tD37TW3%2FWHGB2wwt3eKEq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDIfOt6NB45DlBHFbMSrcA5cNhcs98FdDkUmMPsYQiBPM68SKB%2F70n7p4asvw1RUQSypv04HVkWce%2FzDI4xYvFuZP1Z64XP0wQa8xeMA%2Fg1GrpUXaU9GLaeZKx4PKLWh9j4xEJo7KTdGeTKXPQ%2BkNeY0cuZJRJc53Xast4Gr7fnGhWxRcAUTI39FjSFj1Lp4jXsXQO8LG%2BP%2BSAwC02tIwVNZpt8xvTmKckd9PNsRZi2cqDGI6wvrw030Zi%2Bf4MT5O2Ezxj%2FohG9RSmCgGKIAWDtGbG6G4yc5OiNWe8flulukb7BMIeptzXPj1NBWGCGF8%2BqPctn1aPG9JWPNRJbjRiU%2BOLBQt1PStaR%2BIExo5rAvSmOX%2Byyufr0T7bHWEPH4LyLz2KBopRH2sIG8c%2B%2FQQFoyHsdKUgS0k6SH%2BCvD5jWfb8IQKRRlqd8EysmTgmex9btKcXkVmEBPjiHFFa0at0wXaU6Ok%2B4H4DGnMzFRKBnW3FWupTsyDGvtNsqdNGXsYA5VTgdsG4T6lOw%2B3m2r0G%2FXuaj2IDR1I09x4qiCrtHQ5a7%2BnFvfSwfGaDV6BaSC9Nrjcy1xnT9tMysf1JDLBD5xBajCycWHaH%2FP%2FMRr005dIUF0Flz1jykufhToGdTTus1gtTLWbTxD%2BwNQ%2FMOTT4MsGOqUBQyKge%2FEyQ%2FMdGhdenrTn%2BFjSXd859p3QyI1zn%2FbZ8rYmDuaeI23iOx5mX7gzrKOLOqRPse2F7RMNleBFMfTGLtdWnq8boqRXwxkF4vpJj7NfIWGPnTtUGRtXc%2B8d%2BKBGO3RWTT8LZgzkNzRXKu2h80XOL6iNMLw3ZztTDExZWGWJ%2BhgbMZYkNeZX2EP5xQfhKr2sS1DY22p054wTAkbnvV%2FyCuN%2F&X-Amz-Signature=079ef0ecf2b86ad8888fc6c23847ad992eadcda58467c458404cabba597991a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AHUJMLI%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5BIdanbmabAokd7QYpokYM%2BCnln0JbavrcXuuqku95gIgZyzO8maR1kSFEiybQT9jnK7tD37TW3%2FWHGB2wwt3eKEq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDIfOt6NB45DlBHFbMSrcA5cNhcs98FdDkUmMPsYQiBPM68SKB%2F70n7p4asvw1RUQSypv04HVkWce%2FzDI4xYvFuZP1Z64XP0wQa8xeMA%2Fg1GrpUXaU9GLaeZKx4PKLWh9j4xEJo7KTdGeTKXPQ%2BkNeY0cuZJRJc53Xast4Gr7fnGhWxRcAUTI39FjSFj1Lp4jXsXQO8LG%2BP%2BSAwC02tIwVNZpt8xvTmKckd9PNsRZi2cqDGI6wvrw030Zi%2Bf4MT5O2Ezxj%2FohG9RSmCgGKIAWDtGbG6G4yc5OiNWe8flulukb7BMIeptzXPj1NBWGCGF8%2BqPctn1aPG9JWPNRJbjRiU%2BOLBQt1PStaR%2BIExo5rAvSmOX%2Byyufr0T7bHWEPH4LyLz2KBopRH2sIG8c%2B%2FQQFoyHsdKUgS0k6SH%2BCvD5jWfb8IQKRRlqd8EysmTgmex9btKcXkVmEBPjiHFFa0at0wXaU6Ok%2B4H4DGnMzFRKBnW3FWupTsyDGvtNsqdNGXsYA5VTgdsG4T6lOw%2B3m2r0G%2FXuaj2IDR1I09x4qiCrtHQ5a7%2BnFvfSwfGaDV6BaSC9Nrjcy1xnT9tMysf1JDLBD5xBajCycWHaH%2FP%2FMRr005dIUF0Flz1jykufhToGdTTus1gtTLWbTxD%2BwNQ%2FMOTT4MsGOqUBQyKge%2FEyQ%2FMdGhdenrTn%2BFjSXd859p3QyI1zn%2FbZ8rYmDuaeI23iOx5mX7gzrKOLOqRPse2F7RMNleBFMfTGLtdWnq8boqRXwxkF4vpJj7NfIWGPnTtUGRtXc%2B8d%2BKBGO3RWTT8LZgzkNzRXKu2h80XOL6iNMLw3ZztTDExZWGWJ%2BhgbMZYkNeZX2EP5xQfhKr2sS1DY22p054wTAkbnvV%2FyCuN%2F&X-Amz-Signature=2ccbd86e236566715cd96d200ddbbf889660b70c0f2dd34a0f7ffed1c9ccf957&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









