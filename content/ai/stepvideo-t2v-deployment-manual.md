---
title: Stepvideo-t2v Deployment Manual
date: '2025-04-22T00:43:00.000Z'
lastmod: '2025-04-23T02:58:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 记录部署阶跃星辰发布的stepvideo-ti2v (图片生成视频)模型，全流程。含踩坑记录，以及webui展示代码。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD3JHJLC%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLzTTRA9Er8kPv6perCpmj95M3GwwGd1hMn32h4Gm8JAiEAr27ofUqUUGq8Q02lJJXS7XuL7Zt4tu1hp5oRt%2BBUIS0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFADPEpu4vHoghWPvCrcA0wiRJtOLpLrrrux2kw91fq9ajFFxc6ZYjCxtv8kZ1gtRgZMILJwSZeBYvFUBB%2FE47K4pdoj0ur%2BVMri2HUKl9jsu4NFr6nLvipvRs1fJre7s1CdrQOWt2GQyI9BQ7n5gv5upHlU0pWPpx5sppGPJe1kqlw7ZEtkmaRQXRv3PdUVZPz4xP%2Fa8tak92VByxBs2KoUOryKMIfuBOvboW46CP5KnjTCp6iSgyp48pkSS6jmII%2FBHDsmVkUc%2BVYfUrhfZG2oLJlB69f04onH0vE5bfd%2Bfj9XsuS8kXv2DyXuK5jMJeymH%2FxLSzm%2FAaarZOI5CQR1UUVUdLXKQImh5w74gpdHMdLPoDUdv34%2Frh6pim2kVZ5c%2Bhar0SdCg1f93kyqIlHz6UdZ81dKFdFAhfwNngyGBntyRFoW7UNsaaGRO36addE3OzIB9arOp05gLnyw8TLMszLqHbOYXilwaQ2y3SKEKKEbEAi8OuulaUz9pSNoOOYij7K2eGO9pWTXImbGxawfQvAzo%2BZSbGqDNGYRolX%2BMxJ6eFWnEkE0cMS2623B0AcGwPqminqtCRnDo3d6miBboonwSOrYdSOOacU8LUe6qTCJ1LVObtqVn7rDoLtLWOGdNE4GIZ2bYJp8MLPEqswGOqUBlKGZ%2FPKOxdr4c%2Bgdtoj0UGG9Hdy3ADyRg1JWQxMIeeAA7mqvu6Fd5fimhKppL%2F3%2Bsw6b6L1F%2F4Afdem8mX%2FB%2F5IzIPDPyA9mjYX4WjhtMmY3qK41a13v0fafi61otjroKQVzeTdUDq0goMy8O3x1TK9YU6QYzuWWZC42qJjVbUfkEfX6MPjtcCFKsO6drfSBTMcg76OaNfkdANM6W1qZuujZu1cO&X-Amz-Signature=aa1ecf5d294dbb65e8e3cae40ed315b59bd4d502b7395f95943678ebcc79f094&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 环境安装

## 1.1 拉取Docker镜像

```bash
docker pull nvcr.io/nvidia/pytorch:23.10-py3
docker run -dit --gpus all --privileged  --ipc=host --net host --name=stepfun--shm-size=100g --ulimit memlock=-1 -v /data/:/data/ 镜像ID  /bin/bash
docker exec -it stepfun /bin/bash
```

推荐拉取该镜像，在此镜像基础上进行模型的安装运行。忽略docker的安装。

## 1.2安装StepVideo环境

演示所用的webui基于streamlit库进行开发，其中的numpy版本与stepvideo有冲突，首先安装streamlit。

```bash
pip install streamlit
```

```bash
git clone https://github.com/stepfun-ai/Step-Video-TI2V.git
cd StepFun-StepVideo
pip install -e .
```

opencv报错：如遇到 xxx 报错，利用opencv-fixer工具进行清理更新

```bash
pip install opencv-fixer==0.2.5
python -c "from opencv_fixer import AutoFix; AutoFix()"
```

<details><summary>requirements.txt</summary>

</details>

---

# 2. 模型下载

```bash
mkdir stepfun
cd stepfun
pip install modelscope
modelscope download --model stepfun-ai/stepvideo-ti2v  --local_dir .
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD3JHJLC%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLzTTRA9Er8kPv6perCpmj95M3GwwGd1hMn32h4Gm8JAiEAr27ofUqUUGq8Q02lJJXS7XuL7Zt4tu1hp5oRt%2BBUIS0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFADPEpu4vHoghWPvCrcA0wiRJtOLpLrrrux2kw91fq9ajFFxc6ZYjCxtv8kZ1gtRgZMILJwSZeBYvFUBB%2FE47K4pdoj0ur%2BVMri2HUKl9jsu4NFr6nLvipvRs1fJre7s1CdrQOWt2GQyI9BQ7n5gv5upHlU0pWPpx5sppGPJe1kqlw7ZEtkmaRQXRv3PdUVZPz4xP%2Fa8tak92VByxBs2KoUOryKMIfuBOvboW46CP5KnjTCp6iSgyp48pkSS6jmII%2FBHDsmVkUc%2BVYfUrhfZG2oLJlB69f04onH0vE5bfd%2Bfj9XsuS8kXv2DyXuK5jMJeymH%2FxLSzm%2FAaarZOI5CQR1UUVUdLXKQImh5w74gpdHMdLPoDUdv34%2Frh6pim2kVZ5c%2Bhar0SdCg1f93kyqIlHz6UdZ81dKFdFAhfwNngyGBntyRFoW7UNsaaGRO36addE3OzIB9arOp05gLnyw8TLMszLqHbOYXilwaQ2y3SKEKKEbEAi8OuulaUz9pSNoOOYij7K2eGO9pWTXImbGxawfQvAzo%2BZSbGqDNGYRolX%2BMxJ6eFWnEkE0cMS2623B0AcGwPqminqtCRnDo3d6miBboonwSOrYdSOOacU8LUe6qTCJ1LVObtqVn7rDoLtLWOGdNE4GIZ2bYJp8MLPEqswGOqUBlKGZ%2FPKOxdr4c%2Bgdtoj0UGG9Hdy3ADyRg1JWQxMIeeAA7mqvu6Fd5fimhKppL%2F3%2Bsw6b6L1F%2F4Afdem8mX%2FB%2F5IzIPDPyA9mjYX4WjhtMmY3qK41a13v0fafi61otjroKQVzeTdUDq0goMy8O3x1TK9YU6QYzuWWZC42qJjVbUfkEfX6MPjtcCFKsO6drfSBTMcg76OaNfkdANM6W1qZuujZu1cO&X-Amz-Signature=a38717e486fd250d53b027c307dc091243c169971909d9fe065a25a6bfb1b1a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 推理脚本

## 3.1 启动API服务

```bash
python api/call_remote_server.py --model_dir /data/stepfun & 
```

运行此操作后，可观察到服务器内的最后一张卡，有大约45%的显存占用。

## 3.2 图生视频

> 💡 本次测试环境在H800 * 8的裸金属服务器内，目前模型存在显存过大的问题。如果使用H20（单卡显存141G），可取消标红的配置参数。

```bash
# 优化显存使用，减少碎片
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

```bash
torchrun --nproc_per_node 4 run_parallel.py \
    --model_dir /data/stepfun \ ## 权重路劲
    --vae_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --caption_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --ulysses_degree  4 \ ## 4卡运行
    --prompt "男孩快速长大" \ 
    --first_image_path ./assets/demo.png \ ## 图片路径
    --infer_steps 50 \ ## 视频降噪参数
    --save_path ./results \ ## 生成视频保存路径
    --cfg_scale 9.0 \ ## 内置提示词关联度参数，详见config.py
    --motion_score 5.0 \ ## 帧间变化参数
    --time_shift 12.573 \ ## 降噪相关参数
    --use-cpu-offload ## 使用内存加载权重
```

---

# 4. WebUI推理

## 4.1 代码

### 将以下代码放入StepFun-StepVideo文件夹内

---

## 4.2 运行服务

streamlit run webui.py —server.port 8080

---

## 4.3 页面效果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD3JHJLC%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLzTTRA9Er8kPv6perCpmj95M3GwwGd1hMn32h4Gm8JAiEAr27ofUqUUGq8Q02lJJXS7XuL7Zt4tu1hp5oRt%2BBUIS0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFADPEpu4vHoghWPvCrcA0wiRJtOLpLrrrux2kw91fq9ajFFxc6ZYjCxtv8kZ1gtRgZMILJwSZeBYvFUBB%2FE47K4pdoj0ur%2BVMri2HUKl9jsu4NFr6nLvipvRs1fJre7s1CdrQOWt2GQyI9BQ7n5gv5upHlU0pWPpx5sppGPJe1kqlw7ZEtkmaRQXRv3PdUVZPz4xP%2Fa8tak92VByxBs2KoUOryKMIfuBOvboW46CP5KnjTCp6iSgyp48pkSS6jmII%2FBHDsmVkUc%2BVYfUrhfZG2oLJlB69f04onH0vE5bfd%2Bfj9XsuS8kXv2DyXuK5jMJeymH%2FxLSzm%2FAaarZOI5CQR1UUVUdLXKQImh5w74gpdHMdLPoDUdv34%2Frh6pim2kVZ5c%2Bhar0SdCg1f93kyqIlHz6UdZ81dKFdFAhfwNngyGBntyRFoW7UNsaaGRO36addE3OzIB9arOp05gLnyw8TLMszLqHbOYXilwaQ2y3SKEKKEbEAi8OuulaUz9pSNoOOYij7K2eGO9pWTXImbGxawfQvAzo%2BZSbGqDNGYRolX%2BMxJ6eFWnEkE0cMS2623B0AcGwPqminqtCRnDo3d6miBboonwSOrYdSOOacU8LUe6qTCJ1LVObtqVn7rDoLtLWOGdNE4GIZ2bYJp8MLPEqswGOqUBlKGZ%2FPKOxdr4c%2Bgdtoj0UGG9Hdy3ADyRg1JWQxMIeeAA7mqvu6Fd5fimhKppL%2F3%2Bsw6b6L1F%2F4Afdem8mX%2FB%2F5IzIPDPyA9mjYX4WjhtMmY3qK41a13v0fafi61otjroKQVzeTdUDq0goMy8O3x1TK9YU6QYzuWWZC42qJjVbUfkEfX6MPjtcCFKsO6drfSBTMcg76OaNfkdANM6W1qZuujZu1cO&X-Amz-Signature=bd47201c905d5d739fc67e93b16568e29adc6293a168da0738952f4ccd2e520f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD3JHJLC%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLzTTRA9Er8kPv6perCpmj95M3GwwGd1hMn32h4Gm8JAiEAr27ofUqUUGq8Q02lJJXS7XuL7Zt4tu1hp5oRt%2BBUIS0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFADPEpu4vHoghWPvCrcA0wiRJtOLpLrrrux2kw91fq9ajFFxc6ZYjCxtv8kZ1gtRgZMILJwSZeBYvFUBB%2FE47K4pdoj0ur%2BVMri2HUKl9jsu4NFr6nLvipvRs1fJre7s1CdrQOWt2GQyI9BQ7n5gv5upHlU0pWPpx5sppGPJe1kqlw7ZEtkmaRQXRv3PdUVZPz4xP%2Fa8tak92VByxBs2KoUOryKMIfuBOvboW46CP5KnjTCp6iSgyp48pkSS6jmII%2FBHDsmVkUc%2BVYfUrhfZG2oLJlB69f04onH0vE5bfd%2Bfj9XsuS8kXv2DyXuK5jMJeymH%2FxLSzm%2FAaarZOI5CQR1UUVUdLXKQImh5w74gpdHMdLPoDUdv34%2Frh6pim2kVZ5c%2Bhar0SdCg1f93kyqIlHz6UdZ81dKFdFAhfwNngyGBntyRFoW7UNsaaGRO36addE3OzIB9arOp05gLnyw8TLMszLqHbOYXilwaQ2y3SKEKKEbEAi8OuulaUz9pSNoOOYij7K2eGO9pWTXImbGxawfQvAzo%2BZSbGqDNGYRolX%2BMxJ6eFWnEkE0cMS2623B0AcGwPqminqtCRnDo3d6miBboonwSOrYdSOOacU8LUe6qTCJ1LVObtqVn7rDoLtLWOGdNE4GIZ2bYJp8MLPEqswGOqUBlKGZ%2FPKOxdr4c%2Bgdtoj0UGG9Hdy3ADyRg1JWQxMIeeAA7mqvu6Fd5fimhKppL%2F3%2Bsw6b6L1F%2F4Afdem8mX%2FB%2F5IzIPDPyA9mjYX4WjhtMmY3qK41a13v0fafi61otjroKQVzeTdUDq0goMy8O3x1TK9YU6QYzuWWZC42qJjVbUfkEfX6MPjtcCFKsO6drfSBTMcg76OaNfkdANM6W1qZuujZu1cO&X-Amz-Signature=2af7873a5ea24c46efd34b10a54ba0a63b5b71b523affaf5626e2a06f1a55ca0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



