
# 注意力跟踪：间隙日志（Interstitial Logger）

一个极简的“注意力转移/任务切换”记录器：在你分心、被打断、准备切换任务的那一刻，用全局快捷键弹出输入框，记录刚才做什么、触发原因/情绪、以及接下来要转向哪里。日志按时间追加写入本地文件，便于后续复盘。

## 功能

- 全局快捷键触发（默认 `Ctrl + Alt + J`）
- 置顶弹窗输入（避免被当前窗口遮挡）
- 自动加时间戳并追加写入日志文件（UTF-8）
- 使用 `.pyw` 后台运行（无控制台窗口）

## 目录结构

```
Project2-注意力跟踪/
  interstitial_logger.pyw          # 主程序
  interstitial_logger - 快捷方式.lnk # 便于放入开机自启动（可选）
  log/
    log.txt                        # 日志输出（默认）
```

## 环境依赖

- Windows（本项目按 Windows 使用方式编写）
- Python 3.6+（使用 f-string）
- 第三方库：`keyboard`
  - `tkinter` 为 Python 常见自带组件（Windows 安装包通常默认包含）

## 安装

在项目目录打开 PowerShell（或终端）

Win+R，输入 `powershell` 并回车，然后在弹出的 PowerShell 窗口中执行：

```bash
pip install keyboard
```

## 快速开始（手动运行）

- 直接双击文件 `interstitial_logger.pyw` 运行
- 或使用命令行运行（推荐用 `pythonw`，不弹出控制台）：

```bash
pythonw .\interstitial_logger.pyw
```

运行后程序会在后台监听快捷键。按下 `Ctrl + Alt + J` 会弹出输入框，输入内容确认后写入日志。

如果后台程序被关停，可以手动双击然后快捷键唤起。

## 开机自启动

1. `Win + R` 打开运行，输入：

```text
shell:startup
```

2. 将快捷方式放入启动文件夹：
   - 直接复制仓库内的 `interstitial_logger - 快捷方式.lnk` 到该文件夹

## 配置项

在 `interstitial_logger.pyw` 中修改：

- 日志文件路径：`LOG_FILE_PATH`
  - 默认：`D:\26SPRING\Project2-注意力跟踪\log\log.txt`
  - 建议确保目录存在（例如 `log/` 已存在）
- 快捷键：`keyboard.add_hotkey('ctrl+alt+j', log_entry)`
  - `keyboard` 的按键字符串格式示例：`ctrl+shift+l`、`alt+space` 等
- 提示语：`simpledialog.askstring(... prompt=...)`

## 日志格式

每条记录为一行，格式如下：

```text
[YYYY-MM-DD HH:MM:SS] 你的输入内容
```

默认输出到：`log/log.txt`。

## 常见问题

- 快捷键不生效
  - 尝试以管理员权限运行（`keyboard` 在某些环境下需要更高权限才能捕获全局按键）
  - 检查快捷键是否与其他软件冲突，换一个组合键再试
- 写入失败/找不到路径
  - 确认 `LOG_FILE_PATH` 指向的目录存在且你有写权限
- 弹窗被挡住
  - 程序已设置 `topmost`，若仍被挡住，尝试切换到桌面后再按快捷键

## 隐私说明

日志默认写入本地文件，不会联网上传。请自行妥善保管日志文件（可能包含个人敏感信息）。
