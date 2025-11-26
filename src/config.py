# Global configuration for the Polymarket Copy Trading Bot

CONFIG = {
    "wallets_to_track": [
        "0x1234567890abcdef...",
        "0xabcdefabcdef12345..."
    ],

    "mode": "fixed",   # "fixed" or "proportional"
    "fixed_stake": 25,
    "min_stake": 5,
    "max_stake": 300,

    "profit_take_percent": 20,  # auto-close at +X% profit

    "api_base": "https://api.polymarket.com",
}
