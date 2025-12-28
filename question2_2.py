"""
HIT137 - Assignment 2
Question 2: Australian Weather Data Analysis System

Student: Suraj Devkota
Student ID: S397467
Date: December 2026

Description:
This program analyzes temperature data from multiple weather stations across Australia.
It processes CSV files, calculates seasonal averages, finds temperature ranges,
and determines temperature stability metrics.
"""

import pandas as pd
import numpy as np
import os
import glob


def load_all_temperature_data(folder_path="/Users/surajdevkota/Desktop/HIT137_ASSIGNMENT2/temperatures"):
    """
    Loads all CSV files from the temperatures folder and combines them.
    
    Args:
        folder_path (str): Absolute path to folder containing CSV files
    
    Returns:
        pd.DataFrame: Combined dataframe with all temperature data
    """
    try:
        csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
        
        if not csv_files:
            print(f"✗ Error: No CSV files found in '{folder_path}/' folder!")
            return None
        
        print(f"Found {len(csv_files)} CSV files:")
        for file in csv_files:
            print(f"  - {os.path.basename(file)}")
        
        dataframes = []
        for file in csv_files:
            df = pd.read_csv(file)
            dataframes.append(df)
        
        combined_df = pd.concat(dataframes, ignore_index=True)
        print(f"\n✓ Successfully loaded {len(combined_df)} records from {len(csv_files)} files")
        return combined_df
    
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None


def calculate_seasonal_averages(df):
    seasons = {
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November']
    }
    seasonal_averages = {}
    
    print("\nCalculating seasonal averages...")
    
    for season_name, months in seasons.items():
        season_temps = []
        for month in months:
            if month in df.columns:
                temps = df[month].dropna()
                season_temps.extend(temps.tolist())
        
        if season_temps:
            avg_temp = np.mean(season_temps)
            seasonal_averages[season_name] = avg_temp
            print(f"  {season_name}: {avg_temp:.2f}°C")
        else:
            print(f"  {season_name}: No data available")
    
    return seasonal_averages


def find_largest_temperature_range(df):
    month_cols = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    
    station_ranges = []
    for station_name in df['STATION_NAME'].unique():
        station_data = df[df['STATION_NAME'] == station_name]
        all_temps = []
        for month in month_cols:
            if month in station_data.columns:
                temps = station_data[month].dropna()
                all_temps.extend(temps.tolist())
        
        if all_temps:
            max_temp = max(all_temps)
            min_temp = min(all_temps)
            temp_range = max_temp - min_temp
            station_ranges.append((station_name, temp_range, max_temp, min_temp))
    
    station_ranges.sort(key=lambda x: x[1], reverse=True)
    if station_ranges:
        largest_range = station_ranges[0][1]
        largest_stations = [s for s in station_ranges if s[1] == largest_range]
        print(f"  Found {len(largest_stations)} station(s) with largest range: {largest_range:.2f}°C")
        return largest_stations
    return []


def find_temperature_stability(df):
    month_cols = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    
    station_stdev = []
    for station_name in df['STATION_NAME'].unique():
        station_data = df[df['STATION_NAME'] == station_name]
        all_temps = []
        for month in month_cols:
            if month in station_data.columns:
                temps = station_data[month].dropna()
                all_temps.extend(temps.tolist())
        if len(all_temps) > 1:
            std_dev = np.std(all_temps, ddof=1)
            station_stdev.append((station_name, std_dev))
    
    if not station_stdev:
        return [], []
    
    station_stdev.sort(key=lambda x: x[1])
    min_stdev = station_stdev[0][1]
    max_stdev = station_stdev[-1][1]
    most_stable = [s for s in station_stdev if s[1] == min_stdev]
    most_variable = [s for s in station_stdev if s[1] == max_stdev]
    
    print(f"  Most Stable: {len(most_stable)} station(s) with StdDev {min_stdev:.2f}°C")
    print(f"  Most Variable: {len(most_variable)} station(s) with StdDev {max_stdev:.2f}°C")
    
    return most_stable, most_variable


def save_seasonal_averages(seasonal_averages, output_file="average_temp.txt"):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("SEASONAL AVERAGE TEMPERATURES\n")
            f.write("(Across all stations and all years)\n")
            f.write("=" * 60 + "\n\n")
            for season, avg_temp in seasonal_averages.items():
                f.write(f"{season}: {avg_temp:.1f}°C\n")
        print(f"\n✓ Saved seasonal averages to '{output_file}'")
    except Exception as e:
        print(f"✗ Error saving seasonal averages: {e}")


def save_largest_range(largest_stations, output_file="largest_temp_range_station.txt"):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("STATION(S) WITH LARGEST TEMPERATURE RANGE\n")
            f.write("=" * 60 + "\n\n")
            for station_name, temp_range, max_temp, min_temp in largest_stations:
                f.write(f"Station {station_name}: Range {temp_range:.1f}°C ")
                f.write(f"(Max: {max_temp:.1f}°C, Min: {min_temp:.1f}°C)\n")
        print(f"✓ Saved largest range stations to '{output_file}'")
    except Exception as e:
        print(f"✗ Error saving largest range: {e}")


def save_stability(most_stable, most_variable, output_file="temperature_stability_stations.txt"):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("TEMPERATURE STABILITY ANALYSIS\n")
            f.write("=" * 60 + "\n\n")
            f.write("MOST STABLE STATION(S):\n")
            f.write("-" * 60 + "\n")
            for station_name, std_dev in most_stable:
                f.write(f"Most Stable: Station {station_name}: StdDev {std_dev:.1f}°C\n")
            f.write("\nMOST VARIABLE STATION(S):\n")
            f.write("-" * 60 + "\n")
            for station_name, std_dev in most_variable:
                f.write(f"Most Variable: Station {station_name}: StdDev {std_dev:.1f}°C\n")
        print(f"✓ Saved stability analysis to '{output_file}'")
    except Exception as e:
        print(f"✗ Error saving stability data: {e}")


def main():
    print("=" * 60)
    print("AUSTRALIAN WEATHER DATA ANALYSIS SYSTEM")
    print("=" * 60)
    
    # Load data
    print("\nLoading temperature data...")
    df = load_all_temperature_data()
    
    if df is None:
        print("\n✗ Failed to load data. Exiting...")
        return
    
    # Calculate seasonal averages
    print("\n" + "-" * 60)
    print("TASK 1: SEASONAL AVERAGES")
    print("-" * 60)
    seasonal_averages = calculate_seasonal_averages(df)
    save_seasonal_averages(seasonal_averages)
    
    # Find largest temperature range
    print("\n" + "-" * 60)
    print("TASK 2: LARGEST TEMPERATURE RANGE")
    print("-" * 60)
    largest_stations = find_largest_temperature_range(df)
    save_largest_range(largest_stations)
    
    # Find temperature stability
    print("\n" + "-" * 60)
    print("TASK 3: TEMPERATURE STABILITY")
    print("-" * 60)
    most_stable, most_variable = find_temperature_stability(df)
    save_stability(most_stable, most_variable)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - average_temp.txt")
    print("  - largest_temp_range_station.txt")
    print("  - temperature_stability_stations.txt")


if __name__ == "__main__":
    main()
