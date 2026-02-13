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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KZLFPRT%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDb8K4WA%2Bw3VnAnBlfKPZ4CA1e1PXV3O%2FuBWxmJjcerdAIhAPbFpyeGnqX%2FsRq2JYIt6vqxgM4H8S2T7Gq1UT%2Bjed5KKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySe4tlDh%2Bi2M9dMn4q3AOWcpKHGmfjkMXPl%2B%2BAdBN8m81dlCYiiBn%2F1gdlow0TjU9NkQbK7VCWSt7UydU3vDcuJihKNUwiNDy%2BCVTWstcaoNr%2Fie%2B2FG5R7p7gGAzQ1Cgv7axpLyD0TVEGj0G4pAFwIoth4iG4CpicX7MASPB1svuW1yfC4qPCLlxyXhMWwkIlJcE1AUicclPF0qKo3if3ZB8D%2FoBWR3QSI8WaM6xE9xq1lzIFpVUxxnaAshyli5WPKVXuyQU8n1PIgVx5%2F3dGC0rtHFUZiuWVP5qg6hr9rGUDvlDU%2Fwgxu%2FER31L7Raol1xTaPH1Pq8HDiEW3aJ5C%2FJPbblnpgXnFctYmE0zwLzTRo3K6CLLjw1%2BYzzG1OiOQbFLw82jO963RWP0ADSnh1QfjhmE4X91AuC0ChSRH6wr2qWfWwJhVDMgamoqtpz7oLgZhzCJ%2B5bcHnOYgUm9EKaACWv%2B%2B1ATyCCgosohG6jJLtYhf8eWiUirJ28szXrQMMMM5%2BkK9HoPiRJ7nkTDvyOtyT2YemwSLwD%2F5XM5lp4KnAJYDWJ9iCFXllCHd7IlaF7OA%2F%2FQaqlWz8YwzAQinyFiGbPDrrk8LBbUd6w838%2BcEPjRgcgZ4q7HogzOG3TQH6SjIrB2fjg3KsTDgurrMBjqkAVkYcz1njhWwOn22x5z24t4uFFGTuuLZ%2Fd0LiP7dEDW0rZiVHUhOWE%2BPMzYf7C%2F93zZQFltIvqfIyQLaEymvAILA%2FTtFPaRk2PLHgZte%2FZ6pOK18nQ25rzLnLixGMceP9xNLrEis2gt1wJdWz8LLGwVsTtfLCvZs4t1MFwcNizZdIZLYarswKErfYCvxSPfcNgSuSZ3KDWdCHqmhem%2BdKOL6q4SA&X-Amz-Signature=646afbc8438ea933258780742dd61e4ffcb5c3d692107634bd90e111f823ca59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KZLFPRT%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDb8K4WA%2Bw3VnAnBlfKPZ4CA1e1PXV3O%2FuBWxmJjcerdAIhAPbFpyeGnqX%2FsRq2JYIt6vqxgM4H8S2T7Gq1UT%2Bjed5KKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySe4tlDh%2Bi2M9dMn4q3AOWcpKHGmfjkMXPl%2B%2BAdBN8m81dlCYiiBn%2F1gdlow0TjU9NkQbK7VCWSt7UydU3vDcuJihKNUwiNDy%2BCVTWstcaoNr%2Fie%2B2FG5R7p7gGAzQ1Cgv7axpLyD0TVEGj0G4pAFwIoth4iG4CpicX7MASPB1svuW1yfC4qPCLlxyXhMWwkIlJcE1AUicclPF0qKo3if3ZB8D%2FoBWR3QSI8WaM6xE9xq1lzIFpVUxxnaAshyli5WPKVXuyQU8n1PIgVx5%2F3dGC0rtHFUZiuWVP5qg6hr9rGUDvlDU%2Fwgxu%2FER31L7Raol1xTaPH1Pq8HDiEW3aJ5C%2FJPbblnpgXnFctYmE0zwLzTRo3K6CLLjw1%2BYzzG1OiOQbFLw82jO963RWP0ADSnh1QfjhmE4X91AuC0ChSRH6wr2qWfWwJhVDMgamoqtpz7oLgZhzCJ%2B5bcHnOYgUm9EKaACWv%2B%2B1ATyCCgosohG6jJLtYhf8eWiUirJ28szXrQMMMM5%2BkK9HoPiRJ7nkTDvyOtyT2YemwSLwD%2F5XM5lp4KnAJYDWJ9iCFXllCHd7IlaF7OA%2F%2FQaqlWz8YwzAQinyFiGbPDrrk8LBbUd6w838%2BcEPjRgcgZ4q7HogzOG3TQH6SjIrB2fjg3KsTDgurrMBjqkAVkYcz1njhWwOn22x5z24t4uFFGTuuLZ%2Fd0LiP7dEDW0rZiVHUhOWE%2BPMzYf7C%2F93zZQFltIvqfIyQLaEymvAILA%2FTtFPaRk2PLHgZte%2FZ6pOK18nQ25rzLnLixGMceP9xNLrEis2gt1wJdWz8LLGwVsTtfLCvZs4t1MFwcNizZdIZLYarswKErfYCvxSPfcNgSuSZ3KDWdCHqmhem%2BdKOL6q4SA&X-Amz-Signature=5d8835a69b2557679d27fe117e07ae3c435f75ee33f28eeaaf79fa0a84cf7fa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









