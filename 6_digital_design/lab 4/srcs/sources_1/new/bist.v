`timescale 1ns / 1ps

module bist(
    input [15:0] SW,
    input CLK, //100MHZ
    input BTNC, //START
    input BTNU, // RESET
    input BTND, //MODE
    input BTNL, //MODE CHANGE (SHOW CTR)
    output BUSY,//LED16_B
    output MODE, //LED17_R
    output SHOW_COUNT, //LED17_G
    output [7:0] LEDS
    );
    
    localparam TEST_MODE = 2'b0;
    localparam REQUEST_MODE = 2'b1;
    
    localparam FALSE_SHOW = 2'b0;
    localparam TRUE_SHOW = 2'b1;
    
    reg mode = TEST_MODE;
    
    wire rst_btn_debounce;
    wire start_btn_debounce;
    wire test_btn_debounce;
    wire test_mode_ctr_debounce; //amount of test starts
    
    debounce rst_deb(CLK, BTNU, rst_btn_debounce);
    debounce start_deb(CLK, BTNC, start_btn_debounce);
    debounce test_deb(CLK, BTND, test_btn_debounce);
    debounce test_ctr_deb(CLK, BTNL, test_mode_ctr_debounce);
    
    wire [7:0] a;
    wire [7:0] b;
    
    wire [7:0] lfsr1_out;
    wire [7:0] lfsr2_out;
    wire [7:0] crc8_out;
    
    reg [7:0] test_mode_ctr = 0;
    reg show_count = 0;
    
    
    wire [4:0] func_out;
    wire func_busy;
    
    wire checker;
    
    func tester (
        .clk_i(CLK),
        .rst_i(rst_btn_debounce),
        .a_bi(a),
        .b_bi(b),
        .start_i(checker),
        .busy_o(func_busy),
        .y_bo(func_out)
    );
    
    reg clk_lfsr = 0;
    reg clk_crc = 0;
    
    integer step = 0;
    reg data_ready_test = 0;
    
    lfsr1 lsfr1_inst(clk_lfsr, rst_btn_debounce, lfsr1_out );
    
    lfsr2 lsfr2_inst(clk_lfsr, rst_btn_debounce, lfsr2_out);
    
    crc8 crc8_inst(CLK, rst_btn_debounce, clk_crc, func_out, crc8_out);
    
    assign a = (mode == TEST_MODE)? lfsr1_out: SW[7:0];
    assign b = (mode == TEST_MODE)? lfsr2_out: SW[15:8];
    assign LEDS = (mode == REQUEST_MODE)? 
                    func_out  : (show_count == TRUE_SHOW ? test_mode_ctr : crc8_out );
    
    assign BUSY = func_busy;
    assign SHOW_COUNT = show_count;
    assign MODE = mode;
    
    assign checker = (data_ready_test) | (start_btn_debounce);
    
    localparam S1 = 3'b000;
    localparam S2 = 3'b001;
    localparam S3 = 3'b010;
    localparam S4 = 3'b011;
    localparam S5 = 3'b100;
     
    reg[2:0] state = S1;
    
    always @(posedge test_btn_debounce) begin
                if (mode == REQUEST_MODE) begin
                    test_mode_ctr <= test_mode_ctr + 1;
                end
                mode <= (mode == TEST_MODE)? REQUEST_MODE: TEST_MODE;
    end
    
    always @(posedge CLK) begin
                if(mode == TEST_MODE) begin
                    case(state)
                        S1 : begin
                            clk_crc <= 0;
                            if(step == 255) begin
                                state <= S3;
                            end
                            if(~func_busy) begin
                                state <= S4;
                                clk_lfsr <= 1;
                            end
                        end

                        S4 : 
                            begin
                                clk_lfsr <= 0;
                                step <= step + 1;
                                data_ready_test <= 1;
                                state <= S2;
                            end
                        S2 : 
                            begin
                                if(~func_busy) begin
                                    data_ready_test <= 0;
                                    state <= S5;
                                end
                            end

                        S5: 
                            begin
                                clk_crc <= 1;
                                state <= S1;
                            end

                        S3 : 
                            begin
                                clk_lfsr <= 0;
                            end
                    endcase
                end
                else begin
                    step <= 0;
                end
            end

always @(posedge test_mode_ctr_debounce) begin
                if (mode == TEST_MODE) begin
                    show_count  <= (show_count == TRUE_SHOW)? FALSE_SHOW: TRUE_SHOW;
                end
            end
            
endmodule
