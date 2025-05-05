# LES TRIS

## TRI PAR SELECTION O(n^2)
- prend le min de TOUTE la liste et le met au début  
- **Complexité constante donc la liste ne change rien**

```js
export function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) { 
    let min = i; 
    for (let j = i + 1; j < arr.length; j++) { 
      if (arr[j] < arr[min]) {
        min = j;   
      }
    }
    if (min !== i) {
      [arr[i], arr[min]] = [arr[min], arr[i]]; 
    }
  }
  return arr; 
}
```


## TRI PAR INSERTION O(n^2)
- commence à 0, compare avec la gauche --> rien donc avance à l'indice 1, tant que l'élément à gauche est plus grand, le décale à gauche, puis reprend l'élément à l'indice de base + 1 (2) et ainsi de suite
- **très fort si tableau déjà un peu trié, éclaté sinon**

```js
export function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    let current = arr[i];

    let j = i - 1;

    while (j > -1 && current < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  return arr;
}
```

## TRI A BULLES O(n^2)
- indice d'arrêt tout au fond, on compare deux à deux les éléments en partant de la gauche, si plus grand on le pousse jusqu'à atteindre l'indice d'arrêt puis on décale l'indice d'arrêt de -1 et on recommence
- **très fort si déjà un peu trié, éclaté sinon**
```js
export function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}
```

## TRI FUSION O(nlogn)
- récursif, fonction partitioner  
- partitionne la liste à trier jusqu'à avoir un élément puis re fusionne les sous listes en triant petit à petit
- **constant, rapide**

```js
export function mergeSort(arr) {
  const mid = arr.length / 2;

  if (arr.length < 2) {
    return arr;
  }

  const left = arr.splice(0, mid);
  return merge(mergeSort(left), mergeSort(arr));
}

function merge(left, right) {
  let arr = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      arr.push(left.shift());
    } else {
      arr.push(right.shift());
    }
  }

  return [...arr, ...left, ...right];
}
```

## TRI RAPIDE O(nlogn)
- récursif
- place un pivot en dernier, met dans la liste de gauche tous les éléments plus petits et dans la liste de droite le pivot puis tous les éléments plus grands, reproduit l'algo sur chaque sous liste jusuq'à n'avoir plus qu'un élément
- **très rapide (constant), mais moins quand valeurs non uniques**
```js
export function quickSort(arr, left = 0, right = arr.length - 1) {
    if (left >= right) {
      return;
    }
  
    let pivotIndex = partition(arr, left, right);
    quickSort(arr, left, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, right);
  
    return arr;
  }
  
  function partition(arr, left, right) {
    let pivotValue = arr[right];
    let partitionIndex = left;
  
    for (let i = left; i < right; i++) {
      if (arr[i] < pivotValue) {
        swap(arr, i, partitionIndex);
        partitionIndex++;
      }
    }
  
    swap(arr, right, partitionIndex);
    return partitionIndex;
  }
  
  function swap(arr, firstIndex, secondIndex) {
    let temp = arr[firstIndex];
    arr[firstIndex] = arr[secondIndex];
    arr[secondIndex] = temp;
  }
```