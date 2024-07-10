

module crc8_tb;
	reg clk, rst, calc;
	reg [7:0] x = 0;
	wire [7:0] answer;
	integer i;


	crc8 my_crc8(clk, rst, clk, x, answer);


	initial begin
		clk = 0;
		forever begin
			#50
			clk = ~clk;
		end
	end


	initial begin
		rst <= 0;
		for(i = 1; i < 256; i=i+1) begin
			iterator(i);
			$display("FINISHED");
		end
		$finish;
	end


	task iterator;
		input [7:0] x_t;

		begin
			x <= x_t;
			calc <= 1;
			#100
			calc <= 0;
			$display("FOR : %d; Value : %d", x_t, answer);

		end
	endtask

endmodule