//`include "comp_1bit_behv.v"
`include "comp_1bit_dataflow.v"

module tb;
	reg a, b;
	wire g, l, e;

comp_1bit dut (a, b, g, l, e);

	initial begin
		repeat (10) begin
			a = $random;
			b = $random;
			#1;
			$display("a=%b, b=%b, g=%b, l=%b, e=%b", a, b, g, l, e);
		end
	end
endmodule
