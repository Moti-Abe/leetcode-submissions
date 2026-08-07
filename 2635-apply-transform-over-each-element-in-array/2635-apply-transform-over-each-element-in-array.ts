function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    let res: number[] = []
    for (let i: number = 0; i < arr.length; i++) {
        let val = fn(arr[i], i)
        res.push(val)
    }
    return res
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna