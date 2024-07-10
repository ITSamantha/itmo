`timescale 1ns / 1ps

module adder_tb;
    reg [7:0] a_bi;
    reg [7:0] b_bi;

    wire [15:0] y_bo;

    integer i, j;
    

    adder adder (
        .a_bi(a_bi),
        .b_bi(b_bi),
        .y_bo(y_bo)
    );


     initial begin
        for(i = 0; i < 255; i = i + 1) begin
            for(j = 0; j < 255; j = j + 1) begin
                testcase(i,j, i+j);
            end
        end

        $display("All tests passed!");
        #1 $finish;
    end

    task testcase;
        input [7:0] a_tb;
        input [7:0] b_tb;
        input [7:0] expected_answer;
        begin
        a_bi = 0;
        b_bi = 0;
        
        #10
          
        a_bi = a_tb;
        b_bi = b_tb;
        
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