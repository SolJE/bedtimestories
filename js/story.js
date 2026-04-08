// ===== story.js — Story page logic =====

document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const storyId = params.get('id');

  if (!storyId) {
    showError('No story selected.');
    return;
  }

  loadStory(storyId);
});

async function loadStory(storyId) {
  const main = document.getElementById('story-main');
  main.innerHTML = '<p class="loading">Loading story…</p>';

  try {
    const res = await fetch(`data/stories/${encodeURIComponent(storyId)}.json`);
    if (!res.ok) throw new Error('Story not found');
    const story = await res.json();
    renderStory(story, main);
  } catch (err) {
    console.error(err);
    main.innerHTML = '<p class="error-msg">Could not load the story. Please go back and try again.</p>';
  }
}

function renderStory(story, container) {
  const paragraphsHTML = (story.paragraphs || []).map((p, i) => {
    const isNarrator = (p.speaker || '').toLowerCase() === 'narrator';
    const badgeClass = isNarrator ? 'speaker-narrator' : 'speaker-character';
    const speakerLabel = p.speakerZh ? `${p.speaker} · ${p.speakerZh}` : p.speaker;
    return `
      <div class="paragraph" id="${escAttr(p.id)}" data-text="${escAttr(p.text)}" data-pid="${escAttr(p.id)}" data-speaker="${escAttr(p.speaker)}" tabindex="0" role="button" aria-label="Click to read aloud">
        <span class="speaker-badge ${badgeClass}">${escHtml(speakerLabel)}</span>
        <div class="para-text">${escHtml(p.text)}</div>
      </div>
    `;
  }).join('');

  const vocabHTML = (story.vocabulary || []).map(v => `
    <tr data-word="${escAttr(v.word)}">
      <td>${escHtml(v.word)}</td>
      <td><span class="phonetic">${escHtml(v.phonetic || '')}</span></td>
      <td>${escHtml(v.meaning || '')}</td>
    </tr>
  `).join('');

  container.innerHTML = `
    <a class="back-link" href="index.html">← Back to Stories</a>

    <div class="story-header">
      <span class="story-cover-emoji">${story.coverEmoji || '📖'}</span>
      <h1 class="story-title-en">${escHtml(story.title)}</h1>
      <div class="story-title-zh">${escHtml(story.titleZh || '')}</div>
      <div class="story-date">📅 ${formatDate(story.publishDate)}</div>
    </div>

    <div class="section-title">📖 Story</div>
    <p class="click-hint">👆 Click any paragraph to hear it read aloud!</p>
    <div id="paragraphs-container">
      ${paragraphsHTML}
    </div>

    <div class="section-title">📚 Vocabulary</div>
    <table class="vocab-table">
      <thead>
        <tr>
          <th>Word</th>
          <th>Phonetic</th>
          <th>中文释义</th>
        </tr>
      </thead>
      <tbody>${vocabHTML}</tbody>
    </table>

    <div class="section-title">💡 Moral · 寓意</div>
    <div class="moral-box">
      <div class="moral-en">${escHtml(story.moral || '')}</div>
      <div class="moral-zh">${escHtml(story.moralZh || '')}</div>
    </div>
  `;

  // Bind paragraph click events
  document.querySelectorAll('.paragraph').forEach(el => {
    el.addEventListener('click', () => {
      const text = el.dataset.text;
      const pid = el.dataset.pid;
      const speaker = el.dataset.speaker;
      speakText(text, pid, speaker);
    });
    el.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        el.click();
      }
    });
  });

  // Vocabulary word click — speak the word
  document.querySelectorAll('.vocab-table tbody tr').forEach(tr => {
    tr.addEventListener('click', () => {
      const word = tr.dataset.word;
      if (word) speakText(word, null);
    });
  });
}

function formatDate(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr + 'T00:00:00');
  return d.toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' });
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function escAttr(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function showError(msg) {
  const main = document.getElementById('story-main');
  if (main) main.innerHTML = `<p class="error-msg">${escHtml(msg)}</p>`;
}
