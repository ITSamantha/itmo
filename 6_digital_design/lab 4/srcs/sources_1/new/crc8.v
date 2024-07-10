`timescale 1ns / 1ps

module crc8(
    input clk_i,
    input rst_i,
    input calc_i,
    input[4:0] a_bi,
    output reg[7:0] y_bo
);

parameter DEFAULT = 8'b10111010;
parameter K = 8'b00011011; //polinome


integer i;

reg[7:0] shifted_reg = DEFAULT;

always @(posedge calc_i) begin
    shifted_reg = y_bo;
    for (i = 0; i < 8; i = i + 1) begin
        shifted_reg = shifted_reg ^ a_bi;
        if (shifted_reg[7] == 1'b1) begin
            shifted_reg = {shifted_reg[6:0], 1'b0};
            shifted_reg = shifted_reg ^ K;    
        end 
        else begin
            shifted_reg = {shifted_reg[6:0], 1'b0};
        end
    end
end

always @(posedge clk_i) begin
    if (rst_i)
        y_bo <= DEFAULT;
    else
        y_bo <= shifted_reg;
end

endmodule