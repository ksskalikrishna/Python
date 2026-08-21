`include "fa_nbit.v"
module tb;
	parameter N = 10;
	reg [N-1:0] a, b;
	reg cin;
	wire [N-1:0] sum;
	wire co;
	integer i;

nbit_fa dut(.*);
	initial begin
		for(i=0; i<(2**((2*N)+1)); i=i+1) begin
			{a, b, cin} = i;
			#1;
			$display("p=%b,q=%b,c=%b,s=%b,cout=%b",p,q,c,s,cout);
		end
	end
endmodule

