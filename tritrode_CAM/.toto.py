import seaborn as sns
fig = figure()
ax = fig.add
plot(t,y[0,:],label='ch1')
plot(t,y[1,:],label='ch2')
xlabel('sec')
ylabel('uV')
legend()
fig.savefig('10sec_recording.pdf', bbox_inches='tight')