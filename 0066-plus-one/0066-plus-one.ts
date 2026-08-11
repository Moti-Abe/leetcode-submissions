function plusOne(digits: number[]): number[] {
    

    for(let i:number = digits.length-1; i >= 0 ; i--){
        if (digits[i] < 9){
            digits[i]++
            return digits
        }
        digits[i] = 0
    }
    digits.unshift(1);

    return digits;

    
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna