
module bist_tb;
	reg clk, up, center, left, down = 0;
	reg [15:0] x = 0;
	reg start = 0;
	reg test = 0;
	wire [7:0] answer;
	wire ledik1, ledik2, ledik3;

	bist bistik(x, clk, up, center, down, left, ledik1, ledik2, ledik3, answer);

	initial begin
        clk = 0;
        forever
            #5
            clk = ~clk;
    end


    initial begin
    	usermode(16'b0010001000100011);
    	$display("Answer is %d", answer);
    	
    	//testmode(16'b1111001110000011);
    	//$display("Answer is %d", answer);
    	$finish;
    end


    task usermode;
    	input [15:0] inner;
    	begin
    		up = 1;
    		left = 0;
    		down = 0;
    		center = 0;    		
    		#100
    		up = 0;
	    	x = inner;
	    	center = 1;
	    	#100
	    	center = 0;
	    	#1000000
	    	$display("usermode check");
    	end
    endtask

    task testmode;
    	input [15:0] inner;
    	begin
    		up = 1;
    		left = 0;
    		down = 0;
    		center = 0;
    		#100
    		up = 0;
    		x = inner;
	    	center = 1;
	    	#100
	    	center = 0;
	    	#5000000
	    	$display("testmode check");
    	end
    endtask

endmodule