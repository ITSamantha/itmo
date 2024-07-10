`timescale 1ns / 1ps

module lfsr1(   
    input clk_i,
    input rst_i,
    output reg [7:0] y_bo = 8'h21
    );
    
reg rst_delay_reg = 0;

always @(posedge clk_i)
    begin
        rst_delay_reg <= rst_i;
    end
    
wire rst_start = rst_i & ~rst_delay_reg;

always @(posedge clk_i)
    begin
        if (rst_start)
            begin
                y_bo <= 8'h21;
            end
        else begin
            y_bo <= {y_bo[6:0], (y_bo[5] ^ y_bo[6] ^ y_bo[7] ^ y_bo[0])};
        end
    end
endmodule
