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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZ7P6TA%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD8ChYhqF1jdC7KoBf1SjRb%2Bs6RCI%2BMitL26G%2Fg5aX%2BegIhANitzuj6zO1C4eUM4aynvR52uJMGmhf%2B3CMab3%2B2b5yRKv8DCAwQABoMNjM3NDIzMTgzODA1IgydPZlS8cklozDHdsUq3ANVdAQ28Bg71nEaJr94I65q7zgK4cRlXiMeoa8klvLYIAtYluT3sDGDGlZifQRQKf00%2Bsalfxw%2BOIQIbzC%2BgLN0BLqZmAQLBhMxqq2h%2BOH3SQqKMJBkCKVIm0dpov4L6dg7viWWREzbjFTYLMKftGi%2FUCCwbbMneXCJ4UcFcMLa5lnPQgWyYSNqvN04QdfHxt0Yz8whJHtt61kaldKjhJdK3Cs2%2BU6wGguqq4FBZtqV594ieaOoxsPLIuMSQn9KSyjo5aXLSqVcAbQ3PiJfDVdkCvG5ArQibb9erPCqf6NjT8kUSaTO2FVSh%2BHPuvkuC5TTNuj9xjzd5YmGmecv2aEL83Kk3LuX%2BZLhbMMRKomIMl1eQM7kkGryqiQt3dgssdD4tsm6VtF8HkGvCbuaCkgM3rdETjzlR4FDL%2BujTTvdlEEx9c4hAU7m0z0RC1E42dIZ1TYLONTD4ObG8Pr7R959dsmPIf04b%2FboZn7PjZYRmSYjh%2B%2BhzjudHnDTrQAwbTRG1j0MMvJlXxfdyZPy1mSoLVs3uACSA2NJ%2F6MHy5pbii45QaPdIMkKOeBwAblk3QMiOBKxbgO6okpvC%2FpCgSzvGr4kcTfzPmP%2FhqpsXkILw62eKxlxnFSOwH9eYDDv6IrMBjqkAV3q5cXXOrSFQiWodyfzneh5bd4Q1fz4IAlY2q5wXldxPK29rhDz7TyrcaqqP1ph9RtcRh3qLygZvuEep0ZVFXC8gTty3p2LYiPevcActUGP3RtMfOzCA1ATgc8%2Fn9AXtxuOsc1GIPkOd7BYySscjay6D4zu2zcQEU%2F29WvWwQDCyuiNGExzF3RirofVr9UwF5M7Cnc1c5JOnCkqfNPp3HFEvxlq&X-Amz-Signature=7ed5a6b3b41f73f08d4775db0e9aaf04bea5741b9823a702134fd0f52cf41495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIZ7P6TA%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD8ChYhqF1jdC7KoBf1SjRb%2Bs6RCI%2BMitL26G%2Fg5aX%2BegIhANitzuj6zO1C4eUM4aynvR52uJMGmhf%2B3CMab3%2B2b5yRKv8DCAwQABoMNjM3NDIzMTgzODA1IgydPZlS8cklozDHdsUq3ANVdAQ28Bg71nEaJr94I65q7zgK4cRlXiMeoa8klvLYIAtYluT3sDGDGlZifQRQKf00%2Bsalfxw%2BOIQIbzC%2BgLN0BLqZmAQLBhMxqq2h%2BOH3SQqKMJBkCKVIm0dpov4L6dg7viWWREzbjFTYLMKftGi%2FUCCwbbMneXCJ4UcFcMLa5lnPQgWyYSNqvN04QdfHxt0Yz8whJHtt61kaldKjhJdK3Cs2%2BU6wGguqq4FBZtqV594ieaOoxsPLIuMSQn9KSyjo5aXLSqVcAbQ3PiJfDVdkCvG5ArQibb9erPCqf6NjT8kUSaTO2FVSh%2BHPuvkuC5TTNuj9xjzd5YmGmecv2aEL83Kk3LuX%2BZLhbMMRKomIMl1eQM7kkGryqiQt3dgssdD4tsm6VtF8HkGvCbuaCkgM3rdETjzlR4FDL%2BujTTvdlEEx9c4hAU7m0z0RC1E42dIZ1TYLONTD4ObG8Pr7R959dsmPIf04b%2FboZn7PjZYRmSYjh%2B%2BhzjudHnDTrQAwbTRG1j0MMvJlXxfdyZPy1mSoLVs3uACSA2NJ%2F6MHy5pbii45QaPdIMkKOeBwAblk3QMiOBKxbgO6okpvC%2FpCgSzvGr4kcTfzPmP%2FhqpsXkILw62eKxlxnFSOwH9eYDDv6IrMBjqkAV3q5cXXOrSFQiWodyfzneh5bd4Q1fz4IAlY2q5wXldxPK29rhDz7TyrcaqqP1ph9RtcRh3qLygZvuEep0ZVFXC8gTty3p2LYiPevcActUGP3RtMfOzCA1ATgc8%2Fn9AXtxuOsc1GIPkOd7BYySscjay6D4zu2zcQEU%2F29WvWwQDCyuiNGExzF3RirofVr9UwF5M7Cnc1c5JOnCkqfNPp3HFEvxlq&X-Amz-Signature=3879f45cb7d5dbfcdc704954bcb6ce75f66e7e67e01114dbc3518ae806890825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









