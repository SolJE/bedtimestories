# Automation-2 记忆（bedtimestories 周四自动化）

## 任务
每周自动为儿童英文故事网站 bedtimestories 生成一篇新故事并部署到 GitHub Pages。

## 执行记录

### 2026-09-03（首次执行 · story-028）
- **新故事**: story-028「The Little Mole Who Met the Moon / 遇见月亮的小鼹鼠」
- **主题**: 好奇心 Curiosity
- **风格**: 卡通矢量（cartoon vector，story-027 水彩 → 本周轮换）
- **发布日**: 2026-09-03（周四）
- **文件**: data/stories/story-028.json（25 段、15 生词、3 插图锚点 p5/p13/p20）
- **角色**: Narrator / Mo 小莫 / Mama Mole 鼹鼠妈妈 / Dot 小瓢虫 / Hoot 猫头鹰
- **插图**: 1 封面 + 3 场景（顺序 ImageGen 生成，无时间戳碰撞）
- **Git**: commit e9f45b1, push 5ae32d4 → e9f45b1 main，6 files changed
- **提交信息**: "Add Week 28 story: The Little Mole Who Met the Moon"
- **结果**: 推送成功，远程已更新，GitHub Pages 将于约 1 分钟内自动刷新

## 工作流要点（已验证）

1. **JSON 生成**: Python 脚本在系统临时目录构建 story dict + 索引（确保引号转义安全），运行后立即删除
2. **ImageGen 顺序生成**: 一次一张 + 立即 `mv` 重命名为 `story-XXX-*.png`，彻底避免时间戳碰撞（再验证一次通过）
3. **风格轮换**: 024 水彩 → 025 卡通矢量 → 026 彩铅手绘 → 027 水彩 → 028 卡通矢量
4. **主题轮换**: 022 勇气 → 023 同理心 → 024 友谊 → 025 诚实 → 026 坚持 → 027 善良 → 028 好奇心

## 注意事项
- 不使用 AskUserQuestion（自动化无人值守）
- 临时脚本存于 `C:/Users/hexiaohua/AppData/Local/Temp/`，运行后清理
- automation-2 记忆目录若不存在需先创建
- ImageGen 每次生成约消耗 5-10 积分（工具提示）
