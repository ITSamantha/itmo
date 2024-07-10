
module debounce_tb;


	reg clk;
	reg button = 0;
	wire answer;

	debounce deb(clk, button, answer);

    initial begin
        clk = 0;
        forever
            #5
            clk = ~clk;
    end


	initial begin
		button <= 1;
		#1000
		button <= 0;
		#1000
		$display("ANSWER : %d", answer);

		button <= 1;
		#1000
		$display("ANSWER : %d", answer);

		button <= 0;
		#1000
		$display("ANSWER : %d", answer);
		$finish;
	end
endmodule