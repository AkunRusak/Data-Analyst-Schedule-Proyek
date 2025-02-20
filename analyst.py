# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Set style untuk visualisasi
sns.set(style="whitegrid")

# Muat dataset contoh (kita akan menggunakan dataset 'tips' dari seaborn)
data = sns.load_dataset('tips')

# Tampilkan 5 baris pertama dari dataset
print("5 Baris Pertama dari Dataset:")
print(data.head())

# Informasi dasar tentang dataset
print("\nInformasi Dataset:")
print(data.info())

# Statistik deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())

# Cek missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualisasi distribusi tip
plt.figure(figsize=(10, 6))
sns.histplot(data['tip'], kde=True, bins=20, color='blue')
plt.title('Distribusi Tip')
plt.xlabel('Tip')
plt.ylabel('Frekuensi')
plt.show()

# Visualisasi hubungan antara total bill dan tip
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=data, hue='time', style='sex', palette='viridis')
plt.title('Hubungan antara Total Bill dan Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Visualisasi boxplot untuk tip berdasarkan hari
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='tip', data=data, palette='pastel')
plt.title('Distribusi Tip Berdasarkan Hari')
plt.xlabel('Hari')
plt.ylabel('Tip')
plt.show()

# Encoding variabel kategorikal
data_encoded = pd.get_dummies(data, columns=['sex', 'smoker', 'day', 'time'], drop_first=True)

# Pisahkan fitur dan target
X = data_encoded.drop('tip', axis=1)
y = data_encoded['tip']

# Bagi data menjadi training set dan test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standarisasi fitur
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Prediksi dengan Linear Regression
y_pred_lr = lr_model.predict(X_test)

# Evaluasi Linear Regression
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("\nLinear Regression Performance:")
print(f'MSE: {mse_lr}')
print(f'R^2: {r2_lr}')

# Model Random Forest Regression
rf_model = RandomForestRegressor(random_state=42)

# Hyperparameter tuning dengan GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Model terbaik dari GridSearchCV
best_rf_model = grid_search.best_estimator_

# Prediksi dengan Random Forest Regression
y_pred_rf = best_rf_model.predict(X_test)

# Evaluasi Random Forest Regression
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("\nRandom Forest Regression Performance:")
print(f'MSE: {mse_rf}')
print(f'R^2: {r2_rf}')

# Visualisasi hasil prediksi vs aktual
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Aktual')
plt.ylabel('Prediksi')
plt.title('Aktual vs Prediksi (Random Forest Regression)')
plt.show()

# Feature importance dari Random Forest
feature_importances = best_rf_model.feature_importances_
features = X.columns
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.title('Feature Importance (Random Forest Regression)')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

# Simpan model terbaik
import joblib
joblib.dump(best_rf_model, 'best_rf_model.pkl')

print("\nModel terbaik telah disimpan sebagai 'best_rf_model.pkl'")
