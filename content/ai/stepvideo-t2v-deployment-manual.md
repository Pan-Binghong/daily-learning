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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSUCJVQD%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIClZfQa9Rttfch23qmm0%2FjERM99pS0AJTuSwCUGpRPmlAiEAy6UQB%2F%2FZbVPirwdCPv1zMmNBRPtPRgCKc8EhFCacXSsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDN6YCN4lna1OY6k7GSrcA7qFBCGO8YNIT0nfD2TR1bKmE0pJ%2F2H00%2FE414SpacTxLhNfAUHMx857GpFP5CgQO8XbPBfhNBo%2FeNPY6gXDOI1IMcV4sM3tKJIaVN4pQYymq4QdFk8hKu03WEYIbwCF2DrM4A1P5sOp0pobWNx5CSMTUDsBJlu9Dyc3kUbDg4sjMDaX5Y205sxI4LKnqGgWFLSeNXtAJFR9HPtFpuL%2F4OnCRz9BJcPxav4MAkmYKGC9NPzalN6VltXvwaIXvnXLuQL6nrueGctjisTZnH4CPLAUxEi8gpdonhE01U37Vzt316jPG0bljEzMg0GddJLke4q0py8CqAEaEPerPkShXNk83sqWPFQRkswh32bBuaI%2Fs1R78%2BTGwfPgHxAywJ%2BpNabI5yi5wvwNl%2Fz6wDQYH%2BPwsG24i3M8sto9pI6JAH93w0Bw5s1MVb33KRlYZhfvTYt%2B9uKadLg1V%2F%2FCGXpneCmjOgh19MeSV3B0%2BnTGxR8G9eKqeJG0dCUXSLkPpX0a2zK7wa4%2BrHGyeac1Df%2FlfdfvSpfLuzdbDInQ4GPBcVI%2B2oCZSUwRe3GwSK1KQzUNLpGCNDhiRCql1VwmbX6%2BLe3ScvY61Ruiu5rKLoGHEz1pkTvVmjUD930VAj9xMNKghMkGOqUBUkEU6c5Fk4QmWvdWZr4qEl0M8Vv4HJGCfzT4ZAEvuP1CSDSxfa0iTReN4oJegH7q2r4ogwCRbOn63%2BCo84CUsn3mY85eqn2WrFhUB4H0C2hPYL2f0poAJqUTIuAgynbQrrIE0%2FawaN%2Bi3qZTB05eI84s4cf7cEXFMSqt%2Fy63ZPOAId4CeWs8EwdejO2zxduvkn9oP4IzhMVmYSYPW7j1vNm4D4Oy&X-Amz-Signature=b852fade660eab42c71cea154ab2102d0c4d382ef90c1e46f9ce81b26f1500d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSUCJVQD%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIClZfQa9Rttfch23qmm0%2FjERM99pS0AJTuSwCUGpRPmlAiEAy6UQB%2F%2FZbVPirwdCPv1zMmNBRPtPRgCKc8EhFCacXSsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDN6YCN4lna1OY6k7GSrcA7qFBCGO8YNIT0nfD2TR1bKmE0pJ%2F2H00%2FE414SpacTxLhNfAUHMx857GpFP5CgQO8XbPBfhNBo%2FeNPY6gXDOI1IMcV4sM3tKJIaVN4pQYymq4QdFk8hKu03WEYIbwCF2DrM4A1P5sOp0pobWNx5CSMTUDsBJlu9Dyc3kUbDg4sjMDaX5Y205sxI4LKnqGgWFLSeNXtAJFR9HPtFpuL%2F4OnCRz9BJcPxav4MAkmYKGC9NPzalN6VltXvwaIXvnXLuQL6nrueGctjisTZnH4CPLAUxEi8gpdonhE01U37Vzt316jPG0bljEzMg0GddJLke4q0py8CqAEaEPerPkShXNk83sqWPFQRkswh32bBuaI%2Fs1R78%2BTGwfPgHxAywJ%2BpNabI5yi5wvwNl%2Fz6wDQYH%2BPwsG24i3M8sto9pI6JAH93w0Bw5s1MVb33KRlYZhfvTYt%2B9uKadLg1V%2F%2FCGXpneCmjOgh19MeSV3B0%2BnTGxR8G9eKqeJG0dCUXSLkPpX0a2zK7wa4%2BrHGyeac1Df%2FlfdfvSpfLuzdbDInQ4GPBcVI%2B2oCZSUwRe3GwSK1KQzUNLpGCNDhiRCql1VwmbX6%2BLe3ScvY61Ruiu5rKLoGHEz1pkTvVmjUD930VAj9xMNKghMkGOqUBUkEU6c5Fk4QmWvdWZr4qEl0M8Vv4HJGCfzT4ZAEvuP1CSDSxfa0iTReN4oJegH7q2r4ogwCRbOn63%2BCo84CUsn3mY85eqn2WrFhUB4H0C2hPYL2f0poAJqUTIuAgynbQrrIE0%2FawaN%2Bi3qZTB05eI84s4cf7cEXFMSqt%2Fy63ZPOAId4CeWs8EwdejO2zxduvkn9oP4IzhMVmYSYPW7j1vNm4D4Oy&X-Amz-Signature=97a0ba034e22fd6ad9ddcde9c7225436b7b4e6a9507ffef4f1d22e42c3feb2e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSUCJVQD%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIClZfQa9Rttfch23qmm0%2FjERM99pS0AJTuSwCUGpRPmlAiEAy6UQB%2F%2FZbVPirwdCPv1zMmNBRPtPRgCKc8EhFCacXSsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDN6YCN4lna1OY6k7GSrcA7qFBCGO8YNIT0nfD2TR1bKmE0pJ%2F2H00%2FE414SpacTxLhNfAUHMx857GpFP5CgQO8XbPBfhNBo%2FeNPY6gXDOI1IMcV4sM3tKJIaVN4pQYymq4QdFk8hKu03WEYIbwCF2DrM4A1P5sOp0pobWNx5CSMTUDsBJlu9Dyc3kUbDg4sjMDaX5Y205sxI4LKnqGgWFLSeNXtAJFR9HPtFpuL%2F4OnCRz9BJcPxav4MAkmYKGC9NPzalN6VltXvwaIXvnXLuQL6nrueGctjisTZnH4CPLAUxEi8gpdonhE01U37Vzt316jPG0bljEzMg0GddJLke4q0py8CqAEaEPerPkShXNk83sqWPFQRkswh32bBuaI%2Fs1R78%2BTGwfPgHxAywJ%2BpNabI5yi5wvwNl%2Fz6wDQYH%2BPwsG24i3M8sto9pI6JAH93w0Bw5s1MVb33KRlYZhfvTYt%2B9uKadLg1V%2F%2FCGXpneCmjOgh19MeSV3B0%2BnTGxR8G9eKqeJG0dCUXSLkPpX0a2zK7wa4%2BrHGyeac1Df%2FlfdfvSpfLuzdbDInQ4GPBcVI%2B2oCZSUwRe3GwSK1KQzUNLpGCNDhiRCql1VwmbX6%2BLe3ScvY61Ruiu5rKLoGHEz1pkTvVmjUD930VAj9xMNKghMkGOqUBUkEU6c5Fk4QmWvdWZr4qEl0M8Vv4HJGCfzT4ZAEvuP1CSDSxfa0iTReN4oJegH7q2r4ogwCRbOn63%2BCo84CUsn3mY85eqn2WrFhUB4H0C2hPYL2f0poAJqUTIuAgynbQrrIE0%2FawaN%2Bi3qZTB05eI84s4cf7cEXFMSqt%2Fy63ZPOAId4CeWs8EwdejO2zxduvkn9oP4IzhMVmYSYPW7j1vNm4D4Oy&X-Amz-Signature=976b3e670ecadba1b6be5cda75cfcdbf3676a5b37f54845e85beafae5cd74eb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSUCJVQD%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIClZfQa9Rttfch23qmm0%2FjERM99pS0AJTuSwCUGpRPmlAiEAy6UQB%2F%2FZbVPirwdCPv1zMmNBRPtPRgCKc8EhFCacXSsq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDN6YCN4lna1OY6k7GSrcA7qFBCGO8YNIT0nfD2TR1bKmE0pJ%2F2H00%2FE414SpacTxLhNfAUHMx857GpFP5CgQO8XbPBfhNBo%2FeNPY6gXDOI1IMcV4sM3tKJIaVN4pQYymq4QdFk8hKu03WEYIbwCF2DrM4A1P5sOp0pobWNx5CSMTUDsBJlu9Dyc3kUbDg4sjMDaX5Y205sxI4LKnqGgWFLSeNXtAJFR9HPtFpuL%2F4OnCRz9BJcPxav4MAkmYKGC9NPzalN6VltXvwaIXvnXLuQL6nrueGctjisTZnH4CPLAUxEi8gpdonhE01U37Vzt316jPG0bljEzMg0GddJLke4q0py8CqAEaEPerPkShXNk83sqWPFQRkswh32bBuaI%2Fs1R78%2BTGwfPgHxAywJ%2BpNabI5yi5wvwNl%2Fz6wDQYH%2BPwsG24i3M8sto9pI6JAH93w0Bw5s1MVb33KRlYZhfvTYt%2B9uKadLg1V%2F%2FCGXpneCmjOgh19MeSV3B0%2BnTGxR8G9eKqeJG0dCUXSLkPpX0a2zK7wa4%2BrHGyeac1Df%2FlfdfvSpfLuzdbDInQ4GPBcVI%2B2oCZSUwRe3GwSK1KQzUNLpGCNDhiRCql1VwmbX6%2BLe3ScvY61Ruiu5rKLoGHEz1pkTvVmjUD930VAj9xMNKghMkGOqUBUkEU6c5Fk4QmWvdWZr4qEl0M8Vv4HJGCfzT4ZAEvuP1CSDSxfa0iTReN4oJegH7q2r4ogwCRbOn63%2BCo84CUsn3mY85eqn2WrFhUB4H0C2hPYL2f0poAJqUTIuAgynbQrrIE0%2FawaN%2Bi3qZTB05eI84s4cf7cEXFMSqt%2Fy63ZPOAId4CeWs8EwdejO2zxduvkn9oP4IzhMVmYSYPW7j1vNm4D4Oy&X-Amz-Signature=7c5beee6ac0b770a7a62862e465b30a58d7b5cfb1a68db017551f022da8ae03d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



