import pandas as pd
df = pd.read_csv('sberbank_housing_market.csv', sep=',')

def calculate_data_shape(x):
    return x.shape
print(calculate_data_shape(df))

def take_columns(x):
    return x.columns
print(take_columns(df))

def calculate_target_ratio(x, target_name):
    return round(x[target_name].mean(), 2)
print(calculate_target_ratio(df, 'price_doc'))

def calculate_data_dtypes(x):
    return [x.dtypes[x.dtypes != 'object'].count(), x.dtypes[x.dtypes == 'object'].count()]
print(calculate_data_dtypes(df))

def calculate_cheap_apartment(x):
    return (x.price_doc <= 1000000).count()
print(calculate_cheap_apartment(df))

def calculate_squad_in_cheap_apartment(x):
    return x[x.price_doc <= 1000000].full_sq.mean()
print(calculate_squad_in_cheap_apartment(df))

def calculate_mean_price_in_new_housing(x):
    return x[(x.num_room == 3) & (x.build_year >= 2010)].price_doc.mean()
print(calculate_mean_price_in_new_housing(df))

def calculate_mean_squared_by_num_rooms(x):
    return round(x.groupby('num_room').full_sq.mean(), 2)
print(calculate_mean_squared_by_num_rooms(df))

def calculate_squared_stats_by_material(x):
    return round(x.groupby('material').full_sq.agg(['max', 'min']), 2)
print(calculate_squared_stats_by_material(df))

def calculate_crosstab(x):
    return round(x.pivot_table('price_doc', index=['sub_area'], columns=['product_type'], aggfunc='mean').fillna(0), 2)
print(calculate_crosstab(df))