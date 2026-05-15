# ✊ 🖐 ✌️ Rock Paper Scissors — Streamlit Game

A fully-featured **Rock Paper Scissors** game built with Python and Streamlit.  
Clean white UI, blue buttons, score tracking, difficulty modes, match history, and more.

| Home Screen | Result Panel | History |
|---|---|---|
| ![Home](screenshots/home.png) | ![Result](screenshots/result.png) | ![History](screenshots/history.png) |


## ✨ Features

| Feature | Details |
|---|---|
| 🎮 **3 Difficulty Modes** | Easy (CPU makes mistakes), Normal (random), Hard (AI predicts your move) |
| 🏆 **3 Game Modes** | Classic (endless), Best of 5, Best of 10 |
| 📊 **Live Score Tracking** | Your wins, CPU wins, draws — all update every round |
| 🔥 **Win Streak Counter** | Tracks current streak and all-time best streak |
| 📈 **Win Rate %** | Live win rate with animated progress bar in sidebar |
| 📜 **Round History** | Last 15 rounds shown with timestamps and WIN/LOSE/DRAW badges |
| ⬇️ **Export to CSV** | Download your full match history as a CSV file |
| 🔄 **Reset Button** | Clear all scores and start fresh anytime |
| 🎨 **Clean White UI** | Professional white theme, blue buttons, custom fonts |

---

## 🗂️ Project Structure

```
rock-paper-scissors/
│
├── rock_paper_scissors.py   
├── requirements.txt         
├── README.md                
└── screenshots/            
```
# ▶️ How to Run

# ✊ 🖐 ✌️ Rock Paper Scissors Game — How to Run

> Don't worry if you are not from IT background — just follow each step carefully and the game will work! 😊

---

## 📥 Step 1 — Install Python

Python is the language this game is built in. You need to install it first.

1. Go to → **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python"** button
3. Open the downloaded file
4. ⚠️ **Very Important** — Before clicking Install, check the box that says **"Add Python to PATH"**
5. Click **Install Now**
6. Done ✅

---

## 📥 Step 2 — Download the Game Files

1. Go to the GitHub page of this project
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Open your Downloads folder
5. **Right click** the ZIP file → click **"Extract All"**
6. You will see a folder — open it

---

## 💻 Step 3 — Open Terminal / Command Prompt

This is where you type commands to run the game.

**Windows:**
- Press `Windows key + R` on your keyboard
- Type `cmd` and press Enter
- A black window will open — that is the terminal ✅

**Mac:**
- Press `Cmd + Space`
- Type `Terminal` and press Enter ✅

---

## 📂 Step 4 — Go to the Game Folder

In the terminal, type this and press Enter:

**Windows:**
```
cd Downloads\rock-paper-scissors
```

**Mac:**
```
cd Downloads/rock-paper-scissors
```

> 💡 `cd` means "go into this folder"

---

## 📦 Step 5 — Install Required Tools

Type this exactly and press Enter:

```
pip install streamlit pandas
```

Wait for it to finish. It will download what the game needs.
This only needs to be done **once** — never again! ✅

---

## ▶️ Step 6 — Run the Game!

Type this and press Enter:

```
python -m streamlit run rock_paper_scissors.py
```

After a few seconds, your **browser will open automatically** with the game! 🎮

If browser doesn't open by itself, open any browser (Chrome, Firefox) and go to:
```
http://localhost:8501
```

---

## 🎮 How to Play

1. You will see **3 buttons** — Rock, Paper, Scissors
2. Click the one you want to play
3. Click the **"Play"** button
4. The computer will make its move
5. Result shows instantly — Win, Lose or Draw!
6. Your score is saved automatically at the top

---

## 🛑 How to Close the Game

- Go back to the terminal (black window)
- Press **Ctrl + C** on your keyboard
- Game will stop ✅

---

## ❓ Something Not Working?

| Problem | Solution |
|---|---|
| `pip is not recognized` | Restart your computer and try again |
| Game doesn't open | Make sure you typed the command correctly |
| Browser opens but shows error | Wait 10 seconds and refresh the page |
| Nothing happens after Step 6 | Open Chrome and go to `http://localhost:8501` |

---

## 🌐 Easiest Way — Play Online

If someone shares a link like this with you:
```
https://rock-paper-scissors.streamlit.app
```

Just **click the link** and play directly in your browser.
**No installation needed at all!** 🎉

---

> Made with ❤️ using Python & Streamlit