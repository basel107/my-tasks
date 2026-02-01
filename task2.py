from typing import Sequence, Dict
data=[10,20,30,40]

def calculate_stats(data:list[float])-> dict[str,float]:
    if not data :
        print("this data is empyte")
    mean_value = sum(data)/len(data)
    max_value = max(data)
    min_value = min(data)
    return {
        "mean":mean_value,"max":max_value , "min":min_value
        }

print(calculate_stats(data))

def normalized (data:list[float])-> list[float]:
    min_value = min(data)
    range_val = max(data)-min(data)
    
    return [(data-min_value)/range_val for data in data]

print(normalized(data))

def remove_outlires (data : list[float],threshold=15):
    mean = sum(data)/len(data)
    clean_data = [x for x in data if abs (x - mean)>=threshold]
    return clean_data

print(remove_outlires(data,1.5))

def train_test_split(data:list[float],ratio:float=0.8)-> tuple[list[float],list[float]]:
    split = int(len(data)*ratio)
    return data [:split] , data [split:]

print(train_test_split(data))

g = ["cat","dog","cat"]

def encode_labels(labels: list[str])->dict[str,int]:
    
    unique_labels = sorted(set(labels))
    return{label:idx for idx , label in enumerate(sorted(set(unique_labels)))}

print(encode_labels(g))