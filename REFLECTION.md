# Reflection

## (a) What was the hardest part, and how did you work through it?
The hardest part was handling the different types of failures gracefully,
because not all failures look the same. A DNS failure (like a completely
made-up URL), a timeout (a real server that never responds), and a bad
HTTP status code (a server that responds but reports an error) all fail
in completely different ways.

For example, when a URL doesn't exist at all, there is no HTTP code and
no response time to report the connection never even starts. When a
site times out, the request hangs until the limit is hit, and again no
HTTP code is received. Only when a server actually responds (even with
a 500 error) do you get real data back.

I worked through it by catching specific exception types like: ConnectionError
for DNS/network failures and Timeout for unresponsive servers  separately,
so each failure produces a clear, meaningful error message. I also made
the script report N/A for HTTP code and response time in cases where no
connection was made, rather than showing misleading zeroes or crashing.
This means the report is always honest about what was and wasn't measurable.

## (b) How would you scale this to 1,000 URLs every 5 minutes?

For 1,000 URLs, I would improve performance by using asynchronous requests or multithreading so that websites could be checked concurrently instead of sequentially.
I would also add logging, retry mechanisms, and possibly store historical results in a database for monitoring trends.

## (c) What would you do if the script reported a real client site as UNHEALTHY at 3 AM?

1. **Don't panic but rather verify first.** Manually open the URL in a browser
   and run a `curl` command to confirm the site is actually down, ruling
   out a false positive (e.g. a temporary network blip).
2. **Check if it's widespread.** Use a tool like downforeveryoneorjustme.com
   or test from a different network/region.
3. **Notify the client** according to the agreed SLA  even at 3 AM if
   the contract requires it.
4. **Escalate internally** if the issue is beyond my access to fix
   (e.g. a server the client manages).
5. **Document everything** timeline, what I checked, what I found, and
   what was done — so the post-mortem is easy.

## AI Tool Usage
I used AI tools to help structure the project and understand best practices, but I reviewed and understood all code before using it.
