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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZBXP53%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMYl5Lg4Bvf2Qzl3Ed%2F3auyPxZyy2B%2FCTqOvWLvoQFdgIgaUTjzIn9bJNT%2B88HQ8yyfCj%2BfiIBWfYAN4eYpD%2F8%2F5YqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATF0kHTS73qEYywSyrcA7gefM2I9AffGdapNAMCfnhCy%2BPpeCJoLtis%2BDMIL4dlWc7nCKhYlu3Ubzk1ShcNjWMh4H03CWgmMquEcnbvR6giz1eAoNNIbRDUVVm7v7JSdThaTGbZq1I%2FiY3F7aHSLkXdv5ly3r86Kf5crDexWMpeNxS2Z8lQGrM5pdHNc%2FcpotHCSz8TI%2Bfnec7x9KiVGZ%2BY4jBCWwmkl88OnPscYldzDvmnrYv5oieLF%2F4NjvlbIfT18eseCygBlqtPhJ1JuO0NDhsMT0oNLZ7S6eEpPYme%2BZN7lQy8S1qB6UaVtOFEVCg6OC%2B%2Bib79b19%2Bw10Mon70pC1uz9BpuJsPXmjQEj5HAS%2FRmfdSpg4D7a19Sb5Q4QBTo6Z8mmO7ockyXiUz3BRJ9vFxHu1R0my3DDbpk8cSHz2yf2mL%2BiiJc2S5LhM%2BzNGmEdYH%2BTFtESsvck08xrYtTvtB3EiHj3xzfzv%2Bv1GWVxz2aIy9GBZQbiPEqu2MNWdx5SRBoR7VCpT5I9QCM9AmyNEGWP5Kf%2BW3HW9AVuiIsS%2BsWSjN28jWAUqmx4Orc7PTjrtKtNWytDrgfQYqrlEueYCnWHNexuVCXQRhH0W1DJE7WYDDe4v7EdtcAs1ov0M2kxMw8bnlUDMtMKvIks4GOqUBlzg6AJ67%2Fu6VfXe4DHNrT%2BJJUYOYL6yjCLzy6wjDcFpXDbGw0L9qGHzbuMXrKjFiQwVuyov0VLy2Emc3lJ34axou5nw2%2B9O5RLdAsFV1xi%2BQg4VJK6PKmtvxnTUvix%2FRgPVDT%2FI1nN3kYRDZmM5NE%2FrTExKYqB6rN0ZclO8fHJ%2FHD7FvrVfJi5Pr5zfeMrMlDKoURoCB8fp3WradFVfvo%2BTswWsF&X-Amz-Signature=d4dc3133abf580ff3794d27c084e6421c65e5124c7ed53be67d803dd4ca2b2a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZBXP53%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMYl5Lg4Bvf2Qzl3Ed%2F3auyPxZyy2B%2FCTqOvWLvoQFdgIgaUTjzIn9bJNT%2B88HQ8yyfCj%2BfiIBWfYAN4eYpD%2F8%2F5YqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATF0kHTS73qEYywSyrcA7gefM2I9AffGdapNAMCfnhCy%2BPpeCJoLtis%2BDMIL4dlWc7nCKhYlu3Ubzk1ShcNjWMh4H03CWgmMquEcnbvR6giz1eAoNNIbRDUVVm7v7JSdThaTGbZq1I%2FiY3F7aHSLkXdv5ly3r86Kf5crDexWMpeNxS2Z8lQGrM5pdHNc%2FcpotHCSz8TI%2Bfnec7x9KiVGZ%2BY4jBCWwmkl88OnPscYldzDvmnrYv5oieLF%2F4NjvlbIfT18eseCygBlqtPhJ1JuO0NDhsMT0oNLZ7S6eEpPYme%2BZN7lQy8S1qB6UaVtOFEVCg6OC%2B%2Bib79b19%2Bw10Mon70pC1uz9BpuJsPXmjQEj5HAS%2FRmfdSpg4D7a19Sb5Q4QBTo6Z8mmO7ockyXiUz3BRJ9vFxHu1R0my3DDbpk8cSHz2yf2mL%2BiiJc2S5LhM%2BzNGmEdYH%2BTFtESsvck08xrYtTvtB3EiHj3xzfzv%2Bv1GWVxz2aIy9GBZQbiPEqu2MNWdx5SRBoR7VCpT5I9QCM9AmyNEGWP5Kf%2BW3HW9AVuiIsS%2BsWSjN28jWAUqmx4Orc7PTjrtKtNWytDrgfQYqrlEueYCnWHNexuVCXQRhH0W1DJE7WYDDe4v7EdtcAs1ov0M2kxMw8bnlUDMtMKvIks4GOqUBlzg6AJ67%2Fu6VfXe4DHNrT%2BJJUYOYL6yjCLzy6wjDcFpXDbGw0L9qGHzbuMXrKjFiQwVuyov0VLy2Emc3lJ34axou5nw2%2B9O5RLdAsFV1xi%2BQg4VJK6PKmtvxnTUvix%2FRgPVDT%2FI1nN3kYRDZmM5NE%2FrTExKYqB6rN0ZclO8fHJ%2FHD7FvrVfJi5Pr5zfeMrMlDKoURoCB8fp3WradFVfvo%2BTswWsF&X-Amz-Signature=103de1bfceece0bebcbb97a73024e8f415bb1e5f7510bc444af483cb92193e41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZBXP53%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMYl5Lg4Bvf2Qzl3Ed%2F3auyPxZyy2B%2FCTqOvWLvoQFdgIgaUTjzIn9bJNT%2B88HQ8yyfCj%2BfiIBWfYAN4eYpD%2F8%2F5YqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATF0kHTS73qEYywSyrcA7gefM2I9AffGdapNAMCfnhCy%2BPpeCJoLtis%2BDMIL4dlWc7nCKhYlu3Ubzk1ShcNjWMh4H03CWgmMquEcnbvR6giz1eAoNNIbRDUVVm7v7JSdThaTGbZq1I%2FiY3F7aHSLkXdv5ly3r86Kf5crDexWMpeNxS2Z8lQGrM5pdHNc%2FcpotHCSz8TI%2Bfnec7x9KiVGZ%2BY4jBCWwmkl88OnPscYldzDvmnrYv5oieLF%2F4NjvlbIfT18eseCygBlqtPhJ1JuO0NDhsMT0oNLZ7S6eEpPYme%2BZN7lQy8S1qB6UaVtOFEVCg6OC%2B%2Bib79b19%2Bw10Mon70pC1uz9BpuJsPXmjQEj5HAS%2FRmfdSpg4D7a19Sb5Q4QBTo6Z8mmO7ockyXiUz3BRJ9vFxHu1R0my3DDbpk8cSHz2yf2mL%2BiiJc2S5LhM%2BzNGmEdYH%2BTFtESsvck08xrYtTvtB3EiHj3xzfzv%2Bv1GWVxz2aIy9GBZQbiPEqu2MNWdx5SRBoR7VCpT5I9QCM9AmyNEGWP5Kf%2BW3HW9AVuiIsS%2BsWSjN28jWAUqmx4Orc7PTjrtKtNWytDrgfQYqrlEueYCnWHNexuVCXQRhH0W1DJE7WYDDe4v7EdtcAs1ov0M2kxMw8bnlUDMtMKvIks4GOqUBlzg6AJ67%2Fu6VfXe4DHNrT%2BJJUYOYL6yjCLzy6wjDcFpXDbGw0L9qGHzbuMXrKjFiQwVuyov0VLy2Emc3lJ34axou5nw2%2B9O5RLdAsFV1xi%2BQg4VJK6PKmtvxnTUvix%2FRgPVDT%2FI1nN3kYRDZmM5NE%2FrTExKYqB6rN0ZclO8fHJ%2FHD7FvrVfJi5Pr5zfeMrMlDKoURoCB8fp3WradFVfvo%2BTswWsF&X-Amz-Signature=55d513febab2e3e1838b64532aeaf87c5b2d1c8fc30bdb782e4a9911218349bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAZBXP53%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMYl5Lg4Bvf2Qzl3Ed%2F3auyPxZyy2B%2FCTqOvWLvoQFdgIgaUTjzIn9bJNT%2B88HQ8yyfCj%2BfiIBWfYAN4eYpD%2F8%2F5YqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDATF0kHTS73qEYywSyrcA7gefM2I9AffGdapNAMCfnhCy%2BPpeCJoLtis%2BDMIL4dlWc7nCKhYlu3Ubzk1ShcNjWMh4H03CWgmMquEcnbvR6giz1eAoNNIbRDUVVm7v7JSdThaTGbZq1I%2FiY3F7aHSLkXdv5ly3r86Kf5crDexWMpeNxS2Z8lQGrM5pdHNc%2FcpotHCSz8TI%2Bfnec7x9KiVGZ%2BY4jBCWwmkl88OnPscYldzDvmnrYv5oieLF%2F4NjvlbIfT18eseCygBlqtPhJ1JuO0NDhsMT0oNLZ7S6eEpPYme%2BZN7lQy8S1qB6UaVtOFEVCg6OC%2B%2Bib79b19%2Bw10Mon70pC1uz9BpuJsPXmjQEj5HAS%2FRmfdSpg4D7a19Sb5Q4QBTo6Z8mmO7ockyXiUz3BRJ9vFxHu1R0my3DDbpk8cSHz2yf2mL%2BiiJc2S5LhM%2BzNGmEdYH%2BTFtESsvck08xrYtTvtB3EiHj3xzfzv%2Bv1GWVxz2aIy9GBZQbiPEqu2MNWdx5SRBoR7VCpT5I9QCM9AmyNEGWP5Kf%2BW3HW9AVuiIsS%2BsWSjN28jWAUqmx4Orc7PTjrtKtNWytDrgfQYqrlEueYCnWHNexuVCXQRhH0W1DJE7WYDDe4v7EdtcAs1ov0M2kxMw8bnlUDMtMKvIks4GOqUBlzg6AJ67%2Fu6VfXe4DHNrT%2BJJUYOYL6yjCLzy6wjDcFpXDbGw0L9qGHzbuMXrKjFiQwVuyov0VLy2Emc3lJ34axou5nw2%2B9O5RLdAsFV1xi%2BQg4VJK6PKmtvxnTUvix%2FRgPVDT%2FI1nN3kYRDZmM5NE%2FrTExKYqB6rN0ZclO8fHJ%2FHD7FvrVfJi5Pr5zfeMrMlDKoURoCB8fp3WradFVfvo%2BTswWsF&X-Amz-Signature=25bda53047143b06920d5df56a47eb3ebfc6f8a8edd85311b79deb481aa611b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



