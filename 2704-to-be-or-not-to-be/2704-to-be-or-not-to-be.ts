type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    
    function toBe (other: any): boolean{
        if (val === other) return true
        else throw new Error ("Not Equal")
    }

    function notToBe (other: any): boolean{
        if (val !== other) return true
        else throw new Error ("Equal")
    }

    return {
    toBe,
    notToBe
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna