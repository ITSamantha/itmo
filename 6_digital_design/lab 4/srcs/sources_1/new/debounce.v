`timescale 1ns / 1ps

module debounce(
    input clk_i,
    input btn_bi,
	output btn_bo
    );
    
    localparam IDLE = 2'b0;
    localparam CHECK = 2'b1;
    
    integer K = 100;
    
    reg state = IDLE;
    reg btn_reg;
    
    integer btn_cntr;
    
    assign btn_bo = btn_reg;

    always @(posedge clk_i) 
            begin
                case(state)
                    IDLE: 
                        begin
                            btn_cntr <= 0;
                            btn_reg <= btn_bi;
    
                            if (btn_bi) 
                                begin
                                    btn_cntr <= btn_cntr + 1;
                                    state <= CHECK;
                                end
                        end
                    CHECK: 
                        begin
                            btn_reg <= btn_bi;
                            if (btn_bi) begin
                                if (btn_cntr < K) begin
                                    btn_cntr <= btn_cntr + 1;
                                end
                                else begin 
                                    btn_reg <= 1;
                                    state <= IDLE;
                                end
                            end
                            else begin
                                if (btn_cntr > 0) begin
                                    btn_cntr <= btn_cntr - 1;
                                end
                                else begin 
                                    btn_reg <= 0;
                                    state <= IDLE;
                                end
                            end
                        end
                endcase
            end
endmodule
