`timescale 1ns / 1ps

module adder32(
    input [15:0] a_bi,
    input [15:0] b_bi,
    
    output [31:0] y_bo
    );
    
    assign y_bo = a_bi + b_bi;
    
endmodule
