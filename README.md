# Housing-Price-Time-Series-Forecasting

### Introduction

We aim to develop a time series forecasting model for predicting housing prices in Singapore's HDB
market using transaction data and geographical information.

### Running the Notebooks

Look out for the serialisation of the notebooks (e.g. 0X where X represents the order it is to be run). 00 to 10 can be found under `src(00-10)` while the rest (11-15) are found in the root directory.

### Data Cleaning & Processing

`mrt_coordinates_opening_dates.ipynb`

This file scrapes the MRT stations in Singapore through the Wikipedia website as well as their respective coordinates and opening dates. The results are written to the `mrt_stations.csv` file

`school_coordinates.ipynb`

This file scrapes the primary schools in Singapore through the Wikipedia website as well as their respective coordinates from the OneMap API/Site. The results are written to the primary_school_coordinates.csv file in the PointsOfInterest folder


`mall_coordinates_opening.ipynb`

This file scrapes the shopping malls in Singapore via Wikipedia and obtaining their respective coordinates and opening dates. 

`data_cleaning.ipynb`

This file deals with the following:
- Cleaning the HDB resale flat prices dataset 
    -  Converting `remaining_lease` into float for standardisation purposes and creating an `address` column that concatenates `block` and `street_name`.
    - Merging the two HDB resale flat prices datasets into one.
    - Calculating the coordinates of each unique HDB flat in the merged dataset using OneMapSG API.
-  Cleaning the `mrt_stations.csv` file
    - Remove rows where the MRT stations are yet to be opened (e.g. Brickland MRT Station).
    - Ensure that the opening dates are standardised,
- Cleaning the BTO supply dataset
    - Dropping redundant rows and remove rows with empty values.
    - Standardise the dates to `DD-MMM-YY`.
    - Add the coordinates of each BTO.
- Cleaning the SORA dataset
    - Creating new column `SORA Value Month` that will match the HDB transaction record dates.
    - Aggregating compounded SORA based on the month.

### Feature Engineering

`add_sora.ipynb`

Adds the SORA values associated with the HDB transaction record dates.

`mrt_stations_nearby_and_BTO_supply.ipynb`

- Identifies the MRT stations that are within a 1km radius from each HDB flat if the opening date of the MRT station is before the flat's transaction record date. For HDB flats that do not have any MRT stations within a 1km radius, the nearest MRT station is noted. Geometric distances between points are taken into account using `GeoPandas`.
- Identifies the number of BTO flats that are launching within a 4km radius from the flat (the launch dates of the BTOs are compared with the flat's transaction record date - only launch dates that happen before the transaction record date are taken into account) and the supply of units associated with these BTOs.

`malls2kmRadius.ipynb`

- Identifies the malls that are within a 1km radius from each HDB flat if the opening date of the mall is before the flat's transaction record date. Geometric distances between points are taken into account using `geopy`.

`distance2cbd.ipynb`

- Calculates the distance from HDB to Central Business District area (Coordinate(lon=103.851784, lat=1.287953)). Geometric distances between points are taken into account using `geopy`. 

`word_embedding.ipynb`

- Combine name and distance information about POIs (mrt, sch, mall)
- Convert to POI density vector using `spacy`

`pre_modelling.ipynb`

This file deals with processing the data prior to model building, including scaling for numerical features and one-hot encoding for categorical features. It also normalises the `resale_price` and drops relevant columns not needed for model building.


### Model Building

`xgboost_model.ipynb`

- Train xgboost regressor on working dataset
- Predict 2024 resale prices and evaluate performance

`random_forest.ipynb`

We build 2 Random Forest Regression models using Out-of-bag (OOB) method and 10-fold Cross Validation. Both models are evaluated by minimising Mean Absolute Error (MAE). Their performances across various criteria are compared against each other.

`CatBoost.ipynb`

This file utilises the Catboost gradient boosting algorithm to train the cleaned, normalised, and one-hot encoded data from `data_sklearn_models` before testing on the 2024 data. Following training, evaluation and analysis of model performance is conducted.

`gnnwr.ipynb`

This model uses incorporates geospatial features (latitude, longitude) using neural networks. 

`lstm.ipynb`

We first prepare the data for model training by performing necessary preprocessing steps and splitting it into distinct sets for training, validation, and testing purposes. We then train and evaluate the Long Short-Term Memory (LSTM) neural network model.

**Properties**:
- An LSTM model with three layers and dropout regularization is used to capture temporal dependencies.
- Uses the Adam optimizer and mean squared error loss function for regression tasks.
- Overfitting is prevented with early stopping, monitoring validation loss with a patience of 5.
- The model is trained for 100 epochs with a batch size of 32, with performance evaluated on the validation set to prevent overfitting.