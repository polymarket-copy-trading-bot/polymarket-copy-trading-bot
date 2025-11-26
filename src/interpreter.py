class TradeInterpreter:
    """Normalize raw event into unified structure."""

    def normalize(self, trade):
        return {
            "wallet": trade["wallet"],
            "event_id": trade["event"],
            "side": trade["side"],
            "stake": float(trade["stake"]),
        }
