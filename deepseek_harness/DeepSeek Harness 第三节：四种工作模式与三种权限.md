# DeepSeek Harness 第三节：四种工作模式与三种权限

上一节我们已经完成了：

- DeepSeek Harness 安装
- 工作目录配置
- API Key 配置
- Web 界面基本认识

这一节开始了解 DeepSeek Harness 最重要的两个概念：

> **工作模式（Agent Preset）和权限（Permission）**

两者不是一个东西。

可以先记住：

```
工作模式
→ 决定 Agent “有什么能力、怎么工作”

权限
→ 决定 Agent “最多能操作到什么程度”
```

# 一、什么是工作模式？

DeepSeek Harness 中的工作模式，本质上是一个 **Agent Preset（Agent 预设）**。

不同模式会给 Agent 配置不同的：

- 工具
- 提示词
- 工作能力
- 执行方式
- 其他插件能力

所以：

> **工作模式决定 Agent 是“以什么方式工作”。**

当前官方 Web 版本提供四种内置 Agent Preset：

| 模式     | 英文     | 核心特点                    |
| -------- | -------- | --------------------------- |
| 标准模式 | Standard | 日常开发的默认模式          |
| PTC 模式 | PTC      | 使用程序化工具调用能力      |
| 极简模式 | Minimal  | 尽可能精简 Agent 能力       |
| 创造模式 | Creator  | 用于创建和设计 Agent Preset |

官方 Web App 当前随发行版提供 `standard`、`ptc`、`minimal`、`cordis` 四个 preset，其中 `cordis` 对应 Creator 模式。

# 二、Standard：标准模式

## 1. 什么是标准模式？

Standard 是最适合日常使用的模式。

可以把它理解成：

> **一个能力比较完整、适合正常开发工作的 Agent。**

例如：

```
你：
帮我检查这个 Python 项目，
找到登录功能中的 Bug 并修复。

Agent：
读取项目
   ↓
分析代码
   ↓
定位 Bug
   ↓
修改代码
   ↓
运行测试
   ↓
反馈结果
```

这类正常的软件开发任务，就是 Standard 模式最典型的使用场景。

## 2. Standard 适合做什么？

例如：

### 代码开发

```
帮我实现一个 Python 爬虫。
```

### Bug 修复

```
帮我检查这个程序为什么运行报错。
```

### 项目分析

```
分析这个项目的目录结构，
告诉我程序从哪里开始运行。
```

### 功能修改

```
给这个项目增加一个用户登录功能。
```

### 文件处理

```
检查项目中的 Markdown 文档，
统一标题格式。
```

这些都可以直接使用：

```
Standard
```

# 三、PTC 模式

## 1. PTC 是什么？

PTC 可以理解为：

> **Programmatic Tool Calling**

也就是：

> **程序化工具调用。**

普通情况下，Agent 使用工具时，可以理解成：

```
Agent
 ↓
调用工具
 ↓
得到结果
 ↓
继续思考
 ↓
再次调用工具
```

例如需要处理多个文件：

```
读取 A.py
    ↓
读取 B.py
    ↓
读取 C.py
    ↓
修改 A.py
    ↓
修改 B.py
```

Agent 可能需要进行多次工具调用。

PTC 模式的核心思路是：

> **让 Agent 能够通过程序化方式组织工具调用。**

官方实现中，PTC 是一个独立的 Agent Preset，并提供程序化工具调用相关能力。官方 CLI 文档也说明 `DSH_TOOLS_MODE` 可以选择 `native`、`ptc` 或 `both`。

## 2. 为什么需要 PTC？

假设现在有：

```
100 个文件
```

我们需要：

```
找出所有使用旧 API 的文件
        ↓
统计
        ↓
筛选
        ↓
修改
        ↓
检查修改结果
```

如果每一个文件都单独调用工具：

```
调用工具
调用工具
调用工具
调用工具
……
```

效率可能比较低。

PTC 的思路是：

```
Agent
 ↓
编写一段程序
 ↓
程序批量调用工具
 ↓
统一处理结果
 ↓
返回给 Agent
```

可以简单理解为：

```
普通工具调用：

Agent → 工具 → Agent → 工具 → Agent


PTC：

Agent → 程序 → 多次工具调用 → 结果 → Agent
```

因此 PTC 更适合：

- 批量处理
- 多文件操作
- 复杂工具组合
- 需要大量工具调用的任务

# 四、Minimal：极简模式

## 1. 什么是极简模式？

Minimal 的核心思想非常简单：

> **尽可能少地给 Agent 加载额外能力。**

官方 CLI 文档说明，内置 `minimal` preset 会保持非常精简的 Agent 组成；除基础的 Agent 能力外，其他提示词段和面向模型的插件不会被加入。

可以把它理解成：

```
Standard

Agent
├── 基础能力
├── 工具
├── 提示词
├── 各种辅助能力
└── 其他插件
```

而 Minimal 更接近：

```
Minimal

Agent
└── 尽量保留核心能力
```

## 2. 为什么需要极简模式？

不是所有任务都需要一个“全副武装”的 Agent。

例如：

```
你好
```

或者：

```
解释一下 Python 中的装饰器。
```

如果只是简单问答：

```
完整开发工具
+
大量插件
+
复杂工作流
```

并不一定有必要。

这时候 Minimal 可以减少不必要的能力和上下文。

## 3. Minimal 适合什么？

例如：

```
解释一下 Python 的闭包。
帮我解释这段代码。
比较 list 和 tuple 的区别。
简单分析一下这个函数。
```

因此可以简单记忆：

> **Minimal = 少一点工具，少一点复杂度，专注核心任务。**

# 五、Creator：创造模式

## 1. Creator 是干什么的？

Creator 是四种模式中非常特殊的一种。

它不是主要用来：

```
写 Python
修 Bug
改项目
```

而是用于：

> **创建和设计 Agent Preset。**

也就是说：

普通模式：

```
我让 Agent 帮我完成任务
```

Creator：

```
我让 Agent 帮我设计一个 Agent
```

# 六、为什么需要 Creator？

假设你经常需要做：

```
Python 代码审查
```

你可能希望有一个专门的 Agent：

```
Python Code Review Agent
```

它应该：

```
读取 Python 文件
       ↓
检查代码规范
       ↓
检查潜在 Bug
       ↓
检查异常处理
       ↓
输出代码审查报告
```

如果每次都重新告诉 Agent：

```
你要检查什么
你应该怎么检查
你可以使用什么工具
你应该输出什么格式
```

就比较麻烦。

Creator 模式的作用就是帮助你：

```
设计 Agent
    ↓
选择需要的能力
    ↓
组合插件
    ↓
形成新的 Preset
```

官方 Agent Preset 页面也明确说明，Creator 模式用于创建或覆盖 Agent Preset，并通过 `cordis` preset 启动 Creator 模式任务。

# 七、四种工作模式怎么选？

可以先记住下面这张表：

| 模式         | 核心思想       | 适合场景                     |
| ------------ | -------------- | ---------------------------- |
| **Standard** | 正常干活       | 日常开发、代码修改、项目分析 |
| **PTC**      | 程序化调用工具 | 批量处理、复杂工具调用       |
| **Minimal**  | 尽量精简       | 简单任务、轻量问答           |
| **Creator**  | 创建 Agent     | 设计自己的 Agent Preset      |

最简单的记忆方式：

```
Standard
→ 正常工作

PTC
→ 批量、程序化地调用工具

Minimal
→ 少一点能力，简单处理

Creator
→ 创建新的 Agent
```

# 八、工作模式 ≠ 权限

这是本节最重要的知识点。

例如：

```
Standard
```

是工作模式。

而：

```
workspace-write
```

是权限。

它们完全不是一个维度。

可以想象成一个员工：

```
工作模式
    ↓
这个员工会什么？
怎么工作？
有什么工具？
```

而：

```
权限
    ↓
这个员工能进入哪些房间？
能不能修改里面的东西？
```

所以：

```
Standard + read-only
```

是完全可能的。

也就是说：

> **Agent 可以拥有完整的工作能力，但文件操作权限受到限制。**

同样：

```
Minimal + workspace-write
```

也可以存在。

# 九、三种权限

DeepSeek Harness 的底层文件沙箱主要有三种权限模式：

```
read-only
workspace-write
danger-full-access
```

官方沙箱文档定义了这三种文件效果模式。

## 1. read-only

字面意思：

> **只读**

Agent 可以：

```
读取文件
分析代码
查看项目
```

但不能通过文件沙箱直接写入文件。

可以理解成：

```
┌───────────────┐
│   项目文件     │
│               │
│   👀 Agent    │
│               │
│   ❌ 修改      │
└───────────────┘
```

适合：

```
代码审查
项目分析
问题诊断
学习项目结构
```

# 十、workspace-write

意思是：

> **允许 Agent 修改当前 Workspace 范围内的文件。**

例如：

```
D:\AI_Project
```

是当前 Workspace。

那么 Agent 可以在允许的工作区范围内：

```
读取文件
创建文件
修改文件
```

可以理解成：

```
Workspace
┌──────────────────────┐
│ main.py       ✅      │
│ test.py       ✅      │
│ config.py     ✅      │
│ README.md     ✅      │
└──────────────────────┘

Workspace 外
┌──────────────────────┐
│ other_project  ❌     │
└──────────────────────┘
```

这是日常开发中最常见的权限模式。

官方当前基础配置也是以 `workspace-write` 作为新会话常见的默认权限基础。

# 十一、danger-full-access

这个权限可以理解为：

> **不再受到文件沙箱的限制。**

也就是：

```
read-only
       ↓
workspace-write
       ↓
danger-full-access
```

权限范围逐渐扩大。

其中：

```
danger-full-access
```

表示取消文件沙箱限制。官方文档将其定义为不进行文件隔离限制的模式。

因此它的风险也最高。

一般情况下：

```
能用 workspace-write
就不要使用 danger-full-access
```

# 十二、三种权限的区别

| 权限                 | 读取 | 修改 Workspace | 突破文件沙箱 |
| -------------------- | ---- | -------------- | ------------ |
| `read-only`          | ✅    | ❌              | ❌            |
| `workspace-write`    | ✅    | ✅              | ❌            |
| `danger-full-access` | ✅    | ✅              | ✅            |

可以记成：

```
read-only
→ 只能看

workspace-write
→ 能看 + 能改当前工作区

danger-full-access
→ 不受文件沙箱限制
```

# 十三、工作模式和权限组合起来

真正使用 Harness 时，是两个维度共同决定 Agent 的行为。

例如：

### 组合一

```
Standard
+
read-only
```

含义：

> 使用标准 Agent，但只能查看和分析，不能直接修改文件。

### 组合二

```
Standard
+
workspace-write
```

含义：

> 使用标准 Agent，并允许它在当前 Workspace 中进行开发。

这通常是日常开发比较常见的组合。

### 组合三

```
PTC
+
workspace-write
```

含义：

> 使用 PTC 的工具调用方式，同时允许修改工作区。

适合比较复杂、批量性的开发任务。

### 组合四

```
Minimal
+
read-only
```

含义：

> 使用精简 Agent，同时限制为只读。

适合：

```
看看项目
分析代码
回答问题
```

而不希望 Agent 修改任何东西。

# 十四、最终建立一个完整概念

现在可以把 DeepSeek Harness 理解成：

```
                    DeepSeek Harness
                           │
              ┌────────────┴────────────┐
              │                         │
          工作模式                    权限
        Agent Preset              Permission
              │                         │
      ┌───────┼────────┐        ┌───────┼────────┐
      │       │        │        │       │        │
   Standard  PTC    Minimal  read-only workspace danger
                         │               write    full
                         │
                      Creator
```

两边解决的是不同问题：

```
工作模式
↓
“Agent 怎么工作？”

权限
↓
“Agent 最多能操作什么？”
```

# 十五、最重要的记忆

如果只记住一句话：

> **工作模式决定 Agent 的能力和工作方式，权限决定 Agent 的操作边界。**

四种工作模式：

```
Standard
PTC
Minimal
Creator
```

三种权限：

```
read-only
workspace-write
danger-full-access
```

不要把它们混在一起。

例如：

```
Standard ≠ workspace-write
PTC ≠ danger-full-access
Minimal ≠ read-only
Creator ≠ full-access
```

它们属于两个完全不同的概念。

## 官方资料

- [DeepSeek Harness Agent Preset 官方文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/client/ui-agent-preset/README.md)
- [DeepSeek Harness Web App 官方文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/bundle/web-app/README.zh.md)
- [DeepSeek Harness 沙箱权限官方文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/shell/bash-sandbox/README.md)