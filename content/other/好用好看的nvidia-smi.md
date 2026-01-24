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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XHJOHWP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDW5mGuLdA3QSKeCMusi5IA5gZNR2Wyh%2BLhWL2O74wjdgIhAN9OxNgFXFFhAyAj4ho8XyXol7gthBpW4bKL5%2FuRrKtLKv8DCAMQABoMNjM3NDIzMTgzODA1IgwEAUtpRgW8sMqsItMq3ANn8hTATcp1oMwAH%2F9lCyRqZOMlJVJrNE26W3wyDWTUBHu3WzuDTDpvAjT9d0rwJvfw6HFqKCpwAhb%2FoYi%2FbcMNtItqp%2Fx70jhMJerxfkbqVbh1uFnTyqAY26VXxlR7HWdvINXSeA9nV%2FImkNPnClHTpfCZqyWQp%2B2q6icx9866Tdwax%2BC7z78zJt%2Fn9SUuwG5WH5YZz6EaEPoLF65WAXLScC2iOPwQKZSSlkcRhECY5jRwrjrw1f1kNvJIv0N1TO3CIt9Tnej9GCl0BnQ1rsIxqtL%2FDx%2BJY4mOHhoQzLhoyAYOc0s4Z%2FHnYnscvhflUtptxGu7xFywchVLO%2BxurawhJ8yxhxICIwAmHj2vEFhvcaDoDu241YZUsNPAiq%2F9WtNjt62xR8Lb3nXufI2WKBG8ZZVkiaA4nUhXG6kQzeJ36iDoW9egnIOeFmu5B25TBp5XGT8LVMGEpXwd%2Bun%2F7SUwh8h9dG36zFiWFarm04ug5r%2F0jIV6TksbKcvXjr8ceIIZlUwb3WUZ6FtIs1heda2skISwMsYL%2Bpj%2BcmQBxyO4063EIca9EeWJX8rVRbVY7DE4RBJlKyQHbIOyRVVI5nZWSsbp%2FSS2GWH9GvFuIV9ByJw1m5txsnyHvv2UHjCfztDLBjqkAWgomzTvUxLdCN627WkDvrRJkUvHS1625I6X8sJPxJ%2F4HPOJPtwscbiANsl5S1%2FbG2af3vzcvg73C146T7YenjkFhnqtavY96htiztP2BKGKoqMczIrSQVMp24jbRr0Aqq%2FuOLWgDagRH8WTn6joZNWaBV1ihtuhDVZkYjNuEmsfqDDBbTiGmBt6QJCMUmg62FkhkyfOJkS2r7LlXDhgfWOLpV9Z&X-Amz-Signature=e0d61ac7f3989bde9b15bea59409ec09760a04d6aaf68b8db9e99792c4908410&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XHJOHWP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDW5mGuLdA3QSKeCMusi5IA5gZNR2Wyh%2BLhWL2O74wjdgIhAN9OxNgFXFFhAyAj4ho8XyXol7gthBpW4bKL5%2FuRrKtLKv8DCAMQABoMNjM3NDIzMTgzODA1IgwEAUtpRgW8sMqsItMq3ANn8hTATcp1oMwAH%2F9lCyRqZOMlJVJrNE26W3wyDWTUBHu3WzuDTDpvAjT9d0rwJvfw6HFqKCpwAhb%2FoYi%2FbcMNtItqp%2Fx70jhMJerxfkbqVbh1uFnTyqAY26VXxlR7HWdvINXSeA9nV%2FImkNPnClHTpfCZqyWQp%2B2q6icx9866Tdwax%2BC7z78zJt%2Fn9SUuwG5WH5YZz6EaEPoLF65WAXLScC2iOPwQKZSSlkcRhECY5jRwrjrw1f1kNvJIv0N1TO3CIt9Tnej9GCl0BnQ1rsIxqtL%2FDx%2BJY4mOHhoQzLhoyAYOc0s4Z%2FHnYnscvhflUtptxGu7xFywchVLO%2BxurawhJ8yxhxICIwAmHj2vEFhvcaDoDu241YZUsNPAiq%2F9WtNjt62xR8Lb3nXufI2WKBG8ZZVkiaA4nUhXG6kQzeJ36iDoW9egnIOeFmu5B25TBp5XGT8LVMGEpXwd%2Bun%2F7SUwh8h9dG36zFiWFarm04ug5r%2F0jIV6TksbKcvXjr8ceIIZlUwb3WUZ6FtIs1heda2skISwMsYL%2Bpj%2BcmQBxyO4063EIca9EeWJX8rVRbVY7DE4RBJlKyQHbIOyRVVI5nZWSsbp%2FSS2GWH9GvFuIV9ByJw1m5txsnyHvv2UHjCfztDLBjqkAWgomzTvUxLdCN627WkDvrRJkUvHS1625I6X8sJPxJ%2F4HPOJPtwscbiANsl5S1%2FbG2af3vzcvg73C146T7YenjkFhnqtavY96htiztP2BKGKoqMczIrSQVMp24jbRr0Aqq%2FuOLWgDagRH8WTn6joZNWaBV1ihtuhDVZkYjNuEmsfqDDBbTiGmBt6QJCMUmg62FkhkyfOJkS2r7LlXDhgfWOLpV9Z&X-Amz-Signature=2f35379b37a2da38c045459ed89ebb25306ecbc09a0cdc07f3d06f3500437820&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









