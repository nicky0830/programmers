function solution(balls, share) {
    const factorial = e => e == 0 ? 1 : e * factorial(e-1)
    return Math.round(factorial(balls)/(factorial(share)*factorial(balls-share)))
}