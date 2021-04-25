function partition(arr, left, right) {
  let low = left + 1;
  let high = right;
  let p = arr[left];

  while (low < high) {
    while (low <= right && arr[low] < p) {
      low++;
    }

    while (high >= left && arr[high] > p) {
      high--;
    }

    if (low < high) {
      let temp = arr[low];
      arr[low] = arr[high];
      arr[high] = temp;
    }
  }

  let temp = arr[left];
  arr[left] = arr[high];
  arr[high] = temp;

  return high;
}

function quick_sort(arr, left, right) {
  if (left < right) {
    let p = partition(arr, left, right);

    quick_sort(arr, left, p - 1);
    quick_sort(arr, p + 1, right);
  }
}

const arr = [5, 3, 8, 4, 9, 1, 6, 2, 7];
quick_sort(arr, 0, arr.length - 1);
console.log(arr);
