`timescale 1ns / 1ps

module cubic_root(
    input clk_i,
    input rst_i,
    input start_i,
    
    input [7:0] x_bi,
    input [15:0]sum_result,
    
    output busy_o,
    output reg [2:0] y_bo,
    output reg [7:0]sum_a,
    output reg [7:0]sum_b
    );


    localparam IDLE = 16'h0;
    localparam S1 = 16'h1;
    localparam S2 = 16'h2;
    localparam S3 = 16'h3;
    localparam S4 = 16'h4;
    localparam S5 = 16'h5;
    localparam S6 = 16'h6;
    localparam S7 = 16'h7;
    localparam S8 = 16'h8;
    localparam S9 = 16'h9;
    localparam S10 = 16'h10;
    localparam S11 = 16'h11;
    localparam S12 = 16'h12;
    localparam S13 = 16'h13;
    localparam S14 = 16'h14;
    localparam S15 = 16'h15;
    localparam S16 = 16'h16;
    localparam S17 = 16'h17;
    
    
    localparam N = 3'h6;
    
    reg [7:0] x;
    reg [7:0] y;
    
    reg [7:0]state;
    
    reg [7:0] s; 
    reg [7:0] b;
    
    reg [7:0] tmp;
    
    wire end_step;
    
    reg[7:0] shifted_b;
    
    reg [7:0] mult_a, mult_b;
    reg mult_start;
    wire mult_busy;
    wire [15:0] mult_result;
    
    
    assign busy_o = (state != IDLE);
    assign end_step = ($signed(s) < 0);
    
    multiplier mult_inst1(
    .clk_i(clk_i),
    .rst_i(rst_i),
    .start_i(mult_start),
    .a_bi(mult_a),
    .b_bi(mult_b),
    .busy_o(mult_busy),
    .y_bo(mult_result)
    );
    
    always @(posedge clk_i)
    begin
        if (rst_i) begin
            y_bo <= 0;
            sum_a <= 0;
            sum_b <= 0;
            s <= 0;
            state <= IDLE;
            
        end else begin
            case (state)
                IDLE:
                    if (start_i) begin
                        state <= S1;
                        x <= x_bi;
                        y <= 0;
                        s <= N;
                        mult_start <= 0;
                    end
                S1:
                    begin 
                        if (end_step) begin
                            state <= IDLE;
                            y_bo <= y;
                        end else begin
                            state <= S14;
                            mult_a <= 2;
                            mult_b <= y;
                            mult_start <= 1;
                        end
                    end
                    
               S14:
                    begin 
                        state <= S2;
                        mult_start <= 0;
                    end
               S2:
                    begin
                        if (~mult_busy) begin 
                            state <= S3;
                            y <= mult_result;
                        end
                    end
               S3:
                    begin
                        state <= S4;
                        sum_a <= y;
                        sum_b <= 1;
                    end
               S4:
                    begin
                        state <= S15;
                        mult_a = y;
                        mult_b = sum_result;
                        mult_start <= 1;
                    end
               S15:
                    begin
                        state <= S5;
                        mult_start <= 0;
                    end
               S5:
                    begin
                        if (~mult_busy) begin 
                            state <= S6;
                            mult_a <= mult_result;
                            mult_b <= 3;
                            mult_start <= 1;
                        end                    
                    end
               S6:
                    begin
                        state <= S7;
                        mult_start <= 0;
                    end
               S7:
                    begin
                        if (~mult_busy) begin 
                            state <= S8;
                            sum_a <= mult_result;
                            sum_b <= 1;
                        end  
                    end
               S8:
                    begin
                        state  <= S9;
                        b <= sum_result;
                    end
               S9:
                    begin
                        state <= S10;
                        b <= (b << s);
                    end
               S10:
                    begin
                        if (x >= b) begin
                            state <= S11;
                            sum_a <= ~b;
                            sum_b <= 1;
                        end else begin
                            state <= S16;
                        end
                    end
               S11:
                    begin
                        state <= S12;
                        sum_b <= sum_result;
                        sum_a <= x;
                    end
               S12:
                    begin
                        state <= S13;
                        x <= sum_result;
                        sum_a <= y;
                        sum_b <= 1;
                    end
               S13:
                    begin
                        state <= S16;
                        y <= sum_result;
                    end
               S16:
                    begin
                        state <= S17;
                        sum_a <= s;
                        sum_b <= -3;
                    end
               S17:
                    begin
                        state <= S1;
                        s <= sum_result;
                    end 
             endcase
        end
        end
endmodule
