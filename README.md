# 🤖 Polymarket AI Copy Trading & Prediction Bot

**High-precision, AI-augmented copy trading engine for Polymarket ---
built to replicate top traders with speed, safety, and autonomy.**

![Polymarket AI Copy Trading](assets/AGENT.png)

------------------------------------------------------------------------

## 🧠 Overview

At its core, this system is **a next-generation copy trading engine**,
not a generic trading bot.
It tracks selected wallets in real time, analyzes each position,
validates the trade with AI, and mirrors it with optimal sizing.

Unlike traditional copiers that blindly mirror every trade, this system
**evaluates the reasoning behind the trader's action**, filters noise,
and only executes trades that pass risk and probability checks.

------------------------------------------------------------------------

## 🌟 Core Copy-Trading Features

### 🟢 1. Real-Time Wallet Mirroring

Live monitoring of selected Polymarket wallets:

-   Detects trades instantly
-   Identifies event, direction, and stake
-   Executes mirrored trades within milliseconds
-   Built on a fully asynchronous event-driven pipeline

------------------------------------------------------------------------

### 🟢 2. Intelligent Position Scaling

Your position automatically adjusts according to strategy:

**Scale Mode (proportional):**

    YourStake = (YourBank / TraderBank) × TraderStake

**Allocate Mode (fixed allocation):**

    Always bet $X regardless of trader’s bet size

Includes minimum/maximum trade thresholds and liquidity filters.

------------------------------------------------------------------------

### 🟢 3. AI-Assisted Copy Validation

Before mirroring a trade, the system validates it using multiple AI
models:

-   ChatGPT / DeepSeek → probability estimation
-   Claude / Gemini → context & fundamentals
-   Grok → sentiment & news patterns
-   Event EV calculation
-   Kelly-based sizing recommendation

If a trade is emotional, random, or low-quality --- **the bot will NOT
copy it**.

------------------------------------------------------------------------

### 🟢 4. Multi-Wallet Copy Portfolio

You can copy:

-   a single wallet
-   multiple wallets
-   a weighted portfolio of wallets

Weights are based on:

-   historical accuracy
-   volatility
-   risk profile

This builds a **diversified, risk-weighted copy-trading portfolio**, not
random mirrored trades.

------------------------------------------------------------------------

### 🟢 5. Fail-Safe Execution Layer

Engineered for reliability:

-   Deduplication (no double positions)
-   Automatic retries with exponential backoff
-   Recovery from Polymarket API errors
-   Automatic exit when the original trader exits

------------------------------------------------------------------------

## ⚙️ Architecture (Copy-Trading Focus)

    +--------------------------------------------------------------+
    |                       Wallet Watcher                         |
    |         Live monitoring of trader wallet activity            |
    +----------------------------+---------------------------------+
                                 |
                                 v
    +--------------------------------------------------------------+
    |           Trade Interpreter & Normalizer                     |
    |   • Detects direction, event, and stake                      |
    |   • Filters noise & artifacts                                |
    +----------------------------+---------------------------------+
                                 |
                                 v
    +--------------------------------------------------------------+
    |             AI-Assisted Copy Decision Layer                  |
    |   • LLM validation                                           |
    |   • EV/Kelly scoring                                         |
    |   • Approve/Reject                                           |
    +----------------------------+---------------------------------+
                                 |
                                 v
    +--------------------------------------------------------------+
    |                Position Scaling Engine                       |
    |   • Scale / Allocate                                         |
    |   • Risk filters                                             |
    +----------------------------+---------------------------------+
                                 |
                                 v
    +--------------------------------------------------------------+
    |                     Trade Executor                           |
    |   • Market/limit execution                                   |
    |   • Retry & fail-safe                                        |
    +----------------------------+---------------------------------+
                                 |
                                 v
                             Polymarket API

------------------------------------------------------------------------

## 📊 Example Copy Scenario

1.  A top wallet buys **"Trump wins PA"** at 42%.
2.  The bot detects the trade instantly.
3.  AI validates the idea (probability \~44--46%).
4.  EV is positive → trade approved.
5.  Position is scaled using Kelly: **2.3% of your capital**.
6.  Trade executes in \<150 ms.
7.  When the trader exits, the bot exits too.

------------------------------------------------------------------------

## 📈 Why AI Matters in Copy Trading

Traditional copy trading has a critical flaw:
**it copies good trades and bad trades equally.**

This system copies only trades that pass:

-   EV screening
-   likelihood estimation
-   fundamental checks
-   volatility and liquidity thresholds
-   trader consistency checks

If the trader makes an emotional or inconsistent trade ---\
**the bot rejects it**, protecting your capital.

------------------------------------------------------------------------

## 🧩 Tech Stack
```
  Layer        Technology
  ------------ ---------------------------------------------
  Language     Python 3.13+
  Runtime      asyncio, uvloop
  Data         Polymarket API + WebSockets
  AI Models    ChatGPT · DeepSeek · Claude · Gemini · Grok
  DB           PostgreSQL (optional)
  Queue        Redis / Async Queue
  Interfaces   CLI · FastAPI · Telegram Bot
```
------------------------------------------------------------------------

## 🔒 Copy-Trading Risk Controls

-   Max stake per event
-   Max daily/weekly exposure
-   Cooldown after losing streak
-   Minimum liquidity filter
-   Maximum exposure per trader
-   Automatic error recovery
-   Full trade journal logging

------------------------------------------------------------------------

## 📄 License

MIT License.

------------------------------------------------------------------------

## ⚖️ Disclaimer

This software is for research and educational use only.\
The author is not responsible for any financial losses or trading
outcomes.

------------------------------------------------------------------------

## 🚀

**Copy smarter, not harder.\
Let AI filter the noise --- and follow only high-quality signals.**
