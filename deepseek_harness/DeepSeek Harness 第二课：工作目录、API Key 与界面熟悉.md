# DeepSeek Harness 第二课：工作目录、API Key 与界面熟悉

## 一、本节内容

本节完成 DeepSeek Harness 第一次使用前的基本配置：

```
启动 Harness
    ↓
配置工作目录
    ↓
获取 DeepSeek API Key
    ↓
配置 API Key
    ↓
选择模型
    ↓
熟悉 Harness 界面
    ↓
完成第一次 Agent 对话
```

完成本节后，可以使用 DeepSeek Harness 对指定项目目录进行分析、创建文件、修改代码以及执行相关任务。

# 二、什么是工作目录？

在 DeepSeek Harness 中，**Workspace（工作区）就是 AI Agent 可以工作的项目目录。**

例如电脑上有一个 Python 项目：

```
D:\python_project
│
├── main.py
├── utils.py
├── requirements.txt
└── README.md
```

将：

```
D:\python_project
```

设置为 Workspace 后，Harness 就可以围绕这个目录进行工作。

例如：

```
分析这个项目
```

Agent 可以读取项目中的文件。

又例如：

```
帮我找到项目中的 Bug
```

Agent 可以检查项目代码。

还可以：

```
创建一个 README.md
```

或者：

```
修改 main.py
```

# 三、为什么需要 Workspace？

传统聊天机器人主要处理：

```
用户
 ↓
文字
 ↓
AI
 ↓
文字
```

而 Harness 面向的是 Agent 工作流：

```
用户
 ↓
Agent
 ↓
Workspace
 ├── 文件
 ├── 代码
 ├── 项目
 └── 目录
```

因此 Harness 不只是回答问题，还需要知道：

> **“我应该在哪个项目里工作？”**

Workspace 就是对这个问题的回答。

# 四、启动目录和 Workspace 的关系

这里需要区分两个概念：

## 1. 启动目录

执行：

```
dsh web
```

时，CMD 当前所在的目录就是 `dsh` 进程的启动目录。

例如：

```
cd D:\python_project
```

然后：

```
dsh web
```

那么：

```
D:\python_project
```

就是 Harness 的默认文件系统位置。

官方文档明确说明：

> `dsh` 进程会把启动时所在的目录作为默认文件系统位置。

## 2. Workspace

但是：

> **启动目录 ≠ 已经选择的 Workspace**

一个全新的 Web UI 启动以后，并不会自动选择 Workspace。

需要在界面中：

```
Choose workspace
```

然后添加并选择项目目录。

官方文档明确说明，新启动的 Web UI 默认没有选中的 Workspace，必须添加并选择一个工作区。

# 五、推荐的工作目录启动方式

假设有一个项目：

```
D:\AI_Project
```

推荐：

```
cd D:\AI_Project
```

然后：

```
dsh web
```

启动以后：

```
Choose workspace
        ↓
选择 D:\AI_Project
        ↓
进入项目 Workspace
```

这样：

```
D:\AI_Project
```

就成为当前 Agent 的工作区。

# 六、如何选择 Workspace？

进入 Harness Web UI 后，找到：

```
Choose workspace
```

点击以后选择项目目录。

例如：

```
D:\
 ├── AI_Project
 ├── Python_Project
 ├── Spider_Project
 └── Test_Project
```

如果当前学习的是：

```
Python_Project
```

就选择：

```
D:\Python_Project
```

# 七、Workspace 的作用范围

Workspace 是 Agent 工作的主要文件范围。

例如：

```
D:\Python_Project
│
├── main.py
├── user.py
├── database.py
└── README.md
```

设置：

```
D:\Python_Project
```

作为 Workspace 后，可以让 Agent：

```
读取文件
   ↓
分析代码
   ↓
修改文件
   ↓
创建文件
   ↓
运行命令
```

# 八、Workspace 并不等于“上传文件”

这一点非常重要。

使用 Harness 时：

```
Workspace
```

指的是：

> **电脑上的真实目录。**

不是：

```
上传到云端的文件
```

例如：

```
D:\Python_Project\main.py
```

仍然保存在自己的电脑上。

Harness 根据权限访问这个工作目录中的文件。

# 九、Workspace 与普通聊天的区别

普通聊天：

```
你：
帮我看看这段代码有没有问题？

AI：
分析你发送过来的代码
```

Harness：

```
你：
帮我检查这个项目有没有 Bug

        ↓

Agent

        ↓

Workspace

        ↓

读取项目文件

        ↓

分析代码

        ↓

执行工具

        ↓

修改 / 测试

        ↓

返回结果
```

因此：

> **Workspace 是 Harness 从“聊天工具”进入“项目工作环境”的关键一步。**

# 十、获取 DeepSeek API Key

DeepSeek Harness 需要模型服务才能运行 Agent。

使用 DeepSeek 官方模型时，需要：

```
DeepSeek API Key
```

DeepSeek 官方 API 文档明确要求，在调用 DeepSeek API 前需要先创建 API Key。

# 十一、API Key 是什么？

可以把 API Key 理解成：

> **程序访问 DeepSeek API 的身份凭证。**

普通网页使用：

```
登录账号
   ↓
密码
   ↓
访问服务
```

程序调用 API：

```
程序
 ↓
API Key
 ↓
DeepSeek API
 ↓
模型
```

因此 API Key 相当于：

```
“允许这个程序使用我的 DeepSeek API 服务”
```

# 十二、获取 API Key

进入 DeepSeek 开放平台：

```
https://platform.deepseek.com/
```

登录 DeepSeek 账号。

进入 API Key / API Keys 管理页面。

选择：

```
创建 API Key
```

按照页面提示创建。

创建成功后会得到一串密钥。

API Key 通常以：

```
sk-
```

开头。

例如：

```
sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

**示例中的 Key 只是格式示例，不是真实密钥。**

DeepSeek 官方文档也说明 API Key 是创建 API 后进行认证所需的凭证。

# 十三、API Key 安全注意事项

API Key 属于敏感凭证。

不要：

```
❌ 发到微信群
❌ 发到 QQ 群
❌ 发到 GitHub
❌ 写进公开代码
❌ 截图公开发布
❌ 发给其他人使用
```

尤其不要把真实 API Key 写进：

```
main.py
README.md
Git 仓库
```

如果 API Key 泄露，其他人可能使用你的 API 额度。

# 十四、在 Harness 中配置 API Key

启动 Harness：

```
dsh web
```

进入 Web UI。

打开：

```
Settings
   ↓
Models
```

官方当前 Web UI 的模型配置入口就是：

```
Settings → Models
```

在 DeepSeek 模型配置区域输入 API Key，然后保存。

# 十五、配置步骤

完整流程：

```
Settings
   ↓
Models
   ↓
DeepSeek
   ↓
API Key
   ↓
输入 Key
   ↓
Save
```

例如：

```
API Key：

sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

然后点击：

```
Save
```

# 十六、配置完成以后需要重启吗？

**不需要。**

DeepSeek Harness 官方文档明确说明：

> 模型配置修改后，在下一次请求时立即生效，不需要重启服务器。

因此：

```
输入 API Key
      ↓
Save
      ↓
直接开始使用
```

不需要：

```
Ctrl + C
```

也不需要重新：

```
dsh web
```

# 十七、Harness 如何保存 API Key？

DeepSeek Harness 当前不会把 API Key 直接保存到普通的设置配置中。

官方文档说明：

```
API Key
   ↓
凭据系统
   ↓
$DSH_HOME/.credentials.yaml
```

Settings 中保存的是：

```
Credential Reference
```

而不是明文 API Key。

同时，保存以后页面只会收到脱敏后的凭据描述，不会重新返回完整的明文 Key。

因此：

> **API Key 配置完成后，如果界面没有再次显示完整 Key，这是正常现象。**

# 十八、模型配置

进入：

```
Settings
   ↓
Models
```

可以看到模型提供商配置。

DeepSeek 官方 Harness 当前提供 DeepSeek 模型配置入口。

配置完成后：

```
API Key
   ↓
DeepSeek API
   ↓
DeepSeek Model
   ↓
Harness Agent
```

# 十九、API Key 与模型是什么关系？

需要区分：

### API Key

解决：

> **“我有没有权限调用 DeepSeek API？”**

### Model

解决：

> **“我要调用哪个模型？”**

关系：

```
API Key
   ↓
身份认证
   ↓
DeepSeek API
   ↓
Model
   ↓
返回结果
```

因此：

```
只有 API Key
```

不代表已经理解模型配置。

而：

```
API Key + Model
```

才构成完整的模型调用配置。

# 二十、第一次进入 Harness 的界面

完成 Workspace 和 API Key 配置后，就可以开始认识 Harness 的主要界面。

整体可以理解为：

```
┌─────────────────────────────────────────────┐
│                  顶部区域                    │
├──────────────┬────────────────┬─────────────┤
│              │                │             │
│   Workspace  │   Conversation │   Sidebar   │
│   / Session  │                │             │
│              │                │             │
│              │                │             │
├──────────────┴────────────────┴─────────────┤
│                  输入区域                    │
└─────────────────────────────────────────────┘
```

具体布局可能随着 Developer Preview 版本更新而变化。

# 二十一、左侧区域：Workspace / Session

左侧主要用于：

```
Workspace
Session
```

可以理解成：

```
Workspace
   ↓
项目
   ↓
Session
   ↓
具体一次 Agent 工作
```

例如：

```
Python_Project
│
├── Session 1：分析项目结构
├── Session 2：修复登录 Bug
└── Session 3：增加日志功能
```

# 二十二、什么是 Session？

Session 可以理解成：

> **一次独立的 Agent 工作会话。**

例如：

```
Session 1
“帮我分析这个项目”
```

然后 Agent：

```
读取文件
 ↓
分析项目
 ↓
输出结果
```

之后可以继续在这个 Session 中工作。

例如：

```
再帮我检查数据库部分
```

Agent 可以基于当前会话继续工作。

# 二十三、中间区域：Conversation

中间区域是主要的：

```
Agent 对话区域
```

这里可以看到：

```
用户消息
     ↓
Agent 思考 / 执行
     ↓
工具调用
     ↓
执行结果
     ↓
Agent 回复
```

与普通聊天最大的区别是：

> **这里不仅显示文字回答，还可能显示 Agent 的工具调用和执行过程。**

# 二十四、输入区域

底部是任务输入区域。

例如：

```
分析这个项目的目录结构，并告诉我每个主要文件的作用。
```

发送后，Agent 会根据：

```
Workspace
+
Model
+
Tools
+
你的任务
```

执行工作。

# 二十五、Agent 与普通聊天的区别

普通聊天：

```
问题
 ↓
模型
 ↓
答案
```

Harness：

```
任务
 ↓
Agent
 ↓
判断需要做什么
 ↓
调用工具
 ↓
读取文件
 ↓
执行命令
 ↓
分析结果
 ↓
继续执行
 ↓
最终结果
```

所以 Harness 的核心不是：

> “让模型回答得更像人。”

而是：

> **让模型能够围绕目标调用工具完成任务。**

# 二十六、工具调用

Agent 执行任务时，可能会使用工具。

例如：

```
读取文件
搜索文件
修改文件
运行命令
执行代码
```

这些工具让模型从：

```
只能“说”
```

变成：

```
可以“做”
```

# 二十七、为什么有时候需要确认？

Harness 并不是让 Agent 无限制地执行所有操作。

某些操作可能需要用户确认。

例如：

```
修改文件
```

或者：

```
执行某个命令
```

此时 Web UI 可能出现：

```
Approve
```

或者：

```
Reject
```

让用户决定是否允许执行。

官方文档明确说明，如果某项操作根据当前权限策略需要审批，Web UI 会先向用户请求批准。

# 二十八、右侧区域

右侧区域用于显示与当前工作相关的信息。

根据当前安装的 Harness 版本和插件，可能看到：

```
文件
工具
任务
文档
Agent 状态
```

其中 Workspace 文件浏览相关功能可以帮助查看当前项目目录。

官方客户端目前包含 Workspace、文件树、会话、工具调用、审批等多个 UI 模块。

# 二十九、Settings 设置

Settings 是 Harness 的配置中心。

当前可以通过：

```
Settings
```

进入不同配置页面。

其中本节最重要的是：

```
Settings
   ↓
Models
```

用于配置：

```
DeepSeek API Key
模型
其他模型提供商
自定义模型 API
```

官方当前也支持添加第三方模型提供商以及自定义 OpenAI-compatible API。

# 三十、第一次完整配置

第一次使用 Harness，可以按照下面流程操作：

```
① 启动 Harness
       ↓
② 打开 Web UI
       ↓
③ Choose workspace
       ↓
④ 添加项目目录
       ↓
⑤ 选择 Workspace
       ↓
⑥ Settings
       ↓
⑦ Models
       ↓
⑧ 配置 DeepSeek API Key
       ↓
⑨ Save
       ↓
⑩ 创建 / 进入 Session
       ↓
⑪ 输入第一个任务
```

# 三十一、第一次任务

Workspace 和 API Key 配置完成以后，可以输入一个简单任务进行测试：

```
请分析当前项目的目录结构，并告诉我这个项目主要由哪些部分组成。
```

Agent 应该能够：

```
读取 Workspace
      ↓
查看目录
      ↓
分析文件
      ↓
整理项目结构
      ↓
返回结果
```

# 三十二、推荐第一次测试

可以依次测试三个任务。

## 测试一：读取项目

```
请分析当前项目的目录结构。
```

目的：

```
确认 Workspace 正常
```

## 测试二：读取文件

```
请找到项目中的入口文件，并告诉我这个项目是如何启动的。
```

目的：

```
确认 Agent 可以读取项目文件
```

## 测试三：创建文件

```
请在项目根目录创建一个 test.md，内容写入：
DeepSeek Harness 测试成功。
```

目的：

```
确认 Agent 可以执行文件操作
```

如果 Harness 要求审批：

```
Approve
```

允许操作即可。

# 三十三、常见问题

## 1. 没有 Workspace，为什么不能输入任务？

因为新的 Web UI 默认没有选中的 Workspace。

点击：

```
Choose workspace
```

添加并选择一个目录。

官方文档明确说明，在选择 Workspace 之前，会话输入区域不可用。

## 2. API Key 配置以后为什么看不到完整 Key？

这是正常现象。

Harness 的凭据机制采用：

```
只写
+
脱敏引用
```

保存后不会再次返回完整明文 Key。

## 3. API Key 配置以后需要重启吗？

不需要。

保存后下一次请求即可生效。

## 4. 出现 401 Authentication Fails

通常表示：

```
API Key 错误
```

DeepSeek 官方 API 文档中：

```
401
Authentication Fails
```

对应的主要原因就是认证失败，需要检查 API Key。

## 5. 出现 402

如果出现：

```
402
```

通常表示：

```
Insufficient Balance
```

也就是 API 账户余额不足。

DeepSeek 官方错误码文档将 402 定义为余额不足。

# 三十四、本节知识结构

```
DeepSeek Harness
│
├── Workspace
│   ├── 工作目录
│   ├── 项目文件
│   └── Agent 工作范围
│
├── Model
│   ├── Provider
│   ├── API Key
│   └── Model
│
├── Session
│   └── Agent 工作会话
│
├── Tools
│   ├── 文件操作
│   ├── Shell
│   └── 其他工具
│
└── Web UI
    ├── Workspace / Session
    ├── Conversation
    ├── Tool / Approval
    ├── 文件
    └── Settings
```

# 三十五、本节最终目标

完成本节后，应能够独立完成：

```
启动 DeepSeek Harness
        ↓
选择项目目录
        ↓
创建 Workspace
        ↓
获取 DeepSeek API Key
        ↓
配置 API Key
        ↓
选择模型
        ↓
创建 Session
        ↓
向 Agent 提交任务
        ↓
查看 Agent 执行过程
```

最终形成完整的工作链路：

```
本地项目
   ↓
Workspace
   ↓
Harness
   ↓
Agent
   ↓
Model
   ↓
Tools
   ↓
完成任务
```

# 三十六、官方资料

DeepSeek Harness 官方 GitHub：

https://github.com/deepseek-ai/deepseek-harness/

DeepSeek Harness Web UI 使用指南：

https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/index.zh.md

DeepSeek Harness 模型配置：

https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/providers.zh.md

DeepSeek API 官方文档：

https://api-docs.deepseek.com/zh-cn/

DeepSeek 开放平台：

https://platform.deepseek.com/