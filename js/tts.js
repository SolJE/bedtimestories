// ===== tts.js — Text-to-Speech module =====

let currentUtterance = null;
let activeParagraphId = null;

/**
 * Speak a text string in English.
 * @param {string} text - The text to speak.
 * @param {string} paragraphId - The paragraph element ID to highlight.
 */
function speakText(text, paragraphId) {
  if (!window.speechSynthesis) {
    showToast('Your browser does not support text-to-speech. 😢');
    return;
  }

  // If the same paragraph is speaking, stop it (toggle off)
  if (activeParagraphId === paragraphId && window.speechSynthesis.speaking) {
    window.speechSynthesis.cancel();
    clearSpeakingState();
    return;
  }

  // Cancel any ongoing speech
  window.speechSynthesis.cancel();
  clearSpeakingState();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  utterance.rate = 0.85;   // Slightly slower for children
  utterance.pitch = 1.1;   // Slightly higher pitch for liveliness
  utterance.volume = 1.0;

  // Try to pick a good English voice
  const voices = window.speechSynthesis.getVoices();
  const preferred = voices.find(v =>
    v.lang.startsWith('en') && (v.name.includes('Samantha') || v.name.includes('Karen') || v.name.includes('Daniel'))
  ) || voices.find(v => v.lang === 'en-US') || voices.find(v => v.lang.startsWith('en'));
  if (preferred) utterance.voice = preferred;

  utterance.onstart = () => {
    activeParagraphId = paragraphId;
    const el = document.getElementById(paragraphId);
    if (el) el.classList.add('speaking');
  };

  utterance.onend = () => { clearSpeakingState(); };
  utterance.onerror = () => { clearSpeakingState(); };

  currentUtterance = utterance;
  window.speechSynthesis.speak(utterance);
}

function clearSpeakingState() {
  if (activeParagraphId) {
    const el = document.getElementById(activeParagraphId);
    if (el) el.classList.remove('speaking');
  }
  activeParagraphId = null;
  currentUtterance = null;
}

// Voices load asynchronously on some browsers
if (window.speechSynthesis) {
  window.speechSynthesis.onvoiceschanged = () => { window.speechSynthesis.getVoices(); };
}

// ===== Toast helper =====
function showToast(msg) {
  let toast = document.getElementById('tts-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'tts-toast';
    toast.style.cssText = `
      position:fixed;bottom:28px;left:50%;transform:translateX(-50%);
      background:#3D2B1F;color:#fff;padding:10px 22px;border-radius:30px;
      font-size:0.9rem;z-index:9999;opacity:0;transition:opacity 0.3s;
      font-family:'Nunito',sans-serif;box-shadow:0 4px 16px rgba(0,0,0,0.2);
    `;
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.style.opacity = '1';
  setTimeout(() => { toast.style.opacity = '0'; }, 2800);
}
