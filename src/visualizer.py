def plot_temperature_trend(datas,temps,title='温度变化趋势',save_path="output/temperature_trend.png"):
    plt.figure(figsize=(12,5))
    plt.plot(datas,temps,marker='o',linestyle='-',color='tomato',markersize=4,linewidth=2)
    plt.title(title,fontsize=14)
    plt.xlabel('日期')
    plt.ylabel('温度（°C）')
    plt.xticks(rotation=45)
    plt.grid(True,alpha=0.3)

    max_idx = np.argmax(temps)
    min_idx = np.argmin(temps)
    plt.annotate(f'最高：{temps[max_idx]}°C',
                 xy=(max_idx,temps[max_idx]),
                 xytext=(max_idx,temps[max_idx] + 2),
                 arrowprops=dict(arrowstyle='->',color='red'),
                 color='red',fontsize=10)
    plt.annotate(f'最低：{temps[min_idx]}°C',
                 xy=(min_idx, temps[min_idx]),
                 xytext=(min_idx, temps[min_idx] - 4),
                 arrowprops=dict(arrowstyle='->',color='blue'),
                 color='blue', fontsize=10)

    plt.tight_layout()
    plt.savefig(save_path,dpi=150,bbox_inches='tight')
    plt.close()
    print(f'温度变化趋势图已保存在{save_path}')

def plot_bar_comparsion(labels,values,title='对比柱状图',save_path="output/bar_comparsion.png",color='steelblue'):
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=color,edgecolor='black',alpha=0.8)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                 height + 0.1,
                 f'{height:.1f}',
                 ha='center', va='bottom',
                 fontsize=11)
    plt.title(title,fontsize=14)
    plt.grid(axis='y',alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path,dpi=150,bbox_inches='tight')
    plt.close()

def plot_histogram(data,bins=15,title='数据分布直方图',save_path="output/histogram.png"):
    plt.figure(figsize=(8,5))
    plt.hist(data,bins=bins,edgecolor='black',density=True,alpha=0.7)
    plt.title(title,fontsize=14)
    plt.xlabel('数值')
    plt.ylabel('概率密度')
    plt.grid(True,alpha=0.3)

    mean_val = np.mean(data)
    plt.axvline(mean_val,color='r',linestyle='--',alpha=0.7,linewidth=2,label=f'均值: {mean_val:.1f}')
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path,dpi=150,bbox_inches='tight')
    plt.close()