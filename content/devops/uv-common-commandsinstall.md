---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBEWDSC%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQD5fbKBJMORIQOTCVYRV6OcHEnYEb%2B41%2BPPVU7z1R3psAIhAPixPG0BcATwFzemgjXTIPpcQ6p8QwrVHo7OTGaMasTGKv8DCEUQABoMNjM3NDIzMTgzODA1IgzjbiZMM4k4IrpQiZsq3APtOyJfzivGfRg4JMEsuGsZAHt1%2FQekMjzO6HehF6OG%2Ba0oi4RFhcAl9BrjHR03TWQmloztyU4jlv%2BNlyoxj%2Bs7oQBzgmQuET%2BlI9p%2F6iaNTUpqQsKlTBpUQOEIez7CIkwndznuShsUph2xyFZ0Niw3dHEnLchQfv4wCvu1HVKrip4NicVd5BvNYMeKbV8q42Y9y%2F1zbuZiRvGI5zVdxe9FSH%2BW%2B%2Bo7fE77ygSOivxPjSrviMRodWkjlNdF969vDorMdLDsdNqyI8cHMMr2yzHs9bziSbPjmZDcuQwzYo74NqJPFRUbzXTCKC%2F%2ByDWqZ3TvikIH4GrtiJWjC3yLoacACgxilZtG9CpNcCeMMF%2FEnqDMyX%2BZpLuuwHjd2LadyZ4Gqu%2Frd7sdmSthyjAlfeqanxPBWlwtLO0EyGktlzP1op4FRmqEJp08IQfulbwokOtANvaZCeKvqUQQ5DiArLQQWueJvNrQuf1yXueTvKG6elkskir3fPmE6cI4gpZbb2dagRPPPPCTcJplGBYL9N%2F8FeI1myy2CIBuybB1xCgmYRx9DtBzrK1pR4t4Xe3o9xUB6GmtcZ1rHBhG5Jae7%2BWro10tiD9tdBe9VyiTIjmGqzAvIe5r3yz%2BvGUjqzCtv8%2FMBjqkAbBSf6AwMAIKOnVvUMPoSBaAjS76QATRC1lcHivtLMfoy78FPzwmFSKDl0R59E34RP%2BYvNcak7hnHIqZ2A7G%2FsRlpnEZ47gjfOV0wXUBppL4Yf805fdQJrJHBVCJbbrtrfHDwYS14YNwRZluB0w5bqspB6wDTG8wU3ovntxfeBfCUSuSQd5Snt7M%2FISJhWNd4ws7sZd2TJ5oq60iBiYALnoBmf%2BM&X-Amz-Signature=50e459149d7063a60947d2183257b43680891b26fcb09086c40955674bdaf883&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBEWDSC%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQD5fbKBJMORIQOTCVYRV6OcHEnYEb%2B41%2BPPVU7z1R3psAIhAPixPG0BcATwFzemgjXTIPpcQ6p8QwrVHo7OTGaMasTGKv8DCEUQABoMNjM3NDIzMTgzODA1IgzjbiZMM4k4IrpQiZsq3APtOyJfzivGfRg4JMEsuGsZAHt1%2FQekMjzO6HehF6OG%2Ba0oi4RFhcAl9BrjHR03TWQmloztyU4jlv%2BNlyoxj%2Bs7oQBzgmQuET%2BlI9p%2F6iaNTUpqQsKlTBpUQOEIez7CIkwndznuShsUph2xyFZ0Niw3dHEnLchQfv4wCvu1HVKrip4NicVd5BvNYMeKbV8q42Y9y%2F1zbuZiRvGI5zVdxe9FSH%2BW%2B%2Bo7fE77ygSOivxPjSrviMRodWkjlNdF969vDorMdLDsdNqyI8cHMMr2yzHs9bziSbPjmZDcuQwzYo74NqJPFRUbzXTCKC%2F%2ByDWqZ3TvikIH4GrtiJWjC3yLoacACgxilZtG9CpNcCeMMF%2FEnqDMyX%2BZpLuuwHjd2LadyZ4Gqu%2Frd7sdmSthyjAlfeqanxPBWlwtLO0EyGktlzP1op4FRmqEJp08IQfulbwokOtANvaZCeKvqUQQ5DiArLQQWueJvNrQuf1yXueTvKG6elkskir3fPmE6cI4gpZbb2dagRPPPPCTcJplGBYL9N%2F8FeI1myy2CIBuybB1xCgmYRx9DtBzrK1pR4t4Xe3o9xUB6GmtcZ1rHBhG5Jae7%2BWro10tiD9tdBe9VyiTIjmGqzAvIe5r3yz%2BvGUjqzCtv8%2FMBjqkAbBSf6AwMAIKOnVvUMPoSBaAjS76QATRC1lcHivtLMfoy78FPzwmFSKDl0R59E34RP%2BYvNcak7hnHIqZ2A7G%2FsRlpnEZ47gjfOV0wXUBppL4Yf805fdQJrJHBVCJbbrtrfHDwYS14YNwRZluB0w5bqspB6wDTG8wU3ovntxfeBfCUSuSQd5Snt7M%2FISJhWNd4ws7sZd2TJ5oq60iBiYALnoBmf%2BM&X-Amz-Signature=6b1ee11534c2732ae6143d548e5ebd8916bd557ea49e04669e1189bf18467bf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYBEWDSC%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQD5fbKBJMORIQOTCVYRV6OcHEnYEb%2B41%2BPPVU7z1R3psAIhAPixPG0BcATwFzemgjXTIPpcQ6p8QwrVHo7OTGaMasTGKv8DCEUQABoMNjM3NDIzMTgzODA1IgzjbiZMM4k4IrpQiZsq3APtOyJfzivGfRg4JMEsuGsZAHt1%2FQekMjzO6HehF6OG%2Ba0oi4RFhcAl9BrjHR03TWQmloztyU4jlv%2BNlyoxj%2Bs7oQBzgmQuET%2BlI9p%2F6iaNTUpqQsKlTBpUQOEIez7CIkwndznuShsUph2xyFZ0Niw3dHEnLchQfv4wCvu1HVKrip4NicVd5BvNYMeKbV8q42Y9y%2F1zbuZiRvGI5zVdxe9FSH%2BW%2B%2Bo7fE77ygSOivxPjSrviMRodWkjlNdF969vDorMdLDsdNqyI8cHMMr2yzHs9bziSbPjmZDcuQwzYo74NqJPFRUbzXTCKC%2F%2ByDWqZ3TvikIH4GrtiJWjC3yLoacACgxilZtG9CpNcCeMMF%2FEnqDMyX%2BZpLuuwHjd2LadyZ4Gqu%2Frd7sdmSthyjAlfeqanxPBWlwtLO0EyGktlzP1op4FRmqEJp08IQfulbwokOtANvaZCeKvqUQQ5DiArLQQWueJvNrQuf1yXueTvKG6elkskir3fPmE6cI4gpZbb2dagRPPPPCTcJplGBYL9N%2F8FeI1myy2CIBuybB1xCgmYRx9DtBzrK1pR4t4Xe3o9xUB6GmtcZ1rHBhG5Jae7%2BWro10tiD9tdBe9VyiTIjmGqzAvIe5r3yz%2BvGUjqzCtv8%2FMBjqkAbBSf6AwMAIKOnVvUMPoSBaAjS76QATRC1lcHivtLMfoy78FPzwmFSKDl0R59E34RP%2BYvNcak7hnHIqZ2A7G%2FsRlpnEZ47gjfOV0wXUBppL4Yf805fdQJrJHBVCJbbrtrfHDwYS14YNwRZluB0w5bqspB6wDTG8wU3ovntxfeBfCUSuSQd5Snt7M%2FISJhWNd4ws7sZd2TJ5oq60iBiYALnoBmf%2BM&X-Amz-Signature=5ce6688e33add741bb71b85bcf1f077773306c7e09f25137c34329b74cc6d746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

