import numpy as np

def expected_value(prob_ai: float, prob_market: float, reward: float = 1.0):
    """Simple Expected Value calculation"""
    return (prob_ai * reward) - (prob_market * reward)

def kelly_fraction(prob: float, odds: float):
    """Kelly Criterion: optimal bet fraction"""
    b = odds - 1
    return (b * prob - (1 - prob)) / b if b > 0 else 0
