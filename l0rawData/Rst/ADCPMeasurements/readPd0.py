import dolfyn as dl
import matplotlib.pyplot as plt

# 1. Path to your raw TRDI PD0 binary file
# If using WSL, point to your mounted Windows path or local Linux path
file_path = "1_0/1_0_000.PD0"

# 2. Read the PD0 file into an xarray Dataset
# dolfyn automatically handles frame parsing and sensor orientation
ds = dl.read(file_path)

# 3. Print the dataset structure
print("--- Dataset Overview ---")
print(ds)

# 4. Access core variables
# Velocities shape: (beam/coordinate_dir, range_bin, time)
velocity = ds.vel.values
time = ds.time.values
depth_cells = ds.range.values  # Cell distance from transducer head
heading = ds.heading.values    # Magnetometer/Compass heading in degrees

print("\n--- Key Dimensions & Shapes ---")
print(f"Number of Ensembles (Time steps): {len(time)}")
print(f"Number of Depth Bins: {len(depth_cells)}")
print(f"Velocity Array Shape: {velocity.shape}")

# 5. Coordinate Transformations (Beam -> Instrument -> Earth / ENU)
# Check current coordinate system
print(f"\nCurrent Coordinate System: {ds.coord_sys}")

# Rotate to Earth coordinates (East, North, Up) if not already transformed
if ds.coord_sys != "Earth":
    ds = dl.rotate2(ds, "Earth")
    print("Rotated data to Earth (ENU) coordinates.")

# Now velocity components represent East, North, Vertical velocity
east_vel = ds.vel.sel(dir="E")
north_vel = ds.vel.sel(dir="N")
up_vel = ds.vel.sel(dir="U1")

