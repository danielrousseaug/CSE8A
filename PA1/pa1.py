def main():
    weight_in_oz_str = input("Enter weight in oz: \n")
    weight_in_oz = float(weight_in_oz_str)
    weight_in_g = ounces_to_grams(weight_in_oz)
    print("Weight in grams = ",weight_in_g)
    print("Weight converted back to ounces = ", grams_to_ounces(weight_in_g))
    

def ounces_to_grams(weight_in_oz):
    """
    Converts ounces to grams
    """
    return(weight_in_oz*28.34952313)

def grams_to_ounces(weight_in_g):
    """
    Converts grams to ounces
    """
    return(weight_in_g*0.03527396)

if __name__ == '__main__':
    main()