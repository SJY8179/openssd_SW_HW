import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gc_bw.1.log', header=None, names = ['ms','bw', 'dir', 'bs'], usecols=[0,1,2,3])
df['sec'] = df ['ms'] /1000
df['MBps'] = df['bw'] /1024

plt.figure(figsize=(11,4))
plt.plot(df['sec'],df['MBps'], linewidth=0.8)
plt.xlabel('Time(s)')
plt.ylabel('Bandwidth (MB/s)')
plt.title('4K Random Write Bandwidth over Time')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('gc_graph.png', dpi=150)
print(df['MBps'].describe())
