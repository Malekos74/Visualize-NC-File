# Visualize .NC file

## Description
This Python script serves as a visualizer for .NC (NetCDF) files. It offers two options for visualization:
you can choose to visualize one variable in a 3D fashion or four variables in a 3D fashion displayed in a 2x2 grid of graphs.

## Input
- **File Path**: The user is prompted to enter the path for the .NC files.
- **Variable Selection**: The user is prompted to choose either a single variable for visualization or four variables for simultaneous visualization.

## Output
- The script opens a new window displaying the selected visualization graphs.

## Notes
1. **Dependencies**: Make sure to install the required dependencies specified in the `import` statements at the beginning of the script. You can install them using pip:
   
    ```
    pip install netCDF4 matplotlib numpy Axes3D
    ```
    
2. **Interrupting Execution**: You can interrupt the download process by pressing `Ctrl+C` in the terminal. The script will handle the interruption gracefully.

## Important Notes
- There is a test.nc file you can use to test the script.
- The script includes basic error handling to deal with exceptions that may occur during process.
- Feel free to modify and adapt this script according to your specific requirements. If you encounter any issues or have further questions, please don't hesitate to reach out for assistance.
