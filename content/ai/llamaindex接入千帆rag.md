---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ORT7E3J%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEqNomOV%2BrfVWhacot%2FJixV86e1wCuNYMLJXUwZrfJvOAiEAtMUQ%2FZ0J0QSQpFgk%2BBmkRLWpVr6WyAP5Rqro9roZZZcqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN1G2r%2BC1Zp6DR7P%2FircA9e4QgZq7RWROs1Kuvh06BNsNcMiM%2B4n7v%2FpAi1rlsOzIVx6cqseV26Cigw4ShTLkXM7mjYggL3O%2BHJTMkjVF8S0yNnAy4sTO3Jp3V%2FHQfQOHylsrGM36Ai5vTDtvw%2BtRq2z7gJiafNClZeJM3HQsh7qcbNEq2PvV22eYaha1Jz8XDMJ2tsgmvQSwQ6tAB42zdWSYL1%2B%2FG%2Fi8fa19J7GBKpLhnc9%2Ftpknrw3IGzPfWO8awRx46dHR3N7PmJXWFgufsOkS%2B5ZhrDs8eIlqgDKav%2B6BKLBm7jff4dI2l%2BL18x203ll8lX68w9zOnvehnRTA%2FlxtpreGZd6Ba6h4SXqtQV52HzB2uoAnlc1d6NZTVoSmpKoxQ8PIdHfUPlG2Uny1DmhC%2Fnmx2aZhRlbHQ0Z5y%2FdqijtOI5XfH1wdfnYOfp0v%2Boam%2B5FAJO4%2B9aIpxkGEXH%2BA6SXeMe0aaeqPOlQ%2FK%2FX6Qu0%2FN6dwRUHzEx41J4nuOQrY5knUMUKL0VkfmDsxYPUHol9rMTLnRm9JfJkPtGa9f9TmUUdPwkrpWEJ8%2FE3hPyAVaB0KQMzTeKtpqvlxK2eMwu1Axy3QdN5m1vH5eu4sPZCsL4Hi5BvZrowPz8x7CXVbNSCddaDC%2BCLMI2jrMgGOqUB%2FMSJmMb6CkLhsS77JeV6raOBWQZJPBRCr7oCfigQvZ3FJ4GFvMTn87CbpmrEwF03KpED7sdaRtdkhf%2BN%2FPn%2B0fBl2gAnPSfder7sLwmkJNN%2FHFARLA2CD2DsEKN4SqMFEnKjXq5VuMPDmr6HfUO9LszU2HkGOLBq2w2xFhgeG1JO6adVT9bU1SB3q8cmqnoHOU72rHVkeEalhdSCyxJG2QVSndHD&X-Amz-Signature=b76a3cc33917c3141f21a150f916e84f33287af0f3b6eb8472d4bb287855c4f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ORT7E3J%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEqNomOV%2BrfVWhacot%2FJixV86e1wCuNYMLJXUwZrfJvOAiEAtMUQ%2FZ0J0QSQpFgk%2BBmkRLWpVr6WyAP5Rqro9roZZZcqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN1G2r%2BC1Zp6DR7P%2FircA9e4QgZq7RWROs1Kuvh06BNsNcMiM%2B4n7v%2FpAi1rlsOzIVx6cqseV26Cigw4ShTLkXM7mjYggL3O%2BHJTMkjVF8S0yNnAy4sTO3Jp3V%2FHQfQOHylsrGM36Ai5vTDtvw%2BtRq2z7gJiafNClZeJM3HQsh7qcbNEq2PvV22eYaha1Jz8XDMJ2tsgmvQSwQ6tAB42zdWSYL1%2B%2FG%2Fi8fa19J7GBKpLhnc9%2Ftpknrw3IGzPfWO8awRx46dHR3N7PmJXWFgufsOkS%2B5ZhrDs8eIlqgDKav%2B6BKLBm7jff4dI2l%2BL18x203ll8lX68w9zOnvehnRTA%2FlxtpreGZd6Ba6h4SXqtQV52HzB2uoAnlc1d6NZTVoSmpKoxQ8PIdHfUPlG2Uny1DmhC%2Fnmx2aZhRlbHQ0Z5y%2FdqijtOI5XfH1wdfnYOfp0v%2Boam%2B5FAJO4%2B9aIpxkGEXH%2BA6SXeMe0aaeqPOlQ%2FK%2FX6Qu0%2FN6dwRUHzEx41J4nuOQrY5knUMUKL0VkfmDsxYPUHol9rMTLnRm9JfJkPtGa9f9TmUUdPwkrpWEJ8%2FE3hPyAVaB0KQMzTeKtpqvlxK2eMwu1Axy3QdN5m1vH5eu4sPZCsL4Hi5BvZrowPz8x7CXVbNSCddaDC%2BCLMI2jrMgGOqUB%2FMSJmMb6CkLhsS77JeV6raOBWQZJPBRCr7oCfigQvZ3FJ4GFvMTn87CbpmrEwF03KpED7sdaRtdkhf%2BN%2FPn%2B0fBl2gAnPSfder7sLwmkJNN%2FHFARLA2CD2DsEKN4SqMFEnKjXq5VuMPDmr6HfUO9LszU2HkGOLBq2w2xFhgeG1JO6adVT9bU1SB3q8cmqnoHOU72rHVkeEalhdSCyxJG2QVSndHD&X-Amz-Signature=9c3c919c639eaae201386702178457e863f6eb1dcefff7ae2a4ab3184cd1b459&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

