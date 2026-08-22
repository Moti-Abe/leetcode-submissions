type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let ref
    return function(...args) {
        clearTimeout(ref)
        
        ref = setTimeout(()=>{
            return fn(...args)
        }, t)

        
    
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna