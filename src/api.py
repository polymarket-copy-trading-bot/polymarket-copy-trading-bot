import httpx
import asyncio

class PolymarketAPI:
    """Simple HTTP wrapper for Polymarket REST API."""

    BASE = "https://api.polymarket.com"

    async def get_wallet_trades(self, wallet: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.BASE}/wallet/{wallet}/activity")
            return r.json()

    async def send_trade(self, event_id: str, side: str, amount: float):
        # Placeholder for real API trading
        print(f"[EXECUTE] {side.upper()} {amount} on event {event_id}")
