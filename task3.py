import pandas as pd
raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}

df=pd.DataFrame(raw)

g=df["price"]=df["price"].apply(lambda x: float(x.replace("$","").replace(",","")))

print(g)

full_null=df.fillna(0)

print(full_null)

total_price=df["price"]*df["quantity"]

print(total_price)

low_high=df["price"]=df["price"].apply(lambda x: "low" if x<1100 else "med" if x<2000 else "high")


print(low_high)
