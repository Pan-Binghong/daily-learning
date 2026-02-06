---
title: 查看本机的SSH公钥&绑定到Github
date: '2026-02-03T02:14:00.000Z'
lastmod: '2026-02-03T03:32:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 配置Git使用SSH方式, 本文环境：windows + powershell + git guissh 

---

## 查看

```json
ls  ~/.ssh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QU2RLLV%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIEwg7WyNSj8p4L8DmWP7hUkV7kaMqpOO7vJcZv7CuB5TAiA8E2flNCx70glVGcvLqU8m4M6PWJgwznhJELlkKpE1oCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMWjidBXlvCzP2QyACKtwD1KDyj2fuzJ%2BWmGxG7tA0jTbLp8f7u44opvIZPA%2BHyPn2ky%2F%2B%2FGJVDiyVeazwIcWCQYHqdLn8%2B3jryI3LQXNDey6YIb3406qOIBjuiYh9BIepBeXpt4RFbn17PcBEqHuB529IotPETMViNnNl3d%2BCC5J%2BpZhIrQxzdsiewRaewKtLPmNig7PX9%2FUfrx2IrbTzxUQzfvgtnduu9KxqMtbCPIIdTyoYFrKDWoUSFPqJdILExKj17PFJuYZAnstjrZwVAX51UClKuCOsG%2FkI0WvtdmYoSrZrZqpl0d7saVI8ixxKwpoYdk7Tmc2SGIing%2Bia%2FoyTWV8DYWTikb%2FUYmtim9wYHLvL31W3Z1Qz0US%2B0SCRk%2FtR0%2FpPRRsxeaqDDQjqS3mI5XwWMOzkgNlj3gxYKtWxerK%2BZgd2HvepdogN2DdGdbsx8kNrWudbvVFjxqm47Pram7qON8t79MD%2Bsbbb1kXvBR%2FIqD9K4dZ2WPBH%2B4%2BCEmYmC1QIQdD%2Ba6qe4W0GGD1dwTbOJMvf7UTqVRLDYKEdb5x0zYbfgAFVALyxoscR5PIGt6bzvzgp5YGEpdyXlizY84HHBJI5cTVBbbrR852i%2BVBLjRUBK84oyrJlIDIQk9yP40L%2Fmn7EdeYw07uVzAY6pgHvM6F3QwQ%2BTmQSfWmytODESeBla%2Bm2sVIPm94hTQxl8JvJ0i63alF9KqtFHdRZkjcuem8Hbd9DTirLXotnOLmlh5v76o4%2BmIEm4cxUXTBkztTY49N8VR%2F%2B4GkWhQc76xlvGskbCaGdkvSqoWIm9elUBFgFCBHShrrDg3f%2F%2BflBuWkOq93E%2B5t%2BUcOTgkSB4tmlW4R7iKaXKHW%2FWrkbQSn7HW8irAVu&X-Amz-Signature=a19f672ed9518b239a2c4b5c01e6d06c2994db6cac3449cdc853f3ade5b0df16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 创建

```json
# 推荐使用Ed25519算法
ssh-keygen -t ed25519 -C "your_email@example.com"

# 备选
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

## 配置

```json
# 将ssh密钥添加到ssh-agent
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add .\.ssh\id_ed25519

# 查看是否添加成功
ssh-add -l
```

### 安装gh（github cli）

```json
# 打开powershell
choco install gh

# 登录
gh auth login
```

## 打开GIT/提交

```json
gh ssh-key add ~/.ssh/id_ed25519.pub --title "公司主机"
```

## 验证

```json
ssh -T git@github.com
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QU2RLLV%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIEwg7WyNSj8p4L8DmWP7hUkV7kaMqpOO7vJcZv7CuB5TAiA8E2flNCx70glVGcvLqU8m4M6PWJgwznhJELlkKpE1oCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMWjidBXlvCzP2QyACKtwD1KDyj2fuzJ%2BWmGxG7tA0jTbLp8f7u44opvIZPA%2BHyPn2ky%2F%2B%2FGJVDiyVeazwIcWCQYHqdLn8%2B3jryI3LQXNDey6YIb3406qOIBjuiYh9BIepBeXpt4RFbn17PcBEqHuB529IotPETMViNnNl3d%2BCC5J%2BpZhIrQxzdsiewRaewKtLPmNig7PX9%2FUfrx2IrbTzxUQzfvgtnduu9KxqMtbCPIIdTyoYFrKDWoUSFPqJdILExKj17PFJuYZAnstjrZwVAX51UClKuCOsG%2FkI0WvtdmYoSrZrZqpl0d7saVI8ixxKwpoYdk7Tmc2SGIing%2Bia%2FoyTWV8DYWTikb%2FUYmtim9wYHLvL31W3Z1Qz0US%2B0SCRk%2FtR0%2FpPRRsxeaqDDQjqS3mI5XwWMOzkgNlj3gxYKtWxerK%2BZgd2HvepdogN2DdGdbsx8kNrWudbvVFjxqm47Pram7qON8t79MD%2Bsbbb1kXvBR%2FIqD9K4dZ2WPBH%2B4%2BCEmYmC1QIQdD%2Ba6qe4W0GGD1dwTbOJMvf7UTqVRLDYKEdb5x0zYbfgAFVALyxoscR5PIGt6bzvzgp5YGEpdyXlizY84HHBJI5cTVBbbrR852i%2BVBLjRUBK84oyrJlIDIQk9yP40L%2Fmn7EdeYw07uVzAY6pgHvM6F3QwQ%2BTmQSfWmytODESeBla%2Bm2sVIPm94hTQxl8JvJ0i63alF9KqtFHdRZkjcuem8Hbd9DTirLXotnOLmlh5v76o4%2BmIEm4cxUXTBkztTY49N8VR%2F%2B4GkWhQc76xlvGskbCaGdkvSqoWIm9elUBFgFCBHShrrDg3f%2F%2BflBuWkOq93E%2B5t%2BUcOTgkSB4tmlW4R7iKaXKHW%2FWrkbQSn7HW8irAVu&X-Amz-Signature=594db2b095b428320eafc56220fde07b1bde4fdd78e568fc8a918272ef158799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

