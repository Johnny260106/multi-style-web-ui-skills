# Multi-Style Web UI Skills

[中文](#中文) · [English](#english)

## 中文

一套面向 AI 编码 Agent 的 Web UI 设计 Skill。总控 Skill 会先判断产品类型，再选择一个主视觉体系完成设计、实现和渲染验收。

### 包含的 Skill

| Skill | 适用场景 |
|---|---|
| `web-ui-design-router` | 所有 Web UI 需求的入口；判断领域并选择一个主风格 |
| `tech-blue-b2b-ui` | AI、云平台、数据平台、企业 SaaS、研发工具 |
| `industrial-orange-b2b-ui` | 制造、设备、工程、仓储、供应链、工单和故障处理 |
| `green-operations-b2b-ui` | 能源、环保、园区、农业、碳管理和资源效率 |
| `dark-cockpit-ui` | 实时监控、态势感知、NOC/SOC、指挥中心和大屏 |
| `patient-medical-web-ui` | 中文患者服务：预约、问诊、报告、处方、缴费和档案 |
| `health-management-web-ui` | 中文健康管理：慢病、运动、饮食、睡眠、计划和趋势 |

### 设计特点

- 大型设计在确定视觉方向前研究 12–20 个近期案例，覆盖 Pinterest、Dribbble、Behance、花瓣等至少三个来源。
- 从多个案例提炼层级、密度、排版、组件和交互规律，不复制单一作品、品牌或专有资产。
- 主动移除常见 AI 模板痕迹：无意义渐变、玻璃拟态、同质 KPI 卡片、假数据图表、过度圆角和装饰性科技元素。
- 子 Skill 均包含设计 token、领域模式、完整状态、反模式、响应式和 WCAG 2.2 AA 验收要求。
- 保持前端框架中立，优先适配现有项目；空项目默认 React + TypeScript + Vite。

### 安装

安装全部 Skill，保证总控路由能够找到相邻的子 Skill。

#### Codex

```bash
git clone https://github.com/Johnny260106/multi-style-web-ui-skills.git
cp -R multi-style-web-ui-skills/web-ui-design-router multi-style-web-ui-skills/*-ui ~/.codex/skills/
```

也可以使用兼容 Agent Skills 的安装器：

```bash
npx skills add Johnny260106/multi-style-web-ui-skills
```

不同 Agent 的个人或项目级 Skill 目录可能不同，请以对应产品文档为准。`agents/openai.yaml` 提供 Codex 界面元数据；不识别该文件的 Agent 仍可使用 `SKILL.md` 和 `references/`。

### 使用

推荐从总控开始：

```text
使用 $web-ui-design-router 为一个光伏电站运营平台设计响应式 Web 后台。
```

也可以直接指定风格：

```text
使用 $dark-cockpit-ui 设计一个 1920×1080 的实时安全态势大屏。
```

总控与六个子 Skill 应作为一个整体安装。一次页面设计只选择一个主风格；确有不同使用环境时，可以明确限定局部覆盖，例如浅色管理后台中的独立深色监控页面。

### 验证

```bash
python3 scripts/validate.py
```

验证脚本检查 Skill 数量、目录名称、frontmatter、引用文件、路由映射和 UI 元数据。它不代替真实任务测试、视觉评审或可访问性人工检查。

## English

Seven portable Agent Skills for Web UI work. The router class skill selects one domain-specific visual system before design and implementation.

- Technology-blue enterprise SaaS
- Industrial-orange operations
- Green energy and sustainability operations
- Dark real-time command centers
- Simplified-Chinese patient services
- Simplified-Chinese health management

Install the complete repository so the router can resolve all sibling skills. Each leaf skill includes visual research, semantic tokens, domain patterns, state coverage, anti-patterns, responsive verification, and WCAG 2.2 AA guidance.

```bash
git clone https://github.com/Johnny260106/multi-style-web-ui-skills.git
cp -R multi-style-web-ui-skills/web-ui-design-router multi-style-web-ui-skills/*-ui ~/.codex/skills/
```

Or, with a compatible Agent Skills installer:

```bash
npx skills add Johnny260106/multi-style-web-ui-skills
```

Start with `$web-ui-design-router`, or explicitly invoke a leaf skill when the visual system is already known.

## License

MIT. Inspiration platforms and referenced design systems remain the property of their respective owners. This repository contains instructions and original guidance, not copied third-party visual assets.
