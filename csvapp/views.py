import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
import matplotlib.pyplot as plt
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)
            context = process_data(df)
            return render(request, 'csvapp/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'csvapp/upload.html', {'form': form})

def process_data(df):
    # Display the first few rows of the data
    preview = df.head().to_html()

    # Calculate summary statistics for numerical columns
    summary = df.describe().to_html()

    # Identify and handle missing values by filling with mean values of respective columns
    numeric_df = df.select_dtypes(include=[float, int])
    df[numeric_df.columns] = numeric_df.apply(lambda x: x.fillna(x.mean()), axis=0)

    # Generate histograms for numerical columns
    histograms = {}
    for col in numeric_df.columns:
        plt.figure()  # Create a new figure for each histogram
        df[col].plot(kind='hist', title=col)
        plt.xlabel(col)
        plt.ylabel('Frequency')
        hist_path = f'static/{col}_hist.png'
        plt.savefig(hist_path)
        histograms[col] = f'/{hist_path}'  # Adjusted path to serve from static directory
        plt.close()  # Close the current figure to free up memory

    return {
        'preview': preview,
        'summary': summary,
        'histograms': histograms
    }