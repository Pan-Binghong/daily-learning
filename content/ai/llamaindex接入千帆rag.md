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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSYRUDBP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVRlvPmkO%2BTbsGefV9bez3mcNBkv7csp3f3SpsCgccwwIhAN3s%2F%2BX9lZhZFkmlFfYWfsXA7hJl2xHRgnIcZJSNsPajKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg0hsoDxV%2BwCOT1coq3APKF0k97zpYebgCiSgOpMSdF7tFfD7tYuQUCrdSzpa0W9N5vPo8Ng2WUkMnFejV%2BCyuxQ%2FGqb5%2FVQYsFCveD%2BrKy9Y6WhgfHJ9HhQ4hKbwdkIHBeqLHfVo%2BM8K0zI0FovUwaHmH%2FD8yYYrIEyrzanL5q7xAsQ%2FQ7wwX9l7g9S5CMWbVHXZIVbWoeWRU05kV%2Fj4HumfT8QvN0z%2F%2Bnr1BzA7hMM0ioho6ITmPXeYxekHN787PhvRyGDeUQDp5BGR3Arf%2B%2FKyG403%2Fn3LkP8Hn2tufBCfKGRLAjmnlGbRr6EdH04245Dd1UrVsF%2FqI8yn83Rsfur1XlVzkQain%2FYxHzUK0X5zuSRfNtt5LP6cHAkomgBEXfQK%2BWmRF8vh3D4i%2BRA2BqYDSYpnXHNBflRsVf3o4wrPpP6ab972eJzd6rfdEVXvKrE%2F6n8Jkh96JlNl56WAqN5YQKNSrB7AVvwBN6IJFeu5glKibquSbsdF44Z3T8eoSK8XzxFm%2BdWBQ7c0BsJuFGKxOU6wAO6qNoLa%2BrlEUl7%2BAxHJEmJx3lq4ASh6nwjoxcW0tTiZOjzjKZRAO%2B%2F8HwpvuLXvOA%2BZDiX4KJKNJYaCAByFN2VzK68S6xKvcuDUNR9EY4PB20Nz40TDC8K%2FIBjqkARuqUKY30QLmOsejRyQq3W0L%2ByJoyF%2B5haUrTZQYk7pGK1cE7MjgS4ZYux0n9ky0%2FM%2FV3fP%2FEzJY7CSryDgncaoaYgwfb0LRfpoioB4rcKWVpmgkxr09pdYmTSDKol%2FkVes6LwF6%2Bb6MpZLo%2Bpvb4kWL0O2EF42btWrSxtvT5k%2BDdDfTohWtyrDzNMh4zIgPj02o84pHSUCtRT%2FcmsQCiVu3tK8O&X-Amz-Signature=f1f64d50e7273b08909c73b283e9650a42c16522a5b817b4c9d77df6ddb533ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSYRUDBP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVRlvPmkO%2BTbsGefV9bez3mcNBkv7csp3f3SpsCgccwwIhAN3s%2F%2BX9lZhZFkmlFfYWfsXA7hJl2xHRgnIcZJSNsPajKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg0hsoDxV%2BwCOT1coq3APKF0k97zpYebgCiSgOpMSdF7tFfD7tYuQUCrdSzpa0W9N5vPo8Ng2WUkMnFejV%2BCyuxQ%2FGqb5%2FVQYsFCveD%2BrKy9Y6WhgfHJ9HhQ4hKbwdkIHBeqLHfVo%2BM8K0zI0FovUwaHmH%2FD8yYYrIEyrzanL5q7xAsQ%2FQ7wwX9l7g9S5CMWbVHXZIVbWoeWRU05kV%2Fj4HumfT8QvN0z%2F%2Bnr1BzA7hMM0ioho6ITmPXeYxekHN787PhvRyGDeUQDp5BGR3Arf%2B%2FKyG403%2Fn3LkP8Hn2tufBCfKGRLAjmnlGbRr6EdH04245Dd1UrVsF%2FqI8yn83Rsfur1XlVzkQain%2FYxHzUK0X5zuSRfNtt5LP6cHAkomgBEXfQK%2BWmRF8vh3D4i%2BRA2BqYDSYpnXHNBflRsVf3o4wrPpP6ab972eJzd6rfdEVXvKrE%2F6n8Jkh96JlNl56WAqN5YQKNSrB7AVvwBN6IJFeu5glKibquSbsdF44Z3T8eoSK8XzxFm%2BdWBQ7c0BsJuFGKxOU6wAO6qNoLa%2BrlEUl7%2BAxHJEmJx3lq4ASh6nwjoxcW0tTiZOjzjKZRAO%2B%2F8HwpvuLXvOA%2BZDiX4KJKNJYaCAByFN2VzK68S6xKvcuDUNR9EY4PB20Nz40TDC8K%2FIBjqkARuqUKY30QLmOsejRyQq3W0L%2ByJoyF%2B5haUrTZQYk7pGK1cE7MjgS4ZYux0n9ky0%2FM%2FV3fP%2FEzJY7CSryDgncaoaYgwfb0LRfpoioB4rcKWVpmgkxr09pdYmTSDKol%2FkVes6LwF6%2Bb6MpZLo%2Bpvb4kWL0O2EF42btWrSxtvT5k%2BDdDfTohWtyrDzNMh4zIgPj02o84pHSUCtRT%2FcmsQCiVu3tK8O&X-Amz-Signature=a1f3414fbcb1b569671d80a1638707e4b2808383919f9168785c63112b21d62e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

