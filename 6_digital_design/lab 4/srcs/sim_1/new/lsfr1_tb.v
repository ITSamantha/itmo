
module lfsr1_tb;

	reg clk;
	reg rst;
	
	wire [7:0] answer;
	

	integer i;
	

	lfsr1 lfsr1_inst(clk, rst, answer); 


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
			$display("answer : %d", answer);
		end

		$display("FINISHED");
		$finish;
	end

endmodule



