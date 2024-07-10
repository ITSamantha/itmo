`timescale 1ns / 1ps

module square_root(
    input clk_i,
    input rst_i,
    input start_i,
    
    input [7:0] x_bi,
    input [15:0]sum_result,
    
    output busy_o,
    output reg [3:0] y_bo,
    output reg [7:0]sum_a,
    output reg [7:0]sum_b
    );
    
    localparam IDLE = 8'h1;
    localparam CHECK_M = 8'h2;
    localparam CHECK_X = 8'h3;
    localparam CALC_X = 8'h4;
    localparam CALC_M = 8'h5;
    localparam SUB_B = 8'h6;
    
    localparam N = 8'h6;
    
    
    reg [7:0] x;
    reg [7:0] y;
    
    
    reg[7:0] state;
    
    reg [7:0] m;
    reg [7:0] b;
    
    
    wire end_step;
    
    assign busy_o = (state != IDLE);
    assign end_step = (m == 0);
    
    
    always @(posedge clk_i)
        if (rst_i) begin
            y_bo <= 0;
            sum_a <= 0;
            sum_b <= 0;
            b <= 0;
            state <= IDLE;
            
        end else begin
            case (state)
                IDLE:
                    if (start_i) begin
                        state <= CHECK_M;
                        x <= x_bi;
                        m <= 1 << N;
                        y <= 0;
                    end
                CHECK_M:
                    if (end_step) begin
                        state <= IDLE;
                        y_bo <= y;
                    end else begin
                        state <= CHECK_X;
                        b <= y | m;
                        y <= y >> 1;
                    end
                CHECK_X:
                    begin 
                        state <= CALC_M;
                        if (x >= b) begin
                            state <= SUB_B;
                            sum_a <= ~b;
                            sum_b <= 1;
                        end
                    end
                SUB_B:
                    begin
                        state <= CALC_X;
                        sum_b <= sum_result;
                        sum_a <= x;
                    end
                CALC_X:
                    begin
                        state <= CALC_M;
                        x <= sum_result;
                        y <= y | m;
                    end
                CALC_M:
                    begin
                        state <= CHECK_M;
                        m <= m >> 2;
                    end
            endcase
        end
endmodule
