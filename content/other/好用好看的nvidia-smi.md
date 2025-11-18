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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXELPLN3%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTeI95Jt61vm57P2Dm6a%2F38HtWzir%2FJghTLVzQAJzThQIhAJKEjq7S%2B1%2BlBf%2FPkbZ%2FPIsxnYSz7IyPHVCaRgU2%2BiNWKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJgg4Zvn5E749320wq3AM0ZA1YRZM8rs143tuO7bDS0rg6LozjKikiqAPMRlpsSWOrBIkzyaIFXqtVSGr%2BM1brWLCwyjuUVI8tvrrkCrP3PDAh5u9gbUFPqXsBHmhzjAz1CvdShCVR%2BwbSGgU0laP5lKoSAX6WzHdhxb77ekps%2Bwx4P%2FapEGiBvRJA2RRZ1YKk5Np6nha12SlzYrK%2BabYEHlPq02LMThOD7j85JW5vMRDCXJd%2B908CjqKYzr9DsOipGOkmfvBH95bmxH771jce6gNudd6tw1aAor4gTT4sCyUOM%2BfojPFLuNJIHp65Of9pd563r%2BchPwlTXtGsWwzO8QwCVDXt6W%2BEFJhIZq3wKM5iQx610RJIUboielGr0gG9I%2B82oT5U4inD2AtQvCKxn9J1IllYBl%2FmQB1px%2B1RDvPImUq9Jw46elITzWLxiBbS3gNRWiuYb3msHAqLy7LCwKKjjDre5fNiFGyDWOtUfesT5PVfE7ymv8lWHykaUq10Upj9CrmHa8p9vt0r4EXhAELXJv6ArVcrEt%2Fowl1Odn8wSEM2TeEhMV0lodIoTBw5U1gl9%2FJMuts0sbg%2FQdaTbiuLAQCXcrWONrKlGond6m2zvy41U6JL8cGztlVfJ7CGsdI4jU2G0tI00DDNmO%2FIBjqkAQR66JLusLlKUoSWAmBX%2BRvapdL5LNCNyXV7z362tgh7rAor3g3rezXyoAnsu%2BPjMh155K5xGEdWbqEPcfAqXFycpo5d92G6TUMbPWsmsntyMbJ9Q3QiS0sbjQxODgY9HDkyoYiJoVf%2FXEZ09ehi4C%2B9UEvkFztbqycwK90%2BMuDyggCWqM8wdYLypJlDBGLsSap3WWWdBWlLhN0wSWjxxnf7z3oO&X-Amz-Signature=99067fea6c91e7f96df1831ae90fc1060b251983c4054009cc9b18d7ff039a93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXELPLN3%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTeI95Jt61vm57P2Dm6a%2F38HtWzir%2FJghTLVzQAJzThQIhAJKEjq7S%2B1%2BlBf%2FPkbZ%2FPIsxnYSz7IyPHVCaRgU2%2BiNWKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJgg4Zvn5E749320wq3AM0ZA1YRZM8rs143tuO7bDS0rg6LozjKikiqAPMRlpsSWOrBIkzyaIFXqtVSGr%2BM1brWLCwyjuUVI8tvrrkCrP3PDAh5u9gbUFPqXsBHmhzjAz1CvdShCVR%2BwbSGgU0laP5lKoSAX6WzHdhxb77ekps%2Bwx4P%2FapEGiBvRJA2RRZ1YKk5Np6nha12SlzYrK%2BabYEHlPq02LMThOD7j85JW5vMRDCXJd%2B908CjqKYzr9DsOipGOkmfvBH95bmxH771jce6gNudd6tw1aAor4gTT4sCyUOM%2BfojPFLuNJIHp65Of9pd563r%2BchPwlTXtGsWwzO8QwCVDXt6W%2BEFJhIZq3wKM5iQx610RJIUboielGr0gG9I%2B82oT5U4inD2AtQvCKxn9J1IllYBl%2FmQB1px%2B1RDvPImUq9Jw46elITzWLxiBbS3gNRWiuYb3msHAqLy7LCwKKjjDre5fNiFGyDWOtUfesT5PVfE7ymv8lWHykaUq10Upj9CrmHa8p9vt0r4EXhAELXJv6ArVcrEt%2Fowl1Odn8wSEM2TeEhMV0lodIoTBw5U1gl9%2FJMuts0sbg%2FQdaTbiuLAQCXcrWONrKlGond6m2zvy41U6JL8cGztlVfJ7CGsdI4jU2G0tI00DDNmO%2FIBjqkAQR66JLusLlKUoSWAmBX%2BRvapdL5LNCNyXV7z362tgh7rAor3g3rezXyoAnsu%2BPjMh155K5xGEdWbqEPcfAqXFycpo5d92G6TUMbPWsmsntyMbJ9Q3QiS0sbjQxODgY9HDkyoYiJoVf%2FXEZ09ehi4C%2B9UEvkFztbqycwK90%2BMuDyggCWqM8wdYLypJlDBGLsSap3WWWdBWlLhN0wSWjxxnf7z3oO&X-Amz-Signature=b5a021acbb369e8d87118ea5eecb2b28dbc0c18f6ae5f4749fa6dc1bda500a94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









