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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UTHGWWN%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIArAUuISGP%2Bg1bwIP5qC6UvOtof0cVL14pUa5SFWEKh2AiEAvnMJLRcwB7yz%2F4Kv0hOcKnsDQ3TFWAyvviBGz4zP8iwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FT9i1HwmWmr3P%2F7yrcA4BILUYS1NSzdDze63ERYLPriEuLPxB%2Bn4GFQi9TkSWD95JMVDGupibW2hRAmK2jCQf6wbeO3zquDXD7c28%2FWz4oFEsHTl7ZVP64IWnq681E2AHSR7OIjrWSsl8ARLR9hNp4tvKy%2FH2LYmquClwN2u2C0RL%2B6zSrYyATRESwQTGYdS0duu%2F9afa0iselsg680x9UJYj2GeUvSQvkNmSVvXZ%2FTt2dEr6XnPmctLPHxI%2F0YdgKP5ZJHjBo2F%2BNBkIDbz2g0891X5OWnJ%2FZuAL4yq1Q2XUzjvdMZhnU7Ut0XMJ1Fx9ZyP3ORpfH82LHN%2BbwVzfcehC1b4fL9HHK02r0Oms2uLXLDmoFDdq6SQGA8qCEqk6Veolchn75ZoWpSY9%2FDT5dkG3KVLLTXSaGl2ilzxl1W67gyuF6Zw%2B6nrKyxgVz2wkTEJ8hvw3B6zQnPqlkGknTd3VbrVaQ6Q%2BeV540%2BrVyVxxdns2yYs6vm3%2Blgr%2BIi672pOmqBNEnIaz0IAK3mSUkEYxfEmSuRvh1PmtyMc48QGuNvaho8WHIPO1G7H5Ku9glqmLbBkjZO84dec6S7ewDPhrvsI1POkCC8Ms1Yrscngsdxua61xhEpw%2F01mVTkLQvVIhMYc2iHcppMNXXxcsGOqUBJZLqKhEj7a%2BmBUdhjolTaCIdR8f6TwJDazGS9k%2FST3FjI97w%2Bj0tEFKHBn3oEdIGdX3bC2Ni4SuF5ih3RTDZJa5cRPfxeFuX2Cb8XxPwlEFweX9g0AkuoRId9QPYPOub6jSggcN1j2LZrvCc%2F6yCyjcaeOcuifi0G8Ci%2BjGBKWNUcNwbEXsTX0nMaAPHNyXw2Hchr39kpwxFa%2B5qQwQIj3nKm1rc&X-Amz-Signature=04d13f86299abc130acbc6a0dfd7b4a55225f058f572afeb0636f54578974a04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UTHGWWN%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIArAUuISGP%2Bg1bwIP5qC6UvOtof0cVL14pUa5SFWEKh2AiEAvnMJLRcwB7yz%2F4Kv0hOcKnsDQ3TFWAyvviBGz4zP8iwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FT9i1HwmWmr3P%2F7yrcA4BILUYS1NSzdDze63ERYLPriEuLPxB%2Bn4GFQi9TkSWD95JMVDGupibW2hRAmK2jCQf6wbeO3zquDXD7c28%2FWz4oFEsHTl7ZVP64IWnq681E2AHSR7OIjrWSsl8ARLR9hNp4tvKy%2FH2LYmquClwN2u2C0RL%2B6zSrYyATRESwQTGYdS0duu%2F9afa0iselsg680x9UJYj2GeUvSQvkNmSVvXZ%2FTt2dEr6XnPmctLPHxI%2F0YdgKP5ZJHjBo2F%2BNBkIDbz2g0891X5OWnJ%2FZuAL4yq1Q2XUzjvdMZhnU7Ut0XMJ1Fx9ZyP3ORpfH82LHN%2BbwVzfcehC1b4fL9HHK02r0Oms2uLXLDmoFDdq6SQGA8qCEqk6Veolchn75ZoWpSY9%2FDT5dkG3KVLLTXSaGl2ilzxl1W67gyuF6Zw%2B6nrKyxgVz2wkTEJ8hvw3B6zQnPqlkGknTd3VbrVaQ6Q%2BeV540%2BrVyVxxdns2yYs6vm3%2Blgr%2BIi672pOmqBNEnIaz0IAK3mSUkEYxfEmSuRvh1PmtyMc48QGuNvaho8WHIPO1G7H5Ku9glqmLbBkjZO84dec6S7ewDPhrvsI1POkCC8Ms1Yrscngsdxua61xhEpw%2F01mVTkLQvVIhMYc2iHcppMNXXxcsGOqUBJZLqKhEj7a%2BmBUdhjolTaCIdR8f6TwJDazGS9k%2FST3FjI97w%2Bj0tEFKHBn3oEdIGdX3bC2Ni4SuF5ih3RTDZJa5cRPfxeFuX2Cb8XxPwlEFweX9g0AkuoRId9QPYPOub6jSggcN1j2LZrvCc%2F6yCyjcaeOcuifi0G8Ci%2BjGBKWNUcNwbEXsTX0nMaAPHNyXw2Hchr39kpwxFa%2B5qQwQIj3nKm1rc&X-Amz-Signature=c63948bc83ed46b64a19c61597a98b68edc83ce2ad20e8f85451156b0cd5c1c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

