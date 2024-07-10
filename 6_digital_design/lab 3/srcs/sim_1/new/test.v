`timescale 1ns / 1ps

module test(
    input [15:0] SW,
    input CLK, //100MHZ
    input BTNC, //START
    input BTNU, // RESET
    output BUSY,//LED16_B
    output [15:0] LEDS
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
    
    
    integer rst_n = 0;
            integer start_n = 0;

            integer prob_limit = 100;

            localparam DO_NOTHING = 2'b00;
            localparam ITERATOR_START = 2'b10;
            localparam ITERATOR_RST = 2'b11;

            reg [2:0] STATE = DO_NOTHING;

            always @(posedge CLK) begin
                case(STATE)
                    DO_NOTHING : begin
                        rst_n <= 0;
                        start_n <= 0;
                        BTN_RST <= 0;
                        BTN_START <= 0;

                        if(BTNU) begin
                            rst_n <= rst_n + 1;
                            STATE <= ITERATOR_RST;
                        end

                        if(BTNC) begin
                            start_n <= start_n + 1;
                            STATE <= ITERATOR_START;
                        end
                    end

                    ITERATOR_RST : begin
                        if(rst_n >= prob_limit) begin
                            BTN_RST <= 1;
                            STATE <= DO_NOTHING;
                        end

                        if(BTN_RST < 0) begin
                            BTN_RST <= 0;
                            STATE <= DO_NOTHING;
                        end

                        if(BTNU) begin
                            rst_n <= rst_n + 1;
                        end
                        else begin
                            rst_n <= rst_n - 1;
                        end
                    end

                    ITERATOR_START : begin
                        if(start_n >= prob_limit) begin
                            BTN_START <= 1;
                            STATE <= DO_NOTHING;
                        end

                        if(start_n < 0) begin
                            BTN_START <= 0;
                            STATE <= DO_NOTHING;
                        end


                        if(BTNC) begin
                            start_n <= start_n + 1;
                        end
                        else begin
                            start_n <= start_n - 1;
                        end
                    end
                endcase
            end
endmodule
