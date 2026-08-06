/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
 var num;
var createCounter = function(init) {
    num = init
    function increment(){
        init ++
        return init
    }
    function decrement(){
        init --
        return init
    }
    function reset(){
        init = num
        return init
    }
    return{
        increment,
        decrement,
        reset
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