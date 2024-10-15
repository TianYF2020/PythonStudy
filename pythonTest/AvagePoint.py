import random
import time
import matplotlib.pyplot as plt

data = []
averages = []
test = []
num_data_points = 50  # 产生数据的总数
interval = 0.01  # 产生数据的间隔时间（秒）


def generate_random_data():
    return random.uniform(0, 0.2) + 0.5


def calculate_average(data_list):
    if len(data_list) == 0:
        return 0
    return sum(data_list) / len(data_list)


def plot_data_and_average():
    plt.plot(data, color='red', label='Random Data', marker='o')
    plt.plot(averages, color='blue', label='Average Data', marker='o')
    plt.plot(test, color='green', label='Average Data', marker='o')
    plt.title('Random Data and Average Over Time')
    plt.xlabel('Time ({}s intervals)'.format(interval))
    plt.ylabel('Value')
    plt.legend()
    plt.show()


try:
    for _ in range(num_data_points):
        # 产生随机数据
        new_data = generate_random_data()
        data.append(new_data)

        # 计算当前所有数据的平均数
        current_average = calculate_average(data)
        averages.append(current_average)

        current_sulm = 1 * current_average + (data[len(data) - 1] - data[len(data) - 2]) * 0.1
        test .append(current_sulm)

        # 打印当前数据和平均数
        print(f"New Data: {new_data}, Current Average: {current_average}")

        # 间隔 0.5s
        time.sleep(interval)

    # 产生数据完成后一次性绘制图表
    plot_data_and_average()

except KeyboardInterrupt:
    print("程序被中断。")
