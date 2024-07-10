`timescale 1ns / 1ps

module adder4_test();
    reg [3:0] a_in, b_in;
    reg p1_in;
    wire [3:0] s_real;
    wire p0_real;
    
    adder4 adder_real(
        .a(a_in),
        .b(b_in),
        .p1(p1_in),
        .s(s_real),
        .p0(p0_real)
    );
    
    wire [3:0] s_expected;
    wire p0_expected;

    adder4_calc adder_expected(
        .a(a_in),
        .b(b_in),
        .p1(p1_in),
        .s(s_expected),
        .p0(p0_expected)
    );


    integer i, j, k;
    
    wire [4:0] result_real;
    wire [4:0] result_expected;
    
    
    assign result_real = {s_real, p0_real};
    assign result_expected = {s_expected, p0_expected};

    initial begin
    for (k = 0; k < 2; k = k + 1) begin
        for(i = 0; i < 16; i = i + 1) begin
            for(j = 0; j < 16; j = j + 1) begin
                a_in = i;
                b_in = j;
                p1_in = k;
                    
                #10
                
                if(result_real != result_expected) begin
                    $display("TEST FAILED %b + %b != %b", i, j, result_expected);
                end else begin
                    $display("TEST PASSED %b + %b", i, j);
                end
            end
        end
        end
        #10 $stop;
    end    

endmodule
