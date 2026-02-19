import { readFileSync, writeFileSync } from 'fs';

const lines = readFileSync('/usr/share/dict/words', 'utf8').split('\n');
const words = new Set();
for (const line of lines) {
  const w = line.trim();
  if (w.length === 5 && /^[a-z]{5}$/.test(w)) {
    words.add(w.toUpperCase());
  }
}

const sorted = [...words].sort();
let out = '';
for (let i = 0; i < sorted.length; i += 10) {
  out += "'" + sorted.slice(i, Math.min(i + 10, sorted.length)).join("','") + "',\n";
}

writeFileSync('/Users/wangxinyi/Projects/wordle-game/words_out.txt', `Total: ${sorted.length}\n${out}`);
