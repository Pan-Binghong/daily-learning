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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN4GRNXA%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDi98%2Bb55KozRdbK9wv58dhLawcE7loTGn7KaZs9QUUwAIgU5hN%2F%2FJN%2B6qFE8GVC24Gj3D8BBBkdm5Lptcmf01kowoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUPo%2Bity%2Fm%2FkS9h7CrcA1XJIgmgo6wWw9W%2BC9SvmEpagc0K7SonNHg%2FRGBJSAcL9esIGILmM7%2FuGoJF3noKkwxj9eBsYrojGlsHhKBzp5BfyRulZqjIQcIRM3Y40HCEtsacIfoZoulHVjdjwYA7X94sf1B0FJrfo8a%2Bgf1TKfCs9roaMU6a1f%2F7rdNLvWhQmdXiYeeCCF8Iqc6hXM78Txr%2FBILqphF7QbNFAyuW9wcoeTVi2apnDk9DsQ2%2Fq8hoI55OpjVVpPV2wFlqXa6WVmOGc7bQv4XWm8C3UZFBuwrnpjiBQKuKOChEi7MG5bjUgcq2XwKG1yU0c0looLzXGA5IdHbrkcmBvaKd1E%2B4lohARWApN8s%2FuIfYQWC4yTfzGUTnE0JqN9XLo8KX631GqdX7pZomeWn%2FYaIYNyyGzXBM06g%2FEF1aUczmvJz8mRhIJrqHAnCVQ6WSN44nlzUoYI4OXxG5XhP9Pu5QDIK0v%2FLMnaAX0EWpPD8lDz570UxzUuKjt9Prouu%2FqrGD7TuVgLI%2FZQEbqCTUQ4Or2zFBzH0P5diE8ot%2FHGcuTtbG7FAUWNXKkeVxOL7Hm8VDcvwMNHChSC2XdNv%2B6MYqLtBTPGUtaDuzedpLwirycUB1vvk4chkI9wLHf1p6zcIJMNPLr8wGOqUBYVIm3R9w3NNH8MG8c46tcsQK3diMibMNgjj6%2FBHZXZmXe3WYa1ENT%2BtaXWififoiWHaIUVZDTBmft1yeO%2FG0FIMDQ5%2BZgrn7oC0%2FHJ69tjHcYwimVzRTY2y8DZq06y6%2Ff%2BtuY1ZFOQ%2BrrospHzKz3oNKZ%2FKgLJqJS7YVAAZRsa1vO55MNas%2Ba2%2Fh%2F9fk1AL9548a0yFdcDLDrt4Cits0kFhapUtK&X-Amz-Signature=f708a42b25586f452b19a0e36f679402212279f05c8d901fbbe7a27fb9a8a663&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN4GRNXA%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDi98%2Bb55KozRdbK9wv58dhLawcE7loTGn7KaZs9QUUwAIgU5hN%2F%2FJN%2B6qFE8GVC24Gj3D8BBBkdm5Lptcmf01kowoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUPo%2Bity%2Fm%2FkS9h7CrcA1XJIgmgo6wWw9W%2BC9SvmEpagc0K7SonNHg%2FRGBJSAcL9esIGILmM7%2FuGoJF3noKkwxj9eBsYrojGlsHhKBzp5BfyRulZqjIQcIRM3Y40HCEtsacIfoZoulHVjdjwYA7X94sf1B0FJrfo8a%2Bgf1TKfCs9roaMU6a1f%2F7rdNLvWhQmdXiYeeCCF8Iqc6hXM78Txr%2FBILqphF7QbNFAyuW9wcoeTVi2apnDk9DsQ2%2Fq8hoI55OpjVVpPV2wFlqXa6WVmOGc7bQv4XWm8C3UZFBuwrnpjiBQKuKOChEi7MG5bjUgcq2XwKG1yU0c0looLzXGA5IdHbrkcmBvaKd1E%2B4lohARWApN8s%2FuIfYQWC4yTfzGUTnE0JqN9XLo8KX631GqdX7pZomeWn%2FYaIYNyyGzXBM06g%2FEF1aUczmvJz8mRhIJrqHAnCVQ6WSN44nlzUoYI4OXxG5XhP9Pu5QDIK0v%2FLMnaAX0EWpPD8lDz570UxzUuKjt9Prouu%2FqrGD7TuVgLI%2FZQEbqCTUQ4Or2zFBzH0P5diE8ot%2FHGcuTtbG7FAUWNXKkeVxOL7Hm8VDcvwMNHChSC2XdNv%2B6MYqLtBTPGUtaDuzedpLwirycUB1vvk4chkI9wLHf1p6zcIJMNPLr8wGOqUBYVIm3R9w3NNH8MG8c46tcsQK3diMibMNgjj6%2FBHZXZmXe3WYa1ENT%2BtaXWififoiWHaIUVZDTBmft1yeO%2FG0FIMDQ5%2BZgrn7oC0%2FHJ69tjHcYwimVzRTY2y8DZq06y6%2Ff%2BtuY1ZFOQ%2BrrospHzKz3oNKZ%2FKgLJqJS7YVAAZRsa1vO55MNas%2Ba2%2Fh%2F9fk1AL9548a0yFdcDLDrt4Cits0kFhapUtK&X-Amz-Signature=722d179d0ab9604c2ce2d5a2801ee784d3cf6476dafc51434e22d5d392a2a46b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









