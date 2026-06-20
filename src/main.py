import sys
import os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_csv, get_column
from src.analyzer import basic_stats, group_mean, filter_by_condition, missing_rate
from src.visualizer import plot_temperature_trend, plot_bar_comparison, plot_histogram

def main():
    os.makedirs(os.path.join(BASE_DIR, 'output'), exist_ok=True)

    data = load_csv(os.path.join(BASE_DIR, 'data/weather.csv'))
    if not data:
        print(f'数据为空，程序退出')
        return

    temp_max = get_column(data, 'temp_max')
    stats = basic_stats(temp_max)
    for k, v in stats.items():
        print(f'{k}: {v:.2f}')


    city_avg = group_mean(data, 'city','temp_max')
    for city, t in city_avg.items():
        print(f'{city}: {t:.2f}°C')

    missing = missing_rate(data)
    for col, rate in missing.items():
        status = f'{rate:.1%}' if rate > 0 else '无缺失 ✓'
        print(f'{col}: {status}')

    dates = get_column(data, 'date',dtype=str)
    plot_temperature_trend(dates,temp_max,title='温度变化趋势',save_path="output/temperature_trend.png")

    cities = list(city_avg.keys())
    avgs = list(city_avg.values())

    plot_bar_comparison(cities,avgs,title='各城市平均最高温度对比', save_path="output/bar_comparsion.png")
    plot_histogram(temp_max,bins=10,title='最高温度分布直方图',save_path="output/histogram.png")

    hot_days = filter_by_condition(data,'temp_max',8,operator='gt')
    for row in hot_days:
        print(f"  {row['date']} {row['city']}: {row['temp_max']}°C")

    print("分析完成！图表已保存到 output/")

if __name__ == '__main__':
    main()



