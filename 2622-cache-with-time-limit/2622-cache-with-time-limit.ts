class TimeLimitedCache {
    private map = new Map<number, {value: number, expires: number}>();

    set(key: number, value: number, duration: number): boolean {
        const exists = this.map.has(key)
        
        this.map.set(key,{
            value:value,
            expires: Date.now()+ duration
        });
        
        return exists
    }
    
    get(key: number): number {
        const item =  this.map.get(key)

        if (!item) return -1

        if (Date.now() >= item.expires) {
            
            return -1;
        }

        return item.value
    }
    
    count(): number {
        let count = 0;

        for (const [key, item] of this.map) {
            if (Date.now() < item.expires) {
                count++;
            } 
        }
    
        return count;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna