type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    let res: number[] = []
    for (let i: number = 0; i < arr.length; i++) {
        let val = fn(arr[i], i)
        if (val !== 0 && val !== undefined && val !== null && val !== false)
        res.push(arr[i])
        
    }
    return res
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna