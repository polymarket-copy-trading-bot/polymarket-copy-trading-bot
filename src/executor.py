import asyncio
from api import PolymarketAPI
from config import CONFIG

class TradeExecutor:
    """Executes trades and handles auto-close on profit."""

    def __init__(self):
        self.api = PolymarketAPI()
        self.positions = {}

    async def open_position(self, event_id, side, stake):
        await self.api.send_trade(event_id, side, stake)
        self.positions[event_id] = {
            "side": side,
            "stake": stake,
            "entry_price": 0.0  # placeholder
        }

    async def close_on_profit(self, event_id, current_price):
        pos = self.positions.get(event_id)
        if not pos:
            return

        entry = pos["entry_price"]
        pct = ((current_price - entry) / entry) * 100 if entry > 0 else 0

        if pct >= CONFIG["profit_take_percent"]:
            print(f"[PROFIT TAKE] Closing {event_id} at +{pct:.2f}%")
            await self.api.send_trade(event_id, "sell", pos["stake"])
            del self.positions[event_id]
