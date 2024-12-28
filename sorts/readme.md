#### 1. **Bubble Sort**
- Compara elementos adjacentes e os troca se estiverem na ordem errada.
- Complexidade: \(O(n^2)\).
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

#### 2. **Selection Sort**
- Encontra o menor elemento e o coloca no início, repetindo para os próximos.
- Complexidade: \(O(n^2)\).
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

#### 3. **Insertion Sort**
- Constrói a lista ordenada gradualmente, inserindo elementos na posição correta.
- Complexidade: \(O(n^2)\), mas pode ser \(O(n)\) em listas quase ordenadas.
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

#### 4. **Merge Sort**
- Divide a lista em metades e as ordena recursivamente, combinando depois.
- Complexidade: \(O(n \log n)\).
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

---

#### 5. **Quick Sort**
- Escolhe um **pivô**, organiza os elementos em relação a ele, e ordena recursivamente as partes.
- Complexidade: \(O(n \log n)\), mas pode ser \(O(n^2)\) no pior caso.
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
```

---

#### 6. **Heap Sort**
- Constrói uma **heap** e remove o maior elemento sucessivamente.
- Complexidade: \(O(n \log n)\).
```python
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

---
