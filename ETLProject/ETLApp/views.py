from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

stored_data = ""

@csrf_exempt
def extract_data(request):
    global stored_data
    data = json.loads(request.body.decode('utf-8'))
    stored_data = data.get('text', '')
    return JsonResponse({'message': 'Data extracted successfully.'})

@csrf_exempt
def transform_data(request):
    global stored_data
    transformation_type = json.loads(request.body.decode('utf-8')).get('transformation', '')

    if not stored_data:
        return JsonResponse({'error': 'No data to transform.'}, status=400)

    if transformation_type == 'UPPER_CASE':
        transformed_data = stored_data.upper()
    elif transformation_type == 'LOWER_CASE':
        transformed_data = stored_data.lower()
    elif transformation_type == 'WORD_CALCULATION':
        # words = stored_data.
        words=stored_data.replace(",","").lower().split()
        
        word_count = {word: words.count(word) for word in set(words)}
        transformed_data = ', '.join([f"{word}:{count}" for word, count in word_count.items()])
    else:
        return JsonResponse({'error': 'Invalid transformation type.'}, status=400)

    stored_data = transformed_data
    return JsonResponse({'message': 'Data transformed successfully.'})

def load_data(request):
    global stored_data
    if not stored_data:
        return JsonResponse({'message': 'No transformed data available.'}, status=404)
    return JsonResponse({'transformed_data': stored_data})
