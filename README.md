# Simple Tetris Game 🧱

A web-based Tetris-like falling blocks game built with vanilla HTML5, CSS3, and JavaScript.

## Features

- ✨ Classic 7 tetromino pieces (I, O, T, S, Z, J, L)
- 🎮 Smooth movement and rotation controls
- 🏆 Line clearing with progressive difficulty system
- 📊 Scoring system with level progression
- ⏸️ Pause/resume functionality
- 🎯 Game over detection and restart
- 🌃 Retro arcade styling with neon theme

## How to Play

### Controls
- **← →** Move pieces left/right
- **↓** Soft drop (faster fall + bonus points)
- **↑** Rotate piece
- **Space** Hard drop (instant drop + more bonus points)
- **P** Pause/unpause game

### Objective
- Stack falling tetromino pieces to form complete horizontal lines
- Complete lines disappear and award points
- Level increases every 10 lines cleared
- Game speed increases with each level
- Game ends when pieces reach the top

### Scoring
- **Lines cleared**: 100 × level × lines cleared at once
- **Soft drop**: +1 point per cell dropped
- **Hard drop**: +2 points per cell dropped

## Getting Started

Simply open `tetris-game.html` in any modern web browser to start playing!

## Technical Details

- Pure vanilla JavaScript (ES6+) - no frameworks or dependencies
- HTML5 Canvas for smooth 2D rendering
- Responsive design for various screen sizes
- Clean, modular code architecture

## Development

Feel free to fork, modify, and enhance! Some ideas for improvements:

- Sound effects and background music
- Mobile touch controls
- Different game modes (time attack, marathon, etc.)
- Online high score leaderboard
- Customizable themes
- Next piece preview
- Ghost piece preview

## License

Open source - feel free to use and modify as you wish!
