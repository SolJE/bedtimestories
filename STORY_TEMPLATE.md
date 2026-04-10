# 故事模板 (Story Template)

> ⚠️ **重要**: 生成新故事时必须严格遵循此格式，否则故事页无法正常显示！

## 文件命名
`data/stories/story-XXX.json` (如 story-006.json)

## JSON 模板

```json
{
  "id": "story-XXX",
  "title": "英文标题",
  "titleZh": "中文标题",
  "publishDate": "YYYY-MM-DD",
  "coverEmoji": "🌟",
  "moral": "English moral message.",
  "moralZh": "中文寓意说明。",
  "vocabulary": [
    { "word": "word", "phonetic": "/ˈwɜːrd/", "meaning": "中文释义" }
  ],
  "paragraphs": [
    {
      "id": "p1",
      "speaker": "Narrator",
      "speakerZh": "旁白",
      "text": "旁白内容..."
    },
    {
      "id": "p2",
      "speaker": "CharacterName",
      "speakerZh": "角色中文名",
      "text": "\"角色对话内容...\""
    }
  ]
}
```

## 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 故事ID，格式 story-XXX |
| `title` | string | ✅ | 英文标题 |
| `titleZh` | string | ✅ | 中文标题 |
| `publishDate` | string | ✅ | 发布日期 YYYY-MM-DD |
| `coverEmoji` | string | ✅ | 封面表情符号 |
| `moral` | string | ✅ | 英文寓意 |
| `moralZh` | string | ✅ | 中文寓意 |
| `vocabulary` | array | ✅ | 生词数组 |
| `paragraphs` | array | ✅ | **故事段落数组，核心字段！** |

## paragraphs 字段详解

| 子字段 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `id` | string | ✅ | 段落ID，格式 p1, p2, p3... |
| `speaker` | string | ✅ | 说话者名称（Narrator = 旁白） |
| `speakerZh` | string | ✅ | 说话者中文名称 |
| `text` | string | ✅ | 文本内容 |

## ❌ 错误示例

```json
// 错误！会导致故事内容不显示
{
  "script": [
    { "type": "narrator", "character": "Narrator", "content": "..." }
  ]
}
```

## ✅ 正确示例

```json
// 正确！
{
  "paragraphs": [
    { "id": "p1", "speaker": "Narrator", "speakerZh": "旁白", "text": "..." }
  ]
}
```

---

**注意**: 自动化任务执行时会自动读取此模板作为参考。
