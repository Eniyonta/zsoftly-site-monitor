import json
import sys
import time
import requests

TIMEOUT_SECONDS = 10

def check_site(site):
    name = site["name"]
    url = site["url"]

    try:
        start = time.time()
        response = requests.get(url, timeout=TIMEOUT_SECONDS, allow_redirects=True)
        elapsed_ms = (time.time() - start) * 1000

        status_code = response.status_code
        healthy = 200 <= status_code < 400

        return {
            "name": name,
            "url": url,
            "status": "HEALTHY" if healthy else "UNHEALTHY",
            "http_code": status_code,
            "response_time_ms": round(elapsed_ms, 2),
            "error": None
        }

    except requests.exceptions.ConnectionError as e:
        return {
            "name": name,
            "url": url,
            "status": "UNHEALTHY",
            "http_code": None,
            "response_time_ms": None,
            "error": "Connection error (DNS failure or host unreachable)"
        }
    except requests.exceptions.Timeout:
        return {
            "name": name,
            "url": url,
            "status": "UNHEALTHY",
            "http_code": None,
            "response_time_ms": None,
            "error": f"Timed out after {TIMEOUT_SECONDS}s"
        }
    except Exception as e:
        return {
            "name": name,
            "url": url,
            "status": "UNHEALTHY",
            "http_code": None,
            "response_time_ms": None,
            "error": str(e)
        }


def print_report(results):
    print("=" * 65)
    print("          WEBSITE HEALTH MONITOR — REPORT")
    print("=" * 65)

    for r in results:
        print(f"\nName   : {r['name']}")
        print(f"URL    : {r['url']}")
        print(f"Status : {r['status']}")
        if r["http_code"]:
            print(f"HTTP   : {r['http_code']}")
        else:
            print(f"HTTP   : N/A")
        if r["response_time_ms"]:
            print(f"Time   : {r['response_time_ms']} ms")
        else:
            print(f"Time   : N/A")
        if r["error"]:
            print(f"Error  : {r['error']}")
        print("-" * 65)

    total = len(results)
    healthy_count = sum(1 for r in results if r["status"] == "HEALTHY")
    unhealthy_count = total - healthy_count

    print(f"\nSummary: {healthy_count}/{total} sites HEALTHY, {unhealthy_count}/{total} UNHEALTHY")
    print("=" * 65)


def main():
    # Load websites.json
    try:
        with open("websites.json", "r") as f:
            sites = json.load(f)
    except FileNotFoundError:
        print("ERROR: websites.json not found.")
        sys.exit(1)

    print(f"Checking {len(sites)} sites...\n")

    results = []
    for site in sites:
        print(f"  Checking {site['name']}...")
        result = check_site(site)
        results.append(result)

    print_report(results)

    # Exit 0 if all healthy, 1 if any unhealthy
    all_healthy = all(r["status"] == "HEALTHY" for r in results)
    sys.exit(0 if all_healthy else 1)


if __name__ == "__main__":
    main()
