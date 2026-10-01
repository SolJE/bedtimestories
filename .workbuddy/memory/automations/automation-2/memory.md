# Automation-2 记忆（bedtimestories 周四自动化）

## 任务
每周自动为儿童英文故事网站 bedtimestories 生成一篇新故事并部署到 GitHub Pages。

## 执行记录

### 2026-09-24（第四次执行 · story-031）
- **新故事**: story-031「The Little Panda Who Learned to Wait / 学会等待的小熊猫」
- **主题**: 耐心 Patience（新主题，此前 31 期未用过）
- **风格**: 卡通矢量 cartoon vector（轮换：029 彩铅手绘 → 030 水彩 → 031 卡通矢量）
- **发布日**: 2026-09-24（周四）
- **文件**: data/stories/story-031.json（25 段、15 生词、3 插图锚点 p5/p13/p22）
- **角色**: Bao 小熊猫 / Mama Panda 熊猫妈妈 / Grandpa Moss 苔藓爷爷（老乌龟） / Momo 小猴子
- **插图**: 1 封面 + 3 场景（顺序 ImageGen 生成 + 立即 mv，每张生成后 Read 视觉核对，全部一次通过）
- **Git**: commit 8a5d874, push 1c2c2ac..8a5d874 main，9 files changed
- **提交信息**: "Add Week 31 story: The Little Panda Who Learned to Wait"
- **结果**: 推送成功，远程已更新

### 2026-09-17（第三次执行 · story-030）
- **新故事**: story-030「The Little Goat Who Crossed the High Bridge / 走过高桥的小山羊」
- **主题**: 勇气 Courage
- **风格**: 水彩 watercolor（轮换：028 卡通矢量 → 029 彩铅手绘 → 030 水彩）
- **发布日**: 2026-09-17（周四）
- **文件**: data/stories/story-030.json（25 段、15 生词、3 插图锚点 p5/p13/p22）
- **角色**: Gilly 小山羊 / Mama Goat 山羊妈妈 / Granny Goat 山羊奶奶 / Bartholomew 老公山羊 / Pico 小麻雀
- **插图**: 1 封面 + 3 场景（顺序 ImageGen 生成，无时间戳碰撞，4 张全部一次通过视觉核对）
- **Git**: commit 1c2c2ac, push c4ac40a..1c2c2ac main，9 files changed
- **提交信息**: "Add Week 30 story: The Little Goat Who Crossed the High Bridge"
- **结果**: 推送成功，远程已更新

### 2026-09-10（第二次执行 · story-029）
- **新故事**: story-029「The Little Beaver Who Shared His River / 分享小河的小河狸」
- **主题**: 分享 Sharing
- **风格**: 彩铅手绘 colored pencil（轮换：027 水彩 → 028 卡通矢量 → 029 彩铅手绘）
- **发布日**: 2026-09-10（周四）
- **文件**: data/stories/story-029.json（25 段、15 生词、3 插图锚点 p5/p13/p22）
- **角色**: Bramble 小河狸 / Mama Beaver 河狸妈妈 / Tilly 鸭子 / Gus 大鹅 / Hopper 青蛙
- **插图**: 1 封面 + 3 场景
- **scene-3 重做**: 首次生成出现篝火、泰迪熊、刺猬、松鼠等故事外元素；用「ONLY four animals / NO campfire / NO other animals」否定式 prompt 重做后成功
- **Git**: commit c4ac40a, push e9f45b1 → c4ac40a main，9 files changed
- **提交信息**: "Add Week 29 story: The Little Beaver Who Shared His River"
- **结果**: 推送成功，远程已更新

### 2026-09-03（首次执行 · story-028）
- **新故事**: story-028「The Little Mole Who Met the Moon / 遇见月亮的小鼹鼠」
- **主题**: 好奇心 Curiosity
- **风格**: 卡通矢量 cartoon vector（story-027 水彩 → 本周轮换）
- **发布日**: 2026-09-03（周四）
- **文件**: data/stories/story-028.json（25 段、15 生词、3 插图锚点 p5/p13/p20）
- **角色**: Narrator / Mo 小莫 / Mama Mole 鼹鼠妈妈 / Dot 小瓢虫 / Hoot 猫头鹰
- **插图**: 1 封面 + 3 场景（顺序 ImageGen 生成，无时间戳碰撞）
- **Git**: commit e9f45b1, push 5ae32d4 → e9f45b1 main，6 files changed
- **提交信息**: "Add Week 28 story: The Little Mole Who Met the Moon"
- **结果**: 推送成功，远程已更新

## 工作流要点（已验证）

1. **JSON 生成**: Python 脚本在系统临时目录构建 story dict + 索引（确保引号转义安全），运行后立即删除
2. **ImageGen 顺序生成**: 一次一张 + 立即 `mv` 重命名为 `story-XXX-*.png`，彻底避免时间戳碰撞（再验证一次通过）
3. **风格轮换**: 025 卡通矢量 → 026 彩铅手绘 → 027 水彩 → 028 卡通矢量 → 029 彩铅手绘 → 030 水彩 → 031 卡通矢量
4. **主题轮换**: 023 同理心 → 024 友谊 → 025 诚实 → 026 坚持 → 027 善良 → 028 好奇心 → 029 分享 → 030 勇气 → 031 耐心
5. **角色去重**: 已用 31 个主角，新故事主角不能重复（story-031 首次用熊猫+乌龟）

## 注意事项
- 不使用 AskUserQuestion（自动化无人值守）
- 临时脚本存于 `C:/Users/hexiaohua/AppData/Local/Temp/`，运行后清理
- automation-2 记忆目录若不存在需先创建
- ImageGen 每次生成约消耗 5-10 积分（工具提示）
- **多角色插图务必使用否定式 prompt**：「ONLY [动物列表] / NO [常见噪声如 campfire、extra animals]」（story-029 scene-3 教训）
- 生成复杂场景时，**生成后必须 Read 图片核对**，发现不匹配立即重做
