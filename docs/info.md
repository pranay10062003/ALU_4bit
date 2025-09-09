## How it works

This project implements a **4-bit Arithmetic Logic Unit (ALU)** in Verilog.  
It takes two 4-bit inputs (`A` and `B`), a 4-bit opcode (operation select), and produces an 8-bit output.

The ALU supports arithmetic (add, subtract, multiply, divide), logic (AND, OR, NOT), and comparison (less than, equal, greater than) operations. Some extended functions like squaring `A` or `B` are also included.

- `ui_in[3:0]` = Operand A (4 bits)  
- `ui_in[7:4]` = Operand B (4 bits)  
- `uio_in[3:0]` = Opcode select (operation)  
- `uo_out[7:0]` = ALU result (8 bits)

---

## How to test

1. Power up the Tiny Tapeout board with this design.  
2. Use `ui_in[7:0]` to set the two operands (`A` and `B`).  
   - Lower 4 bits = `A`  
   - Upper 4 bits = `B`  
3. Set the 4-bit opcode using `uio_in[3:0]` to select an operation.  
4. Observe the 8-bit result on `uo_out[7:0]`.

**Example test cases:**

- If `A = 3 (0011)` and `B = 2 (0010)`, and opcode = `0000` (Addition),  
  → `uo_out = 5 (00000101)`.  

- If `A = 4 (0100)` and `B = 4 (0100)`, and opcode = `1011` (Equal to),  
  → `uo_out = 255 (11111111)`.  

---

## External hardware

This design does **not** require any external hardware.  
It can be tested using the standard Tiny Tapeout board inputs (`ui_in`, `uio_in`) and observing outputs (`uo_out`).  
Optionally, you may connect LEDs to visualize the ALU output bits.
