from django.shortcuts import render
from django.http import HttpResponse
import csv


def import_csv(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['fileUpload']
        if uploaded_file.size > 0:
            fileReader(uploaded_file)
            context['message'] = "Arquivo Recebido!"
        else:
            context['error'] = "Arquivo vazio. Por favor, selecione um arquivo CSV válido."
        return render(request, '_Import/import_transactions.html', context)
    return render(request, '_Import/import_transactions.html')



def fileReader(uploaded_file):
        file_data = uploaded_file.read().decode('utf-8')
        lines = file_data.splitlines()
        reader = csv.reader(lines)


        # Imprimindo linhas
        for row in reader:
                print(row)


        # Nome e tamanho do arquivo
        print(f"Arquivo importado: {uploaded_file.name}")
        size_mb = uploaded_file.size / 1024 / 1024
        print(f"Tamanho do Arquivo: {size_mb: .2f} MB")
    

    