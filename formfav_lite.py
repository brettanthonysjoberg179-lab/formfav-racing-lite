#!/usr/bin/env python3
"""
FormFav Racing Intelligence — Open-Source Lite Edition
===================================================
Basic manual calculator for calculating boxed trifecta combinations and runner barrier weights.
"""

def calculate_trifecta_box(horses: list) -> int:
    """Calculates number of combinations for a boxed trifecta."""
    n = len(horses)
    if n < 3:
        raise ValueError("Need at least 3 horses for a trifecta box.")
    # n * (n - 1) * (n - 2)
    return n * (n - 1) * (n - 2)

def main():
    print("🐎 FormFav Racing Lite — Manual Trifecta Calculator")
    sample_horses = ["Swift Runner", "Thunder Hoof", "Desert Storm", "Shadow Dancer"]
    combos = calculate_trifecta_box(sample_horses)
    print(f"Sample horses: {sample_horses}")
    print(f"Boxed Trifecta Combinations: {combos}")
    print("\n💡 Want 100% automated daily AU gallops form cards, algorithmic barrier/weight selections,")
    print("   and 1-click PDF booklet generation? Get the fully automated Pro subscription on Gumroad:")
    print("   👉 https://brettanthonysjoberg1.gumroad.com")

if __name__ == "__main__":
    main()
