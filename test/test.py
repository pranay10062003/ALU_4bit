# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_alu_4bit(dut):
    """Test the 4-bit ALU"""

    dut._log.info("Start ALU test")

    # Test inputs
    a = 0b1110  # 14
    b = 0b1001  # 9

    # Apply inputs
    dut.ui_in.value = a
    dut.uio_in.value = b

    # A dictionary of operation: expected_value
    expected = {
        0b0000: a + b,          # Add
        0b0001: a - b,          # Sub
        0b0010: a * b,          # Mul
        0b0011: a // b,         # Div (integer division)
        0b0100: a & b,          # AND
        0b0101: a | b,          # OR
        0b0110: (~a) & 0xF,     # NOT a (mask to 4 bits)
        0b0111: (~b) & 0xF,     # NOT b (mask to 4 bits)
        0b1000: a * a,          # Square a
        0b1001: b * b,          # Square b
        0b1010: 0xFF if a < b else 0x00,   # Less than
        0b1011: 0xFF if a == b else 0x00,  # Equal
        0b1100: 0xFF if a > b else 0x00,   # Greater than
    }

    # Loop through all operations
    for sel, exp in expected.items():
        dut.ena.value = sel
        await Timer(1, units="ns")  # small delay to settle

        got = int(dut.uo_out.value)
        dut._log.info(f"sel={sel:04b}, ui_in={a}, uio_in={b}, got={got}, expected={exp}")

        assert got == (exp & 0xFF), f"Mismatch: sel={sel:04b}, got={got}, expected={exp}"
