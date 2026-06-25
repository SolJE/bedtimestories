# bedtimestories 项目长期记忆

## 故事发布记录
| ID | 标题 | 主题 | 日期 | 状态 |
|----|------|------|------|------|
| story-001 | The Brave Little Rabbit | 勇气 | 2026-04-08 | ✅ |
| story-002 | The Clever Fox and the Magic Apple | 分享 | 2026-04-08 | ✅ |
| story-003 | The Secret Garden of Friendship | 友谊 | 2026-04-09 | ✅ |
| story-004 | The Boy Who Told the Truth | 诚实 | 2026-04-09 | ✅ |
| story-005 | The Little Star Who Never Gave Up | 坚持 | 2026-04-10 | ✅ |
| story-006 | The Kind Little Fox | 善良 | 2026-04-16 | ✅ |
| story-007 | The Curious Little Owl | 好奇心 | 2026-04-16 | ✅ |
| story-008 | The Little Penguin Who Made a Mistake | 诚实 | 2026-04-23 | ✅ |
| story-009 | The Little Elephant Who Dreamed in Colors | 想象力 | 2026-04-30 | ✅ |
| story-010 | The Little Squirrel's Big Feast | 分享 | 2026-05-07 | ✅ |
| story-011 | The Little Bear Who Listened with His Heart | 同理心 | 2026-05-14 | ✅ |
| story-012 | The Kitten Who Found a Friend | 友谊 | 2026-05-21 | ✅ |
| story-013 | The Little Mouse Who Planted Kindness | 善良 | 2026-05-28 | ✅ |
| story-014 | The Little Duckling Who Found Her Courage | 勇气 | 2026-06-04 | ✅ |
| story-015 | The Puppy Who Always Asked Why | 好奇心 | 2026-06-11 | ✅ |
| story-016 | The Little Lamb Who Told a Little Lie | 诚实 | 2026-06-18 | ✅ |

## 最新故事
- **ID**: story-016
- **标题**: The Little Lamb Who Told a Little Lie
- **主题**: 诚实 (Honesty)
- **日期**: 2026-06-18

## 插图系统（2026-06-11 新增）
- **前端支持**：封面图 (`coverImage`) + 场景插图 (`illustrations`)，story.js 在段落前渲染插图
- **首页卡片**：main.js 检测 `coverImage` 字段自动切换到图片封面
- **数据扩展**：story JSON 新增可选字段 `coverImage` 和 `illustrations`
- **插图存储**：`assets/images/story-XXX-*.png`
- **风格轮换**：水彩绘本 → 卡通矢量 → 彩铅手绘，每周轮流
- **风格轮换记录**：story-015 水彩 → story-016 卡通矢量 → story-017 彩铅手绘
- **story-015 已配图**：1 封面 + 3 场景（水彩风格）
- **story-016 已配图**：1 封面 + 3 场景（卡通矢量风格）
