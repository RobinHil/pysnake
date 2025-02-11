# 🐍 PySnake

A classic Snake game built with Python and Tkinter.

## 🎮 Game Features

- Clean and minimalist interface
- High score tracking
- Smooth controls
- Welcome and game over screens
- Classic snake gameplay mechanics

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/RobinHil/pysnake.git
cd pysnake
```

2. Install the required dependencies:
```bash
pip install tkinter pyinstaller
```

## 🛠️ Building the Game

### On Windows
```powershell
.\build.ps1
```

### On Linux
```bash
chmod +x build.sh
./build.sh
```

The executable will be created in the `dist` directory.

## 🎯 How to Play

1. Launch the game
2. Press SPACE to start
3. Use arrow keys to control the snake:
   - ⬆️ Up arrow
   - ⬇️ Down arrow
   - ➡️ Right arrow
   - ⬅️ Left arrow
4. Eat the red food to grow
5. Avoid hitting the walls and yourself
6. Try to beat your high score!

## 💾 Save System

The game automatically saves your high score in a `.high_score` file.

## 🔧 Technical Details

- Built with Python 3
- Uses Tkinter for GUI
- Single executable file after build
- Custom icon included
