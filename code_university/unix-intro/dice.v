module dice(
	    input clk, rst_n, stop,
	    output reg [2:0] me);
always @(posedge clk or negedge rst_n)
	if(!rst_n) me <=1;
        else if (stop==1) me <= me;
	else if (me==6) me <=1;
	else me <= me+1;
         
endmodule
