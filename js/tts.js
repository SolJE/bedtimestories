// ===== tts.js — Text-to-Speech module (Enhanced) =====

let currentUtterance = null;
let activeParagraphId = null;
let cachedVoices = [];

// Voice quality tiers (highest quality first)
const VOICE_TIERS = {
  // Premium voices - most natural sounding
  premium: ['Google US English', 'Google UK English Female', 'Google UK English Male',
            'Microsoft Jenny', 'Microsoft Sonia', 'Microsoft Libby', 'Microsoft Ryan',
            'Apple Samantha', 'Apple Victoria', 'Apple Daniel'],
  // High quality voices
  high: ['Samantha', 'Karen', 'Daniel', 'Tessa', 'Moira', 'Fiona', 'Veena',
         'Microsoft David', 'Microsoft Mark', 'Microsoft Zira', 'Microsoft Hazel'],
  // Good fallback voices
  good: ['Alex', 'Fred', 'Vicki', 'Victoria', 'Bruce', 'Agnes']
};

// Speaker type configurations for more natural storytelling
const SPEAKER_CONFIGS = {
  narrator: {
    rate: 0.85,
    pitch: 1.0,
    voicePreference: 'premium'
  },
  child: {
    rate: 0.90,
    pitch: 1.2,
    voicePreference: 'high'
  },
  adult: {
    rate: 0.88,
    pitch: 0.95,
    voicePreference: 'premium'
  },
  animal: {
    rate: 0.88,
    pitch: 1.15,
    voicePreference: 'high'
  }
};

/**
 * Initialize and cache available voices
 */
function initVoices() {
  if (!window.speechSynthesis) return;
  cachedVoices = window.speechSynthesis.getVoices();
}

/**
 * Get the best available voice
 * @param {string} preference - 'premium' or 'high'
 * @returns {SpeechSynthesisVoice|null}
 */
function getBestVoice(preference = 'premium') {
  if (!cachedVoices.length) initVoices();
  if (!cachedVoices.length) return null;

  const enVoices = cachedVoices.filter(v => v.lang.startsWith('en'));
  if (!enVoices.length) return cachedVoices[0];

  const tier = preference === 'premium' ? VOICE_TIERS.premium : VOICE_TIERS.high;
  
  for (const name of tier) {
    const voice = enVoices.find(v => v.name.includes(name));
    if (voice) return voice;
  }

  // Fallback
  return enVoices.find(v => !v.localService) || enVoices[0];
}

/**
 * Detect speaker type from name
 * @param {string} speaker
 * @returns {string} - config key
 */
function detectSpeakerType(speaker) {
  const s = (speaker || '').toLowerCase();
  
  if (s === 'narrator' || s === '旁白') return 'narrator';
  
  const childNames = ['max', 'lily', 'bear', 'bunny', 'rabbit', 'fox', 'bird', 'mouse', 
                      'squirrel', 'deer', 'kitty', 'puppy', 'little'];
  if (childNames.some(n => s.includes(n))) return 'child';
  
  const adults = ['mama', 'papa', 'mom', 'dad', 'mother', 'father', 'grandma', 'grandpa'];
  if (adults.some(n => s.includes(n))) return 'adult';
  
  return 'child';
}

/**
 * Preprocess text for natural speech
 * @param {string} text
 * @returns {string}
 */
function preprocessText(text) {
  return text
    .replace(/, /g, ', , ')
    .replace(/\. ([A-Z"])/g, '. . $1')
    .replace(/\? /g, '? ? ')
    .replace(/! /g, '! ! ')
    .replace(/"([^"]+)"/g, '" $1 "');
}

/**
 * Enhanced speak function with role-based voices
 * @param {string} text - Text to speak
 * @param {string} paragraphId - Element ID to highlight
 * @param {string} speaker - Speaker name for voice selection
 */
function speakText(text, paragraphId, speaker = '') {
  if (!window.speechSynthesis) {
    showToast('Your browser does not support text-to-speech. 😢');
    return;
  }

  // Toggle off if same paragraph
  if (activeParagraphId === paragraphId && window.speechSynthesis.speaking) {
    window.speechSynthesis.cancel();
    clearSpeakingState();
    return;
  }

  window.speechSynthesis.cancel();
  clearSpeakingState();

  const speakerType = detectSpeakerType(speaker);
  const config = SPEAKER_CONFIGS[speakerType];
  
  const processedText = preprocessText(text);
  const utterance = new SpeechSynthesisUtterance(processedText);
  
  utterance.lang = 'en-US';
  utterance.rate = config.rate;
  utterance.pitch = config.pitch;
  utterance.volume = 1.0;

  // Select appropriate voice
  const voice = getBestVoice(config.voicePreference);
  if (voice) utterance.voice = voice;

  utterance.onstart = () => {
    activeParagraphId = paragraphId;
    const el = document.getElementById(paragraphId);
    if (el) el.classList.add('speaking');
  };

  utterance.onend = () => { clearSpeakingState(); };
  utterance.onerror = (e) => { 
    console.error('TTS error:', e);
    clearSpeakingState(); 
  };

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

// Initialize voices when available
if (window.speechSynthesis) {
  initVoices();
  window.speechSynthesis.onvoiceschanged = initVoices;
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
