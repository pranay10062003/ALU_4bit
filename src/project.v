`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs: [7:4] opcode, [3:0] part of operand
    output wire [7:0] uo_out,   // Dedicated outputs: lower 8 bits of result
    input  wire [7:0] uio_in,   // IOs: Input path (operand 2)
    output wire [7:0] uio_out,  // IOs: Output path (upper 8 bits of result)
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // always 1 when powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset, active low
);

  // Internal connections
  wire [3:0] sel = ui_in[7:4];  // opcode from upper nibble
  wire [7:0] in1 = ui_in;       // operand1
  wire [7:0] in2 = uio_in;      // operand2
  wire [15:0] alu_out;

  // Instantiate ALU
  ALU_4bit alu_inst (
    .out(alu_out),
    .sel(sel),
    .in1(in1),
    .in2(in2)
  );

  // Map ALU outputs
  assign uo_out  = alu_out[7:0];   // lower byte
  assign uio_out = alu_out[15:8];  // upper byte
  assign uio_oe  = 8'hFF;          // drive all uio_out bits

  // Prevent unused input warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule


// ALU module (unchanged)
module ALU_4bit(
  output reg [15:0] out,
  input [3:0] sel,
  input [7:0] in1,in2
);
  always @(*) begin
    case(sel)
      4'b0000: out = in1+in2;
      4'b0001: out = in1-in2;
      4'b0010: out = in1*in2;
      4'b0011: out = in1/in2;
      4'b0100: out = in1&in2;
      4'b0101: out = in1|in2;
      4'b0110: out = ~in1;
      4'b0111: out = ~in2;
      4'b1000: out = in1*in1;
      4'b1001: out = in2*in2;
      4'b1010: out = (in1 < in2) ? 16'hFFFF : 16'h0000;
      4'b1011: out = (in1 == in2) ? 16'hFFFF : 16'h0000;
      4'b1100: out = (in1 > in2) ? 16'hFFFF : 16'h0000;
      default: out = 16'h0000;
    endcase
  end
endmodule
