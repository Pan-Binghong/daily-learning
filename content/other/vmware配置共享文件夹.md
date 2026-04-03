---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPO7ELXO%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEXERe0w%2FoHk6Y85G0%2BbA8BdQr%2B84ebO5nYSEKaIY75rAiBPBqB%2F%2BYsH1AVcwT%2F%2Bwv%2BS4%2BJMprmXiktkyWSCR9fkMyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM4D2wyecnYFh6lMUTKtwDzvT2i9%2FlDnrBK1JvBngXvhSZibvmn2pPS%2F66w0cZBf0KcEHMz9I3KI3MWXgj9wmRW%2BFJ7E%2Bi13dBsgGRfQjnyHyGH0iwxf4FY6UJVUcu5VmF26MMU7HirNYNUYRRi7ophze4G7QWctAYIbWdxEHFt0ADE6UvDv7kdWGFwSFqstzDsLj%2F4LwDGWtCaBOR%2FZKtmM38DPo%2FcSaIFdhF2JKoP13eZTYcGaUEgBywvgPW1m5%2FE30eRTMSHlqzQl4L7XHy4Ckaj6yf0j%2FgRK0TXR5nxTjJ6DnncOJ%2FSnlLFO9z19OERUalMzrXJMjlIDUKF956ZM4tlPmyGXDCcDnGN9Lm1xm7vjz1XYVKa8II8DQ6srVD07A8kDuWcBH8gWflXBFLtCaHqlqawPaxNEZt8tOCD9J03Wd61nxdyYq6hjXiQbIrFJnSURbSlJJP8EyizSUNDDqtRTYrp1TQ0EU0apewmBwodBu%2BJily5PiWsC0ogmxLMg%2BI%2Fe6XzLX3mPhzsHtYbPnnEgXh%2FQpufc8rjKboL64vsnRvU0rrxZ03rql8em8h2QsgJ547kwH3BMq%2F0GPh72CewN0eVIe8t76krZLyO%2BokxzwTKAW0IEw7XNkuVdtvwRxFLvYRaUWiUHYwr669zgY6pgH2Icnp79OK1pVfQuT7SQlq0PNlfz%2B3QAQSk%2BQkOaRs0w6p2fH%2BpqoW4UfBpSlQfb7wl9uCajdNr%2FZbZ2v07vkMvx94P16GqVuI%2BGFj1bg%2BKx%2FBOzsGnXdsbneDExe6OoyLq5re%2BNmFfiZ5Eh6oLAI2Rr4Owi%2BKCelR7B39%2BsMCNyLYAPdtiul1r9CJEjy%2Bnh%2FaJykygaSMDzxfyEGbMS3ULzqB%2FcZJ&X-Amz-Signature=ac81af6ed0b8e04c8f2ff9b62e90beb90f23a445e8c9b173b1bb1c863f40c10f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```



