`timescale 1ns / 1ps

module test(
    input [15:0] SW,
    input CLK, //100MHZ
    input BTNC, //START
    input BTNU, // RESET
    output BUSY,//LED16_B
    output [4:0] LEDS
    );
    
    reg BTN_RST;
    reg BTN_START;
    
    func tester (
        .clk_i(CLK),
        .rst_i(BTN_RST),
        .a_bi(SW[7:0]),
        .b_bi(SW[15:8]),
        .start_i(BTN_START),
        .busy_o(BUSY),
        .y_bo(LEDS)
    );
    
    
    integer rst_count = 0;
    integer start_count = 0;

    integer K = 100;

    localparam IDLE = 2'b00;
    localparam CHECK_START = 2'b10;
    localparam CHECK_RST = 2'b11;

    reg [1:0] state = IDLE;

    always @(posedge CLK) 
            begin
                case(state)
                    IDLE: 
                        begin
                            rst_count <= 0;
                            start_count <= 0;
                            BTN_RST <= 0;
                            BTN_START <= 0;
    
                            if (BTNU) begin
                                rst_count <= rst_count + 1;
                                state <= CHECK_RST;
                            end
    
                            if(BTNC) begin
                                start_count <= start_count + 1;
                                state <= CHECK_START;
                            end
                        end

                    CHECK_RST : 
                        begin
                            if(rst_count >= K) begin
                                BTN_RST <= 1;
                                state <= IDLE;
                            end
    
                            if (rst_count < 0) begin
                                BTN_RST <= 0;
                                state <= IDLE;
                            end
    
                            if(BTNU) begin
                                rst_count <= rst_count + 1;
                            end
                            else begin
                                rst_count <= rst_count - 1;
                            end
                        end

                    CHECK_START : 
                        begin
                            if(start_count >= K) begin
                                BTN_START <= 1;
                                state <= IDLE;
                            end
    
                            if(start_count < 0) begin
                                BTN_START <= 0;
                                state <= IDLE;
                            end
    
    
                            if(BTNC) begin
                                start_count <= start_count + 1;
                            end
                            else begin
                                start_count <= start_count - 1;
                            end
                        end
                endcase
            end
endmodule
