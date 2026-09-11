import dolfyn as dl

# Force dolfyn to skip optional vendor/user datablocks
ds = dl.read('1_0/1_0_000.PD0', userdata=False)
print(ds)
