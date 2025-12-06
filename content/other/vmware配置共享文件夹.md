---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WURI6T2P%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDj%2FLeT9XrlyejYHK%2FgGTVbGMfM88DOSJuwdriovg3NfAiBKdylkYpfVd47eCJW3cVAFr%2B5OlVnS%2BZFyvW7KitfMACr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMkWs6BtYbZ9eGh73uKtwDxvoMNUQ4lImf%2FBhejdxGXqia%2FmLhaWmur8ZsZSb%2FdRdojbdFYtrpHZupeKa0SyE8i1AAbQrHyDaAU2N9sKPiGiE7gkLlQHEL9TTOxCZAdGjmmRA8Aq48x8JHFKckw5ZZJ%2F12wdtolgNU8tLD2IoG0x2wa30qUUFAfK5p7NnrvY5waaHzGNWJO1Tap%2Fx8cg9s038UH7rUvQVfOaTjhKklPhhsY9R7tmi42AW5ZG94RsEi3ye%2BwHg2pgrfMfkVKNE3hvFfkS9oSHvoFSIqAORS0SjA8LDwmUr0LwDCc%2B6Hpuf2ia26Kc86lysmnwwAMnArGVfB0Q3QxeSgobNz8fELAdkqllOZq%2BJSAelxMqvhUX4OgQuNz5sibEhXeH4mFjbs6Q0ihXJl9SO9NE%2Fv%2FB2fjjQd5vGpiqW8oZ01rTeHjY0Gmh%2B%2Bgg%2F4zQ%2FDwbInNBuGZj7eO7zNPBF27XaiBoSTS1BZQNPIEAlBreyPNCbOx1D8DyBiYk3dXNMIvqKGFEPksQ6wN6%2BhLrPfdaun2FTbEFLZpDfdDCqA90Lken1dyI92NYykgGnPLMm3sRSoEfmyNvKdamSU3Cb75SVAWRjDfdm655OFO1yYZC72k6KIzT%2FImDq8ZWrlD3Sb1AcwgqjOyQY6pgFuq795XLb%2F1mkgQ35RQeHdj8%2Fh1RhrXhxPekOox1ktCMCiCGNgDzwdNcJ93T6%2F1zZ49S9dr3y72cQTO965NNFEado8Lia3s%2FL6Jk5ePjtnRxt%2FRdBGRwrwXrtZxrUfI4ZLs8jdnAhiAPIvkAEThLuGzx0cAtwIT8505BxHTolo%2BrytTDlfBNJqkUKfVTwI6gjdDMY5JYKrA7fcJg7OtMP0V7QaM9QK&X-Amz-Signature=6eafa6e406374b6ffa88b4e530e4e3477888a708b2ddcf66ba89e458dd877d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



