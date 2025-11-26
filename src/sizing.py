from config import CONFIG

class PositionSizer:
    """Fixed or proportional sizing."""

    def scale(self, trader_stake: float) -> float:
        mode = CONFIG["mode"]

        if mode == "fixed":
            return CONFIG["fixed_stake"]

        if mode == "proportional":
            # Fake example for demonstration
            return trader_stake * 0.5

        return CONFIG["fixed_stake"]
