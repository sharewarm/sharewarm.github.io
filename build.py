#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepShare · Markdown 批量转 HTML 脚本（用于 GitHub Pages 部署）

用法:
    python3 build.py

功能:
    - 扫描 DIRS 中配置的目录, 将其中所有 .md 转换为同目录下的同名 .html
    - 生成页面为暖色主题, 与 index.html 导航页风格一致
    - 页面顶部带"返回导航"链接, 可回到首页
    - 新增模块后: 在下方 DIRS 追加目录名, 并在 index.html 的 MODULES 中配置链接

依赖(首次使用需安装):
    pip3 install --user markdown
"""

import glob
import os
import re
import sys
from html import escape as html_escape

try:
    import markdown
except ImportError:
    sys.exit("缺少依赖 markdown, 请先执行:  pip3 install --user markdown")

# ── 配置: 需要转换的目录(新增模块在此追加) ──────────────────────
DIRS = ["deepseek_harness"]
# ───────────────────────────────────────────────────────────────

MD_EXTENSIONS = ["extra", "sane_lists"]

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}} · DeepShare</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
<style>
  :root {
    --bg: #fdf6ee;
    --card: #fffaf4;
    --primary: #e07b39;
    --primary-deep: #c95d1e;
    --text: #4a3527;
    --text-light: #8a6f5c;
    --border: #f0dcc5;
    --code-bg: #fbf0e1;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", -apple-system, sans-serif;
    background: linear-gradient(160deg, #fbe8d3 0%, #fdf9f3 45%, var(--bg) 100%);
    min-height: 100vh;
    color: var(--text);
    line-height: 1.8;
  }

  .topbar {
    position: sticky; top: 0; z-index: 10;
    background: rgba(253, 246, 238, 0.92);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--border);
  }
  .topbar-inner {
    max-width: 900px; margin: 0 auto;
    padding: 13px 20px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .back-link {
    color: var(--primary-deep); text-decoration: none;
    font-size: 14px; font-weight: 600;
    display: inline-flex; align-items: center; gap: 6px;
  }
  .back-link:hover { text-decoration: underline; }
  .crumb { font-size: 13px; color: var(--text-light); }

  .container { max-width: 900px; margin: 0 auto; padding: 36px 20px 70px; }

  .markdown-body {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(200, 120, 50, 0.10);
    padding: 40px 46px;
  }

  .markdown-body h1 {
    font-size: 30px; line-height: 1.4;
    background: linear-gradient(120deg, #c95d1e, #e79a52);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    padding-bottom: 14px; margin-bottom: 26px;
    border-bottom: 2px solid var(--border);
  }
  .markdown-body h2 {
    font-size: 23px; margin: 1.9em 0 0.8em;
    padding-left: 13px;
    border-left: 4px solid var(--primary);
  }
  .markdown-body h3 { font-size: 18.5px; margin: 1.6em 0 0.6em; color: var(--primary-deep); }
  .markdown-body h4 { font-size: 16.5px; margin: 1.4em 0 0.5em; }

  .markdown-body p { margin: 0.9em 0; }
  .markdown-body a { color: var(--primary-deep); text-decoration: none; border-bottom: 1px dashed #d9a06a; }
  .markdown-body a:hover { border-bottom-style: solid; }

  .markdown-body ul, .markdown-body ol { padding-left: 1.6em; margin: 0.9em 0; }
  .markdown-body li { margin: 0.4em 0; }
  .markdown-body li::marker { color: var(--primary); }

  .markdown-body blockquote {
    background: #fdf1e3;
    border-left: 4px solid #eeb384;
    border-radius: 0 10px 10px 0;
    padding: 12px 18px;
    margin: 1.2em 0;
    color: #7a5c44;
  }
  .markdown-body blockquote p { margin: 0.3em 0; }

  .markdown-body code {
    font-family: "SF Mono", Menlo, Consolas, "Courier New", monospace;
    background: #f9e9d5;
    color: var(--primary-deep);
    padding: 2px 7px;
    border-radius: 6px;
    font-size: 0.88em;
  }

  .markdown-body pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 18px;
    overflow-x: auto;
    margin: 1.3em 0;
    line-height: 1.6;
  }
  .markdown-body pre code {
    background: transparent;
    padding: 0;
    border-radius: 0;
    color: #5b4433;
    font-size: 13.5px;
  }
  .markdown-body pre code.hljs { background: transparent; padding: 0; color: inherit; }

  .markdown-body table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.5em 0;
    font-size: 14px;
  }
  .markdown-body th { background: #f9e9d5; color: var(--primary-deep); }
  .markdown-body th, .markdown-body td {
    border: 1px solid var(--border);
    padding: 8px 13px;
    text-align: left;
  }
  .markdown-body tr:nth-child(even) td { background: #fdf8f1; }

  .markdown-body img { max-width: 100%; border-radius: 10px; }
  .markdown-body hr { border: none; border-top: 2px dashed var(--border); margin: 2.4em 0; }
  .markdown-body strong { color: #7a4a22; }

  footer { text-align: center; margin-top: 40px; color: #c2a48c; font-size: 13px; }

  @media (max-width: 600px) {
    .container { padding: 22px 14px 50px; }
    .markdown-body { padding: 24px 18px; }
    .markdown-body h1 { font-size: 24px; }
    .markdown-body h2 { font-size: 20px; }
  }
</style>
</head>
<body>
<nav class="topbar">
  <div class="topbar-inner">
    <a class="back-link" href="{{BACK}}">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
      返回导航
    </a>
    <span class="crumb">{{MODULE}}</span>
  </div>
</nav>

<div class="container">
  <article class="markdown-body">
{{BODY}}
  </article>
  <footer>DeepShare · 由 build.py 生成 · 部署于 GitHub Pages</footer>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
</body>
</html>
"""


def extract_title(text):
    """取第一个一级标题作为页面标题"""
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return ""


def convert(md_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    base = os.path.splitext(os.path.basename(md_path))[0]
    title = extract_title(text) or base

    body = markdown.markdown(text, extensions=MD_EXTENSIONS)

    # 相对目录, 如 deepseek_harness; 用于计算返回首页的链接层级
    rel_dir = os.path.dirname(md_path).replace(os.sep, "/")
    back = "../" * (rel_dir.count("/") + 1) + "index.html"

    page = (
        TEMPLATE
        .replace("{{TITLE}}", html_escape(title))
        .replace("{{MODULE}}", html_escape(rel_dir))
        .replace("{{BACK}}", back)
        .replace("{{BODY}}", body)
    )

    out_path = os.path.splitext(md_path)[0] + ".html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    return out_path


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    total = 0
    for d in DIRS:
        files = sorted(glob.glob(os.path.join(d, "*.md")))
        if not files:
            print(f"⚠ 目录 {d}/ 下没有找到 .md 文件")
            continue
        for md_file in files:
            out = convert(md_file)
            total += 1
            print(f"✔ {md_file} → {out}")
    print(f"\n完成: 共转换 {total} 个文件")


if __name__ == "__main__":
    main()
