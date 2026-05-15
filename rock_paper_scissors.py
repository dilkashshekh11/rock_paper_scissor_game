import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✊",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    color: #1e293b;
}

/* ── Background: clean white ── */
.stApp {
    background: #f5f7fa;
    min-height: 100vh;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; }

/* ── Title ── */
.game-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #1e293b;
    margin-bottom: 0.2rem;
}
.game-subtitle {
    text-align: center;
    font-size: 0.85rem;
    color: #64748b;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* ── Score cards ── */
.score-row {
    display: flex;
    gap: 12px;
    margin-bottom: 1.5rem;
}
.score-card {
    flex: 1;
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.score-card .label {
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #64748b;
    font-family: 'DM Mono', monospace;
    margin-bottom: 6px;
}
.score-card .number {
    font-size: 2.4rem;
    font-weight: 800;
    line-height: 1;
}
.score-card.wins .number   { color: #2563eb; }
.score-card.draws .number  { color: #94a3b8; }
.score-card.losses .number { color: #f59e0b; }
.score-card .sub {
    font-size: 0.7rem;
    color: #94a3b8;
    margin-top: 4px;
}

/* ── Result panel ── */
.result-panel {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.8rem;
    text-align: center;
    margin: 1.5rem 0;
    box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}
.result-vs {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 1rem;
}
.result-pick { text-align: center; }
.result-pick .icon { font-size: 3rem; }
.result-pick .name {
    font-size: 0.75rem;
    color: #64748b;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 4px;
}
.vs-text {
    font-size: 0.75rem;
    color: #cbd5e1;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.15em;
}
.result-outcome {
    font-size: 1.6rem;
    font-weight: 800;
    margin-top: 0.5rem;
}
.result-outcome.win  { color: #2563eb; }
.result-outcome.lose { color: #f59e0b; }
.result-outcome.draw { color: #94a3b8; }
.result-msg {
    font-size: 0.8rem;
    color: #94a3b8;
    margin-top: 4px;
    font-family: 'DM Mono', monospace;
}

/* ── History rows ── */
.history-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    border-radius: 10px;
    margin-bottom: 4px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    font-size: 0.82rem;
}
.history-row .round-num {
    font-family: 'DM Mono', monospace;
    color: #94a3b8;
    font-size: 0.7rem;
    min-width: 32px;
}
.history-row .picks { flex: 1; color: #334155; }
.history-row .badge {
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 700;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
}
.badge-win  { background: #dbeafe; color: #2563eb; }
.badge-lose { background: #fef3c7; color: #d97706; }
.badge-draw { background: #f1f5f9; color: #94a3b8; }

/* ── Difficulty pills ── */
.difficulty-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.08em;
    border: 1.5px solid #bfdbfe;
    color: #2563eb;
    background: #eff6ff;
}

/* ── Streak banner ── */
.streak-banner {
    background: #eff6ff;
    border: 1.5px solid #bfdbfe;
    border-radius: 12px;
    padding: 0.6rem 1rem;
    text-align: center;
    font-size: 0.82rem;
    color: #2563eb;
    margin-bottom: 0.8rem;
    font-family: 'DM Mono', monospace;
}

/* ── Win rate bar ── */
.wr-bar-bg {
    height: 6px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
    margin: 6px 0 2px;
}
.wr-bar-fill {
    height: 100%;
    border-radius: 4px;
    background: linear-gradient(90deg, #2563eb, #60a5fa);
    transition: width 0.4s ease;
}

/* ── All Streamlit buttons → blue ── */
.stButton > button {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    transition: background 0.2s !important;
}
.stButton > button:hover {
    background-color: #1d4ed8 !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.3) !important;
}
.stButton > button:disabled {
    background-color: #cbd5e1 !important;
    color: #94a3b8 !important;
}

/* ── Sidebar: white with light border ── */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1.5px solid #e2e8f0 !important;
}
section[data-testid="stSidebar"] * {
    color: #1e293b !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #1e293b !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
defaults = {
    "wins": 0, "losses": 0, "draws": 0,
    "total": 0, "streak": 0, "best_streak": 0,
    "history": [],          # list of round dicts
    "last_result": None,    # dict with result info
    "selected": None,       # user's current pick
    "difficulty": "Normal", # Easy / Normal / Hard
    "game_mode": "Classic", # Classic / Best of 5 / Best of 10
    "round_in_set": 0,
    "set_wins": 0, "set_losses": 0,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Game logic helpers ────────────────────────────────────────────────────────
CHOICES    = ["Rock", "Paper", "Scissors"]
ICONS      = {"Rock": "✊", "Paper": "🖐", "Scissors": "✌️"}
BEATS      = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
BEATEN_BY  = {v: k for k, v in BEATS.items()}

WIN_MSGS   = ["You crushed it!", "Flawless play!", "The computer weeps.", "Dominant!", "Too easy for you."]
LOSE_MSGS  = ["The machine wins.", "Ouch.", "Better luck next round.", "The algorithm got you.", "It calculated your move!"]
DRAW_MSGS  = ["Great minds think alike.", "A perfect mirror.", "Stalemate.", "Neither yields.", "Dead even."]

def computer_move(difficulty, history):
    if difficulty == "Easy":
        # Computer makes random mistakes ~40% of the time
        if random.random() < 0.4:
            return random.choice(CHOICES)
        # Otherwise picks a random losing move against user's last move
        if history:
            user_last = history[-1]["user"]
            return BEATS[user_last]  # This LOSES to user's last move (intentional for easy)
        return random.choice(CHOICES)

    elif difficulty == "Hard":
        # Hard: tries to predict by most-frequent user move
        if len(history) >= 3:
            from collections import Counter
            user_moves = [h["user"] for h in history[-10:]]
            predicted = Counter(user_moves).most_common(1)[0][0]
            # Beat the predicted move
            return BEATEN_BY[predicted]
        return random.choice(CHOICES)

    else:  # Normal
        return random.choice(CHOICES)

def judge(user, cpu):
    if user == cpu:
        return "draw"
    if BEATS[user] == cpu:
        return "win"
    return "loss"

def win_rate():
    t = st.session_state.total
    return round(st.session_state.wins / t * 100) if t else 0

def set_target():
    return {"Best of 5": 3, "Best of 10": 6}.get(st.session_state.game_mode, None)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    st.markdown("---")

    st.session_state.difficulty = st.selectbox(
        "Difficulty", ["Easy", "Normal", "Hard"],
        index=["Easy", "Normal", "Hard"].index(st.session_state.difficulty)
    )
    st.session_state.game_mode = st.selectbox(
        "Game mode", ["Classic", "Best of 5", "Best of 10"],
        index=["Classic", "Best of 5", "Best of 10"].index(st.session_state.game_mode)
    )

    st.markdown("---")
    st.markdown("### 📊 Statistics")

    wr = win_rate()
    st.markdown(f"""
    <div style='margin-bottom:1rem'>
      <div style='display:flex;justify-content:space-between;font-size:0.8rem;margin-bottom:4px'>
        <span>Win rate</span><span style='color:#2563eb;font-weight:700'>{wr}%</span>
      </div>
      <div class='wr-bar-bg'>
        <div class='wr-bar-fill' style='width:{wr}%'></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Best streak", st.session_state.best_streak)
        st.metric("Wins", st.session_state.wins)
    with col2:
        st.metric("Total rounds", st.session_state.total)
        st.metric("Losses", st.session_state.losses)

    st.markdown("---")
    st.markdown("### 📖 Rules")
    st.markdown("""
    - ✊ **Rock** beats ✌️ Scissors  
    - 🖐 **Paper** beats ✊ Rock  
    - ✌️ **Scissors** beats 🖐 Paper  
    """)

    st.markdown("---")
    if st.button("🔄 Reset all scores", use_container_width=True):
        for k in ["wins","losses","draws","total","streak","best_streak","history","last_result","selected","round_in_set","set_wins","set_losses"]:
            st.session_state[k] = defaults[k]
        st.rerun()

# ── Main layout ───────────────────────────────────────────────────────────────
st.markdown('<div class="game-title">✊ 🖐 ✌️</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">Rock · Paper · Scissors</div>', unsafe_allow_html=True)

# Difficulty + mode pills
mode_display = st.session_state.game_mode
diff_display = st.session_state.difficulty
st.markdown(f"""
<div style='display:flex;gap:8px;justify-content:center;margin-bottom:1.5rem'>
  <span class='difficulty-pill'>⚡ {diff_display}</span>
  <span class='difficulty-pill'>🎮 {mode_display}</span>
</div>
""", unsafe_allow_html=True)

# ── Score display ─────────────────────────────────────────────────────────────
target = set_target()
if target:
    sw = st.session_state.set_wins
    sl = st.session_state.set_losses
    rounds_left = (target * 2 - 1) - st.session_state.round_in_set
    st.markdown(f"""
    <div class='streak-banner'>
      🏆 {mode_display} — You {sw} · CPU {sl} · Need {target} to win · {rounds_left} rounds left
    </div>
    """, unsafe_allow_html=True)
elif st.session_state.streak >= 3:
    st.markdown(f"""
    <div class='streak-banner'>
      🔥 {st.session_state.streak}-round win streak!
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class='score-row'>
  <div class='score-card wins'>
    <div class='label'>Your Wins</div>
    <div class='number'>{st.session_state.wins}</div>
    <div class='sub'>🔥 streak: {st.session_state.streak}</div>
  </div>
  <div class='score-card draws'>
    <div class='label'>Draws</div>
    <div class='number'>{st.session_state.draws}</div>
    <div class='sub'>win rate: {win_rate()}%</div>
  </div>
  <div class='score-card losses'>
    <div class='label'>CPU Wins</div>
    <div class='number'>{st.session_state.losses}</div>
    <div class='sub'>best streak: {st.session_state.best_streak}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Move selection ─────────────────────────────────────────────────────────────
st.markdown("<p style='text-align:center;color:#6b7280;font-size:0.82rem;font-family:\"DM Mono\",monospace;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.5rem'>Choose your move</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
for col, choice in zip([col1, col2, col3], CHOICES):
    with col:
        is_sel = st.session_state.selected == choice
        label = f"{ICONS[choice]}\n\n{'**' if is_sel else ''}{choice}{'**' if is_sel else ''}"
        if st.button(label, key=f"btn_{choice}", use_container_width=True):
            st.session_state.selected = choice
            st.rerun()

# ── Play button ────────────────────────────────────────────────────────────────
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
play_disabled = st.session_state.selected is None

# Check if set is over
set_over = False
if target:
    set_over = (st.session_state.set_wins >= target or st.session_state.set_losses >= target)

if set_over:
    winner_str = "🏆 You won the set!" if st.session_state.set_wins >= target else "💀 CPU won the set!"
    st.success(winner_str)
    if st.button("🔁 New set", use_container_width=True):
        st.session_state.round_in_set = 0
        st.session_state.set_wins = 0
        st.session_state.set_losses = 0
        st.session_state.selected = None
        st.session_state.last_result = None
        st.rerun()
else:
    if st.button(
        "▶  Play" if not play_disabled else "← Pick a move first",
        disabled=play_disabled,
        use_container_width=True,
        type="primary" if not play_disabled else "secondary"
    ):
        user   = st.session_state.selected
        cpu    = computer_move(st.session_state.difficulty, st.session_state.history)
        result = judge(user, cpu)

        # Update scores
        st.session_state.total += 1
        st.session_state.round_in_set += 1

        if result == "win":
            st.session_state.wins   += 1
            st.session_state.streak += 1
            st.session_state.set_wins += 1
            st.session_state.best_streak = max(
                st.session_state.best_streak, st.session_state.streak
            )
            msg = random.choice(WIN_MSGS)
        elif result == "loss":
            st.session_state.losses += 1
            st.session_state.streak  = 0
            st.session_state.set_losses += 1
            msg = random.choice(LOSE_MSGS)
        else:
            st.session_state.draws  += 1
            msg = random.choice(DRAW_MSGS)

        round_data = {
            "round": st.session_state.total,
            "user": user, "cpu": cpu,
            "result": result, "msg": msg,
            "time": datetime.now().strftime("%H:%M:%S"),
        }
        st.session_state.history.insert(0, round_data)
        st.session_state.last_result = round_data
        st.session_state.selected = None
        st.rerun()

# ── Last result ────────────────────────────────────────────────────────────────
if st.session_state.last_result:
    r = st.session_state.last_result
    outcome_class = r["result"]          # win / loss / draw
    outcome_label = {"win":"YOU WIN","loss":"CPU WINS","draw":"DRAW"}[outcome_class]

    st.markdown(f"""
    <div class='result-panel'>
      <div class='result-vs'>
        <div class='result-pick'>
          <div class='icon'>{ICONS[r['user']]}</div>
          <div class='name'>You · {r['user']}</div>
        </div>
        <div class='vs-text'>VS</div>
        <div class='result-pick'>
          <div class='icon'>{ICONS[r['cpu']]}</div>
          <div class='name'>CPU · {r['cpu']}</div>
        </div>
      </div>
      <div class='result-outcome {outcome_class}'>{outcome_label}</div>
      <div class='result-msg'>{r['msg']}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Round history ─────────────────────────────────────────────────────────────
if st.session_state.history:
    st.markdown("---")
    st.markdown("<p style='color:#6b7280;font-size:0.78rem;font-family:\"DM Mono\",monospace;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:0.75rem'>Round history</p>", unsafe_allow_html=True)

    # Show last 15 rounds
    for h in st.session_state.history[:15]:
        badge_class = f"badge-{h['result'] if h['result'] != 'loss' else 'lose'}"
        badge_text  = {"win":"WIN","loss":"LOSE","draw":"DRAW"}[h["result"]]
        st.markdown(f"""
        <div class='history-row'>
          <div class='round-num'>#{h['round']}</div>
          <div class='picks'>{ICONS[h['user']]} {h['user']} &nbsp;vs&nbsp; {ICONS[h['cpu']]} {h['cpu']}</div>
          <div style='color:#4b5563;font-size:0.7rem;font-family:"DM Mono",monospace'>{h['time']}</div>
          <div class='badge {badge_class}'>{badge_text}</div>
        </div>
        """, unsafe_allow_html=True)

    # Export history
    if len(st.session_state.history) > 0:
        df = pd.DataFrame([{
            "Round": h["round"], "You": h["user"], "CPU": h["cpu"],
            "Result": h["result"].upper(), "Time": h["time"]
        } for h in st.session_state.history])
        st.download_button(
            "⬇ Download history (CSV)",
            df.to_csv(index=False),
            "rps_history.csv", "text/csv",
            use_container_width=True
        )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align:center;font-size:0.72rem;color:#374151;font-family:"DM Mono",monospace;letter-spacing:0.08em'>
  ROCK · PAPER · SCISSORS — built with Streamlit
</p>
""", unsafe_allow_html=True)
