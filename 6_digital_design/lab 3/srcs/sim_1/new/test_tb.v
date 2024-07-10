`timescale 1ns / 1ps

module test_tb;

    reg clk_i;
    reg rst_i;
    reg [15:0] sw_bi;
    reg start_i;

    wire busy_o;
    wire [4:0] y_bo;
    
    
    test tester (
        .CLK(clk_i),
        .BTNU(rst_i),
        .SW(sw_bi),
        .BTNC(start_i),
        .BUSY(busy_o),
        .LEDS(y_bo)
    );

    initial begin
        clk_i = 0;
        forever #5 clk_i = ~clk_i; 
    end

     initial begin
     
        testcase(126, 10);
        testcase(216, 21);
        testcase(255, 10);
        testcase(19, 11);
        testcase(96, 11);
        testcase(8, 12);
        testcase(28, 18);
        testcase(0, 1);
        testcase(218, 20);
        testcase(93, 7);
      
        $display("All tests passed!");
        #1 $finish;
    end

    task testcase;
        input [15:0] sw_tb;
        input [4:0] expected_answer;
        
        begin
        sw_bi = 0;
        clk_i = 0;
        start_i = 0;
        rst_i = 1;
        
        #10
        
        rst_i = 0;
          
        sw_bi = sw_tb;
        start_i = 1;
        
        #10;
        
        start_i = 0;

        wait (!busy_o);
        #10;

        if(y_bo != expected_answer) begin
                $display("Test failed. On values : sw=%d. Expected %d found %d.",sw_tb,  expected_answer, y_bo);
                $finish;
            end
         else begin
            $display("Test passed. On values : sw=%d. Expected %d found %d.",sw_tb,  expected_answer, y_bo);
            end
        end
    endtask
   
endmodule