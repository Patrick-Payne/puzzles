/******************************************************************************
 * File: two_out_of_fifty.c
 * Author: Patrick Payne
 * Date Created: Oct 10, 2013
 * Purpose: Creates a counter that has a value of 1 for two consecutive clock
 * cycles out of every fifty. This code is mostly to see how quartus would
 * implement the counter.
 *****************************************************************************/

module two_out_of_fifty (clock, result);
  input clock;
  output reg result;
  reg [5:0] count;

  always @(posedge clock) begin
    count = count + 1'b1;
    if (count >= 50)
      count = 0;

    if (count >= 48)
      result = 1'b1;
    else
      result = 1'b0;
  end

endmodule
      
