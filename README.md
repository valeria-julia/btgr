# Binary-Ternary Greedy Reduction (BTGR) Engine

**Created by:** The Signal Architect & AI Assistant  
**Date:** February 2026  
**Status:** Experimental Logic

## Overview
The **Binary-Ternary Greedy Reduction (BTGR)** is an algorithmic engine designed to explore the structural dynamics between different numerical bases. 
Unlike the classical Collatz Conjecture ($3n+1$), which operates purely on arithmetic operations, BTGR introduces a **hybrid trans-base transition** combined with **greedy entropy reduction**.

1. **Binary Truncation** 
   If the signal ends in a `0` in the Binary Domain (Base 2), the engine performs a **Greedy Truncation**. 
   Instead of a single division by 2, it instantly strips all trailing zeros (`rstrip('0')`), collapsing the even potential of the signal to its odd core ($x / 2^k$).
 *Note - if a single 0 is removed instead of greedy truncation the output will be the original Collatz hailstone numbers sequence.
   
2. **Ternary Append** 
   If the signal is odd, it enters the **Ternary Domain (Base 3)**. The engine performs a **String-based Mutation** by appending a symbolic `"1"` to the end of the ternary string. 
   This effectively shifts the number into a new bitwise architecture ($3n + 1$) before sending it back to the Binary Domain for further filtration.

## Features
- **String-based Mutation:** Uses string manipulation in Base 3 to alter the "genetic code" of the number.
- **Greedy Truncation:** Maximizes binary entropy reduction in a single step.
- **Real-time Signal Monitoring:** Displays the decimal, binary, and ternary transformations for every step of the process.

## Scientific Context
BTGR explores the multiplicative independence between Base 2 and Base 3. The algorithm exposes how symbolic shifts in one base appear as pseudo-random mutations in another.

## License
MIT License - Free for research. Free to use, modify, and distribute with attribution to the original.

## Quick Start
To run a signal analysis (e.g., for value `170`):

```bash
python btgr_engine.py

Example Output (Signal 170)
STEP  | DECIMAL         | BINARY (Base 2)        | TERNARY (Base 3)    
--------------------------------------------------------------------------------
0     | 170             | 10101010               | 20022               
1     | 85              | 1010101                | 10011               
2     | 256             | 100000000              | 100111              
3     | 1               | 1                      | 1                   
--------------------------------------------------------------------------------
SUCCESS: Signal stabilized to 1 in 3 steps.

