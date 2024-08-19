import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

features = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','yr_built']
target_attribute = ['price']
#house_pricing_model = DecisionTreeRegressor(random_state=1)
#house_pricing_model.fit(X,y)
row_test = {
    'bedrooms':1,
    'bathrooms':1,
    'sqft_living':1000,
    'sqft_lot':1200,
    'floors':1,
    'yr_built':2015
}

df_test = pd.DataFrame([row_test])
#df_test.set_index('bedrooms',inplace=True)

def read_csv():
    csv_file = open(file='C:\\Users\\phenn\\Desktop\\projects\\study-project\\datasets\\usa_housing_dataset.csv')
    file_df = pd.read_csv(csv_file)
    return file_df

if __name__ == "__main__":
    print('script start')
    df = read_csv()
    print(df_test)
    house_pricing_df_target = df[target_attribute]
    house_pricing_df_features = df[features]
    print(house_pricing_df_features.head(5))
    house_pricing_model = DecisionTreeRegressor(random_state=1)
    house_pricing_model.fit(house_pricing_df_features,house_pricing_df_target)  
    print("Making predictions for the following 5 houses:")
    print(house_pricing_model.predict(house_pricing_df_features.head(5)))
    print("testing row:")
    print(house_pricing_model.predict(df_test.head(5)))
    print("comparing with first table")
    print(df[['price']].head(5))
    #df.dropna(axis=0)
    #print(df[["sqft_living","sqft_lot"]])
    #print(df.price)
    #print(df.isnull() )
    #print(df.loc(df['price'] > 500))