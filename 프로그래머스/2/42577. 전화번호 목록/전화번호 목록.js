function solution(phone_book) {
    phone_book.sort()
    let answer = phone_book.some((value, index, self) => self[index + 1]?.indexOf(value) === 0);

    return !answer;
}
