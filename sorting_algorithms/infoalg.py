sorting_algorithms = """
### Bubble Sort
- **Description**:  
  Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
  and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. 

- **Key Points**:  
  - Named for the way smaller or larger elements "bubble" to the top of the list.  
  - A comparison sort.  
  - Performs poorly in real-world use.  
  - Primarily used as an educational tool.  
- **Time Complexity**: O(n²) in the worst and average cases, O(n) in the best case (if the list is already sorted).

---

### Insertion Sort
- **Description**:  
  Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.  
- **Key Points**:  
  - Less efficient on large lists compared to advanced algorithms like heapsort.  
  - Advantages:  
    - Simple implementation.  
    - Efficient for small data sets.  
    - More efficient in practice than most other simple quadratic (O(n²)) algorithms like selection sort.  
  - Similar to how people manually sort cards in a bridge hand.  
- **Time Complexity**: O(n²) in the worst and average cases, O(n) in the best case (if the list is already sorted).

---

### Selection Sort
- **Description**:  
  Selection sort divides the input list into two parts: a sorted sublist of items (built from left to right) and an unsorted sublist.  
- **Key Points**:  
  - Initially, the sorted sublist is empty, and the unsorted sublist is the entire input list.  
  - The algorithm finds the smallest (or largest) element in the unsorted sublist, swaps it with the leftmost unsorted element, and moves the sublist boundary one element to the right.  
  - Repeats until the list is sorted.  
- **Time Complexity**: O(n²) in all cases (worst, average, and best).

---

### Bogo Sort
- **Description**:  
  Bogo sort (also known as permutation sort, stupid sort, or slowsort) is a highly inefficient sorting algorithm based on the generate-and-test paradigm.  
- **Key Points**:  
  - Successively generates permutations of its input until it finds one that is sorted.  
  - Not useful for sorting.  
  - Used for educational purposes to contrast with more efficient algorithms.  
  - Analogy: Sorting a deck of cards by throwing them in the air, picking them up randomly, and repeating until sorted.  
- **Time Complexity**: O((n+1)!) in the worst case (unbounded, as it depends on random chance).

---

### Quick Sort
- **Description**:  
  Quick sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays (less than or greater than the pivot).  
- **Key Points**:  
  - Sometimes called partition-exchange sort.  
  - Sorts sub-arrays recursively.  
  - Can be done in-place, requiring small additional memory.  
  - On average, takes O(n log n) comparisons to sort n items.  
- **Time Complexity**: O(n log n) on average, O(n²) in the worst case (if the pivot selection is poor).

---

### Merge Sort
- **Description**:  
  Merge sort is an efficient, general-purpose, and comparison-based sorting algorithm.  
- **Key Points**:  
  - Most implementations produce a stable sort (order of equal elements is preserved).  
  - A divide-and-conquer algorithm invented by John von Neumann in 1945.  
  - Works by recursively dividing the list into halves, sorting them, and merging the sorted halves.  
- **Time Complexity**: O(n log n) in all cases (worst, average, and best).

---

### Heap Sort
- **Description**:  
  Heap sort is a comparison-based sorting algorithm that improves on selection sort.  
- **Key Points**:  
  - Divides input into a sorted and an unsorted region.  
  - Iteratively shrinks the unsorted region by extracting the largest element and inserting it into the sorted region.  
  - Uses a heap data structure to quickly find the largest element in each step.  
  - More efficient than selection sort due to the use of a heap.  
- **Time Complexity**: O(n log n) in all cases (worst, average, and best).
"""


sorting_algorithms_bg = """
### Bubble Sort (Балонково сортиране)
- **Описание**:  
  Bubble sort, понякога наричан "sinking sort", е прост алгоритъм за сортиране, който многократно преминава през списъка, сравнява съседни елементи и ги разменя, ако са в грешен ред. Преминаването през списъка се повтаря, докато списъкът бъде сортиран.  
- **Основни точки**:  
  - Наречен е така, защото по-малките или по-големите елементи "изплуват" към върха на списъка.  
  - Алгоритъмът е базиран на сравнение.  
  - Лошо представяне в реални приложения.  
  - Използва се основно като образователен инструмент.  
- **Сложност**: O(n²) в най-лошия и среден случай, O(n) в най-добрия случай (ако списъкът е вече сортиран).

---

### Insertion Sort (Сортиране чрез вмъкване)
- **Описание**:  
  Insertion sort е прост алгоритъм за сортиране, който изгражда окончателно сортирания масив (или списък) елемент по елемент.  
- **Основни точки**:  
  - По-малко ефективен за големи списъци в сравнение с по-напреднали алгоритми като heapsort.  
  - Предимства:  
    - Лесна реализация.  
    - Ефективен за малки набори от данни.  
    - По-ефективен на практика от други прости квадратични (O(n²)) алгоритми като selection sort.  
  - Подобен на начина, по който хората ръчно сортират карти в ръка.  
- **Сложност**: O(n²) в най-лошия и среден случай, O(n) в най-добрия случай (ако списъкът е вече сортиран).

---

### Selection Sort (Сортиране чрез избор)
- **Описание**:  
  Selection sort разделя входния списък на две части: сортиран подсписък (който се изгражда отляво надясно) и несортиран подсписък.  
- **Основни точки**:  
  - В началото сортираният подсписък е празен, а несортираният е целият входен списък.  
  - Алгоритъмът намира най-малкия (или най-големия) елемент в несортирания подсписък, разменя го с най-левия несортиран елемент и премества границата на подсписъка с един елемент надясно.  
  - Повтаря се, докато списъкът бъде сортиран.  
- **Сложност**: O(n²) във всички случаи (най-лош, среден и най-добър).

---

### Bogo Sort (Бого сортиране)
- **Описание**:  
  Bogo sort (известен още като permutation sort, stupid sort или slowsort) е изключително неефективен алгоритъм за сортиране, базиран на парадигмата "генерирай и тествай".  
- **Основни точки**:  
  - Последователно генерира пермутации на входните данни, докато намери такава, която е сортирана.  
  - Безполезен за практическо сортиране.  
  - Използва се за образователни цели, за да се сравни с по-ефективни алгоритми.  
  - Аналогия: Сортиране на тесте карти, като ги хвърляш във въздуха, събираш на случаен принцип и повтаряш, докато тестето бъде сортирано.  
- **Сложност**: O((n+1)!) в най-лошия случай (неограничено, тъй като зависи от случайността).

---

### Quick Sort (Бързо сортиране)
- **Описание**:  
  Quick sort е алгоритъм за сортиране, базиран на принципа "разделяй и владей". Той избира "основен" елемент (pivot) и разделя останалите елементи на два под-масива (по-малки или по-големи от pivot).  
- **Основни точки**:  
  - Понякога наричан partition-exchange sort.  
  - Сортира под-масивите рекурсивно.  
  - Може да се изпълни на място (in-place), изисквайки малко допълнителна памет.  
  - Средно, изисква O(n log n) сравнения за сортиране на n елемента.  
- **Сложност**: O(n log n) средно, O(n²) в най-лошия случай (ако изборът на pivot е лош).

---

### Merge Sort (Сортиране чрез сливане)
- **Описание**:  
  Merge sort е ефективен, универсален алгоритъм за сортиране, базиран на сравнение.  
- **Основни точки**:  
  - Повечето реализации произвеждат стабилно сортиране (редът на еднаквите елементи се запазва).  
  - Алгоритъмът е базиран на принципа "разделяй и владей" и е изобретен от Джон фон Нойман през 1945 г.  
  - Работи чрез рекурсивно разделяне на списъка на половини, сортиране на всяка половина и сливане на сортираните половини.  
- **Сложност**: O(n log n) във всички случаи (най-лош, среден и най-добър).

---

### Heap Sort (Сортиране с пирамида)
- **Описание**:  
  Heap sort е алгоритъм за сортиране, базиран на сравнение, който подобрява selection sort.  
- **Основни точки**:  
  - Разделя входните данни на сортиран и несортиран регион.  
  - Итеративно намалява несортирания регион, като извлича най-големия елемент и го вмъква в сортирания регион.  
  - Използва структурата от данни heap (пирамида), за да намери най-големия елемент по-бързо.  
  - По-ефективен от selection sort благодарение на използването на heap.  
- **Сложност**: O(n log n) във всички случаи (най-лош, среден и най-добър).
"""
