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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646AW6BHX%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA%2BjV8IMOKjpDcy0jEjipvjNHks%2BWkck8uAsYqYMDpSxAiAGQ31FF0RC1B%2BXOuj5%2FS620JVLPsOcEbOAkhdksxj9UCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJcCamnng%2BH3vySeKtwDeo%2BHcPNy789fNKIQUPl82sDUGScWFgB1F2q9q9nERvWyeJuPGWSF6lzK1awIWQbl7vINDI9AzVxD5GCatQmshNwhsDPG4JW%2FpR84%2BRVIo3Bc5AeBVsSkQ1dQvjo2xsXTyRi8KVnz3guIrfKM2BLpQqvoiQUnl9hpSUxvEaLoVjTGOUJh6fWcTu2b7FDXli%2BgwBJnrfzgr9aQ6RG5GlF6F3OG7ZRGT3vNXzD1QJKuAyNfyOvNVcKG%2BN8BPJSSLrCe1R5zP5Chnq%2Fpj7Rw4b%2BGMV0kbsdU9RayovX%2FdDEkQeRGXkSjA%2FA9yWlE48LNaenYaGW0ZxrUlz7l1Ve7frNe6TbO%2BwzzCkgVWZ7G80VywEuOlt0iFd7BQiRoXkw0COHyWtVoBfbIkh2YB0C9ml6thNOK2SaOnmeMIVo8UcMn%2BNOkC6ddNwxtVs0NWNwLfCXItZrOd%2BxXRC78S%2F1wBQxf7xK6p8bV5byFCIY%2BnN7SOn3QOGenDvzmRPQBW9vSLlBZq6UucULq7AtImr%2F2Erv2R4HRdU8abBiQnr0qfX1V0qhc88S82JFILStlYHbRVXslPmhb3ZbgORWpiNu6IoV9cCnUXnWA0rAmt0ciAjKfSKU05%2FyGjK3kjSKCDSswibX0zAY6pgF27rZV7nJsgXJt51t4jZY%2BnCmWStdvgKZrv3jCH5Ie15NZHAt7JaYLfOyMvaPPCY7roHsJZAZmUGxlGPSZ5qTopNlgHnY%2B4XuxTvtnd1FM4owrSDf9SsO1O9NlXE2TmtrdeZYLIRCXNaRCzuUihbXrQEHrwSzk2Zxc9bP2xG903WW2K1a6catjGszQpwjAQLP8Zc5hUUxT5CPz5A1joLFoXTnciABu&X-Amz-Signature=c9debc67e93a1c353974881628e108089ce13aacb147e4e32123bc8558ce0a05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646AW6BHX%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA%2BjV8IMOKjpDcy0jEjipvjNHks%2BWkck8uAsYqYMDpSxAiAGQ31FF0RC1B%2BXOuj5%2FS620JVLPsOcEbOAkhdksxj9UCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJcCamnng%2BH3vySeKtwDeo%2BHcPNy789fNKIQUPl82sDUGScWFgB1F2q9q9nERvWyeJuPGWSF6lzK1awIWQbl7vINDI9AzVxD5GCatQmshNwhsDPG4JW%2FpR84%2BRVIo3Bc5AeBVsSkQ1dQvjo2xsXTyRi8KVnz3guIrfKM2BLpQqvoiQUnl9hpSUxvEaLoVjTGOUJh6fWcTu2b7FDXli%2BgwBJnrfzgr9aQ6RG5GlF6F3OG7ZRGT3vNXzD1QJKuAyNfyOvNVcKG%2BN8BPJSSLrCe1R5zP5Chnq%2Fpj7Rw4b%2BGMV0kbsdU9RayovX%2FdDEkQeRGXkSjA%2FA9yWlE48LNaenYaGW0ZxrUlz7l1Ve7frNe6TbO%2BwzzCkgVWZ7G80VywEuOlt0iFd7BQiRoXkw0COHyWtVoBfbIkh2YB0C9ml6thNOK2SaOnmeMIVo8UcMn%2BNOkC6ddNwxtVs0NWNwLfCXItZrOd%2BxXRC78S%2F1wBQxf7xK6p8bV5byFCIY%2BnN7SOn3QOGenDvzmRPQBW9vSLlBZq6UucULq7AtImr%2F2Erv2R4HRdU8abBiQnr0qfX1V0qhc88S82JFILStlYHbRVXslPmhb3ZbgORWpiNu6IoV9cCnUXnWA0rAmt0ciAjKfSKU05%2FyGjK3kjSKCDSswibX0zAY6pgF27rZV7nJsgXJt51t4jZY%2BnCmWStdvgKZrv3jCH5Ie15NZHAt7JaYLfOyMvaPPCY7roHsJZAZmUGxlGPSZ5qTopNlgHnY%2B4XuxTvtnd1FM4owrSDf9SsO1O9NlXE2TmtrdeZYLIRCXNaRCzuUihbXrQEHrwSzk2Zxc9bP2xG903WW2K1a6catjGszQpwjAQLP8Zc5hUUxT5CPz5A1joLFoXTnciABu&X-Amz-Signature=86c807550c52dfe4b5d02ebf4f42d1d64c774b35fd71b1771f874c6030b26881&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646AW6BHX%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA%2BjV8IMOKjpDcy0jEjipvjNHks%2BWkck8uAsYqYMDpSxAiAGQ31FF0RC1B%2BXOuj5%2FS620JVLPsOcEbOAkhdksxj9UCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJcCamnng%2BH3vySeKtwDeo%2BHcPNy789fNKIQUPl82sDUGScWFgB1F2q9q9nERvWyeJuPGWSF6lzK1awIWQbl7vINDI9AzVxD5GCatQmshNwhsDPG4JW%2FpR84%2BRVIo3Bc5AeBVsSkQ1dQvjo2xsXTyRi8KVnz3guIrfKM2BLpQqvoiQUnl9hpSUxvEaLoVjTGOUJh6fWcTu2b7FDXli%2BgwBJnrfzgr9aQ6RG5GlF6F3OG7ZRGT3vNXzD1QJKuAyNfyOvNVcKG%2BN8BPJSSLrCe1R5zP5Chnq%2Fpj7Rw4b%2BGMV0kbsdU9RayovX%2FdDEkQeRGXkSjA%2FA9yWlE48LNaenYaGW0ZxrUlz7l1Ve7frNe6TbO%2BwzzCkgVWZ7G80VywEuOlt0iFd7BQiRoXkw0COHyWtVoBfbIkh2YB0C9ml6thNOK2SaOnmeMIVo8UcMn%2BNOkC6ddNwxtVs0NWNwLfCXItZrOd%2BxXRC78S%2F1wBQxf7xK6p8bV5byFCIY%2BnN7SOn3QOGenDvzmRPQBW9vSLlBZq6UucULq7AtImr%2F2Erv2R4HRdU8abBiQnr0qfX1V0qhc88S82JFILStlYHbRVXslPmhb3ZbgORWpiNu6IoV9cCnUXnWA0rAmt0ciAjKfSKU05%2FyGjK3kjSKCDSswibX0zAY6pgF27rZV7nJsgXJt51t4jZY%2BnCmWStdvgKZrv3jCH5Ie15NZHAt7JaYLfOyMvaPPCY7roHsJZAZmUGxlGPSZ5qTopNlgHnY%2B4XuxTvtnd1FM4owrSDf9SsO1O9NlXE2TmtrdeZYLIRCXNaRCzuUihbXrQEHrwSzk2Zxc9bP2xG903WW2K1a6catjGszQpwjAQLP8Zc5hUUxT5CPz5A1joLFoXTnciABu&X-Amz-Signature=89c6e242ff100f9928c7083c3f280ff3beb514b3153ededa7421b94873970d29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646AW6BHX%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA%2BjV8IMOKjpDcy0jEjipvjNHks%2BWkck8uAsYqYMDpSxAiAGQ31FF0RC1B%2BXOuj5%2FS620JVLPsOcEbOAkhdksxj9UCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJcCamnng%2BH3vySeKtwDeo%2BHcPNy789fNKIQUPl82sDUGScWFgB1F2q9q9nERvWyeJuPGWSF6lzK1awIWQbl7vINDI9AzVxD5GCatQmshNwhsDPG4JW%2FpR84%2BRVIo3Bc5AeBVsSkQ1dQvjo2xsXTyRi8KVnz3guIrfKM2BLpQqvoiQUnl9hpSUxvEaLoVjTGOUJh6fWcTu2b7FDXli%2BgwBJnrfzgr9aQ6RG5GlF6F3OG7ZRGT3vNXzD1QJKuAyNfyOvNVcKG%2BN8BPJSSLrCe1R5zP5Chnq%2Fpj7Rw4b%2BGMV0kbsdU9RayovX%2FdDEkQeRGXkSjA%2FA9yWlE48LNaenYaGW0ZxrUlz7l1Ve7frNe6TbO%2BwzzCkgVWZ7G80VywEuOlt0iFd7BQiRoXkw0COHyWtVoBfbIkh2YB0C9ml6thNOK2SaOnmeMIVo8UcMn%2BNOkC6ddNwxtVs0NWNwLfCXItZrOd%2BxXRC78S%2F1wBQxf7xK6p8bV5byFCIY%2BnN7SOn3QOGenDvzmRPQBW9vSLlBZq6UucULq7AtImr%2F2Erv2R4HRdU8abBiQnr0qfX1V0qhc88S82JFILStlYHbRVXslPmhb3ZbgORWpiNu6IoV9cCnUXnWA0rAmt0ciAjKfSKU05%2FyGjK3kjSKCDSswibX0zAY6pgF27rZV7nJsgXJt51t4jZY%2BnCmWStdvgKZrv3jCH5Ie15NZHAt7JaYLfOyMvaPPCY7roHsJZAZmUGxlGPSZ5qTopNlgHnY%2B4XuxTvtnd1FM4owrSDf9SsO1O9NlXE2TmtrdeZYLIRCXNaRCzuUihbXrQEHrwSzk2Zxc9bP2xG903WW2K1a6catjGszQpwjAQLP8Zc5hUUxT5CPz5A1joLFoXTnciABu&X-Amz-Signature=d807eecc2ccd7ac9f555622a2e388e7951582bdbd9e4876656da9453669898f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



