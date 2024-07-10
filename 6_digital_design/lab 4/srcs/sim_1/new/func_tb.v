`timescale 1ns / 1ps

module func_tb;

    reg clk_i;
    reg rst_i;
    reg [7:0] a_bi;
    reg [7:0] b_bi;
    reg start_i;

    wire busy_o;
    wire [4:0] y_bo;
    
    
    func tester (
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
     
        testcase(126, 26, 10);
        testcase(216, 255, 21);
        testcase(255, 24, 10);
        testcase(19, 81, 11);
        testcase(96, 50, 11);
        testcase(8, 100, 12);
        testcase(28, 225, 18);
        testcase(0, 1, 1);
        testcase(218, 196, 20);
        testcase(93, 10, 7);
      
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