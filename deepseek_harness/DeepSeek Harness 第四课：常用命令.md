# DeepSeek Harness（DSH）常用命令速查

> 本文在原始《DeepSeek Harness（DSH）全面教学指南：斜杠命令与常用 CLI 操作》基础上精简优化，只保留日常使用频率较高的命令。具体参数可能随 DSH 版本变化，执行前可用 `dsh --help` 核对。

## 一、Web 工作台启动

```bash
# 启动 Web 工作台
npx @deepseek-ai/dsh web

# 已安装 dsh 时，也可以直接启动
dsh web

# 指定端口启动
dsh web --port 8080
```

- `dsh web`：启动 Web 工作台。
- `--port 8080`：将服务端口指定为 `8080`。

## 二、Headless 无头任务

Headless 适合在终端中执行一次性任务，不启动 Web 界面。

```bash
# 执行一次任务
dsh --profile headless "总结当前项目的目录结构"

# 分析当前 Git 变更
dsh --profile headless "检查当前工作区的 Git 变更并总结重点"

# 通过标准输入传入任务
echo "总结当前项目的主要功能" | dsh --profile headless
```

如果希望将命令输出作为任务内容，可将提示词和输出一起通过管道传入：

```bash
{
  echo "请总结以下 Git 变更的主要影响："
  git diff --stat
} | dsh --profile headless
```

常用参数（请先用当前版本的帮助确认支持情况）：

```bash
# 查看 Headless 参数帮助
dsh --profile headless --help

# JSON 结构化输出
dsh --profile headless --json "总结当前项目"

# 指定会话 ID（用于支持会话续接的版本）
dsh --profile headless --session-id my-session "分析当前项目"
```

## 三、查看帮助与检查配置

```bash
# 查看 CLI 帮助
dsh --help

# 查看 Web Profile 的帮助
dsh --profile web --help

# 查看默认配置组合
dsh --profile web --dump-default-config

# 查看最终组合配置
dsh --profile web --dump-config
```

- `--dump-default-config`：查看默认配置。
- `--dump-config`：查看组合后的配置，适合排查配置覆盖或插件加载问题。

## 四、使用 YAML 配置补丁

```bash
# 使用额外 YAML 配置启动
dsh --profile web --patch ./extra.yml

# 先检查补丁生效后的配置
dsh --profile web --patch ./extra.yml --dump-config
```

使用前请确认 `extra.yml` 路径正确、YAML 语法有效，并检查配置内容是否会改变工具权限或运行行为。

## 五、插件管理

`<plugin-name>` 是占位符，执行时要替换为真实、可信且兼容当前版本的插件包名。

```bash
# 为 Web Profile 添加插件
dsh plugin --profile web add <plugin-name>

# 移除插件
dsh plugin --profile web remove <plugin-name>
```

安装第三方插件前，先确认来源、版本及所需权限，不要直接安装不明来源的插件。

## 六、常见问题

### 1. 找不到 `dsh` 命令

可以先尝试官方 npm 启动方式：

```bash
npx @deepseek-ai/dsh web
```

### 2. Headless 没有读取到项目文件

先切换到目标项目目录，再运行命令。DSH 通常会以启动时的当前目录作为工作区。

```bash
cd my-project
dsh --profile headless "总结当前项目"
```

### 3. 参数提示不支持

检查当前版本的帮助：

```bash
dsh --help
dsh --profile headless --help
```

不同 Profile 的参数不一定通用。例如 Web 的 `--port` 不应直接套用到 Headless。

## 七、斜杠命令说明

`/goal`、`/plan`、`/feedback`、`/compact`、`/permission`、`/model`、`/export` 等属于交互界面的命令形式，是否可用取决于当前 DSH 版本和加载的 UI 插件。请以实际界面的命令提示或对应版本文档为准，不要将其与 `dsh` CLI 参数混为一谈。

## 八、常用命令总表

| 用途 | 命令 |
|---|---|
| 启动 Web | `dsh web` |
| 指定 Web 端口 | `dsh web --port 8080` |
| 查看帮助 | `dsh --help` |
| 执行 Headless 任务 | `dsh --profile headless "任务内容"` |
| 查看 Headless 参数 | `dsh --profile headless --help` |
| 从标准输入传入任务 | `echo "任务内容" \| dsh --profile headless` |
| 查看默认配置 | `dsh --profile web --dump-default-config` |
| 查看最终配置 | `dsh --profile web --dump-config` |
| 使用配置补丁 | `dsh --profile web --patch ./extra.yml` |
| 添加插件 | `dsh plugin --profile web add <plugin-name>` |
| 移除插件 | `dsh plugin --profile web remove <plugin-name>` |

## 官方参考资料

- 官方仓库：<https://github.com/deepseek-ai/deepseek-harness>
- CLI 中文参考：<https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/reference/README.zh.md>
- Headless 文档：<https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/bundle/headless/README.md>
