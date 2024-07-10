
module lfsr2_tb;

	reg clk;
	reg rst;
	
	wire [7:0] answer;
	

	integer i;
	

	lfsr2 lfsr2_inst(clk, rst, answer); 


	initial begin
		clk = 0;
		forever begin
			#50
			clk = ~clk;
		end
	end


	initial begin
		for(i = 1; i < 256; i=i+1) begin
			#100
			$display("%d", answer);
		end

		$display("FINISHED");
		$finish;
	end

endmodule



