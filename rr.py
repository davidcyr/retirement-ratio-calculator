import sys
import argparse

DEFAULT_FINAL_INCOME = 100000.0

# Multiplier based on the 4% rule. 
DEFAULT_RETIREMENT_SAVINGS_MULTIPLIER = 25

# Replacement Ratio range high and low end values
RR_LOW = 0.70
RR_HIGH = 0.85




def get_replacement_income_range( final_income_amount ):
    
    low_range   = float(final_income_amount) * RR_LOW
    high_range  = float(final_income_amount) * RR_HIGH

    low_range  = round(low_range, 2)
    high_range = round(high_range, 2)
    return (low_range, high_range)


def get_required_savings_range ( income_range_tuple, mult ):
    
    low_end =  float(income_range_tuple[0]) * float(mult)
    high_end = float(income_range_tuple[1]) * float(mult)

    low_end  = round(low_end,2)
    high_end = round(high_end,2)

    return (low_end, high_end)

def pretty_string ( float_tuple ):

    a = "{:14,.2f}".format(float_tuple[0])
    b = "{:14,.2f}".format(float_tuple[1])
    return (a, b)



def main( argv=None ):

    if (argv==None):
        argv = sys.argv[:1]


    # 
    # make adjustments to read/parse parameters for e.g. FINAL_INCOME
    #
    parser = argparse.ArgumentParser()
    parser.add_argument ( "--final-income", type=float,
        help="Ending Income amount to use as a basis for determining a range of retirment income needs")
    parser.add_argument ( "--multiplier", type=float,
        help="Multiplier for retirement age. Default is 25 (effectively using the '4 percent rule')")

    print("parsing args")
    args = parser.parse_args()

    if args.final_income:
        inc = args.final_income
    else:
        inc = DEFAULT_FINAL_INCOME

    if args.multiplier:
        mult = args.multiplier
    else:
        mult = DEFAULT_RETIREMENT_SAVINGS_MULTIPLIER 

    print ("Calculating based on income: {0} and multiplier: {1}".format(inc, mult))

    rr_range =  get_replacement_income_range( inc )

    print ( type(rr_range) )
    print ( pretty_string(rr_range) )

    required_savings_range = get_required_savings_range ( rr_range, mult )

    print ( pretty_string(required_savings_range) )
    

    return 0




##############################################################3

if __name__ == "__main__":
    exit(main())
