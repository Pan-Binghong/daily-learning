---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UURN3LGW%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNVrNIkZp9d8OQaSt9BHo6v8DCv98qRhdjGC5AEeai7QIgLx01LfDylewXq6P1jqgpV1WcLMQcYlMLT6wFDv0PT%2BMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHudCg47dRQkMSzq5CrcA36nasa9Cp5eChdf1k8%2BAJakMxEjeRTzZqb8EA%2FpwD7sjtiYfFmCQdGq%2Fx%2F5h7LyHbA%2BqYaAFXbo%2F45DZC1qkInXCfCTBMRwjj4GjHJGk5g2qwyPTGWCyZKwzudpfSVT9HKuaEjpkqwWm5%2FuzSBwfB1hmVsiab3%2FD5yIdxr64QERjXZgS%2BpbNhl7Io4FIdXW6YEQESXmvfQPIRq7HefYoB3UMv6eGNLhPwgRYS8gIKzXRhr0ekHL1c%2FDZ7hhoGl1CuUwbF5aBtAbqct2NdztzZH8uTd5rfidnicHMsgm1lCViEjwQ13GMzHtkRi2PEWW5SZU9tdEz1o9ggl9LE120PvW4LVxFqBOjuxj8jI400p9M5HzMhkyIU%2BQOuo3w2NlQB8mMovmEJiME2Ls9r2ul8YY3HC0RECOdDx%2BBtn0NKCUAjSt2b7PkX7IKhaR6TJg0WcKatgG%2FTDdHF3fpQu1PwaTBOQ1uCPM3aEmq6k4yHvuCSpyeCxkwMFsRyWpdSmpKDzd4QMwLeOKFlFJm8xTyIpuuQoDGeojbHTgHfB%2Fb7Eu7hnoOKVRN%2F54NALVw%2BRiz6kcHbZEjNpY71wGajgfSsAvmN0%2FQjjWcIyKJ0CZYS8vhTO0W3w%2B9oWTEO0lMPTIks4GOqUBmWqU8qsvSSaf%2FdQyoZnAkJ3nCTUNFRcm9hr%2BdnghnZHFgp3xMN2X0Bf4wWQRHxRzRN0PfogqkPfHAUMGD%2FBXWpLkgKu4oLOXzrQ6RVY2dpBFPVKmFrtGLV8CYY%2F4b%2FL4QQe0v%2F7%2BLun2Mvapa7H2ooqGclUi7r8wded2hc4PvJJPocp1MW3t7HQrWMjl2ru5RK4MwAVX4u%2BwEiMBQiraFjstdNvw&X-Amz-Signature=f4132ac316e7cc7bb2607e68eec579967f4a41a0c454c115ea092b9e8d657ebe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UURN3LGW%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNVrNIkZp9d8OQaSt9BHo6v8DCv98qRhdjGC5AEeai7QIgLx01LfDylewXq6P1jqgpV1WcLMQcYlMLT6wFDv0PT%2BMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHudCg47dRQkMSzq5CrcA36nasa9Cp5eChdf1k8%2BAJakMxEjeRTzZqb8EA%2FpwD7sjtiYfFmCQdGq%2Fx%2F5h7LyHbA%2BqYaAFXbo%2F45DZC1qkInXCfCTBMRwjj4GjHJGk5g2qwyPTGWCyZKwzudpfSVT9HKuaEjpkqwWm5%2FuzSBwfB1hmVsiab3%2FD5yIdxr64QERjXZgS%2BpbNhl7Io4FIdXW6YEQESXmvfQPIRq7HefYoB3UMv6eGNLhPwgRYS8gIKzXRhr0ekHL1c%2FDZ7hhoGl1CuUwbF5aBtAbqct2NdztzZH8uTd5rfidnicHMsgm1lCViEjwQ13GMzHtkRi2PEWW5SZU9tdEz1o9ggl9LE120PvW4LVxFqBOjuxj8jI400p9M5HzMhkyIU%2BQOuo3w2NlQB8mMovmEJiME2Ls9r2ul8YY3HC0RECOdDx%2BBtn0NKCUAjSt2b7PkX7IKhaR6TJg0WcKatgG%2FTDdHF3fpQu1PwaTBOQ1uCPM3aEmq6k4yHvuCSpyeCxkwMFsRyWpdSmpKDzd4QMwLeOKFlFJm8xTyIpuuQoDGeojbHTgHfB%2Fb7Eu7hnoOKVRN%2F54NALVw%2BRiz6kcHbZEjNpY71wGajgfSsAvmN0%2FQjjWcIyKJ0CZYS8vhTO0W3w%2B9oWTEO0lMPTIks4GOqUBmWqU8qsvSSaf%2FdQyoZnAkJ3nCTUNFRcm9hr%2BdnghnZHFgp3xMN2X0Bf4wWQRHxRzRN0PfogqkPfHAUMGD%2FBXWpLkgKu4oLOXzrQ6RVY2dpBFPVKmFrtGLV8CYY%2F4b%2FL4QQe0v%2F7%2BLun2Mvapa7H2ooqGclUi7r8wded2hc4PvJJPocp1MW3t7HQrWMjl2ru5RK4MwAVX4u%2BwEiMBQiraFjstdNvw&X-Amz-Signature=ff82a74b6193669988808a21edc8949ef8c38f4e8247f3853904e6e41f7094ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

