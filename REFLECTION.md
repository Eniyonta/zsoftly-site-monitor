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

First, I would verify whether the issue is real by manually checking the site and confirming from another network or monitoring source. If confirmed, I would follow the incident response process like notifying the on-call engineer or client, collect relevant logs and metrics, and continue monitoring until the issue is resolved.

## AI Tool Usage
I used AI tool (Claude) to help structure the project, but I reviewed and understood all code before using it.
