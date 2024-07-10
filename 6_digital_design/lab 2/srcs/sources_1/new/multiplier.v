`timescale 1ns / 1ps


module multiplier(
    input clk_i,
    input rst_i,
    
    input [7:0] a_bi, 
    input [7:0] b_bi, 
    input start_i,
    
    output busy_o,
    output reg [15:0] y_bo
    );
    
    reg [15:0] sum_a, sum_b;
    wire[31:0] sum_result;
    
    adder32 tester(
    .a_bi(sum_a),
    .b_bi(sum_b),
    .y_bo(sum_result)
    );
    
    localparam IDLE = 2'h0;
    localparam WORK = 2'h1;
    localparam SUM_1 = 2'h2;
    localparam SUM_2 = 2'h3;
    
    reg [3:0] ctr;
    wire [3:0] end_step;
    wire [7:0] part_sum;
    wire [15:0] shifted_part_sum;
    reg [7:0] a, b;
    reg [15:0] part_res;
    reg [2:0] state;
    
    assign part_sum = a & {8{b[ctr]}};
    assign shifted_part_sum = part_sum << ctr;
    assign busy_o = (state != IDLE);
    assign end_step = (ctr == 4'h8);
    
    always @(posedge clk_i)
    begin
        if (rst_i) begin
            ctr <= 0;
            part_res <= 0;
            y_bo <= 0;
            state <= IDLE;
            
         end else begin
            case (state)
                IDLE:
                    if (start_i) begin
                        state <= WORK;
                        a <= a_bi;
                        b <= b_bi;
                        ctr <= 0;
                        part_res <= 0;
                    end
                WORK:
                    begin
                        if (end_step) begin
                            state <= IDLE;
                            y_bo <= part_res;
                        end
                        else begin
                            state <= SUM_1;
                            sum_a <= part_res;
                            sum_b <= shifted_part_sum;
                        end
                    end
               SUM_1:
                    begin
                        state <= SUM_2;
                        part_res <= sum_result;
                        sum_a <= ctr;
                        sum_b <= 1;
                    end
               SUM_2:
                    begin
                        state <= WORK;
                        ctr <= sum_result;
                    end
            endcase
       end
       end
endmodule
