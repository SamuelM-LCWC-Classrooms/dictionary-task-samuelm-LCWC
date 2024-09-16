def task(input): # the value of input is an integer which is the total money available

    result = {} # Empty dictionary

    needs = input * 0.5
    wants = input * 0.3
    savings = input * 0.2

    result.update({"Needs": needs})
    result.update({"Wants": wants})
    result.update({"Savings": savings})

    return result # result should be a dictionary wiht the correct values