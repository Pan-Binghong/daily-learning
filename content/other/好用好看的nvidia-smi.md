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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2DXW3GT%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQCVHoloExSxsnUPZKLNU%2FxdeDUxB7NU8iMqBVhC4YNrtgIgFxs513S4oubK8fydRnDDGWFjNbxJp%2BVQ4rMhjDeXjTsq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDEUA%2FqGO4XqwYsQMZircA0nhRo3TWx4xc8FMh0OEmhFj%2B5Z3xhR63pjE1CVUXl71B7mzPTo5bVTytr6oVCw19klHL1YCXpWwFX457os2HDVBWtCrjBcHdQwJF%2BvWshbpej3fFdiryKyJ1s6Z1cPaswF9GGxqG8YvwM6i7DKZWEydk9z9qrex6CmWDCCH0qAdf9gulWROQCXF1aSAdWa40dkjgU5tz0hVvn3hsTH8jRT4HnWN0FCNpyW0lbC9O6k4qC492gCOv5MZ7rD8DLIq0xugGljc8TRlARy9HKTZaPxqvyAAICllP%2F4Bbxw0G8Y4fKQ860ZXouSKjBXJlvJ3CelNu1W8pCJx0w8UKxh44zlcC2UN4bXMsiIKI1qZ%2FGU8Mgp1EeDELJvi96xSRgpazfibiuZqe3yHu2Gc%2BkWjHal1DcIwJR9dmP5dbJNlg%2BY0SgIPY8vsRKTV9gJIneBQYeCISqNO9PQpvOMJ4RVrulqWyOyMvl6CeHfo8%2BUrZm7FHVjIqltHQf1hXcTZ9Ng8BQdKuFXjA2lmp3ohVBd1bGESVIMK7yC5x1rF3%2BFcOGubc99Lkk9gMCk%2FHC2mzudYg4VC8TZ6bXKbBCWckyylt0FFUeoi%2BMyUo0fnmLRmA2LHA1FtWawDEnEg1CQRMJD9p8oGOqUBHD7cqBan%2BcCNuAMm9YhA4JiZgZRBADQWccEdd6LEethHRM42lBxEdd4MQnWoKloG5Y%2FmNxmrL0G%2Bs%2FA1Whfkh1XcaITDch0AfNQRHvytZ8mvQTRQK9x51%2Fa78YOqGJ%2FAFR7xUqQUhcr6WUsb1RFnLcOZ9Cj8ov0RGkddGTZmgPzIXy8%2BsvAIKO4Nrh0qeXiP1KBN95%2BXg02Na3kB8UDcwkabaPvB&X-Amz-Signature=3d0eeb567f061495a3a781454de057b7660ee49047cb340486da6d873192a89e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2DXW3GT%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQCVHoloExSxsnUPZKLNU%2FxdeDUxB7NU8iMqBVhC4YNrtgIgFxs513S4oubK8fydRnDDGWFjNbxJp%2BVQ4rMhjDeXjTsq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDEUA%2FqGO4XqwYsQMZircA0nhRo3TWx4xc8FMh0OEmhFj%2B5Z3xhR63pjE1CVUXl71B7mzPTo5bVTytr6oVCw19klHL1YCXpWwFX457os2HDVBWtCrjBcHdQwJF%2BvWshbpej3fFdiryKyJ1s6Z1cPaswF9GGxqG8YvwM6i7DKZWEydk9z9qrex6CmWDCCH0qAdf9gulWROQCXF1aSAdWa40dkjgU5tz0hVvn3hsTH8jRT4HnWN0FCNpyW0lbC9O6k4qC492gCOv5MZ7rD8DLIq0xugGljc8TRlARy9HKTZaPxqvyAAICllP%2F4Bbxw0G8Y4fKQ860ZXouSKjBXJlvJ3CelNu1W8pCJx0w8UKxh44zlcC2UN4bXMsiIKI1qZ%2FGU8Mgp1EeDELJvi96xSRgpazfibiuZqe3yHu2Gc%2BkWjHal1DcIwJR9dmP5dbJNlg%2BY0SgIPY8vsRKTV9gJIneBQYeCISqNO9PQpvOMJ4RVrulqWyOyMvl6CeHfo8%2BUrZm7FHVjIqltHQf1hXcTZ9Ng8BQdKuFXjA2lmp3ohVBd1bGESVIMK7yC5x1rF3%2BFcOGubc99Lkk9gMCk%2FHC2mzudYg4VC8TZ6bXKbBCWckyylt0FFUeoi%2BMyUo0fnmLRmA2LHA1FtWawDEnEg1CQRMJD9p8oGOqUBHD7cqBan%2BcCNuAMm9YhA4JiZgZRBADQWccEdd6LEethHRM42lBxEdd4MQnWoKloG5Y%2FmNxmrL0G%2Bs%2FA1Whfkh1XcaITDch0AfNQRHvytZ8mvQTRQK9x51%2Fa78YOqGJ%2FAFR7xUqQUhcr6WUsb1RFnLcOZ9Cj8ov0RGkddGTZmgPzIXy8%2BsvAIKO4Nrh0qeXiP1KBN95%2BXg02Na3kB8UDcwkabaPvB&X-Amz-Signature=599b5f32629b4fa122483c9a5f9658b00da93b1e4c8051910718fd3f4f9c4adf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









