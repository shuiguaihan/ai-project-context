# AI Project Context

这是一套用于研发项目管理的轻量方法：让 AI 持续维护项目的当前状态，再把目标与现状之间的差距转化为项目经理今天必须推动的事项。

它不是周报生成器，也不会替项目团队冻结方案或接受风险。它主要解决两个问题：

1. 新资料、会议记录和验证结果怎样进入项目上下文，同时保留来源、版本和确认状态。
2. 项目经理怎样基于最新上下文，每天找出需要协调、追问、升级或组织裁决的 3 至 5 件事。

## 仓库内容

```text
ai-project-context/
├─ sync-project-context/
│  ├─ SKILL.md
│  ├─ agents/openai.yaml
│  ├─ references/operating-contract.md
│  └─ scripts/evidence_inventory.py
├─ prompts/daily-advancement.md
└─ examples/sample-project/
   ├─ README.md
   ├─ project-goal.md
   ├─ shared-context.md
   ├─ new-evidence.md
   └─ daily-advancement-example.md
```

`sync-project-context` 负责归档原始资料、比较变化、区分证据等级，并更新真正受影响的项目资料。

`daily-advancement.md` 负责比较项目目标与当前状态，只输出项目经理当天必须推动的管理动作。

`examples/sample-project` 是完全虚构的示例，不对应任何真实公司、产品、人员或项目。

## 快速开始

克隆仓库：

```powershell
git clone https://github.com/shuiguaihan/ai-project-context.git
cd ai-project-context
```

把 Skill 安装到个人 Codex Skills 目录前，先确认目标位置没有同名 Skill：

```powershell
$skillTarget = Join-Path $env:USERPROFILE '.codex\skills\sync-project-context'
if (Test-Path -LiteralPath $skillTarget) {
    throw "Skill already exists: $skillTarget"
}
Copy-Item -Recurse -LiteralPath '.\sync-project-context' -Destination $skillTarget
```

随后可以在项目目录中提出类似请求：

```text
使用 $sync-project-context，把这批新资料同步到当前项目上下文。
保留原件和来源信息，比较实际变化，区分已确认事实、文档记录、
AI 推断和待确认事项，只更新真正受影响的项目资料。
```

需要生成项目经理的当天推进项时，使用 [`prompts/daily-advancement.md`](prompts/daily-advancement.md)，替换其中的项目路径和时间范围。

## 三种模式

| 模式 | 适用场景 | 是否修改项目状态 |
| --- | --- | --- |
| 只归档 | 保存原件、来源、版本和哈希 | 否 |
| 影响评估 | 查看新资料会影响哪些上下文 | 否 |
| 同步并更新 | 已明确要求把变化纳入项目上下文 | 是，仅做有证据支持的最小更新 |

## 关键边界

- 新文件不因为日期更新就自动成为项目基线。
- 会议转写证明讨论发生过，不自动等于正式决议。
- AI 推断必须明确标注，不能写成项目组已经确认的事实。
- 资料冲突应保留双方说法，并指向需要裁决的角色和关闭证据。
- 发布、发送、删除、替换原件和修改源码不在默认授权范围内。

## 脚本

生成文件清单与 SHA256：

```powershell
python .\sync-project-context\scripts\evidence_inventory.py `
  .\examples\sample-project `
  --root .\examples\sample-project `
  --format markdown
```

脚本默认只向标准输出写结果。使用 `--output` 时只允许创建新文件，不会覆盖已有文件。

## License

[MIT](LICENSE)
