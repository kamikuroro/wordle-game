# Wordle Game Development Conversation

## Date: 2026-02-18

## Context
This documents the development of a two-player Wordle game for GitHub Pages.

---

## Part 1: Learning Cursor CLI for Coding

### Initial Question
User asked: "can u look up online how to ask openclaw to use cursor cli for coding?"

### Research Findings
Found that OpenClaw has a `cursor-agent` skill, but it wasn't installed by default. The skill documentation showed that Cursor CLI requires a TTY - running directly would hang indefinitely.

### Solution: Using tmux
The solution was to wrap Cursor CLI calls inside tmux to provide a pseudo-terminal:

```bash
# Install tmux
brew install tmux

# Create session and run agent
tmux new-session -d -s cursor
tmux send-keys -t cursor "agent --print --force 'your task'" Enter
tmux capture-pane -t cursor -p
```

### Proof of Concept
Successfully tested Cursor CLI via tmux - the agent was able to read files and return results.

---

## Part 2: Wordle Game Development

### Project Setup
- Created project locally
- Single HTML file: `index.html`
- Initialized git repo and pushed to GitHub

### GitHub Pages Deployment
- Created repo on GitHub
- Enabled GitHub Pages
- Live at: https://kamikuroro.github.io/wordle-game/

### Features Implemented

#### 1. Basic Two-Player Mode
- Player 1 enters secret word
- Player 2 guesses in 6 tries
- Standard Wordle color feedback (green/yellow/gray)

#### 2. Mobile Responsive Design
- Added responsive CSS for iPhone and smaller screens
- Tiles resize appropriately on mobile

#### 3. NYT Wordle UI Style
- Updated colors to match NYT Wordle:
  - Green (correct): `#6aaa64`
  - Yellow (present): `#c9b458`
  - Gray (absent): `#787c7e`
- Fixed game logic for evaluating guesses
- Added tile flip animations
- Improved keyboard design

#### 4. Single Player Mode
- Random 5-letter word from built-in ~500 word list
- Mode selection screen at start

#### 5. Shareable Link Mode
- Generate encoded link for Two Player mode
- URL parameter uses base64 encoding
- Recipient opens link to play with pre-selected word

#### 6. Sound Effects (Web Audio API)
- **Key click**: iPhone-style click when typing
- **Tile reveal tones**:
  - Green (correct): 880Hz sine wave
  - Yellow (present): 587Hz triangle wave
  - Gray (absent): 220Hz sine wave

#### 7. Bug Fixes
- Fixed: Only 4 tiles showing per row (should be 5)
- Fixed: Game logic for duplicate letters
- Fixed: Hidden word in shareable URL (base64 encoding)
- Fixed: Double-tap zoom on mobile (touch-action: manipulation)

---

## Cursor CLI Commands Used

```bash
# Initial test
agent --print --force 'List the files in this directory'

# Fix Wordle bugs
agent --print --trust 'Fix the Wordle game bugs...'

# Add features
agent --print --trust 'Add three features to index.html...'

# Fix URL encoding and zoom
agent --print --trust 'Fix two issues...'
```

---

## GitHub Repo
- **URL**: https://github.com/kamikuroro/wordle-game
- **Live Game**: https://kamikuroro.github.io/wordle-game/

---

## Notes
- Cursor CLI via tmux works well for file operations
- Agent can read, analyze, and write files
- Output capture can be tricky - need to wait and capture pane
- Some tasks require multiple attempts due to agent hanging
