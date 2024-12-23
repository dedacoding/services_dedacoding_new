import streamlit as st # Import streamlit to start the framework
import pandas as pd # Import pandas, library to work with pandas

# Function to load the services data from a CSV file
def load_services(services):
    services_df = pd.read_csv(services)  # Reads the CSV file specified by 'services' and loads it into a DataFrame
    return services_df  # Returns the DataFrame containing the data from the CSV file

# Main function to run the Streamlit app
def main():
    st.title("Services Data Viewer")  # Sets the title of the Streamlit web page

    services_file = "services.csv"  # Specifies the file name of the CSV containing the services data
    services_df = load_services(services_file)  # Calls the load_services function to load the data from the CSV file into a DataFrame

    st.write("## Services Data:")  # Writes a header to indicate that the following content is services data
    st.dataframe(services_df)  # Displays the DataFrame in a tabular format in the Streamlit app

# If this script is run directly (not imported as a module), the main function is executed
if __name__ == "__main__":  # Checks if this script is being run directly (not imported)
    main()  # Calls the main function to execute the app

# adding comment to be able to push the code to GitHub
## Test again