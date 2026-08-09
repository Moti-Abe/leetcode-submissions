type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    let value1 = await promise1;
    let value2 = await promise2;
    return value1 + value2;


};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna