type Fn = (...params: number[]) => number;

function memoize(fn: Fn): Fn {
    const cache = new Map<string, number>();

    return function (...args) {
        const key = args.join(",");

        if (cache.has(key)) {
            return cache.get(key)!;
        }

        const result = fn(...args);

        cache.set(key, result);

        return result;
    };
}

/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna