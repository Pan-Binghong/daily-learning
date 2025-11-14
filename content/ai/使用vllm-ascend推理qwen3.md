---
title: 使用Vllm-Ascend推理Qwen3
date: '2025-11-13T06:10:00.000Z'
lastmod: '2025-11-13T06:27:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 使用vllm-ascend进行推理，增加速度优化，禁用思考。

---

### 1. 拉取镜像

```powershell
docker pull quay.io/ascend/vllm-ascend:v0.11.0rc1
```

---

### 2. 启动容器

```powershell
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.11.0rc1
docker run --rm \
-d \
--name vllm-ascend \
--shm-size=1g \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```

---

### 3. 配置环境

```powershell
export VLLM_USE_MODELSCOPE=True
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM=1
export VLLM_ASCEND_ENABLE_PREFETCH_MLP=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export CPU_AFFINITY_CONF=1

# export TASK_QUEUE_ENABLE=2 
unset TASK_QUEUE_ENABLE
```

- 禁用思考
---

### 4. 启动服务

```powershell
vllm serve Qwen/Qwen3-32B --tensor-parallel-size 8 --async-scheduling --chat-template ./qwen3_nonthinking.jinja
```

---

### 5. 测试

```powershell
#!/usr/bin/env python3
"""
vLLM 性能测试脚本 - 无需 jq 依赖
"""
import subprocess
import json
import time
import sys

def call_vllm(prompt: str, max_tokens: int = 4096):
    """调用 vLLM API 并计时"""
    
    url = "http://localhost:8000/v1/chat/completions"
    
    payload = {
        "model": "Qwen/Qwen3-32B",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.6,
        "max_tokens": max_tokens
    }
    
    print(f"📤 发送请求: {prompt[:50]}...")
    start_time = time.time()
    
    try:
        cmd = [
            'curl', '-s',
            '-H', 'Content-Type: application/json',
            '-d', json.dumps(payload),
            url
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode != 0:
            print(f"❌ curl 执行失败: {result.stderr}")
            return None
        
        response = json.loads(result.stdout)
        duration = (time.time() - start_time) * 1000
        
        if 'error' in response:
            print(f"❌ API 错误: {response['error']}")
            return None
        
        # 提取信息
        usage = response.get('usage', {})
        content = response['choices'][0]['message']['content']
        
        prompt_tokens = usage.get('prompt_tokens', 0)
        completion_tokens = usage.get('completion_tokens', 0)
        
        # 计算指标
        throughput = (completion_tokens / duration * 1000) if duration > 0 else 0
        latency_per_token = duration / completion_tokens if completion_tokens > 0 else 0
        
        # 打印性能报告
        print("\n" + "="*60)
        print("📊 性能指标报告")
        print("="*60)
        print(f"⏱️  总耗时:       {duration:.2f}ms ({duration/1000:.2f}s)")
        print(f"📥 输入Tokens:    {prompt_tokens}")
        print(f"📤 输出Tokens:    {completion_tokens}")
        print(f"⚡ 吞吐量:        {throughput:.2f} tokens/s")
        print(f"🎯 延迟/Token:    {latency_per_token:.2f} ms/token")
        print("="*60)
        
        print("\n📝 响应内容（前 200 字符）:")
        print("-" * 60)
        print(content[:200] + "..." if len(content) > 200 else content)
        print("-" * 60 + "\n")
        
        return {
            'duration': duration,
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'throughput': throughput,
            'content': content
        }
        
    except subprocess.TimeoutExpired:
        print("❌ 请求超时（300秒）")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败: {e}")
        print(f"响应内容: {result.stdout[:200]}")
        return None
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return None

def benchmark(num_requests: int = 3):
    """运行多次请求进行基准测试"""
    
    print(f"\n🚀 开始基准测试 ({num_requests} 个请求)\n")
    
    prompts = [
        "Give me a short introduction to large language models.",
        "What are the main applications of artificial intelligence?",
        "Explain quantum computing in simple terms."
    ]
    
    results = []
    
    for i, prompt in enumerate(prompts[:num_requests], 1):
        print(f"\n[请求 {i}/{num_requests}]")
        result = call_vllm(prompt)
        if result:
            results.append(result)
        time.sleep(1)  # 请求间隔
    
    # 汇总统计
    if results:
        print("\n" + "="*60)
        print("📈 汇总统计")
        print("="*60)
        
        durations = [r['duration'] for r in results]
        throughputs = [r['throughput'] for r in results]
        
        print(f"平均耗时:       {sum(durations)/len(durations):.2f}ms")
        print(f"最小耗时:       {min(durations):.2f}ms")
        print(f"最大耗时:       {max(durations):.2f}ms")
        
        print(f"\n平均吞吐量:     {sum(throughputs)/len(throughputs):.2f} tokens/s")
        print(f"最低吞吐量:     {min(throughputs):.2f} tokens/s")
        print(f"最高吞吐量:     {max(throughputs):.2f} tokens/s")
        print("="*60 + "\n")

if __name__ == "__main__":
    # 单次调用
    call_vllm("Give me a short introduction to large language models.")
    
    # 或者运行基准测试（取消注释下一行）
    # benchmark(num_requests=3)


```

---

> References

