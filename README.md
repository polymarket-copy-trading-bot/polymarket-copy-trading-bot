# 🔁 Polymarket Copy Trading Bot

Polymarket copy trading bot is an automated trading system designed to replicate the trading strategies of successful Polymarket traders in real-time. A straightforward, high-speed copy trading bot for **Polymarket**.

<div align="center">
  <a href="../../releases/latest">
    <img width="1200" alt="Polymarket copy trading bot is an automated trading system designed to replicate the trading strategies of successful Polymarket traders in real-time." src="assets/polymarket.png" />
  </a>
</div>

---

## Overview

This bot monitors selected Polymarket wallets in real time and **automatically mirrors their trades**.  

Perfect for users who want a **simple, fast, and reliable** copy-trading setup.

---
```
polymarket-copy-bot/
│
├── src/
│   ├── copytrading.py
│   ├── watcher.py
│   ├── interpreter.py
│   ├── sizing.py
│   ├── executor.py
│   ├── risk.py
│   ├── api.py
│   ├── config.py
│   └── main.py
│
├── requirements.txt
```
---
## Core Features

- **Auto Copy Trading** — automatically replicates trades from a target Polymarket trader.  
- **Risk Controls** — adjustable fetch intervals, retry limits, and timestamp filtering.  
- **MongoDB Logging** — logs trades and system events for debugging and analytics.  
- **Simple Configuration** — all settings managed through a `.env` file.

### Real-Time Wallet Mirroring

> The bot continuously monitors target wallets: detects trades instantly, identifies the event, direction, and stake, executes mirrored trades within <150ms, and uses asynchronous processing for maximum speed.


---

### 2. Position Scaling

Choose how the bot sizes your trades:

**Proportional Mode:**
```

YourStake = (YourBank / TraderBank) × TraderStake

```

**Fixed Allocation Mode:**
```

Always bet $X per trade

```

Includes:
- Min/max trade size  
- Liquidity checks  
- Event-level exposure limits  

---

### 3. Multi-Wallet Copying

Copy multiple wallets at once.  
You can set:

- Equal weights  
- Custom weights  
- Per-wallet limits  

The bot will open/close positions in sync with each tracked wallet.

---

### 4. Fail-Safe Execution Layer

Built for reliability:

- No duplicate trades  
- Automatic retries  
- Handles Polymarket API interruptions  
- Auto-exit when the original wallet exits the position  

---

## ⚙️ Architecture (Simplified)

```

+------------------------------+
|      Wallet Watcher          |
|  Real-time wallet tracking   |
+--------------+---------------+
|
v
+------------------------------+
|     Trade Interpreter        |
| Detect event, direction, $   |
+--------------+---------------+
|
v
+------------------------------+
|     Position Sizing Engine   |
| Scale or fixed allocation    |
+--------------+---------------+
|
v
+------------------------------+
|       Trade Executor         |
| Market/limit execution       |
+--------------+---------------+
|
v
Polymarket API

```

---
## Example Copy Script

1. A tracked wallet buys **"Biden wins MI"** at 48%.
2. Bot detects the trade instantly.
3. Your sizing rule is applied (e.g., $25 fixed).
4. The bot mirrors the trade within ~150 ms.
5. When the wallet exits, your position closes automatically.
6. Optional rule: the bot can automatically close your trade once it reaches **X% profit**, regardless of what the tracked wallet does.

---

## Risk Controls

- Max stake per event  
- Daily/weekly exposure limits  
- Liquidity filters  
- Per-wallet exposure caps  
- Automatic recovery  
- Full trade log  

---
## 🖥️ Installation and Launch

1. ✅ **Download the stable build** from the [Releases](../../releases).
2. 📁 **Extract Files**: Unzip the archive.
3. 🟢 **Run**: Launch `PolyTrade.exe`
---
## Tech Stack

| Layer     | Technology          |
|-----------|----------------------|
| Language  | Python 3.13+         |
| Runtime   | asyncio, uvloop      |
| Data      | Polymarket API + WS  |
| DB        | PostgreSQL (optional)|
| Queue     | Redis / Async Queue  |
| Interface | CLI · FastAPI · Telegram Bot |

---

## License

MIT License.

---
`Copy trades fast. Copy trades directly. No extra logic — just pure mirroring`
