`timescale 1ns / 1ps

module cubic_root_tb;
    reg [7:0] a;
    wire [2:0] answer;
    reg clk, rst, start;
    wire busy;

    integer i;

    wire [7:0] A, B;
    wire [15:0] S;

    adder adder_inst (.a_bi(A), .b_bi(B), .y_bo(S));

    cubic_root tester(
        .clk_i(clk),
        .rst_i(rst),
        .start_i(start),
        .x_bi(a),
        .sum_result(S),
        .busy_o(busy),
        .y_bo(answer),
        .sum_a(A),
        .sum_b(B)
    );

    initial begin
        clk = 0;
        forever #5 clk = ~clk; 
    end

    initial begin
        for(i = 0; i < 7; i = i + 1) begin
            testcase(i * i * i, i);
        end

        $display("All tests passed!");
        #1 $finish;
    end

    task testcase;
        input [7:0] a_tb;
        input [7:0] expected_answer;
        begin
        a = 0;
        clk = 0;
        start = 0;
        rst = 1;
        
        #10
        
        rst = 0;
          
        a = a_tb;
        start = 1;
        
        #10;
        
        start = 0;

            wait (!busy);
            #10;

            if(answer != expected_answer) begin
                $display("Test failed. On values : a=%d. Expected %d found %d.",a_tb,  expected_answer, answer);
                $finish;
            end
            $display("Test passed. On values : a=%d. Expected %d found %d.",a_tb,  expected_answer, answer);
        end
    endtask
endmodule