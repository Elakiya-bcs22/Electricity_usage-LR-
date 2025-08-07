import pandas as pd
import pickle
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('electricity_usage_data.csv')
X = df.drop('electricity_cost', axis=1)
y = df['electricity_cost']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Lasso Regression model
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Save model and scaler
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("Model and Scaler saved successfully.")
