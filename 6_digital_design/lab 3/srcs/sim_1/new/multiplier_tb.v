`timescale 1ns / 1ps

module multiplier_tb;

    reg clk_i;
    reg rst_i;
    reg [7:0] a_bi;
    reg [7:0] b_bi;
    reg start_i;

    wire busy_o;
    wire [15:0] y_bo;
    
    integer i, j;
    

    multiplier tester (
        .clk_i(clk_i),
        .rst_i(rst_i),
        .a_bi(a_bi),
        .b_bi(b_bi),
        .start_i(start_i),
        .busy_o(busy_o),
        .y_bo(y_bo)
    );

    initial begin
        clk_i = 0;
        forever #5 clk_i = ~clk_i; 
    end

     initial begin
        for(i = 0; i < 256; i = i + 1) begin
            for(j = 0; j < 256; j = j + 1) begin
                testcase(i, j, i*j);
            end
        end

        $display("All tests passed!");
        #1 $finish;
    end

    task testcase;
        input [7:0] a_tb;
        input [7:0] b_tb;
        input [15:0] expected_answer;
        begin
        a_bi = 0;
        b_bi = 0;
        clk_i = 0;
        start_i = 0;
        rst_i = 1;
        
        #10
        
        rst_i = 0;
          
        a_bi = a_tb;
        b_bi = b_tb;
        start_i = 1;
        
        #10;
        
        start_i = 0;

        wait (!busy_o);
        #10;

        if(y_bo != expected_answer) begin
                $display("Test failed. On values : a=%d;b=%d. Expected %d found %d.",a_tb, b_tb,  expected_answer, y_bo);
                $finish;
            end
         else begin
            $display("Test passed. On values : a=%d;b=%d. Expected %d found %d.",a_tb, b_tb,  expected_answer, y_bo);
            end
        end
    endtask
   
endmodule