
import polars as pl
import polars.selectors as cs



def add_weekdays(df: pl.DataFrame) -> pl.DataFrame:

    return df.with_columns(pl.col('date').dt.weekday().alias("weekday"))

def add_weekend(df:  pl.DataFrame) -> pl.DataFrame:

    return df.with_columns(pl.when(pl.col("weekday").is_in([6, 7])).then(1).otherwise(0).alias("is_weekend"))

def heating_season(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.col("date")
        .dt.month()
        .is_in([10, 11, 12, 1, 2, 3])
        .cast(pl.Int8) # Jetzt wird NUR dieser Boolean zu 0 oder 1 konvertiert
        .alias("is_heating_season")
    )

def renovation_index(df: pl.DataFrame) -> pl.DataFrame:
    # Saubere Summe der Sanierungsmaßnahmen
    return df.with_columns(
        (
            pl.col('building_renovated_windows').cast(pl.Int8) +
            pl.col('building_renovated_roof').cast(pl.Int8) +
            pl.col('building_renovated_walls').cast(pl.Int8) +
            pl.col('building_renovated_floor').cast(pl.Int8)
        ).alias('renovation_score')
    )

def heating_amount(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (
            pl.col('building_floorareaheated_total') *
            pl.col('building_residents')
        ).alias('heating_amount')
    )

def add_price_features(df: pl.DataFrame) -> pl.DataFrame:
    return df.sort(["household_id", "date"]).with_columns([
        
        pl.col("swissix_base").shift(30).over("household_id").alias("price_lag_30d"),
        pl.col("swissix_base").shift(90).over("household_id").alias("price_lag_90d"),

        pl.col("swissix_base").rolling_mean(window_size=30).over("household_id").alias("price_rolling_mean_30d"),
        pl.col("swissix_base").rolling_mean(window_size=90).over("household_id").alias("price_rolling_mean_90d"),
        
        (pl.col("swissix_base") / pl.col("swissix_base").rolling_mean(window_size=30).over("household_id"))
        .alias("price_relative_to_month")
    ])

def solar_potentials(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        (
            pl.col('sunshine_duration_daily') * pl.col('building_pvsystem_size').fill_null(0)
        ).alias('solar_thermal_potential') # Der Alias muss IN die Klammer von with_columns
    )