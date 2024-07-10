`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Module Name: adder
// Description: This module is a sequential transfer adder.
//////////////////////////////////////////////////////////////////////////////////


module adder(
    // input
    input p1,
    input a,
    input b,
    // output
    output s,
    output p0
    );
    wire nor_a_b, nor_a_ab, nor_b_ab, nor_aab_bab, 
    nor_p1__aab_bab, nor_p1__p1__aab_bab, nor_aab_bab__p1__aab_bab;
    
    nor(nor_a_b, a, b);
    nor(nor_a_ab, a, nor_a_b);
    nor(nor_b_ab, b, nor_a_b);
    nor(nor_aab_bab, nor_b_ab, nor_a_ab);
    nor(nor_p1__aab_bab, p1, nor_aab_bab);
    nor(nor_p1__p1__aab_bab, p1, nor_p1__aab_bab);
    nor(nor_aab_bab__p1__aab_bab,nor_aab_bab,nor_p1__aab_bab);
    nor(s, nor_aab_bab__p1__aab_bab, nor_p1__p1__aab_bab);// result s
    nor(p0, nor_a_b,nor_p1__aab_bab);//result p0
endmodule
