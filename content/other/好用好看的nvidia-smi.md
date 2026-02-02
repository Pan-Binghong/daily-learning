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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH2FOECR%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDzqkx03ZItd3iYpm00YCP3axY647TTZc7IfWQcxizSyAIgcB1WC%2FabdkTEDRvt%2F4ghutufW58mPA9R%2BxzUfqFsL5gqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDHGRbwQ4XtPWEs9CrcA%2BLyG%2BdAWkHoAYpHV8oXKRP%2Bln8SkPZpONqO%2BSDj9fsiRA0w3LeZ454cgULPiXhx%2BqN1BFZS%2FFSgYrsjOfpKy5T1RnoJdw4iojLf0UhPSABZpgLoID9COF2Eh2EqqZDSaxSTGCvqmhZzAg%2F7nPJQFcZ8My3mDibtauAQTNur9MGbYN%2FKRFSIVnJ9pFi1kkXh1uud9My1JmDkaA9s6lY8ZM7cKnxf682sz6cu2evfD30cPARViVN6Zf%2B4aJ92%2F%2FSbKgJxJn4IeNm%2FdarYh2dc4QVjE%2FY1FrL1bPGp2IZCRKTHojSO8hu0dtAOngYYvZyeRY%2Ba6XHksDhA9wgtDVXP%2BVRfJmhBqmcXwGZkoGmzEttlp0eYNvE1Dw5hH2De1sAtHSBG47eI8RcnqTDEFhzfXFR2eiLJ3P%2FppR%2BgcfAN5olmPXCGcmCuHzaprV4caSlNiAfOmH8bV0jWfrgwR7Xwbuj9m92nR9P%2Bgyw5VZEx07VdpctnirVIjSrTkly9GDDYuMwXkeNruxWqEMsepGKv%2BWJgXroky9SD4ZMlKXx34ER1KYzAXCTxtOXbO3MUE7Z7Q77HQlv8viRIcbl23dVbVD3HIczIdjVFOn7XWn94Zap1KvNnc1uoInM1oEM4MOCHgMwGOqUBbARbW2hfKf%2BDT5225gkJW3QskYAJKVxwNh4M%2BxNIm38840D9YFsL%2F2YbqXHRzGqjFi9ORgkMGSjrMG04OXYu1z1RIdJqWdIBWTbR9AS6Q4tuHR%2BYBnhru80M7XgCy4Xok1FJyfMZ%2BTsH0e1SvGYykPI4tstR5AqVTQ70DPjRLsJO2hh59kXWiulCXijJJLuA4xQSoUUh%2Fe2Pshyk0I35MP%2BLux3u&X-Amz-Signature=c5770920be3ffdc8abe00180d381d3fb0a904a6d0dc3e8cfcb8b77d3219880e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH2FOECR%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDzqkx03ZItd3iYpm00YCP3axY647TTZc7IfWQcxizSyAIgcB1WC%2FabdkTEDRvt%2F4ghutufW58mPA9R%2BxzUfqFsL5gqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDHGRbwQ4XtPWEs9CrcA%2BLyG%2BdAWkHoAYpHV8oXKRP%2Bln8SkPZpONqO%2BSDj9fsiRA0w3LeZ454cgULPiXhx%2BqN1BFZS%2FFSgYrsjOfpKy5T1RnoJdw4iojLf0UhPSABZpgLoID9COF2Eh2EqqZDSaxSTGCvqmhZzAg%2F7nPJQFcZ8My3mDibtauAQTNur9MGbYN%2FKRFSIVnJ9pFi1kkXh1uud9My1JmDkaA9s6lY8ZM7cKnxf682sz6cu2evfD30cPARViVN6Zf%2B4aJ92%2F%2FSbKgJxJn4IeNm%2FdarYh2dc4QVjE%2FY1FrL1bPGp2IZCRKTHojSO8hu0dtAOngYYvZyeRY%2Ba6XHksDhA9wgtDVXP%2BVRfJmhBqmcXwGZkoGmzEttlp0eYNvE1Dw5hH2De1sAtHSBG47eI8RcnqTDEFhzfXFR2eiLJ3P%2FppR%2BgcfAN5olmPXCGcmCuHzaprV4caSlNiAfOmH8bV0jWfrgwR7Xwbuj9m92nR9P%2Bgyw5VZEx07VdpctnirVIjSrTkly9GDDYuMwXkeNruxWqEMsepGKv%2BWJgXroky9SD4ZMlKXx34ER1KYzAXCTxtOXbO3MUE7Z7Q77HQlv8viRIcbl23dVbVD3HIczIdjVFOn7XWn94Zap1KvNnc1uoInM1oEM4MOCHgMwGOqUBbARbW2hfKf%2BDT5225gkJW3QskYAJKVxwNh4M%2BxNIm38840D9YFsL%2F2YbqXHRzGqjFi9ORgkMGSjrMG04OXYu1z1RIdJqWdIBWTbR9AS6Q4tuHR%2BYBnhru80M7XgCy4Xok1FJyfMZ%2BTsH0e1SvGYykPI4tstR5AqVTQ70DPjRLsJO2hh59kXWiulCXijJJLuA4xQSoUUh%2Fe2Pshyk0I35MP%2BLux3u&X-Amz-Signature=3c1c0a14dd9a4656980755a52520203aab0f64dab343a2ef036f488078830108&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









