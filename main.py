import pandas as pd
import matplotlib.pyplot as plt
import os

DIRECTORY = "/Users/khoihd/Downloads/"


def plot_runtime():
    agents = [10, 20, 30, 40, 50]
    marker_size = 5

    fig, ax = plt.subplots()
    # quality_df = pd.DataFrame(quality)
    ax.plot(agents, [129, 190, 290, 358, 393], label='HCMS (State of the art)', marker='*', markersize=marker_size, linestyle='--')
    ax.plot([10], [406], label='EC-DPOP', marker='*', markersize=marker_size, linestyle='--')
    ax.plot(agents, [710, 1364, 1982, 3016, 3824], label='AC-DPOP (5 points)', marker='o', markersize=marker_size, linestyle='--')
    ax.plot(agents, [735, 1450, 2046, 3047, 3610], label='AC-DPOP (10 points)', marker='s', markersize=marker_size, linestyle='--')
    ax.plot(agents, [774, 1462, 2080, 3069, 3636], label='AC-DPOP (15 points)', marker='*', markersize=marker_size, linestyle='--')
    ax.plot(agents, [406, 1486, 2160, 3162, 3863], label='AC-DPOP (20 points)', marker='X', markersize=marker_size, linestyle='--')

    ax.set_xticks(agents)
    ax.set_xlabel("Number of Agents")
    ax.set_ylabel("Runtime (ms)")
    ax.set_title("Varying the Number of Agents on Random Trees")
    ax.legend(loc='best')
    # fig.show()
    fig.savefig("Runtime_Trees", dpi=300)


def plot_quality():
    agents = [10, 20, 30, 40, 50]
    marker_size = 5

    fig, ax = plt.subplots()
    # quality_df = pd.DataFrame(quality)
    ax.plot(agents, [129, 306, 436, 636, 832], label='HCMS (State of the art)', marker='*', markersize=marker_size, linestyle='--')
    ax.plot([10], [510], label='EC-DPOP', marker='*', markersize=marker_size, linestyle='--')
    ax.plot(agents, [330, 795, 1128, 1587, 2109], label='AC-DPOP (5 points)', marker='o', markersize=marker_size, linestyle='--')
    ax.plot(agents, [356, 870, 1230, 1728, 2316], label='AC-DPOP (10 points)', marker='s', markersize=marker_size, linestyle='--')
    ax.plot(agents, [374, 947, 1331, 1876, 2533], label='AC-DPOP (15 points)', marker='*', markersize=marker_size, linestyle='--')
    ax.plot(agents, [404, 1008, 1414, 1908, 2687], label='AC-DPOP (20 points)', marker='X', markersize=marker_size, linestyle='--')

    ax.set_xticks(agents)
    ax.set_xlabel("Number of Agents")
    ax.set_ylabel("Solution Quality")
    ax.set_title("Varying the Number of Agents on Random Trees")
    ax.legend(loc='best')
    # fig.show()
    fig.savefig("Quality_Trees", dpi=300)


def move_config():
    os.chdir(DIRECTORY)
    topology = 'random-network'
    for agent in [15]:
        for instance in range(20):
            path = DIRECTORY + "scenario/" + topology + "/d" + str(agent) + "/" + str(instance)
            print(path)
            os.system("cp hardware-configurations.json " + path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    move_config()
