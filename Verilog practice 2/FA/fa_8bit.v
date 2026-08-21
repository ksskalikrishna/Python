`include "FA_behv.v"
module FA_8bit(
	input [3:0] a,b,
	input Cin,
	output [3:0] s,
	output co
);
	wire w1,w2,w3;

	FA fa1(.a(a[0]),.b(b[0]),.Cin(Cin),.sum(s[0]),.carry(w1));
	FA fa2(.a(a[1]),.b(b[1]),.Cin(w1),.sum(s[1]),.carry(w2));
	FA fa3(.a(a[2]),.b(b[2]),.Cin(w2),.sum(s[2]),.carry(w3));
	FA fa4(.a(a[3]),.b(b[3]),.Cin(w3),.sum(s[3]),.carry(co));

	endmodule


