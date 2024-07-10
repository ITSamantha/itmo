`timescale 1ns / 1ps

module adder(
    input [7:0] a_bi,
    input [7:0] b_bi,
    
    output [15:0] y_bo
    );
    
    assign y_bo = a_bi + b_bi;
    
endmodule
