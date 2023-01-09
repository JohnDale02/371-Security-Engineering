module count_bin_top 

	(
		// Clock pins
		CLOCK_50,
		
		
		// SDRAM
		DRAM_ADDR,
		DRAM_BA,
		DRAM_CAS_N,
		DRAM_CKE,
		DRAM_CLK,
		DRAM_CS_N,
		DRAM_DQ,
		DRAM_LDQM,
		DRAM_RAS_N,
		DRAM_UDQM,
		DRAM_WE_N,
		
		
		// Seven Segment Displays
		HEX4,
		HEX5,
		
		// LEDs
		
		LEDR,
		
		// Slider Switches
		SW
		
		
	);
		
	// Clock pins	
	input CLOCK_50;
	
	// SDRAM
	output 		[12: 0]	DRAM_ADDR;
	output		[ 1: 0]	DRAM_BA;
	output					DRAM_CAS_N;
	output					DRAM_CKE;
	output					DRAM_CLK;
	output					DRAM_CS_N;
	inout			[15: 0]	DRAM_DQ;
	output					DRAM_LDQM;
	output					DRAM_RAS_N;
	output					DRAM_UDQM;
	output					DRAM_WE_N;
	
	// Seven Segment Displays
	output		[ 6: 0]	HEX4;
	output		[ 6: 0]	HEX5;
	
	// LEDs
	output		[ 7: 0]	LEDR;
	
	// Slider Switches
	input			[ 3: 0]	SW;
	
	
	wire [15:0] hex5_hex4;

	assign HEX4 = ~hex5_hex4[ 6: 0];
	assign HEX5 = ~hex5_hex4[ 14: 8];
	
//change your_module_name to the name you have chosen for your QSYS module
your_module_name bin_count (
	
	
		.sys_sdram_pll_0_ref_clk_clk  (CLOCK_50),
		.sys_sdram_pll_0_ref_reset_reset (1'b0),
		
		 // SDRAM
		.sys_sdram_pll_0_sdram_clk_clk								(DRAM_CLK),
		.new_sdram_controller_0_wire_addr									(DRAM_ADDR),
		.new_sdram_controller_0_wire_ba									(DRAM_BA),
		.new_sdram_controller_0_wire_cas_n								(DRAM_CAS_N),
		.new_sdram_controller_0_wire_cke									(DRAM_CKE),
		.new_sdram_controller_0_wire_cs_n									(DRAM_CS_N),
		.new_sdram_controller_0_wire_dq									(DRAM_DQ),
		.new_sdram_controller_0_wire_dqm									({DRAM_UDQM,DRAM_LDQM}),
		.new_sdram_controller_0_wire_ras_n								(DRAM_RAS_N),
		.new_sdram_controller_0_wire_we_n									(DRAM_WE_N),
			
		);
		
		
		endmodule
