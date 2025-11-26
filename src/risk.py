class RiskManager:
    """Simple rule-based risk filters."""

    def allow(self, stake: float, liquidity: float = 10000):
        if stake < 5:
            return False
        if stake > 500:
            return False
        if liquidity < 1000:
            return False
        return True
