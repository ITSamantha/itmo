`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Module Name: adder4
// Description: This module is four-digit adder.
//////////////////////////////////////////////////////////////////////////////////


module adder4(
    //inputs
    input [3:0] a,
    input [3:0] b,
    input p1,
    //outputs
    output [3:0] s,
    output p0
    );
    
    wire add1_p0, add2_p0, add3_p0;
    
    adder adder1(
    .a(a[0]),
    .b(b[0]),
    .p1(p1),
    .s(s[0]),
    .p0(add1_p0)
    );
    
    adder adder2(
    .a(a[1]),
    .b(b[1]),
    .p1(add1_p0),
    .s(s[1]),
    .p0(add2_p0)
    );
    
    adder adder3(
    .a(a[2]),
    .b(b[2]),
    .p1(add2_p0),
    .s(s[2]),
    .p0(add3_p0)
    );
    
    adder adder4(
    .a(a[3]),
    .b(b[3]),
    .p1(add3_p0),
    .s(s[3]),
    .p0(p0)
    );
endmodule
