`timescale 1ns / 1ps

module func(
    input clk_i,
    input rst_i,
    
    input [7:0] a_bi,
    input [7:0] b_bi,
    
    input start_i, 
    
    output busy_o,
    output reg [4:0] y_bo
    );

    localparam IDLE = 2'o0;
    localparam S1 = 2'o1;
    localparam S2 = 2'o2;
    
    reg [1:0] state;
    
    wire busy_square_root;
    wire busy_cubic_root;
    
    wire [3:0] square_root_result;
    wire [2:0] cubic_root_result;
    
    wire [7:0] adder_a1, adder_b1;
    wire [7:0] adder_a2, adder_b2;
    
    wire[7:0] sum_a1, sum_b1;
    wire[7:0] sum_a2, sum_b2;
    
    wire [15:0] sum_result1;
    wire [15:0] sum_result2;
    
    adder adder_inst1(
        .a_bi(adder_a1),
        .b_bi(adder_b1),
        .y_bo(sum_result1)
    );
    
    adder adder_inst2(
        .a_bi(adder_a2),
        .b_bi(adder_b2),
        .y_bo(sum_result2)
    );
    
    square_root sqrt(
        .clk_i(clk_i),
        .rst_i(rst_i),
        .x_bi(b_bi), 
        .start_i(start_i),
        .sum_a(sum_a1),
        .sum_b(sum_b1),
        .busy_o(busy_square_root),
        .y_bo(square_root_result),
        .sum_result(sum_result1)
    );
    
    cubic_root cube(
        .clk_i(clk_i),
        .rst_i(rst_i),
        .x_bi(a_bi), 
        .start_i(start_i),
        .sum_a(sum_a2),
        .sum_b(sum_b2),
        .busy_o(busy_cubic_root),
        .y_bo(cubic_root_result),
        .sum_result(sum_result2)
    );
    
    assign busy_o = (state != IDLE);
    assign adder_a1 = (state == S2? square_root_result : sum_a1);
    assign adder_b1 = (state == S2? cubic_root_result : sum_b1);
    assign adder_a2 = (sum_a2);
    assign adder_b2 = (sum_b2);
    
    always @(posedge clk_i) begin
        if (rst_i) begin
            y_bo <= 0;
            state <= IDLE;
        end else begin
            case (state)
                IDLE: begin
                    if (start_i) begin
                        state <= S1;
                    end
                end
                S1: begin
                    if (~busy_square_root && ~busy_cubic_root) begin
                        state <= S2;
                    end 
                end
                S2: begin
                    state <= IDLE;
                    y_bo <= sum_result1;
                end
            endcase
        end
    end
endmodule