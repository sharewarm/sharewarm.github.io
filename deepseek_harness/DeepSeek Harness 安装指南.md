# DeepSeek Harness 安装指南

## 一、DeepSeek Harness 简介

DeepSeek Harness（简称 `dsh`）是由 DeepSeek AI 开发的开源 Agent Harness（智能体框架）。

它可以帮助 AI 完成：

- 文件处理
- 数据分析
- 代码编写与修改
- 代码运行与测试
- 信息检索
- 长时间任务
- 插件扩展

DeepSeek Harness 目前处于 **Developer Preview（开发者预览）阶段**，功能和接口仍在持续更新，后续可能存在兼容性变化。

官方目前提供两种主要使用方式：

```
DeepSeek Harness
│
├── Web 版本
│
└── Desktop 桌面版本
```

官方资料：

- DeepSeek Harness 官网：https://www.deepseek.com/en/harness/
- 官方 GitHub：https://github.com/deepseek-ai/deepseek-harness
- 官方下载页面：https://www.deepseek.com/en/download/

# 二、Web 版本

## 2.1 Web 版本是什么？

Web 版本通过浏览器访问 Harness 的 Web UI。

整体结构：

```
浏览器
   ↓
DeepSeek Harness Web UI
   ↓
本机运行的 Harness 服务
```

Web 版本运行在本机，浏览器主要负责提供操作界面。

# 三、Web 版本环境要求

使用 Web 版本需要准备：

| 环境      | 要求                    |
| --------- | ----------------------- |
| 操作系统  | Windows / macOS / Linux |
| Node.js   | 必需                    |
| npm / npx | 随 Node.js 提供         |
| 浏览器    | 必需                    |
| 网络连接  | 建议保持正常            |
| Python    | 不需要                  |
| Git       | 普通安装方式不需要      |
| pnpm      | 普通安装方式不需要      |

其中最重要的是：

> **Node.js**

官方提供的 npm 启动方式要求先安装 Node.js，然后执行：

```
npx @deepseek-ai/dsh web
```

官方文档说明，该命令默认会在：

```
http://127.0.0.1:3080
```

启动 Web UI，并在本机启动时自动打开默认浏览器。

# 四、安装 Node.js

## 4.1 下载 Node.js

打开 Node.js 官方网站：

https://nodejs.org/

选择 **LTS（长期支持版本）**。

下载完成后运行安装程序。

## 4.2 Windows 安装

Windows 用户下载 Windows 安装程序后：

```
双击安装程序
    ↓
Next
    ↓
接受许可协议
    ↓
选择安装目录
    ↓
Next
    ↓
Install
    ↓
Finish
```

通常保持默认配置即可。

# 五、检查 Node.js 是否安装成功

安装完成后打开：

```
CMD
```

输入：

```
node -v
```

如果能够看到版本号，例如：

```
v22.x.x
```

说明 Node.js 已经安装成功。

继续输入：

```
npm -v
```

如果能够正常显示版本号，说明 npm 可以正常使用。

# 六、启动 DeepSeek Harness Web 版本

Node.js 安装完成后，在 CMD 中执行：

```
npx @deepseek-ai/dsh web
```

首次运行时，`npx` 会获取并运行 DeepSeek Harness 对应的 npm 包。

启动成功后，默认访问：

```
http://127.0.0.1:3080
```

也可以使用：

```
http://localhost:3080
```

官方默认端口为：

```
3080
```

# 七、安装 DeepSeek Harness

## 7.1 推荐：全局安装

长期使用 DeepSeek Harness，推荐先安装一次：

```
npm install -g @deepseek-ai/dsh
```

这个命令的作用是：

```
下载 DeepSeek Harness
        ↓
安装到 npm 全局目录
        ↓
获得 dsh 命令
```

安装完成以后，可以检查：

```
dsh --version
```

如果能够正常输出版本号，说明 DeepSeek Harness 已经安装成功。

# 八、第一次启动

安装完成后执行：

```
dsh web
```

启动 Web 版本。

默认情况下，Web UI 使用：

```
http://127.0.0.1:3080
```

也可以访问：

```
http://localhost:3080
```

官方 README 中 Web 版本的默认端口为 `3080`。

# 九、第一次安装与启动的完整流程

第一次安装只需要执行：

```
npm install -g @deepseek-ai/dsh
```

然后：

```
dsh --version
```

确认安装成功。

最后：

```
dsh web
```

启动 Harness。

完整流程：

```
安装 Node.js
     ↓
检查 Node.js
     ↓
node -v
     ↓
检查 npm
     ↓
npm -v
     ↓
安装 DeepSeek Harness
     ↓
npm install -g @deepseek-ai/dsh
     ↓
检查 DSH
     ↓
dsh --version
     ↓
启动
     ↓
dsh web
     ↓
浏览器访问
     ↓
http://127.0.0.1:3080
```

# 十、以后再次启动怎么办？

安装完成以后，**不需要再次执行安装命令**。

也不需要每次重新执行：

```
npm install -g @deepseek-ai/dsh
```

以后直接：

```
dsh web
```

即可。

因此：

### 第一次

```
npm install -g @deepseek-ai/dsh
```

然后：

```
dsh web
```

### 第二次及以后

直接：

```
dsh web
```

即可。

# 十一、为什么 `npx @deepseek-ai/dsh web` 不作为主要启动方式？

官方 README 当前提供的标准 npm 运行方式是：

```
npx @deepseek-ai/dsh web
```

这个方式可以直接运行 Harness，不需要提前执行全局安装。

但是：

```
npx @deepseek-ai/dsh web
```

更适合：

> **快速运行 / 快速体验**

而长期使用时：

```
npm install -g @deepseek-ai/dsh
```

然后：

```
dsh web
```

更加直观。

两种方式可以理解为：

```
npx
│
└── 获取并运行
```

而：

```
npm install -g
│
└── 安装一次
       ↓
      dsh
       ↓
    dsh web
       ↓
     启动
```

# 十二、`npx` 方式什么时候使用？

如果只是想快速测试 Harness，可以直接：

```
npx @deepseek-ai/dsh web
```

不需要先进行：

```
npm install -g @deepseek-ai/dsh
```

官方 README 当前就是以这种方式作为 npm 运行示例。

# 十三、Web 版本常见问题

## 13.1 `node` 不是内部或外部命令

如果出现类似：

```
'node' 不是内部或外部命令，也不是可运行的程序
```

说明：

```
Node.js 没有正确安装
```

或者：

```
Node.js 没有加入 PATH
```

解决方法：

1. 重新安装 Node.js
2. 安装完成后重新打开 CMD
3. 执行：

```
node -v
```

# 十四、`dsh` 不是内部或外部命令

如果执行：

```
dsh web
```

出现：

```
'dsh' 不是内部或外部命令
```

首先检查：

```
npm install -g @deepseek-ai/dsh
```

是否安装成功。

然后：

```
dsh --version
```

如果仍然无法找到 `dsh`，可以检查 npm 全局安装路径：

```
npm prefix -g
```

Windows 下需要确保该目录对应的 npm 全局可执行目录已经加入系统 `PATH`。

# 十五、安装过程中长时间没有反应

DeepSeek Harness 当前依赖较多，首次安装可能需要较长时间。

尤其是：

```
npx @deepseek-ai/dsh web
```

首次运行时可能需要下载和解析大量依赖。

官方仓库近期已经出现 Windows 用户首次 `npx` 运行长时间没有明显进度的反馈。

因此：

> **看到终端长时间没有新的输出，不要立即认为程序一定崩溃。**

可以先等待一段时间。

# 十六、Windows + npm 安装异常

如果：

```
npm install -g @deepseek-ai/dsh
```

出现依赖解析异常、内存占用持续升高或者长时间卡住，可以先检查：

```
node -v
npm -v
```

确认 Node.js 是否满足要求。

当前官方开发文档要求 Node.js：

```
22.19+
```

或者：

```
24+
```

如果仍然出现 npm 依赖解析问题，可以考虑使用官方仓库讨论中提到的替代方式：

```
pnpm dlx @deepseek-ai/dsh web
```

不过这属于备用方案，正常课程环境优先使用：

```
npm install -g @deepseek-ai/dsh
```

然后：

```
dsh web
```

# 十七、Web 默认端口

DeepSeek Harness Web 默认使用：

```
3080
```

访问：

```
http://127.0.0.1:3080
```

如果 3080 端口已经被其他程序占用，可以指定其他端口：

```
dsh web --port 8080
```

然后访问：

```
http://127.0.0.1:8080
```

# 十八、关闭 Web 版本

在运行：

```
dsh web
```

的 CMD 窗口中：

```
Ctrl + C
```

即可停止当前 Harness 服务。

注意：

> 关闭 CMD 窗口或者按 `Ctrl + C` 只是停止当前运行的 Harness，并不会卸载已经安装的 DeepSeek Harness。

下次使用时重新执行：

```
dsh web
```

即可。

# 十九、Desktop 桌面版本

除了 Web 版本之外，DeepSeek 还提供 Desktop 桌面版本。

Desktop 不需要通过：

```
npm install -g @deepseek-ai/dsh
```

来进行普通安装。

直接下载安装对应的桌面应用即可。

官方目前提供：

```
Windows
```

以及：

```
macOS Apple Silicon
```

版本。

# 二十、Desktop 安装步骤

## Windows

进入 DeepSeek 官方下载页面：

https://www.deepseek.com/en/download/

下载：

```
DeepSeek Harness Desktop
```

Windows 版本。

然后：

```
运行安装程序
      ↓
完成安装
      ↓
启动 DeepSeek Harness
```

## macOS

官方当前 macOS Desktop 要求：

```
Apple Silicon
macOS 13 或更高版本
```

安装：

```
下载 DMG
   ↓
打开 DMG
   ↓
将 DeepSeek Harness 拖入 Applications
   ↓
启动应用
```

# 二十一、Web 与 Desktop 的区别

| 对比项目     | Web       | Desktop                |
| ------------ | --------- | ---------------------- |
| 使用方式     | 浏览器    | 桌面应用               |
| Node.js      | 需要      | 普通使用不需要单独安装 |
| npm          | 需要      | 不需要手动使用         |
| 安装方式     | 命令行    | 安装程序               |
| 启动方式     | `dsh web` | 双击应用               |
| 浏览器       | 需要      | 应用自身提供界面       |
| 服务器使用   | ✅         | 不适合                 |
| SSH 使用     | ✅         | 不适合                 |
| 开发调试     | 更方便    | 相对较少               |
| 普通桌面使用 | 可以      | 更方便                 |

# 二十二、两种版本的核心区别

## Web

```
Node.js
   ↓
dsh
   ↓
dsh web
   ↓
本机 Web 服务
   ↓
浏览器
```

主要特点：

> **通过命令行管理 Harness。**

## Desktop

```
DeepSeek Harness Desktop
          ↓
       Harness
          ↓
       应用界面
```

主要特点：

> **通过桌面应用管理 Harness。**

# 二十三、如何选择？

### 选择 Web

适合：

- 学习 Harness
- 开发调试
- 命令行操作
- SSH
- 服务器
- 自动化
- 源码研究

### 选择 Desktop

适合：

- Windows / macOS 桌面环境
- 不希望使用命令行
- 希望直接打开应用
- 日常使用 Harness
- 操作本地文件

# 二十四、Web 版本安装命令汇总

### 检查 Node.js

```
node -v
```

### 检查 npm

```
npm -v
```

### 全局安装 Harness

```
npm install -g @deepseek-ai/dsh
```

### 检查 Harness

```
dsh --version
```

### 启动 Harness

```
dsh web
```

### 指定端口

```
dsh web --port 8080
```

### 停止 Harness

```
Ctrl + C
```

# 二十五、快速体验方式

如果不想进行全局安装，也可以直接运行：

```
npx @deepseek-ai/dsh web
```

默认访问：

```
http://127.0.0.1:3080
```

这种方式适合快速体验。

长期使用推荐：

```
npm install -g @deepseek-ai/dsh
```

然后：

```
dsh web
```

# 二十六、最终安装流程

## Web 版本

### 第一次

```
# 1. 检查 Node.js
node -v

# 2. 检查 npm
npm -v

# 3. 安装 DeepSeek Harness
npm install -g @deepseek-ai/dsh

# 4. 检查安装
dsh --version

# 5. 启动
dsh web
```

### 以后使用

```
dsh web
```

## Desktop 版本

```
进入官方下载安装页面
        ↓
选择对应操作系统
        ↓
下载安装包
        ↓
完成安装
        ↓
启动 DeepSeek Harness
```

# 二十七、安装完成标准

### Web 版本

满足以下条件：

```
node -v
```

可以正常显示版本。

```
npm -v
```

可以正常显示版本。

```
dsh --version
```

可以正常显示 Harness 版本。

```
dsh web
```

能够启动 Web UI。

浏览器能够访问：

```
http://127.0.0.1:3080
```

即表示安装完成。

### Desktop 版本

能够正常：

```
启动 DeepSeek Harness
        ↓
进入 Harness 界面
```

即表示安装完成。

# 二十八、官方资料

DeepSeek Harness 官方 GitHub：

https://github.com/deepseek-ai/deepseek-harness/

DeepSeek Harness 官方网站：

https://www.deepseek.com/en/harness/

DeepSeek 官方下载页面：

https://www.deepseek.com/en/download/

Node.js 官方网站：

https://nodejs.org/