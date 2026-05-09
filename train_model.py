import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("car_data.csv")

# Select useful columns
df = df[[
    "Year",
    "Selling_Price",
    "Present_Price",
    "Kms_Driven",
    "Fuel_Type",
    "Seller_Type",
    "Transmission",
    "Owner"
]]

# Feature engineering
df["Car_Age"] = 2026 - df["Year"]
df.drop("Year", axis=1, inplace=True)

# Encode categorical
le = LabelEncoder()

df["Fuel_Type"] = le.fit_transform(df["Fuel_Type"])
df["Seller_Type"] = le.fit_transform(df["Seller_Type"])
df["Transmission"] = le.fit_transform(df["Transmission"])

# Features & target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Strong model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
acc = r2_score(y_test, pred)

print("🔥 Model Accuracy:", round(acc * 100, 2), "%")

# Save model
joblib.dump(model, "car_price_model.pkl")

print("✅ New strong model saved!")
