// ===== main.js — Home page logic =====

document.addEventListener('DOMContentLoaded', () => {
  loadStoryList();
});

async function loadStoryList() {
  const grid = document.getElementById('story-grid');

  try {
    const res = await fetch('data/stories.json');
    if (!res.ok) throw new Error('Failed to load stories list');
    const stories = await res.json();

    if (!stories || stories.length === 0) {
      grid.innerHTML = '<p class="loading">No stories yet. Check back soon! 🌙</p>';
      return;
    }

    // Sort by publishDate descending (newest first)
    stories.sort((a, b) => new Date(b.publishDate) - new Date(a.publishDate));

    grid.innerHTML = stories.map(s => createCardHTML(s)).join('');

  } catch (err) {
    console.error(err);
    grid.innerHTML = '<p class="error-msg">Could not load stories. Please try again later.</p>';
  }
}

function createCardHTML(story) {
  const date = formatDate(story.publishDate);
  const emoji = story.coverEmoji || '📖';
  return `
    <a class="story-card" href="story.html?id=${encodeURIComponent(story.id)}">
      <div class="card-cover">${emoji}</div>
      <div class="card-body">
        <div class="en-title">${escHtml(story.title)}</div>
        <div class="zh-title">${escHtml(story.titleZh)}</div>
        <div class="summary">${escHtml(story.summary || '')}</div>
      </div>
      <div class="card-footer">
        <span class="card-date">📅 ${date}</span>
        <span class="read-btn">Read ▶</span>
      </div>
    </a>
  `;
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
