module comp_3bit(
	input [2:0] a, b,
	output g, l, e
);

	assign g = a > b;
	assign l = a < b;
	assign e = (a == b);

endmodule
