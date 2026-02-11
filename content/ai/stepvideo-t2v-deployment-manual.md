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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4B3OOHG%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTKtbd%2BdKo%2FSV1xx%2BxLHBWehd%2Fpn%2BzQwYiO6i8lZLMPgIhAL7wxiEhfxurACcE5RcVh1W5BFTNULHSgqbtnCArKY9UKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw34uusszuLkzGwpJ0q3AMGT1b231LnYtjAG9ujV1YyE9SLZiQp4gM5DTs8Nw%2B%2F%2Fw4JqN%2BbCQJRtQbGd56JhDLfpsRy1kB3I4MeYsxgYeMQ5zL2EWJsiIOxVS8Vet6xFBrSoeosZ9u26VLM8RjKwvzqQrgoJY7Mlzs1m7Aufi6%2B3JuQx4zmsO6REJB99k7StTe%2FjLEdc%2BvXYmdXcPFtgaT%2BTs6v9xB3dSJBMCfVe9%2FkB%2F5g22w%2FVe1WokEC52AbOjuO9qPQpKxjM08iKm4y5JATFwWSYaP0vSG%2B8liEq8amnLYXD4GLZtjnnCXpp3vkTR5wkhlvtTdBLJNHWVXDWigKI9vIqb3tAR3%2FrQyz655btazhAsJm3w5l24OUwXvD%2FUf3%2Bm3UID811cnlExZUG8eeks2UtTUDXMeI98tCBfx2zvu%2Byt74ClsBigO9DusHqOC7ChW35IiaaWW4POpD%2BBGryCo18oaccpEDJ6xaEH%2FnUJCK4KKKch297S0JQBYO93l0bQzUShY1HXoQo0qHD%2Fakoxlmfd0vw1Xz10rxm5A0Ryu%2BS0z7HQL7B5Ixj6DY5FM95K4zJO5%2F4brLnLlPyZhuSZv9yElVjPwy4e8wl1yDP3pjs9Qe6r3MmKmvtyER%2FdVgjyF3IZIUAScIXzDay6%2FMBjqkAc%2FJyvHT5VSn0qEalEyuRovZgvsAQyaHsKq9JYRcweRxVGheoe%2BZViRCoNGeyiR%2F9kFf9YvBBW12uio3APsGJS7G%2FgVZO4P8e1%2FxF1Q%2BuU8%2FSzHpm32XTGE7n4WNnoeW3SjOAdkhgYJCkEHGj3c%2Bpsknl1MHzIqkMXOYDdOjRYTL%2F3An1Ikw%2FH%2F3YqVoU6l5d%2Fb%2Boz1XfQlr%2BlyAhMANlNMN%2F0tA&X-Amz-Signature=8af3a9b221e13d39a01e9ce0b5c76d2296121879dcd09e8016c35de8680d9cad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4B3OOHG%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTKtbd%2BdKo%2FSV1xx%2BxLHBWehd%2Fpn%2BzQwYiO6i8lZLMPgIhAL7wxiEhfxurACcE5RcVh1W5BFTNULHSgqbtnCArKY9UKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw34uusszuLkzGwpJ0q3AMGT1b231LnYtjAG9ujV1YyE9SLZiQp4gM5DTs8Nw%2B%2F%2Fw4JqN%2BbCQJRtQbGd56JhDLfpsRy1kB3I4MeYsxgYeMQ5zL2EWJsiIOxVS8Vet6xFBrSoeosZ9u26VLM8RjKwvzqQrgoJY7Mlzs1m7Aufi6%2B3JuQx4zmsO6REJB99k7StTe%2FjLEdc%2BvXYmdXcPFtgaT%2BTs6v9xB3dSJBMCfVe9%2FkB%2F5g22w%2FVe1WokEC52AbOjuO9qPQpKxjM08iKm4y5JATFwWSYaP0vSG%2B8liEq8amnLYXD4GLZtjnnCXpp3vkTR5wkhlvtTdBLJNHWVXDWigKI9vIqb3tAR3%2FrQyz655btazhAsJm3w5l24OUwXvD%2FUf3%2Bm3UID811cnlExZUG8eeks2UtTUDXMeI98tCBfx2zvu%2Byt74ClsBigO9DusHqOC7ChW35IiaaWW4POpD%2BBGryCo18oaccpEDJ6xaEH%2FnUJCK4KKKch297S0JQBYO93l0bQzUShY1HXoQo0qHD%2Fakoxlmfd0vw1Xz10rxm5A0Ryu%2BS0z7HQL7B5Ixj6DY5FM95K4zJO5%2F4brLnLlPyZhuSZv9yElVjPwy4e8wl1yDP3pjs9Qe6r3MmKmvtyER%2FdVgjyF3IZIUAScIXzDay6%2FMBjqkAc%2FJyvHT5VSn0qEalEyuRovZgvsAQyaHsKq9JYRcweRxVGheoe%2BZViRCoNGeyiR%2F9kFf9YvBBW12uio3APsGJS7G%2FgVZO4P8e1%2FxF1Q%2BuU8%2FSzHpm32XTGE7n4WNnoeW3SjOAdkhgYJCkEHGj3c%2Bpsknl1MHzIqkMXOYDdOjRYTL%2F3An1Ikw%2FH%2F3YqVoU6l5d%2Fb%2Boz1XfQlr%2BlyAhMANlNMN%2F0tA&X-Amz-Signature=09de00fee75a2134dccf89cd6784bf2b7fcc649aaf94ed1187c77b6434fffbb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4B3OOHG%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTKtbd%2BdKo%2FSV1xx%2BxLHBWehd%2Fpn%2BzQwYiO6i8lZLMPgIhAL7wxiEhfxurACcE5RcVh1W5BFTNULHSgqbtnCArKY9UKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw34uusszuLkzGwpJ0q3AMGT1b231LnYtjAG9ujV1YyE9SLZiQp4gM5DTs8Nw%2B%2F%2Fw4JqN%2BbCQJRtQbGd56JhDLfpsRy1kB3I4MeYsxgYeMQ5zL2EWJsiIOxVS8Vet6xFBrSoeosZ9u26VLM8RjKwvzqQrgoJY7Mlzs1m7Aufi6%2B3JuQx4zmsO6REJB99k7StTe%2FjLEdc%2BvXYmdXcPFtgaT%2BTs6v9xB3dSJBMCfVe9%2FkB%2F5g22w%2FVe1WokEC52AbOjuO9qPQpKxjM08iKm4y5JATFwWSYaP0vSG%2B8liEq8amnLYXD4GLZtjnnCXpp3vkTR5wkhlvtTdBLJNHWVXDWigKI9vIqb3tAR3%2FrQyz655btazhAsJm3w5l24OUwXvD%2FUf3%2Bm3UID811cnlExZUG8eeks2UtTUDXMeI98tCBfx2zvu%2Byt74ClsBigO9DusHqOC7ChW35IiaaWW4POpD%2BBGryCo18oaccpEDJ6xaEH%2FnUJCK4KKKch297S0JQBYO93l0bQzUShY1HXoQo0qHD%2Fakoxlmfd0vw1Xz10rxm5A0Ryu%2BS0z7HQL7B5Ixj6DY5FM95K4zJO5%2F4brLnLlPyZhuSZv9yElVjPwy4e8wl1yDP3pjs9Qe6r3MmKmvtyER%2FdVgjyF3IZIUAScIXzDay6%2FMBjqkAc%2FJyvHT5VSn0qEalEyuRovZgvsAQyaHsKq9JYRcweRxVGheoe%2BZViRCoNGeyiR%2F9kFf9YvBBW12uio3APsGJS7G%2FgVZO4P8e1%2FxF1Q%2BuU8%2FSzHpm32XTGE7n4WNnoeW3SjOAdkhgYJCkEHGj3c%2Bpsknl1MHzIqkMXOYDdOjRYTL%2F3An1Ikw%2FH%2F3YqVoU6l5d%2Fb%2Boz1XfQlr%2BlyAhMANlNMN%2F0tA&X-Amz-Signature=d32625c017f5dfa8d4253b28d0ec5bd5c95e9e88f0825c98889fde16f7ad22d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4B3OOHG%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTKtbd%2BdKo%2FSV1xx%2BxLHBWehd%2Fpn%2BzQwYiO6i8lZLMPgIhAL7wxiEhfxurACcE5RcVh1W5BFTNULHSgqbtnCArKY9UKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw34uusszuLkzGwpJ0q3AMGT1b231LnYtjAG9ujV1YyE9SLZiQp4gM5DTs8Nw%2B%2F%2Fw4JqN%2BbCQJRtQbGd56JhDLfpsRy1kB3I4MeYsxgYeMQ5zL2EWJsiIOxVS8Vet6xFBrSoeosZ9u26VLM8RjKwvzqQrgoJY7Mlzs1m7Aufi6%2B3JuQx4zmsO6REJB99k7StTe%2FjLEdc%2BvXYmdXcPFtgaT%2BTs6v9xB3dSJBMCfVe9%2FkB%2F5g22w%2FVe1WokEC52AbOjuO9qPQpKxjM08iKm4y5JATFwWSYaP0vSG%2B8liEq8amnLYXD4GLZtjnnCXpp3vkTR5wkhlvtTdBLJNHWVXDWigKI9vIqb3tAR3%2FrQyz655btazhAsJm3w5l24OUwXvD%2FUf3%2Bm3UID811cnlExZUG8eeks2UtTUDXMeI98tCBfx2zvu%2Byt74ClsBigO9DusHqOC7ChW35IiaaWW4POpD%2BBGryCo18oaccpEDJ6xaEH%2FnUJCK4KKKch297S0JQBYO93l0bQzUShY1HXoQo0qHD%2Fakoxlmfd0vw1Xz10rxm5A0Ryu%2BS0z7HQL7B5Ixj6DY5FM95K4zJO5%2F4brLnLlPyZhuSZv9yElVjPwy4e8wl1yDP3pjs9Qe6r3MmKmvtyER%2FdVgjyF3IZIUAScIXzDay6%2FMBjqkAc%2FJyvHT5VSn0qEalEyuRovZgvsAQyaHsKq9JYRcweRxVGheoe%2BZViRCoNGeyiR%2F9kFf9YvBBW12uio3APsGJS7G%2FgVZO4P8e1%2FxF1Q%2BuU8%2FSzHpm32XTGE7n4WNnoeW3SjOAdkhgYJCkEHGj3c%2Bpsknl1MHzIqkMXOYDdOjRYTL%2F3An1Ikw%2FH%2F3YqVoU6l5d%2Fb%2Boz1XfQlr%2BlyAhMANlNMN%2F0tA&X-Amz-Signature=95ad96ad7197b27305578ba582194ba25a566cbfbafee4c2a03760f00efc7a61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



