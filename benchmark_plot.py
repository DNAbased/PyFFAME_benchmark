import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

benchmark_data = pd.read_csv('benchmark_results.csv')

first = benchmark_data[benchmark_data.dataset==100].mean()
second = benchmark_data[benchmark_data.dataset==500].mean()
third = benchmark_data[benchmark_data.dataset==1000].mean()
fourth = benchmark_data[benchmark_data.dataset==3000].mean()
fifth = benchmark_data[benchmark_data.dataset==5000].mean()
sixth = benchmark_data[benchmark_data.dataset==10000].mean()

data_mean = pd.DataFrame([first, second, third, fourth, fifth, sixth])

seventh = benchmark_data[benchmark_data.dataset==100].std()
eight = benchmark_data[benchmark_data.dataset==500].std()
ninth = benchmark_data[benchmark_data.dataset==1000].std()
tenth = benchmark_data[benchmark_data.dataset==3000].std()
eleventh = benchmark_data[benchmark_data.dataset==5000].std()
twelfth = benchmark_data[benchmark_data.dataset==10000].std()

data_std = pd.DataFrame([seventh, eight, ninth, tenth, eleventh, twelfth])

sns.set()
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.scatterplot(data=data_mean, x=data_mean.dataset, y=data_mean.mpradesigntools, ax=ax, s=50, c=['b'], linewidth=0)
g = sns.scatterplot(data=data_mean, x=data_mean.dataset, y=data_mean.MPRAnator, ax=ax, s=50, c=['g'], linewidth=0)
g = sns.scatterplot(data=data_mean, x=data_mean.dataset, y=data_mean.PyFFAME, ax=ax, s=50, c=['r'], linewidth=0)
#g = sns.scatterplot(data=data_mean, x=data_mean.dataset, y=data_mean.PyFFAME_vcf_to_feature, ax=ax, s=50, c=['c'], linewidth=0)
#g = sns.scatterplot(data=data_mean, x=data_mean.dataset, y=data_mean.PyFFAME_feature_only, ax=ax, s=50, c=['m'], linewidth=0)
g.set(xlabel='Variants', ylabel='Time [sec]', yscale='log')
plt.ylim(1, 20000)
box = g.get_position()
g.set_position([box.x0, box.y0, box.width * 1, box.height])
g.legend(labels=['MPRA design tools', 'MPRAnator', 'PyFFAME'], loc='center right', bbox_to_anchor=(1.5, 0.5), ncol=1)
g.errorbar(x=data_mean.dataset, y=data_mean.mpradesigntools, yerr=data_std.mpradesigntools, fmt='.b')
g.errorbar(x=data_mean.dataset, y=data_mean.MPRAnator, yerr=data_std.MPRAnator, fmt='.g')
g.errorbar(x=data_mean.dataset, y=data_mean.PyFFAME, yerr=data_std.PyFFAME, fmt='.r')
#g.errorbar(x=data_mean.dataset, y=data_mean.PyFFAME_vcf_to_feature, yerr=data_std.PyFFAME_vcf_to_feature, fmt='.c')
#g.errorbar(x=data_mean.dataset, y=data_mean.PyFFAME_feature_only, yerr=data_std.PyFFAME_feature_only, fmt='.m')
fig.savefig('benchmark_results.pdf', dpi=600)
fig.savefig('benchmark_results.png', dpi=600)
