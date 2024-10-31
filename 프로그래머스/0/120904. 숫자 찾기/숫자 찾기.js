function solution(num, k) {
    if (String(num).includes(k)) {
        return String(num).indexOf(k)+1
    } else {
        return -1
    }
}