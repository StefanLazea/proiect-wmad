import datetime
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split


def get_data_set():
    _cars = pd.read_csv('./Car_Prices_Poland_Kaggle.csv')
    return _cars


def refactor_data_set(_cars):
    _cars['age'] = datetime.datetime.now().year - _cars['year']
    _cars = _cars.drop('province', axis=1)
    _cars = _cars.drop('city', axis=1)
    _cars = _cars.drop('id', axis=1)
    _cars = _cars.drop('fuel', axis=1)
    # cars = cars.drop('mark', axis=1)
    # cars = cars.drop('model', axis=1)
    _cars = _cars.drop('generation_name', axis=1)
    return _cars

# get variables that are used for training
def train_variables(cars):
    x = cars.drop('price', axis=1)
    y = cars.price
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, train_size=0.7, test_size=0.3, random_state=100)
    return x_train, x_test, y_train, y_test, x, y


# Regressor from CatBoost 1st try (slow 20sec)
def regressor_catboost(_cars, model):
    x_train, x_test, y_train, y_test, x, y = train_variables(_cars)
    # training
    model.fit(
        x_train, y_train,
        eval_set=(x_test, y_test),
    )
    print(model.score(x, y))


def create_train_model(_cars):
    make_dummies = pd.get_dummies(_cars.mark)
    _cars = _cars.join(make_dummies)
    _cars = _cars.drop('mark', axis=1)
    model_dummies = pd.get_dummies(_cars.model)
    _cars = _cars.join(model_dummies)
    _cars = _cars.drop('model', axis=1)
    model = CatBoostRegressor(iterations=6542, learning_rate=0.03)
    return model, _cars


def bar_chart(_model, _cars):
    sorted_feature_importance = _model.get_feature_importance().argsort(
    )[-20:]
    plt.barh(
        _cars.columns[sorted_feature_importance],
        _model.feature_importances_[sorted_feature_importance]
    )
    plt.xlabel("Feature Importance")
    plt.show()


def predict_price(_model, _cars):
    real_data = pd.DataFrame.from_records(_cars)
    real_data = real_data.drop('price', axis=1)
    real_data['age'] = datetime.datetime.now().year - real_data['year']
    real_data = real_data.drop('year', axis=1)

    fit_model = pd.DataFrame(columns=cars.columns)
    fit_model = fit_model.append(real_data, ignore_index=True)
    fit_model = fit_model.fillna(0)

    # change nr of iterations
    prediction = _model.predict(fit_model)
    print(prediction)
    print(real_data)


if __name__ == '__main__':
    cars_data_set = get_data_set()
    ref_cars = refactor_data_set(cars_data_set)
    # clean_data(_cars)
    print(ref_cars)

    model_created, cars = create_train_model(ref_cars)
    # prediction using CatBoostRegressor
    # regressor_catboost(cars, model_created)

    # using predict from CatBoost
    # predict_price(model_created, cars)

    # bar_chart(model_created, cars)



