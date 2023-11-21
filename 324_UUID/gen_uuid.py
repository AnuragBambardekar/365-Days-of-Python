import uuid
import pandas as pd

data = pd.DataFrame({
    # "id":[300,2,3,400,5,6],
    "id":[uuid.uuid4() for _ in range(6)],
    "value":[40,20,10,20,30,30],
    "value2":[1,1,1,0,0,1]
})

data = data.set_index("id")

existing = pd.read_csv("existing_data.csv")
existing = existing.set_index("id")

combined = pd.concat([existing, data], verify_integrity=True)
print(combined)