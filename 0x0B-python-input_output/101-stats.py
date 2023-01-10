#!/usr/bin/python3
"""Reads stdin"""
import sys

total_size = 0
status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        size = int(parts[-1])
        total_size += size
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_codes.keys()):
                if status_codes[status_code] > 0:
                    print(f"{status_code}: {status_codes[status_code]}")
except KeyboardInterrupt:
    print("Total file size:", total_size)
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status__codes[status_code]}")
