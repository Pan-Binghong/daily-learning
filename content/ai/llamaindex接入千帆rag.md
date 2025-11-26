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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYC3T5A3%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Aul6%2FR9LF8ctSnomyDsdS7O0r04%2FvPpN5YbnLV1KsQIhAIXwZXE7%2BkZPGYTIAKNr1Acpg5J4SlXHVLnRVo7bgf4SKv8DCHsQABoMNjM3NDIzMTgzODA1Igxms4PLYUPNhtE4HgAq3AN0pdgYcb%2BbQ8fbEaHgn%2BheGwIKeV5SKOEG7ZLALJBm%2FgXieTB6mliPPypfeq4MDoVv%2FoN%2BjpAtXiEI4hDKj0Wqt7qEJL7O2S%2Fk%2FazERF0Ie96wi%2FEIUKjA1O%2F658C2JfBi%2Bx80RpfpSYieNYFaxlidWo%2Bj%2FnqSH445RIRFLNXi46dTawT5YvwasNYomluhKST%2BYpmnj6wXQGLzK8XJQcwSWoa7ekSPyPTFocZyObu8ttf6PBQf5sljzUCVxfZd5PAN%2B8QNuqZNYbudR1WemvyaBxid%2BGvNeZlIB4BXziCotkvJFmDVGUjnRwI1G%2FKKHCm24N1%2BGKIgXZj5BV6aQ9Kvdav%2BycrEaJ9MkYuHqsGE9RkM2vxOP9K1UvbjwBtgZ4XLao3ivdPXfSNOZqRxq7R7qj1VdNpHHrwEwOtmkj%2FikK%2BXipkW1aq9RNu9bhADWJh70pi6jY3%2FpgEsxyUnBSIZP5dOFRBrfdFIFXHkZvJXkxg%2FQ7h9HRRiMxVPVYXD9q6x2IR20147T8bXOPjO5iV%2BoqQdKJKDi3BChSiUe%2Bt166WMaIiu28gIzy9SBCHhsWVutdeUq549mAxlVlVeg3%2BXF98SHMdV%2F%2FBi%2BSk8CN0LeXgQX6uNnIvBx9rIFzCCsZnJBjqkAXYAupaz3fKexw4SUo5P3T0gvSBdVhyYwu%2FZEZimUxqsqtBDrmYayWtYIE9Ze5LmmqfqalsyEJAkyZFjVL9oFlf4JQKcLh5gujxdJBwTJ4LdFBsKDUe3QaAIhs5dSk7x3XYtHqj%2BHYknQRZJqUk1sC0HT8lwx5FGLhAmSIRfsTj%2B0317RLRCgDdOIZNkA%2FA323H%2B2CZiaQbzE2dFdmHeQV6jodat&X-Amz-Signature=0f045ba924a057c10aceee92fae60cd4db636142e9c7268a7f5f865ebeaa72c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYC3T5A3%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Aul6%2FR9LF8ctSnomyDsdS7O0r04%2FvPpN5YbnLV1KsQIhAIXwZXE7%2BkZPGYTIAKNr1Acpg5J4SlXHVLnRVo7bgf4SKv8DCHsQABoMNjM3NDIzMTgzODA1Igxms4PLYUPNhtE4HgAq3AN0pdgYcb%2BbQ8fbEaHgn%2BheGwIKeV5SKOEG7ZLALJBm%2FgXieTB6mliPPypfeq4MDoVv%2FoN%2BjpAtXiEI4hDKj0Wqt7qEJL7O2S%2Fk%2FazERF0Ie96wi%2FEIUKjA1O%2F658C2JfBi%2Bx80RpfpSYieNYFaxlidWo%2Bj%2FnqSH445RIRFLNXi46dTawT5YvwasNYomluhKST%2BYpmnj6wXQGLzK8XJQcwSWoa7ekSPyPTFocZyObu8ttf6PBQf5sljzUCVxfZd5PAN%2B8QNuqZNYbudR1WemvyaBxid%2BGvNeZlIB4BXziCotkvJFmDVGUjnRwI1G%2FKKHCm24N1%2BGKIgXZj5BV6aQ9Kvdav%2BycrEaJ9MkYuHqsGE9RkM2vxOP9K1UvbjwBtgZ4XLao3ivdPXfSNOZqRxq7R7qj1VdNpHHrwEwOtmkj%2FikK%2BXipkW1aq9RNu9bhADWJh70pi6jY3%2FpgEsxyUnBSIZP5dOFRBrfdFIFXHkZvJXkxg%2FQ7h9HRRiMxVPVYXD9q6x2IR20147T8bXOPjO5iV%2BoqQdKJKDi3BChSiUe%2Bt166WMaIiu28gIzy9SBCHhsWVutdeUq549mAxlVlVeg3%2BXF98SHMdV%2F%2FBi%2BSk8CN0LeXgQX6uNnIvBx9rIFzCCsZnJBjqkAXYAupaz3fKexw4SUo5P3T0gvSBdVhyYwu%2FZEZimUxqsqtBDrmYayWtYIE9Ze5LmmqfqalsyEJAkyZFjVL9oFlf4JQKcLh5gujxdJBwTJ4LdFBsKDUe3QaAIhs5dSk7x3XYtHqj%2BHYknQRZJqUk1sC0HT8lwx5FGLhAmSIRfsTj%2B0317RLRCgDdOIZNkA%2FA323H%2B2CZiaQbzE2dFdmHeQV6jodat&X-Amz-Signature=45d3f51aded17b97c3749ff97224b646bd4b5b2c82c8f9c2546d9293899727ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

