const arr = [2, 3, 1, 4, 5, 7, 6];
const temp = Array.from({ length: arr.length }, () => {
  return 0;
});

function merge(arr, left, mid, right) {
  let i = left;
  let j = mid + 1;
  let k = left;

  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) {
      temp[k++] = arr[i++];
    } else {
      temp[k++] = arr[j++];
    }
  }

  if (i > mid) {
    for (let l = j; l <= right; l++) {
      temp[k++] = arr[l];
    }
  } else {
    for (let l = i; l <= mid; l++) {
      temp[k++] = arr[l];
    }
  }

  for (let l = left; l <= right; l++) {
    arr[l] = temp[l];
  }
}

function merge_sort(arr, left, right) {
  if (left < right) {
    let mid = parseInt((left + right) / 2);

    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);
    merge(arr, left, mid, right);
  }
}

merge_sort(arr, 0, arr.length - 1);

console.log(arr);
