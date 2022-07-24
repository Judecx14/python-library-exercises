from app.automated_charts import Chart


def main():
    chart = Chart()
    chart.get_data()
    chart.create_chart()

if __name__ == "__main__":
    main()
