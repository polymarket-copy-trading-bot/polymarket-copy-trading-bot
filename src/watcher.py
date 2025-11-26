import asyncio
from api import PolymarketAPI

class WalletWatcher:
    """Real-time wallet activity polling."""

    def __init__(self, wallets):
        self.api = PolymarketAPI()
        self.wallets = wallets

    async def stream(self):
        while True:
            for w in self.wallets:
                trades = await self.api.get_wallet_trades(w)
                for t in trades:
                    yield {
                        "wallet": w,
                        "event": t.get("event_id"),
                        "side": t.get("outcome"),
                        "stake": t.get("amount")
                    }
            await asyncio.sleep(1)  # simple polling
