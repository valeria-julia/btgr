"""
Binary-Ternary Greedy Reduction (BTGR)
Author: The Signal Architect & AI Assistant
Created: February 2026
Logic: String-based Ternary Mutation + Greedy Binary Truncation
"""

class BTGREngine:
    def __init__(self, start_value):
        self.start_value = start_value
        self.history = []

    @staticmethod
    def to_ternary(n):
        """Converts a decimal integer to its base-3 (ternary) string representation."""
        if n == 0: return "0"
        digits = []
        temp = n
        while temp > 0:
            digits.append(str(temp % 3))
            temp //= 3
        return "".join(reversed(digits))

    def run(self, max_steps=1000):
        """
        Executes the BTGR logic.
        """
        x = self.start_value
        
        print(f"--- BTGR ENGINE INITIALIZED | START: {x} ---")
        print(f"{'STEP':<5} | {'DECIMAL':<15} | {'BINARY (Base 2)':<22} | {'TERNARY (Base 3)':<20}")
        print("-" * 80)

        for step in range(max_steps):
            binary_str = bin(x)[2:]
            ternary_str = self.to_ternary(x)
            
            # Real-time signal monitoring
            print(f"{step:<5} | {x:<15} | {binary_str:<22} | {ternary_str:<20}")
            
            if x == 1:
                print("-" * 80)
                print(f"SUCCESS: Signal stabilized to 1 in {step} steps.")
                return True

            # Logic Check: Terminal bit in Binary Domain
            if binary_str.endswith('0'):
                # PHASE 1: GREEDY TRUNCATION (Base 2)
                # Removes all trailing zeros at once (Division by 2^k)
                x = int(binary_str.rstrip('0'), 2)
            else:
                # PHASE 2: STRING-BASED MUTATION (Base 3)
                # Appends '1' symbol to the ternary string (Effective 3n + 1)
                t_mutated = ternary_str + "1"
                x = int(t_mutated, 3)

        print("-" * 80)
        print("HALTED: Step limit reached. Signal complexity exceeding bounds.")
        return False

if __name__ == "__main__":
    # Standard test with signal 170
    engine = BTGREngine(170)
    engine.run()
