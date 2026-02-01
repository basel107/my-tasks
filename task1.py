cat_a =[1,2,3,4,5]
cat_b=[10,20,30]
def calculate_state(data):
    mean=sum(data)/len(data)
    big_value=max(data)
    return {
        "max":big_value,
        "mean":mean

    }
state_a = calculate_state(cat_a)
state_b = calculate_state(cat_b)
print(state_a)
print(state_b)