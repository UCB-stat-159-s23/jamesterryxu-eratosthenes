import matplotlib.pyplot as plt

def plot_sieve(all_nmax, all_proportions, log_scale):
    if log_scale==True:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        plt.xscale("log")
        plt.yscale("log")
    else:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")

