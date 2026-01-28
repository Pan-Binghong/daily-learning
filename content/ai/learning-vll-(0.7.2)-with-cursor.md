---
title: Learning vLL (0.7.2) with Cursor
date: '2025-04-14T00:38:00.000Z'
lastmod: '2025-04-14T09:00:00.000Z'
draft: false
tags:
- VLLM
categories:
- AI
---

> 💡 之前一直用cursor辅助写代码，突然试了一下去利用cursor来学代码，发现效果嘎嘎好。这里记录一下比较火的vllm中提升推理速度的一些关键代码。

# 1. What is vLLM？

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ccc90792-56ef-4142-8b21-8ecb32787141/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MMM3XNS%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBN2Yjf7rQ%2BEJIsarEBXZMFuSs2vsczJtpY5SaaUA%2F8wIhAKPzNYVY0POkZ0Zx%2B68LM1ez6gNLTDW3qQ0DihZN0sgZKv8DCGEQABoMNjM3NDIzMTgzODA1IgxtFKJdHzAnfVOEk5Iq3ANcAG6Ch9wRq7LBykeckiCAPZN8FWqMj3t1OgPFsLilxvwAboZ%2F%2FFKbvWsTpxdsy72KLHToWFs6kVRUwkvFMPY0LJykvBiqnbahfUeabPOSv3V24WzDYfJ28qY1Wb2HFZm6diyO%2Bqce4aXUQ8DiWiHNO2iNuMjgqGj%2BHoZPRUSG3C8iO6HOiWFMJPb7wg%2Fi2PIvounTY6aBmX8WBMEOJosNZqUv3l71dzFxP8iaXOdUCfeUGEYA4aly7w170cAXZsmG1qoC8IbG%2FsX86eyzwrdqf8LJHap7l6I%2FTcOTm8Bunxhu1Dgl6Ll9uE0wBC%2FplsQSe85BiTvIBTiZuImTgZJF8b%2FBbgjSCOYy7m2iqZhqJAZbQVrSt%2F7HsbPY6zqGb3PLjA0yjny%2FgpHvX56G%2FoyL2TuAAC7w0kQLMaoHfZejKodQVcihVE354AIgOYxuk%2B5N2D%2FqJXtV%2Bmtlo%2BIvq1Fgb2azo12FZ8ER32tKxqCTXrIrX9A1wUMDAwD9Aw9OldYMR%2FfnXLKB8G3fD%2FvIWYqQoGIljNOGiCiCBz05DIAHdb1mPmcslOtuZ3Bjn8CMg2NL1LLKhQzsn%2FW6QFUTvsEPieU965lVr3KeKBGTnKcST62TTOta%2FNLN1VaRrDCSluXLBjqkAeWWV3VmzbDjIAs%2BEYOO27vnbta78l8CNJX%2FSz%2BY%2F1u%2Fgux%2FcIfY3HHIbh3D2JSAa5WMs7h3MyMNO2aJGh8RqEjrOKeJtjRcdyk490XSgCy6dGnI3YjCsKT%2FDQRQdSadBtwFWwBRNodlINHyururarygEt9WtkIVqt7JIFzgufjjbFpDQi3ErZkVmHWZBA7V00bv4t32NusGnePkDfFYhtrbJpOx&X-Amz-Signature=3b94f72936ddd57f84b74933c49ab35465bbb763f4e27d33f4c835551100a3c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



vLLM是大模型推理加速框架。主要在KVcache管理中采用了PageAttention技术，支持市面上主流的开源大模型，支持量化类型为：GPTQ, AWQ, INT4, INT8, and FP8

---

# 2. KVcache相关的计算代码

使用claude-3.7-sonnet thinking，对vllm整个项目进行提问。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cb54e376-a945-4f40-a5b9-ff4fc10e9fc2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MMM3XNS%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBN2Yjf7rQ%2BEJIsarEBXZMFuSs2vsczJtpY5SaaUA%2F8wIhAKPzNYVY0POkZ0Zx%2B68LM1ez6gNLTDW3qQ0DihZN0sgZKv8DCGEQABoMNjM3NDIzMTgzODA1IgxtFKJdHzAnfVOEk5Iq3ANcAG6Ch9wRq7LBykeckiCAPZN8FWqMj3t1OgPFsLilxvwAboZ%2F%2FFKbvWsTpxdsy72KLHToWFs6kVRUwkvFMPY0LJykvBiqnbahfUeabPOSv3V24WzDYfJ28qY1Wb2HFZm6diyO%2Bqce4aXUQ8DiWiHNO2iNuMjgqGj%2BHoZPRUSG3C8iO6HOiWFMJPb7wg%2Fi2PIvounTY6aBmX8WBMEOJosNZqUv3l71dzFxP8iaXOdUCfeUGEYA4aly7w170cAXZsmG1qoC8IbG%2FsX86eyzwrdqf8LJHap7l6I%2FTcOTm8Bunxhu1Dgl6Ll9uE0wBC%2FplsQSe85BiTvIBTiZuImTgZJF8b%2FBbgjSCOYy7m2iqZhqJAZbQVrSt%2F7HsbPY6zqGb3PLjA0yjny%2FgpHvX56G%2FoyL2TuAAC7w0kQLMaoHfZejKodQVcihVE354AIgOYxuk%2B5N2D%2FqJXtV%2Bmtlo%2BIvq1Fgb2azo12FZ8ER32tKxqCTXrIrX9A1wUMDAwD9Aw9OldYMR%2FfnXLKB8G3fD%2FvIWYqQoGIljNOGiCiCBz05DIAHdb1mPmcslOtuZ3Bjn8CMg2NL1LLKhQzsn%2FW6QFUTvsEPieU965lVr3KeKBGTnKcST62TTOta%2FNLN1VaRrDCSluXLBjqkAeWWV3VmzbDjIAs%2BEYOO27vnbta78l8CNJX%2FSz%2BY%2F1u%2Fgux%2FcIfY3HHIbh3D2JSAa5WMs7h3MyMNO2aJGh8RqEjrOKeJtjRcdyk490XSgCy6dGnI3YjCsKT%2FDQRQdSadBtwFWwBRNodlINHyururarygEt9WtkIVqt7JIFzgufjjbFpDQi3ErZkVmHWZBA7V00bv4t32NusGnePkDfFYhtrbJpOx&X-Amz-Signature=724ffda283eeb6093b19e0d1fd941acc6acf096f8c704c9112307cd4b1d71dad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

为了更好举例，下载了deepseek-v3-0324版本的config.json，代入项目进行提问。

```json
{
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 8,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 128,
  "num_nextn_predict_layers": 1,
  "pretraining_tp": 1,模型中Transformer层的数量。更多的层数使得模型能够学习更深层次的特征和关系，但也增加了模型的深度和计算成本。

  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.46.3",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}

```

该文件中的关键信息为：

## 2.1 DeepSeek-V1的KVcache是如何计算的？

### 2.1.1 模型参数分析

从提供的config.json文件中提取的关键参数：

- hidden_size: 7168
- num_attention_heads: 128 (Q头数量)
- num_key_value_heads: 128 (KV头数量，无MHA结构)
- num_hidden_layers: 61 (Transformer层数)
- max_position_embeddings: 163840 (最大位置嵌入，表示支持的最大序列长度)
- torch_dtype: "bfloat16" (模型参数数据类型)
---

### 2.1.2 KV缓存显存计算

基础参数计算

- head_size = hidden_size / num_attention_heads = 7168 / 128 = 56
- 数据类型大小 = bfloat16 = 2字节
单个注意力层的KVcache计算

- key cache size = num_key_value_heads * head_size = 128 * 56 = 7168
- value cache size = key cache size = 7168
- 单层单token的KV缓存大小 = (key缓存项 + value缓存项) * dtype = (7168 + 7168) * 2 = 28672 ≈ 28kb
全模型最大KV缓存计算

- 全模型单token的KV缓存大小 = 单层token的KV缓存 * 模型层数 = 28kb * 61 = 1708kb ≈ 1.67MB
- 最大序列长度下的KV缓存大小 = 全模型单token的KV缓存大小 * 最大序列长度 = 273612.8MB ≈ 267.2GB
按块分配计算

如果使用vLLM的分块机制，假设block_size=16：

- 每个块大小 = 数据类型大小 * 注意力层数 * block_size * (key_cache_entry + value_cache_entry) = 2 * 61 * 16 * (7168+7168) ≈ 27.9MB
- 需要块的数量 = 最大序列长度 / block_size = 163840 / 16 = 10240块
- 总显存 = 每个块大小 * 需要的块数量 = 27.9MB * 10240 ≈ 286GB
实际应用考虑

1. 实际使用时可能不会用最大的序列长度，常见的设置为4K - 32K
1. 不同的block_size的选择会影响显存使用效率
例如，如果使用8K的序列长度:

- KV缓存 = 1.67MB * 8192 ≈ 13.7GB
---

### 2.1.3 计算KVcache代码的位置

在0.7.2版本中，vllm\worker\worker.py 

```python
@torch.inference_mode()
    def determine_num_available_blocks(self) -> Tuple[int, int]:
        """确定可用的KV缓存块数量。

        该方法会首先对现有内存使用情况进行分析,然后计算在剩余可用内存下可以分配的最大GPU和CPU块数量。

        主要步骤:
        1. 清空GPU缓存并重置内存统计信息
        2. 执行一次前向传播来分析模型的内存使用情况
        3. 根据GPU内存利用率和可用内存计算可分配的KV缓存块数量
        4. 记录详细的内存使用情况

        Returns:
            Tuple[int, int]: 返回(GPU块数量, CPU块数量)的元组
        """
        # 清空GPU缓存并重置内存统计信息
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()

        # 获取当前空闲内存和总GPU内存
        free_memory_pre_profile, total_gpu_memory = torch.cuda.mem_get_info()

        # 使用虚拟输入执行一次前向传播,分析模型内存使用情况
        with memory_profiling(
                self.baseline_snapshot,
                weights_memory=self.model_runner.model_memory_usage) as result:
            self.model_runner.profile_run()

        # 验证内存占用是否增加
        self._assert_memory_footprint_increased_during_profiling()

        # 计算当前实例可用的总内存
        memory_for_current_instance = total_gpu_memory * \
            self.cache_config.gpu_memory_utilization
        # 计算可用于KV缓存的内存
        available_kv_cache_memory = (memory_for_current_instance -
                                     result.non_kv_cache_memory)

        # 计算可分配的块数量
        cache_block_size = self.get_cache_block_size_bytes()
        if cache_block_size == 0:
            num_gpu_blocks = 0
            num_cpu_blocks = 0
        else:
            # 根据可用内存计算GPU和CPU块数量
            num_gpu_blocks = int(available_kv_cache_memory // cache_block_size)
            num_cpu_blocks = int(self.cache_config.swap_space_bytes //
                                 cache_block_size)
        num_gpu_blocks = max(num_gpu_blocks, 0)
        num_cpu_blocks = max(num_cpu_blocks, 0)

        # 构建详细的内存使用情况日志
        msg = (f"Memory profiling takes {result.profile_time:.2f} seconds\n"
               "the current vLLM instance can use "
               "total_gpu_memory "
               f"({(total_gpu_memory / GiB_bytes):.2f}GiB)"
               " x gpu_memory_utilization "
               f"({self.cache_config.gpu_memory_utilization:.2f})"
               f" = {(memory_for_current_instance / GiB_bytes):.2f}GiB\n"
               "model weights take "
               f"{(result.weights_memory / GiB_bytes):.2f}GiB;"
               " non_torch_memory takes "
               f"{(result.non_torch_increase / GiB_bytes):.2f}GiB;"
               " PyTorch activation peak memory takes "
               f"{(result.torch_peak_increase / GiB_bytes):.2f}GiB;"
               " the rest of the memory reserved for KV Cache is "
               f"{(available_kv_cache_memory / GiB_bytes):.2f}GiB.")

        logger.info(msg)
        # Final cleanup
        gc.collect()

        return num_gpu_blocks, num_cpu_blocks
```

---

## 2.2 在vLLM中实现PageAttention的代码在哪里？

关于PageAttention技术的实现，它主要在以下文件中：

1.  vllm/attention/ops/paged_attn.py：包含PagedAttention类，提供KV缓存形状、分割和写入等操作的接口
1.  vllm/_custom_ops.py：包含paged_attention_v1函数，连接到C++底层实现
1. csrc/attention/attention_kernels.cu：包含PageAttention的CUDA内核实现
1.  docs/source/design/kernel/paged_attention.md：详细解释了PageAttention的设计和实现原理
PageAttention是vLLM的核心技术，通过将KV缓存存储在不连续的内存块中，实现了高效的内存管理。这些内存块可以根据需要动态分配和释放，使得单个GPU能够服务更多并发请求。该技术的关键特点是通过分页机制避免了显存碎片，并支持高效的上下文处理。

---

# 3. 验证

使用4090D基于vllm启用默认参数进行推理。查看启动服务的日志内容。

## 3.1 模型日志

```bash
INFO 04-14 06:00:50 [__init__.py:239] Automatically detected platform cuda.
INFO 04-14 06:00:52 [api_server.py:1034] vLLM API server version 0.8.3
INFO 04-14 06:00:52 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/data/DeepSeek-R1-Distill-Qwen-1.5B', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/DeepSeek-R1-Distill-Qwen-1.5B', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, use_tqdm_on_load=True, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_config=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, enable_reasoning=False, reasoning_parser=None, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0x7f883404a7a0>)
INFO 04-14 06:01:01 [config.py:600] This model supports multiple tasks: {'score', 'generate', 'classify', 'embed', 'reward'}. Defaulting to 'generate'.
INFO 04-14 06:01:01 [config.py:1780] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 04-14 06:01:08 [__init__.py:239] Automatically detected platform cuda.
INFO 04-14 06:01:11 [core.py:61] Initializing a V1 LLM engine (v0.8.3) with config: model='/data/DeepSeek-R1-Distill-Qwen-1.5B', speculative_config=None, tokenizer='/data/DeepSeek-R1-Distill-Qwen-1.5B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/data/DeepSeek-R1-Distill-Qwen-1.5B, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":3,"custom_ops":["none"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":512}
WARNING 04-14 06:01:11 [utils.py:2413] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes,initialize_cache not implemented in <vllm.v1.worker.gpu_worker.Worker object at 0x7fd287cd4670>
INFO 04-14 06:01:12 [parallel_state.py:957] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0
INFO 04-14 06:01:12 [cuda.py:221] Using Flash Attention backend on V1 engine.
INFO 04-14 06:01:12 [gpu_model_runner.py:1258] Starting to load model /data/DeepSeek-R1-Distill-Qwen-1.5B...
WARNING 04-14 06:01:12 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
INFO 04-14 06:01:13 [loader.py:447] Loading weights took 0.95 seconds
INFO 04-14 06:01:14 [gpu_model_runner.py:1273] Model loading took 3.3465 GiB and 1.192773 seconds
INFO 04-14 06:01:23 [backends.py:416] Using cache directory: /root/.cache/vllm/torch_compile_cache/74d872966c/rank_0_0 for vLLM's torch.compile
INFO 04-14 06:01:23 [backends.py:426] Dynamo bytecode transform time: 9.12 s
INFO 04-14 06:01:26 [backends.py:132] Cache the graph of shape None for later use
INFO 04-14 06:01:54 [backends.py:144] Compiling a graph for general shape takes 30.65 s
INFO 04-14 06:02:03 [monitor.py:33] torch.compile takes 39.77 s in total
INFO 04-14 06:02:04 [kv_cache_utils.py:578] GPU KV cache size: 426,448 tokens
INFO 04-14 06:02:04 [kv_cache_utils.py:581] Maximum concurrency for 131,072 tokens per request: 3.25x
INFO 04-14 06:02:33 [gpu_model_runner.py:1608] Graph capturing finished in 29 secs, took 1.47 GiB
INFO 04-14 06:02:33 [core.py:162] init engine (profile, create kv cache, warmup model) took 79.67 seconds
WARNING 04-14 06:02:33 [config.py:1088] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
INFO 04-14 06:02:33 [serving_chat.py:117] Using default chat sampling params from model: {'temperature': 0.6, 'top_p': 0.95}
INFO 04-14 06:02:33 [serving_completion.py:61] Using default completion sampling params from model: {'temperature': 0.6, 'top_p': 0.95}
INFO 04-14 06:02:33 [api_server.py:1081] Starting vLLM API server on http://0.0.0.0:8000
INFO 04-14 06:02:33 [launcher.py:26] Available routes are:
INFO 04-14 06:02:33 [launcher.py:34] Route: /openapi.json, Methods: HEAD, GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /docs, Methods: HEAD, GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /docs/oauth2-redirect, Methods: HEAD, GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /redoc, Methods: HEAD, GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /health, Methods: GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /load, Methods: GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /ping, Methods: GET, POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /tokenize, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /detokenize, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/models, Methods: GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /version, Methods: GET
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/chat/completions, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/completions, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/embeddings, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /pooling, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /score, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/score, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/audio/transcriptions, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /rerank, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v1/rerank, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /v2/rerank, Methods: POST
INFO 04-14 06:02:33 [launcher.py:34] Route: /invocations, Methods: POST
INFO 04-14 06:02:44 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:02:54 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:04 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:14 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:24 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:34 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:44 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:03:54 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:04:04 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
INFO 04-14 06:04:12 [launcher.py:74] Shutting down FastAPI HTTP server.
INFO 04-14 06:04:14 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%

```

---

## 3.2 模型配置

```bash
{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151643,
  "hidden_act": "silu",
  "hidden_size": 1536,
  "initializer_range": 0.02,
  "intermediate_size": 8960,
  "max_position_embeddings": 131072,
  "max_window_layers": 21,
  "model_type": "qwen2",
  "num_attention_heads": 12,
  "num_hidden_layers": 28,
  "num_key_value_heads": 2,
  "rms_norm_eps": 1e-06,
  "rope_theta": 10000,
  "sliding_window": 4096,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.44.0",
  "use_cache": true,
  "use_mrope": false,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

---

## 3.3 计算验证

### 3.3.1 每个token的KV缓存大小计算

- head_size = hidden_size / num_attention_heads = 1536 / 12 = 128
- 单token单层的KV缓存 = 2(K和V) * num_key_value_heads * head_size * dtype  = 2 * 2 * 128 * 2 = 1024字节
- 全模型单token KV缓存 = 单token单层的KV缓存 * num_hidden_layers = 1024 * 28 = 28672字节
---

### 3.3.2 显存分配

- 总可用显存 = 24GB * 0.9 = 21.6GB
- 部分显存用于模型权重、激活值等
- 剩余显存用于KV缓存
---

### 3.3.3 可缓存的token数量

日志的结果为：INFO 04-14 06:02:04 [kv_cache_utils.py:578] GPU KV cache size: 426,448 tokens

- 根据日志结果反推可得到：剩余显存用于KV缓存 / 每个token的KV缓存大小 = 426448
- 剩余显存用于KV缓存大小为：11.38739 GB
---

# 4. vLLM中如何计算KVcache

接上一节，从vLLM代码层面分析，426,448个token的KV缓存容量是通过以下步骤计算得出的：

## 4.1 核心计算函数

```bash
worker.py: determine_num_available_blocks() → 计算可用块数量
cache_engine.py: get_cache_block_size() → 计算每个块大小
kv_cache_utils.py: get_kv_cache_configs() → 配置KV缓存
```

## 4.1.1 determine_num_available_blocks()

对于你的4090D(24GB)，使用0.9的gpu_memory_utilization：

- 总显存: 24GB × 0.9 ≈ 21.6GB
- 减去模型权重和激活值等非KV缓存部分
---

## 4.1.2 get_cache_blockZ_size()

> 💡 计算缓存块的大小

```python
@staticmethod
def get_cache_block_size(cache_config, model_config, parallel_config):
    head_size = model_config.get_head_size()  # 128
    num_heads = model_config.get_num_kv_heads(parallel_config)  # 2
    num_attention_layers = model_config.get_num_layers_by_block_type(
        parallel_config, LayerBlockType.attention)  # 28
    
    # 获取数据类型大小
    if cache_config.cache_dtype == "auto":
        dtype = model_config.dtype  # bfloat16
    else:
        dtype = STR_DTYPE_TO_TORCH_DTYPE[cache_config.cache_dtype]
    
    # 计算key缓存项和value缓存项大小
    key_cache_entry = num_heads * head_size  # 2 * 128 = 256
    value_cache_entry = key_cache_entry  # 256
    
    # 计算一个块的总元素数
    total = num_attention_layers * cache_config.block_size * (key_cache_entry + value_cache_entry)
    # 28 * 16 * (256 + 256) = 28 * 16 * 512 = 229,376个元素
    
    # 每个元素的字节大小(bfloat16 = 2字节)
    dtype_size = get_dtype_size(dtype)  # 2
    
    # 返回块大小(字节)
    return dtype_size * total  # 2 * 229,376 = 458,752字节
```

---

## 4.1.3 determine_num_available_blocks()

> 💡 计算可用块的数量

重新回到determine_num_available_blocks() 

```python
cache_block_size = self.get_cache_block_size_bytes()
num_gpu_blocks = int(available_kv_cache_memory // cache_block_size)
```

这里claude-3.7-sonnet回复结果为：

计算可用块数：

- 假设可用于KV缓存的显存约为12.2GB
- 每个块大小为458.75KB
- 块数量 = 12.2GB ÷ 458.75KB ≈ 26,653块
我觉得12.2GB不是很严谨，专门去查了一下如何估算出12.2GB的过程。代入qwen1.5b模型，推荐场景下不需要计算梯度，所以产生的显存类型应该为：模型权重和前传的激活值。模型权重的计算：参数量 * dtype ≈ 3GB，前传的激活值，没查到来源依据。

---

## 4.1.4 _get_kv_cache_config_uniform_type()

```python
def _get_kv_cache_config_uniform_type(vllm_config: VllmConfig,
                                      kv_cache_spec: KVCacheSpec,
                                      available_memory: int,
                                      num_layers: int) -> KVCacheConfig:
    """
    为具有单一类型KV缓存的模型生成KV缓存配置。
    将可用内存平均分配给所有层。

    参数:
        vllm_config: 全局VllmConfig配置
        kv_cache_spec: 模型的KV缓存规格
        available_memory: KV缓存可用的内存大小(字节)
        num_layers: 模型的层数

    返回:
        生成的KVCacheConfig配置
    """

    # 获取所有层的页面大小(字节)
    page_sizes = {layer.page_size_bytes for layer in kv_cache_spec.values()}
    # 确保所有层使用相同的页面大小
    assert len(page_sizes) == 1
    page_size = page_sizes.pop()

    # 计算每层可分配的块数
    num_blocks = int(available_memory // page_size // num_layers)
    num_blocks = max(num_blocks, 0)

    # 如果配置中指定了GPU块数的覆盖值,则使用该值
    if vllm_config.cache_config.num_gpu_blocks_override is not None:
        num_gpu_blocks_override = \
            vllm_config.cache_config.num_gpu_blocks_override
        logger.info(
            "使用num_gpu_blocks_override=%d覆盖原始num_gpu_blocks=%d",
            num_gpu_blocks_override, num_blocks)
        num_blocks = num_gpu_blocks_override

    # 记录GPU块数信息
    logger.info("GPU块数: %d", num_blocks)
    # 计算最大并发度
    max_concurrency = (num_blocks * vllm_config.cache_config.block_size /
                       vllm_config.model_config.max_model_len)
    logger.info("每个请求%s个token时的最大并发度: %.2fx",
                vllm_config.model_config.max_model_len, max_concurrency)

    # 计算每层的内存大小
    per_layer_size = page_size * num_blocks

    # 创建KV缓存配置
    kv_cache_config = KVCacheConfig(
        num_blocks=num_blocks,
        # 为每一层创建相同大小的KV缓存张量
        tensors={
            layer_name: KVCacheTensor(size=per_layer_size)
            for layer_name in kv_cache_spec
        },
        # 将所有层组织为一个组
        groups=[[layer_name for layer_name in kv_cache_spec]],
        kv_cache_spec=kv_cache_spec)
    return kv_cache_config
    
# 总token容量 = 块数量 * 每块存储的token数
total_tokens = num_gpu_blocks * block_size
logger.info("GPU KV cache size: %d tokens", total_tokens)
```

总token容量 = 26653 * 16 = 426448， 与日志对比发现数值一致。

