import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def visualize_one_3D_variable(dataset):
    # Get latitude, longitude, and data from the dataset
    lats = dataset.variables['latitude'][:]
    lons = dataset.variables['longitude'][:]
    data_variable = input("Give the 3D variable you want to visualize: ")
    data = dataset.variables[data_variable][0, :, :]

    # Create a 3D surface plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    lons, lats = np.meshgrid(lons, lats)
    surf = ax.plot_surface(lons, lats, data, cmap='viridis')

    # Add colorbar
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    cbar.set_label('Your Data Units')

    # Add labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel(data_variable)
    plt.title('3D Surface Plot of Your Data')

    # Show the plot
    plt.show()

def visualize_four_3D_variables(dataset):
    # Prompt user to choose 4 3D variables
    chosen_variables = []
    for i in range(4):
        variable_name = input(f"Choose a 3D variable ({i+1}/4): ")
        chosen_variables.append(variable_name)

    # Create subplots for each variable
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), subplot_kw={'projection': '3d'})
    fig.suptitle('3D Surface Plots of Selected Variables')

    for i, ax in enumerate(axes.flat):
        variable_name = chosen_variables[i]
        lats = dataset.variables['latitude'][:]
        lons = dataset.variables['longitude'][:]
        data = dataset.variables[variable_name][0, :, :]

        # Create a 3D surface plot for each variable
        lons, lats = np.meshgrid(lons, lats)
        surf = ax.plot_surface(lons, lats, data, cmap='viridis')
        ax.set_title(f'Variable: {variable_name}')

        # Add colorbar
        cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
        cbar.set_label('Your Data Units')

        # Add labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Your Data Variable')

    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Show the plot
    plt.show()

def print_info(dataset):
    # Print dimensions
    print("Dimensions:")
    for dimname, dimobj in dataset.dimensions.items():
        print(f"  {dimname}: {len(dimobj)}")

    # Print variables and their shapes
    print("\nVariables:")
    for varname, varobj in dataset.variables.items():
        print(f"  {varname}: {varobj.shape}")

    # Print global attributes
    print("\nGlobal Attributes:")
    for attrname in dataset.ncattrs():
        print(f"  {attrname}: {getattr(dataset, attrname)}")
        
def visualize(dataset):
    # Any input other than 0 is interpreted as 1
    choice = bool(input("\n0 to visualise 1 3D variable, 1 to visualise 4 3D variables: ") == '0')
    if (choice):
        visualize_one_3D_variable(dataset)
    else:
        visualize_four_3D_variables(dataset)

if __name__ == '__main__':
    # Open the NetCDF file
    filename = input("Give the nc file name you want to open (without .nc): ")
    dataset = nc.Dataset(filename + '.nc', 'r')

    print_info(dataset)

    # Call the visualization function
    visualize(dataset)  
