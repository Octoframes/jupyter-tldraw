import marimo

__generated_with = "0.7.17"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import polars as pl
    import quak

    df = pl.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    widget = mo.ui.anywidget(quak.Widget(df))
    widget
    return df, mo, pl, quak, widget


@app.cell
def __(tlwidget, widget):
    widget_df = widget.data().pl()
    df_selected = widget_df.select(
        ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    )
    print(df_selected.to_dicts())
    tlwidget.flower_data = df_selected.to_dicts()
    return df_selected, widget_df


@app.cell
def __():
    from tldraw import FlowerPlot

    # Sample flower data
    flower_data = [
        {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.4},
        {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2},
        # Add more flower data here...
    ]

    # Instantiate the widget
    tlwidget = FlowerPlot(flower_data=flower_data)
    tlwidget
    return FlowerPlot, flower_data, tlwidget


if __name__ == "__main__":
    app.run()
