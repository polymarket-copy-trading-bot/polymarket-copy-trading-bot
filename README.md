# 🔁 Polymarket Copy Trading Bot

A straightforward, high-speed copy trading bot for **Polymarket**. 

![Polymarket Copy Trading](assets/AGENT.png)

---

## 📘 Overview

This bot monitors selected Polymarket wallets in real time and **automatically mirrors their trades**.  

Perfect for users who want a **simple, fast, and reliable** copy-trading setup.

---

## 🌟 Core Features

### 🟢 1. Real-Time Wallet Mirroring

The bot continuously watches target wallets:

- Detects trades instantly  
- Identifies event, direction, and stake  
- Executes mirrored trades within milliseconds  
- Uses asynchronous processing for maximum speed  

---

### 🟢 2. Position Scaling

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

### 🟢 3. Multi-Wallet Copying

Copy multiple wallets at once.  
You can set:

- Equal weights  
- Custom weights  
- Per-wallet limits  

The bot will open/close positions in sync with each tracked wallet.

---

### 🟢 4. Fail-Safe Execution Layer

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
## 📊 Example Copy Script

1. A tracked wallet buys **"Biden wins MI"** at 48%.
2. Bot detects the trade instantly.
3. Your sizing rule is applied (e.g., $25 fixed).
4. The bot mirrors the trade within ~150 ms.
5. When the wallet exits, your position closes automatically.
6. Optional rule: the bot can automatically close your trade once it reaches **X% profit**, regardless of what the tracked wallet does.

---

## 🔒 Risk Controls

- Max stake per event  
- Daily/weekly exposure limits  
- Liquidity filters  
- Per-wallet exposure caps  
- Automatic recovery  
- Full trade log  

---

## 🧩 Tech Stack

| Layer     | Technology          |
|-----------|----------------------|
| Language  | Python 3.13+         |
| Runtime   | asyncio, uvloop      |
| Data      | Polymarket API + WS  |
| DB        | PostgreSQL (optional)|
| Queue     | Redis / Async Queue  |
| Interface | CLI · FastAPI · Telegram Bot |

---

## 📄 License

MIT License.

---

## ⚖️ Disclaimer

This software is for research and educational purposes only.  
The author is not responsible for any financial losses or outcomes.

---

## 🚀

**Copy trades fast. Copy trades directly. No extra logic — just pure mirroring.**
```
