module LFSR_PRNG (input clk, rst, output reg [2:0] out);
  reg [5:0] D123456 = 6'b000001;
  always @ (posedge clk or negedge rst)begin
    if(!rst) begin
      D123456[5] <= D123456[4];
      D123456[4] <= D123456[3];
      D123456[3] <= D123456[2];
      D123456[2] <= D123456[1];
      D123456[1] <= D123456[0];
      D123456[0] <= D123456[5] ^ D123456[4];
    end else begin
      D123456 <= 6'b000001;
    end
      out[0] <= D123456[1];
      out[1] <= D123456[3];
      out[2] <= D123456[5];
  End
endmodule
