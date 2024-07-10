`timescale 1ns / 1ps

module adder4_calc(
    //inputs
    input [3:0] a,
    input [3:0] b,
    input p1,
    //outputs
    output [3:0] s,
    output p0
    );
    
    assign {p0, s} = a + b + p1;

  
endmodule