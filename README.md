# 4-bit ALU (Arithmetic Logic Unit)

## Overview
This project implements a **4-bit Arithmetic Logic Unit (ALU)** in Verilog for Tiny Tapeout.  
The ALU takes two 4-bit inputs (`ui_in[3:0]` and `ui_in[7:4]`), a 4-bit opcode (`uio_in[3:0]`), and produces an 8-bit output (`uo_out[7:0]`).  

The design is **combinational** (no clock/reset), making it simple and efficient.

---

## Features
The ALU supports the following operations based on the opcode (`uio_in[3:0]`):

| Opcode | Operation               | Description                  |
|--------|--------------------------|------------------------------|
| 0000   | Addition                 | `A + B`                     |
| 0001   | Subtraction              | `A - B`                     |
| 0010   | Multiplication           | `A * B`                     |
| 0011   | Division                 | `A / B`                     |
| 0100   | AND                      | `A & B`                     |
| 0101   | OR                       | `A \| B`                    |
| 0110   | NOT A                    | `~A`                        |
| 0111   | NOT B                    | `~B`                        |
| 1000   | Square A                 | `A * A`                     |
| 1001   | Square B                 | `B * B`                     |
| 1010   | Less than                | `11111111` if A < B else 0  |
| 1011   | Equal to                 | `11111111` if A == B else 0 |
| 1100   | Greater than             | `11111111` if A > B else 0  |

---

## Pinout
- **Inputs (`ui_in`)**  
  - `ui_in[3:0]`: Operand A (4-bit)  
  - `ui_in[7:4]`: Operand B (4-bit)  

- **Outputs (`uo_out`)**  
  - `uo_out[7:0]`: ALU result (8-bit)  

- **Bidirectional (`uio_in`)**  
  - `uio_in[3:0]`: Opcode select  

---

## Simulation & Testing
A **Cocotb testbench** verifies all ALU operations.  
Run tests with:

```bash
make test
