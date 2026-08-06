type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

let num:number;
function createCounter(init: number): Counter {
    num = init
    return{

        increment: () => {
            init += 1
            return init
        },

        decrement: () => {
            init -= 1
            return init
        },
        
        reset: () => {
            init = num
            return init
       }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna