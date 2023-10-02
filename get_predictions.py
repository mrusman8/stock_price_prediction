import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from database import Database

db = Database("ADAMS")
data_to_pred = db.fetch_data_from_db(200)


def read_data(data):
    data = pd.DataFrame(data_to_pred)
    data.sort_index(ascending=False, inplace=True)
    data.rename(columns={0: 'ID', 1: 'Date', 2: 'Open', 3: 'High', 4: 'Low', 5: 'Close', 6: 'Volume'}, inplace=True)
    return data

def imputer(data):
    for col in data:
        prev_val = None
        for index, val in enumerate(data[col]):
            if val == 0 or val == 0.0 or val == 0.00:
                data.at[index, col] = prev_val
            else:
                prev_val = val
    return data


def feature_engineering(data):
    data['Upper_Cap'] = None
    data['Lower_Cap'] = None
    upper_cap(data)
    lower_cap(data)
    data.Upper_Cap = data.Upper_Cap.astype(float)
    data.Lower_Cap = data.Lower_Cap.astype(float)
    data.dropna(inplace=True)
    X_data = data.tail(90)[['Open', 'High', 'Low', 'Close', 'Volume', 'Upper_Cap', 'Lower_Cap']]
    y_data = data.tail(90)[['Open', 'High', 'Low', 'Close']]
    return X_data, y_data


def upper_cap(data):
    for i in range(len(data) - 1):
        x = data.Close[i] * 0.075
        if x > 1:
            data.at[i + 1, 'Upper_Cap'] = float(data.Close[i] + x)
        else:
            data.at[i + 1, 'Upper_Cap'] = float(data.Close[i] + 1)


def lower_cap(data):
    for i in range(len(data) - 1):
        x = data.Close[i] * 0.075

        if x > 1:
            data.at[i + 1, 'Lower_Cap'] = float(data.Close[i] - x)
        else:
            data.at[i + 1, 'Lower_Cap'] = float(data.Close[i] - 1)


def reshape_data(X_data, y_data):
    X_test_final = np.array(X_data[0:90])
    y_test_final = np.array(y_data[0:90])
    X_final_data = X_test_final.reshape(1, X_test_final.shape[0], X_test_final.shape[1])
    y_final_data = y_test_final.reshape(1, y_test_final.shape[0], y_test_final.shape[1])
    return X_final_data, y_final_data


def predictions(X_final_data, y_scaler, model):
    preds = model.predict(X_final_data)
    preds = y_scaler.inverse_transform(preds)
    preds = list(preds[0])
    return preds

def final_pipe(data):
    X_scaler = MinMaxScaler()
    y_scaler = MinMaxScaler()
    model = tf.keras.models.load_model("ADAMS_1.4.h5")


    data = read_data(data)
    data = imputer(data)
    X, y = feature_engineering(data)
    X_scaled = X_scaler.fit_transform(X)
    y_scaled = y_scaler.fit_transform(y)

    X_final, y_final = reshape_data(X_scaled, y_scaled)
    return predictions(X_final, y_scaler, model)



