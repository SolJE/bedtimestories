# Bedtime Stories 🌙

**English bedtime stories for children aged 7–9, updated every week.**

Live site → [https://SolJE.github.io/bedtimestories](https://SolJE.github.io/bedtimestories)

---

## Features

- 📖 Weekly English stories told through dialogue (great for role-play!)
- 🔊 Click any paragraph to hear it read aloud (Web Speech API)
- 📚 Vocabulary list with phonetics & Chinese meanings
- 💡 Story moral in English + Chinese
- 🏷️ Story title and moral both in English & Chinese
- 📱 Mobile-friendly, no login required

## How to Add a New Story

1. Create `data/stories/story-XXX.json` (copy `story-001.json` as a template)
2. Add an entry to `data/stories.json`
3. Commit and push:

```bash
git add .
git commit -m "Add Week XX story: <title>"
git push
```

GitHub Pages will update in ~1 minute.

## Story JSON Format

```json
{
  "id": "story-003",
  "title": "The Singing Bird",
  "titleZh": "会唱歌的小鸟",
  "publishDate": "2026-04-21",
  "coverEmoji": "🐦",
  "moral": "Practice every day and you will surprise yourself.",
  "moralZh": "每天坚持练习，你会让自己惊喜。",
  "vocabulary": [
    { "word": "practice", "phonetic": "/ˈpræktɪs/", "meaning": "练习" }
  ],
  "paragraphs": [
    {
      "id": "p1",
      "speaker": "Narrator",
      "speakerZh": "旁白",
      "text": "Once upon a time..."
    }
  ]
}
```

## Tech Stack

- Pure HTML + CSS + JavaScript (no build tools)
- Hosted on GitHub Pages
- Web Speech API for text-to-speech

## Local Development

```bash
# Use VS Code Live Server, or:
npx serve .
# Then open http://localhost:3000
```
