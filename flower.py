import marimo

__generated_with = "0.8.15"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import polars as pl
    import quak
    return mo, pl, quak


@app.cell
def __(mo, pl, quak):
    df = pl.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    widget_quack = mo.ui.anywidget(quak.Widget(df))
    widget_quack
    return df, widget_quack


@app.cell
def __(mo):
    from tldraw import FlowerPlot

    flower_data = [
        {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.4},
        {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2},
    ]

    widget_flower = mo.ui.anywidget(FlowerPlot(flower_data=flower_data))
    widget_flower
    return FlowerPlot, flower_data, widget_flower


@app.cell
def __(widget_flower, widget_quack):
    widget_df = widget_quack.data().pl()
    #print(widget_df.select(["petal_length", "petal_width"]))


    df_selected = widget_df.select(
    ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    )
    print(df_selected.to_dicts())
    # Convert the selected dataframe to a list of dictionaries
    widget_flower.flower_data = df_selected.to_dicts()
    return df_selected, widget_df


@app.cell
def __(widget_flower):
    widget_flower.flower_data  = [
        {"sepal_length": 20.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.4},
        {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2},
    ]
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
