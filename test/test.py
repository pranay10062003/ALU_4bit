import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def alu_test(dut):
    """Test all ALU opcodes with 4-bit operands."""

    # Start clock
    cocotb.fork(Clock(dut.clk, 10, units="ns").start())

    # Apply reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # Enable ALU
    dut.ena.value = 1

    # Test all opcodes and 4-bit operand combinations
    for sel in range(13):       # ALU sel 0..12
        for a in range(16):     # 4-bit operand a
            for b in range(16): # 4-bit operand b
                # Drive inputs (mask to 4 bits)
                dut.ui_in.value = ((sel & 0xF) << 4) | (a & 0xF)
                dut.uio_in.value = b & 0xFF

                await RisingEdge(dut.clk)

                # Compute expected 16-bit result
                if sel == 0:
                    expected = (a + b) & 0xFFFF
                elif sel == 1:
                    expected = (a - b) & 0xFFFF
                elif sel == 2:
                    expected = (a * b) & 0xFFFF
                elif sel == 3:
                    expected = (a // b if b != 0 else 0) & 0xFFFF
                elif sel == 4:
                    expected = a & b
                elif sel == 5:
                    expected = a | b
                elif sel == 6:
                    expected = (~a) & 0xFFFF
                elif sel == 7:
                    expected = (~b) & 0xFFFF
                elif sel == 8:
                    expected = (a * a) & 0xFFFF
                elif sel == 9:
                    expected = (b * b) & 0xFFFF
                elif sel == 10:
                    expected = 0xFFFF if a < b else 0x0000
                elif sel == 11:
                    expected = 0xFFFF if a == b else 0x0000
                elif sel == 12:
                    expected = 0xFFFF if a > b else 0x0000
                else:
                    expected = 0

                # Read actual 16-bit ALU output
                lower = dut.uo_out.value.integer
                upper = dut.uio_out.value.integer
                actual = (upper << 8) | lower

                # Assert result
                assert actual == expected, (
                    f"ALU failed for sel={sel}, a={a}, b={b}: "
                    f"got 0x{actual:04X}, expected 0x{expected:04X}"
                )
