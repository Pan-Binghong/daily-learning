---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRM36AOE%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA0corgJ%2BxTc35yPA2n6pdgCUXp2jSbrcCcvELl7e64AIgTOPvP5KJ8aQvRJuszJkUn5t8j2FS6u3qGZxKjuhULmEqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoqzyXFMhbf5oxmyCrcA9pRdQUvfOmPg67KL0AGVKxEwo%2B%2FelTpk3%2Foma69HFCeTPOW0goppQ%2F95aTItWrxKhqj5sX%2FBVvYfkB7tU1ZI%2FIllmwFdTus82q%2FlPkb11Dal8ZH0wA%2B98eDx%2FvNqOnjQNv6n0csMELOonAKkGCkn%2BWb%2FeW3NuPdLMRjibmncebkfmy1nCXBNhNdYDwuE6hrkLp3P1eI7glnvFOK%2B5e4kVbPuyEFnbFUoeCz3BBShnxgxrH0JOw3kSD0CGkOTU5RdpvIKzRtm3v6F8J61L8NXsNViYtmhUAnJhopGg2PGTln4dYwUCQAI4NmDpMN9E%2BAxZNQN0ETeTaIXUtS7FtP5mThxoYrnKkTMc%2FojPRLBLs9gltR%2FoU%2BCF4Sg%2Bdr%2FXx25IEkrp8kOJLx0hHMP6GtP1TbfYRE5AepG6o5t6eh2QrHuMhQnor9pHVfwwpQTudmV8F%2BmUap8ISrUfDiKDBmiCLnsvFrF%2FnZDb6oikjXaop8rQunAlMMWcJJkEH8JZp8mtif8xmo4MbKYebYlYefNTPV5330lKsxt%2BhZkMbAiM9FcN4%2Bq8OQ3NY6J5kEd8%2By%2B50DSqPMTv6m9tmaWvFiubd8TLH0f95LmRszbkE2sLfEicTk4yy8dWPBvG4XMIGp%2FMoGOqUB1pcvoZieS6VohEIRkWpqRlcK5pqlCq0tKrLF0JEOEdyjEldR%2F%2FXtwcyopx%2Bad6FHoNIYLjxRXXh55VIenJpZPXyo6jfu61wJvgHjG4KBlYnD8OiC6Z%2BtPuvZgNRcg2ZH5Gx2yoHKQVXyMB3chaYL34xTVDFITPdpt3hgorLULKFo6rQe%2BRiTIRqzB8eugWAjhCDLxrV6hx8LIvPI9vlBjoZPFdPC&X-Amz-Signature=0155bbdebc39a22c5bae4a06395d95c661ec81c07298696b3dae14bbe3114176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRM36AOE%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA0corgJ%2BxTc35yPA2n6pdgCUXp2jSbrcCcvELl7e64AIgTOPvP5KJ8aQvRJuszJkUn5t8j2FS6u3qGZxKjuhULmEqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoqzyXFMhbf5oxmyCrcA9pRdQUvfOmPg67KL0AGVKxEwo%2B%2FelTpk3%2Foma69HFCeTPOW0goppQ%2F95aTItWrxKhqj5sX%2FBVvYfkB7tU1ZI%2FIllmwFdTus82q%2FlPkb11Dal8ZH0wA%2B98eDx%2FvNqOnjQNv6n0csMELOonAKkGCkn%2BWb%2FeW3NuPdLMRjibmncebkfmy1nCXBNhNdYDwuE6hrkLp3P1eI7glnvFOK%2B5e4kVbPuyEFnbFUoeCz3BBShnxgxrH0JOw3kSD0CGkOTU5RdpvIKzRtm3v6F8J61L8NXsNViYtmhUAnJhopGg2PGTln4dYwUCQAI4NmDpMN9E%2BAxZNQN0ETeTaIXUtS7FtP5mThxoYrnKkTMc%2FojPRLBLs9gltR%2FoU%2BCF4Sg%2Bdr%2FXx25IEkrp8kOJLx0hHMP6GtP1TbfYRE5AepG6o5t6eh2QrHuMhQnor9pHVfwwpQTudmV8F%2BmUap8ISrUfDiKDBmiCLnsvFrF%2FnZDb6oikjXaop8rQunAlMMWcJJkEH8JZp8mtif8xmo4MbKYebYlYefNTPV5330lKsxt%2BhZkMbAiM9FcN4%2Bq8OQ3NY6J5kEd8%2By%2B50DSqPMTv6m9tmaWvFiubd8TLH0f95LmRszbkE2sLfEicTk4yy8dWPBvG4XMIGp%2FMoGOqUB1pcvoZieS6VohEIRkWpqRlcK5pqlCq0tKrLF0JEOEdyjEldR%2F%2FXtwcyopx%2Bad6FHoNIYLjxRXXh55VIenJpZPXyo6jfu61wJvgHjG4KBlYnD8OiC6Z%2BtPuvZgNRcg2ZH5Gx2yoHKQVXyMB3chaYL34xTVDFITPdpt3hgorLULKFo6rQe%2BRiTIRqzB8eugWAjhCDLxrV6hx8LIvPI9vlBjoZPFdPC&X-Amz-Signature=cd8ba0a0b3f030314f0b26b53d9754fdd29acc70c7ef78c55709dae7ec4194ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



