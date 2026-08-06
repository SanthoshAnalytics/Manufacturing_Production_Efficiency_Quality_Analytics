import pandas as pd


def dataset_shape(df):
    print("=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")


def column_names(df):
    print("=" * 50)
    print("COLUMN NAMES")
    print("=" * 50)

    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")


def dataset_info(df):
    print("=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)

    df.info()


def data_types(df):
    return pd.DataFrame(
        df.dtypes,
        columns=["Data Type"]
    )


def missing_values(df):
    return pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Percentage": round(df.isnull().mean()*100, 2)
    })


def duplicate_records(df):
    print("=" * 50)
    print("DUPLICATE RECORDS")
    print("=" * 50)
    print(df.duplicated().sum())


def unique_values(df):
    return pd.DataFrame({
        "Unique Values": df.nunique()
    })


def descriptive_statistics(df):
    return df.describe(include="all").transpose()


def numerical_columns(df):
    return list(
        df.select_dtypes(
            include=["int64", "float64"]
        ).columns
    )


def categorical_columns(df):
    return list(
        df.select_dtypes(
            include=["object", "category"]
        ).columns
    )


def memory_usage(df):
    memory = df.memory_usage(deep=True)

    print(
        f"Total Memory : {round(memory.sum()/1024,2)} KB"
    )


def random_sample(df):
    return df.sample(
        10,
        random_state=42
    )


def data_quality_report(df):

    report = pd.DataFrame({
        "Data Type": df.dtypes,
        "Missing Values": df.isnull().sum(),
        "Missing %": round(df.isnull().mean()*100, 2),
        "Unique Values": df.nunique()
    })

    return report