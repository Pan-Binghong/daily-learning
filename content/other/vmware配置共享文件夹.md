---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667F4I72P7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDH9A5VZaidmDPtRNLhwEUp1Gi14BDrx0Hia1G5FpmwggIhAPK91HNhth%2FwB5VW9bWrzbZ%2FzKjDUmPy8x3ST480SFErKv8DCHQQABoMNjM3NDIzMTgzODA1Igy%2FwIfFIpOfE7Z5Q0kq3AOkAc%2F1O%2BuRHBvL13xSgcP89un5pfYKxLITGlvw7KoBBVHw5ezRWkJJrGGzSmncYbmQyXvoVfE80DfoIVNlUPYdL1qs2u1JXlh4fQzxF%2B6qIPqx9c4Ai8jnHCQnKXbzn3U6K%2F45n1e32VFNbLY8h81rwfo1DXKFSp28G06lIMEb3CauLIEqdyuwXxPinec9F0hI3pSKQ%2FIbv%2FY6547h2EeBcQ7sIMHnYnszNfwH2lW1xKjtqYuV3wgCjqdR%2BCZB0Gd2KuddDv%2FDHw9jZjiWeZwBOl4yqVtnM0LWPtAjha01Tk0bzCQ%2B%2BS9Q7LV%2F3MU03Uikr4IIqhV4q%2F22ttliKA6rF4vWuw1urbKSWTRzV9q0DOrG%2B9%2BC9VtL7437oiTnEecNARr99pT4ayggp0oH47Vwzl1KWM7aGXOegVBKV43B5LYt4Dp2oDrHMIVVdUGexpIyW%2B6K9ejssAIPkAuD5DN5P1N8XPCwrL1tzgWO3FGSrOS4MThyFaN%2Fn%2BYZJM00QklZeVxCxKmnSuNM0AAxWH%2FgLR15D1iveVaB3uaEqjvOPEOxdKbZO%2FQo0cGw7S93%2BHm9YQAIa%2Bt84kxOyRmxKhqDvI1vbDsvFIFDtNm1Txa54aZW79aSgGzeI6NmTTDY8dnMBjqkAUGS68Xli%2BnJDrB%2FluJ3SZM3uydJP%2BcAx7R3zlQWumEFubOOMA4Ym2%2Be37ZQ1jN4g3PntqOvY9fjC2ACDIumsEOpJA6iJSfdkuduzq8ifUykbxhZItTfhEQN7H98SXCehZSfViyUYa5AtKfurncMnW0uQhPzIBEGelT56VAPc9yGJU7zfMjJWho8LunPlxwq7F1Y6jCdkF5zXXPRsvtZja2C6hq%2B&X-Amz-Signature=94c6a0232dc9c316d397ee437f45eecf8f50d034e1ed2c20ac3aa0ac01689666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



